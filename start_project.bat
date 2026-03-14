@echo off
echo ==============================================
echo   STARTING BINANCE TRACKER PIPELINE
echo ==============================================

:: 1. Shut down any old instances and build the new one
docker-compose down
docker-compose up -d --build

echo.
echo Waiting for Database to initialize (10s)...
timeout /t 10 /nobreak > nul

echo.
echo Pipeline is now LIVE!
echo.
echo To see live data logs, run:
echo docker-compose logs -f app
echo.
echo To see the database, run:
echo docker-compose exec db mysql -u root -pwearegoingtomakeit binance
echo ==============================================
pause