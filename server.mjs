import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PUBLIC_DIR = path.join(__dirname, 'public');
const CACHE_DIR = path.join(__dirname, 'cache');
const PORT = process.env.PORT || 3000;

if (!fs.existsSync(CACHE_DIR)) {
  fs.mkdirSync(CACHE_DIR, { recursive: true });
}

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.avif': 'image/avif',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.bin': 'application/octet-stream',
  '.gz': 'application/gzip'
};

function fetchUpstreamWithCurl(targetUrl) {
  return new Promise((resolve, reject) => {
    const child = spawn('curl.exe', [
      '-sL',
      '-A', 'Mozilla/5.0',
      targetUrl
    ]);
    const chunks = [];
    child.stdout.on('data', chunk => chunks.push(chunk));
    child.stderr.on('data', err => console.error('Curl err:', err.toString()));
    child.on('close', code => {
      if (code === 0) {
        resolve(Buffer.concat(chunks));
      } else {
        reject(new Error(`curl exited with code ${code}`));
      }
    });
  });
}

const server = http.createServer(async (req, res) => {
  try {
    const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
    let pathname = decodeURIComponent(parsedUrl.pathname);

    // 1. Dynamic API Endpoints: /map-place.json and /search-summaries.json
    if (pathname === '/map-place.json' || pathname === '/search-summaries.json') {
      const cacheKey = Buffer.from(req.url).toString('hex') + '.json';
      const cachePath = path.join(CACHE_DIR, cacheKey);

      if (fs.existsSync(cachePath)) {
        res.writeHead(200, {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
        return fs.createReadStream(cachePath).pipe(res);
      }

      try {
        const upstreamUrl = `https://eu5db.com${req.url}`;
        const data = await fetchUpstreamWithCurl(upstreamUrl);
        if (data && data.length > 0) {
          fs.writeFileSync(cachePath, data);
          res.writeHead(200, {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
          });
          return res.end(data);
        }
      } catch (err) {
        console.error(`Upstream proxy error for ${req.url}:`, err);
      }
    }

    // 2. Static file resolution
    if (pathname === '/') {
      pathname = '/index.html';
    }

    let filePath = path.join(PUBLIC_DIR, pathname);

    // Directory check
    if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
      filePath = path.join(filePath, 'index.html');
    }

    // Auto-fetch missing data or asset files from upstream and cache them locally
    if (!fs.existsSync(filePath) && (pathname.startsWith('/data/') || pathname.startsWith('/_astro/'))) {
      try {
        const upstreamUrl = `https://eu5db.com${req.url}`;
        const data = await fetchUpstreamWithCurl(upstreamUrl);
        if (data && data.length > 0) {
          fs.mkdirSync(path.dirname(filePath), { recursive: true });
          fs.writeFileSync(filePath, data);
          console.log(`Auto-cached missing file: ${pathname} (${data.length} bytes)`);
        }
      } catch (err) {
        console.warn(`Could not auto-fetch upstream ${pathname}:`, err.message);
      }
    }

    // SPA fallback
    if (!fs.existsSync(filePath)) {
      if (fs.existsSync(filePath + '.html')) {
        filePath = filePath + '.html';
      } else if (!path.extname(pathname) || pathname.startsWith('/map') || pathname.startsWith('/browse') || pathname.startsWith('/content')) {
        filePath = path.join(PUBLIC_DIR, 'index.html');
      }
    }

    if (!fs.existsSync(filePath)) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('404 Not Found');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    const headers = {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    };

    res.writeHead(200, headers);
    fs.createReadStream(filePath).pipe(res);
  } catch (err) {
    console.error('Request error:', err);
    res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('500 Internal Server Error');
  }
});

server.listen(PORT, () => {
  console.log(`\n======================================================`);
  console.log(`🚀 EU5DB Map Clone running at: http://localhost:${PORT}/map`);
  console.log(`📁 Static files root: ${PUBLIC_DIR}`);
  console.log(`======================================================\n`);
});
