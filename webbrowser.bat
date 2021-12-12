@ECHO off
set "history_file=%~dp0config\webbrowser.history"
set "wanted_history=20"
(for /f %%a in ('findstr /R /N "^" "%history_file%" ^| find /C ":"') do set history_total=%%a)
set /a "history_load_amount=%history_total%-%wanted_history%"
IF %history_load_amount% LEQ 20 (set "history_load_amount=") else (set "history_load_amount=+%history_load_amount%")
echo %H%%AA%
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
echo type 'quit' to leave the browsing-session.
echo.
echo your browser-history:%A%%HA%
call more %history_load_amount% "%history_file%"
echo %H%
echo %B%
goto x
:load
SET "newtoopen="
IF NOT "%toopen%"=="" (echo %toopen%>>"%~dp0config/webbrowser.history")
echo %H%%AA%
echo.
echo loading webpage...
start "Keukeiland" /b /wait "%~dp0htmlloader.exe" "%toopen%"
echo %B%
:x
SET /P newtoopen="%HA%::"
IF "%newtoopen%"=="" (goto x)
IF "%newtoopen%"=="quit" (goto EOF)
IF "%newtoopen:~0,1%"=="/" (set oldtoopen=%toopen%&& set toopen=%toopen%/..%newtoopen%&& goto load)
IF "%newtoopen:~0,4%"=="http" (set oldtoopen=%toopen%&& set toopen=%newtoopen%&& goto load)
IF "%newtoopen%"=="cd.." (set toopen=%oldtoopen%&& goto load)
IF "%newtoopen:~0,3%"=="cd " (set oldtoopen=%toopen%&& set toopen=%toopen%/../%newtoopen:~3,99%&& goto load)
IF "%newtoopen:~0,1%"=="r" (goto load)
IF 1==1 (echo invalid input, please try again&& goto x)
:EOF
endlocal
