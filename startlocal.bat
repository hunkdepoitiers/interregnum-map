@echo off
title Interregnum Map - Localhost
cd /d "%~dp0"
echo ======================================================
echo   Interregnum Yerel Harita Baslatiliyor...
echo   Adres: http://localhost:3000/map
echo ======================================================
echo.

start "" "http://localhost:3000/map"
node local_server.mjs
pause
