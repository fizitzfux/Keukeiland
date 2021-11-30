@ECHO off
ping lettuce.ddns.net -n 1 -l 1 -w 750>NUL
IF %ERRORLEVEL% GTR 0 (goto z)
start /min /wait powershell.exe Invoke-WebRequest "http://lettuce.ddns.net:81/updateservice/latest.version" -OutFile ".\temp\updt.version"
SET /P latest_version=<".\temp\updt.version"
IF "%1" == "%latest_version%" (echo You are running the latest version.&&goto EOF)
choice /C yn /T 10 /D n /M "update found, do you want to update?"
IF %ERRORLEVEL% == 1 (goto x)
IF %ERRORLEVEL% == 2 (goto y)
:x
echo starting update.
start /min /wait powershell.exe Invoke-WebRequest "http://lettuce.ddns.net:81/updateservice/update.bat" -OutFile ".\temp\updt.update.bat"
cmd.exe /c ".\temp\updt.update.bat"
echo update done.
goto EOF
:y
echo update cancelled.
goto EOF
:z
echo no internet connection.
goto EOF
:EOF
erase /Q "%~dp0temp\updt.*">NUL