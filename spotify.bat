@ECHO off
start "Keukeiland" /ABOVENORMAL /B /wait "%~dp0spotify.exe" -b "%~dp0config" -c "spotify.toml"
