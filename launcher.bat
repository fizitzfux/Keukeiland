@ECHO off
VERIFY OTHER 2>NUL
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
IF %ERRORLEVEL% == 1 (command extentions not available, please update your cmd.exe)
if "%1"=="-f" (goto run)
for /f "tokens=4-5 delims=. " %%i in ('ver') do set osver=%%i.%%j
if "%osver%" == "10.0" (goto run) else (goto NOVER)

:run
SET "mmm="
SET ESC=
SET A=%ESC%[40m
SET B=%ESC%[41m
SET C=%ESC%[42m
SET D=%ESC%[43m
SET E=%ESC%[44m
SET F=%ESC%[45m
SET G=%ESC%[46m
SET H=%ESC%[47m
SET AA=%ESC%[30m
SET BA=%ESC%[31m
SET CA=%ESC%[32m
SET DA=%ESC%[33m
SET EA=%ESC%[34m
SET FA=%ESC%[35m
SET GA=%ESC%[36m
SET HA=%ESC%[37m
SET version=1.0.0.alpha
title Keukeiland
GOTO y
:x
ping 192.168.0.0 -n 1 -w 750 >NUL
:y
echo %H%
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
SET /A mmm=%mmm%+1
IF %mmm%==1 (echo %B% 10         %A%&&echo Loading graphical interface...&&goto x)
IF %mmm%==2 (echo %B% 20                     %A%&&echo Setting CodeBase...&&chcp 65001&&goto x)
IF %mmm%==3 (echo %B% 30                                 %A%&&echo Building config...&&start /b /wait cmd.exe /C "%~dp0setup.bat"&&goto x)
IF %mmm%==4 (echo %B% 40                                             %A%&&echo Checking for updates...&&call "%~dp0ckupdate.bat" 1.0.0.alpha&&goto x)
IF %mmm%==5 (echo %B% 50                                                         %A%&&echo Loading libraries...&&goto x)
IF %mmm%==6 (echo %B% 60                                                                     %A%&&echo Loading libraries...&&goto x)
IF %mmm%==7 (echo %B% 70                                                                                 %A%&&echo Loading libraries...&&goto x)
IF %mmm%==8 (echo %B% 80                                                                                             %A%&&echo Loading libraries...&&goto x)
IF %mmm%==9 (echo %B% 90                                                                                                         %A%&&echo Loading libraries...&&goto x)
IF %mmm%==10 (echo %B% 100                                                                                                                    %A%&&echo Starting main menu...&&goto x)
IF %mmm%==11 (echo %B%&&pause&&goto done)
goto error
:done
echo %A%
START /min cmd.exe /C "%~dp0startup.bat"
call "%~dp0main.bat"
goto EOF
:NOVER
echo Your operating system is not officialy supported, to still run this app at your own risk use the argument -f
pause
goto EOF
:error
echo %A% an error has occured, please try again.
pause
goto EOF
:EOF
erase /Q "%~dp0temp\*"
echo %A%
endlocal
