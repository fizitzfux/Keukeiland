@ECHO off
ping lettuce.ddns.net -n 1 -w 750 >NUL
IF %ERRORLEVEL% GTR 0 (goto con_error)
start /min /wait powershell.exe -command "Invoke-WebRequest "http://lettuce.ddns.net:81/updateservice/latest.version" -OutFile '%~dp0temp\updt.version'"
IF %ERRORLEVEL% GTR 0 (goto con_error)
SET /P latest_version=<"%~dp0temp\updt.version"
IF "%1" == "%latest_version%" (echo You are running the latest version.&&goto EOF)
choice /C yn /T 10 /D n /M "update found, do you want to update?"
IF %ERRORLEVEL% == 1 (goto update)
IF %ERRORLEVEL% == 2 (goto cancel)
:update
echo starting update.
start /min /wait powershell.exe -command "Invoke-WebRequest "http://lettuce.ddns.net:81/updateservice/update.bat" -OutFile '%~dp0temp\updt.update.bat'"
cmd.exe /c "%~dp0temp\updt.update.bat"
echo update done.
goto cleanup
:cancel
echo update cancelled.
goto cleanup
:con_error
echo no connection to server, please check your firewall or try again later.
pause
goto EOF
:cleanup
erase /Q /F "%~dp0temp\updt.*"
goto EOF
:EOF
