# EU5DB Interactive Map Clone (Europa Universalis V)

[https://eu5db.com/map](https://eu5db.com/map) sitesinin bire bir çalışan, tam işlevsel WebGL tabanlı yerel klonu.

## Özellikler

- **Bire Bir WebGL Harita Motoru**: 1337 yılı başlangıç tarihi ile tüm dünya haritası, ülke sınırları, eyaletler (provinces), konumlar (locations), nehirler, yollar ve deniz bölgeleri.
- **Tüm Harita Modları (Map Modes)**:
  - Political (Siyasi)
  - Culture (Kültür)
  - Religion (Din)
  - Population (Nüfus & Sosyal Sınıflar: Asiller, Din Adamları, Burjuva, Köylüler, Köleler, Kabileler)
  - Raw Materials / Goods (Hammadde ve Ticaret Malları)
  - Climate (İklim), Topography (Topoğrafya), Vegetation (Bitki Örtüsü)
  - Location, Province, Area, Region, Subcontinent, Continent
- **Katmanlar & Ayarlar (Layers)**: Nehirler (Rivers), Yollar (Roads), İsimler (Names), Tabi Ülkeler (Subjects), Sınır Çizgileri (Mode, Province, Location Borders).
- **Detay & İnceleme Paneli**: Tıklanan herhangi bir konuma ait kültür, din, nüfus dağılımı, hammadde ve bağlı olduğu ülke bilgileri.
- **Arama Paleti & Filtreler**: Sol alt filtre kutusu, Ctrl+K arama çubuğu ve 1.500'den fazla ülkenin listesi.
- **Türkçe & İngilizce Dil Desteği**: Arayüz ve harita isimleri Türkçe ve İngilizce dahil çoklu dil desteğiyle çalışır.
- **Tam Bağımsız & Sıfır Bağımlılık**: Harici npm paketi kurmaya gerek yoktur (`node:http` yerleşik modülü kullanılır).

## Kurulum ve Çalıştırma

Proje dizinine gidin ve sunucuyu başlatın:

```bash
# Proje dizinine geçiş
cd "C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone"

# Sunucuyu başlatma
node server.mjs
# veya
npm start
```

Tarayıcınızda açın:
👉 **[http://localhost:3000/map](http://localhost:3000/map)** veya **[http://localhost:3000/](http://localhost:3000/)**

## Dizin Yapısı

- `public/`: WebGL motoru, CSS, WebAssembly/WebWorker ve Astro JS paketleri.
- `public/data/`: 1337 senaryosu, coğrafya, konum bitmap'leri (`locations.bin.gz`), nehirler, bağlantılar, isimler ve ülke verileri.
- `cache/`: Dinamik detay sorguları için yerel önbellek dizini.
- `server.mjs`: Sıfır bağımlılıklı, yüksek performanslı yerel sunucu ve otomatik önbellek mekanizması.
