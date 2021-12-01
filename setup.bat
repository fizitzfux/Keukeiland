@ECHO off
set /A count=0
if exist "%~dp0temp\*" (goto 1) else (echo making temp directory...&& set /A count=%count%+1&& mkdir "%~dp0temp")
:1
if exist "%~dp0config\*" (goto 2) else (echo making config directory...&& set /A count=%count%+1&& mkdir "%~dp0config")
:2
if exist "%~dp0config\.config\*" (goto 3) else (echo making spotify config directory...&& set /A count=%count%+1&& mkdir "%~dp0config\.config")
:3
if exist "%~dp0config\.config\spotify.toml" (goto 4) else (
echo building spotify config...
set /A count=%count%+1
echo [theme]>>"%~dp0config\.config\spotify.toml"
echo background = "#181818">>"%~dp0config\.config\spotify.toml"
echo primary = "#F1F1F1">>"%~dp0config\.config\spotify.toml"
echo secondary = "#DCDCDC">>"%~dp0config\.config\spotify.toml"
echo title = "#1ED760">>"%~dp0config\.config\spotify.toml"
echo playing = "#1ED760">>"%~dp0config\.config\spotify.toml"
echo playing_selected = "#1ED760">>"%~dp0config\.config\spotify.toml"
echo playing_bg = "#181818">>"%~dp0config\.config\spotify.toml"
echo highlight = "#1DB954">>"%~dp0config\.config\spotify.toml"
echo highlight_bg = "#000000">>"%~dp0config\.config\spotify.toml"
echo error = "#FFE4E4">>"%~dp0config\.config\spotify.toml"
echo error_bg = "#A50000">>"%~dp0config\.config\spotify.toml"
echo statusbar = "#000000">>"%~dp0config\.config\spotify.toml"
echo statusbar_progress = "#00AC4C">>"%~dp0config\.config\spotify.toml"
echo statusbar_bg = "#00AC4C">>"%~dp0config\.config\spotify.toml"
echo cmdline = "#CBFFDE">>"%~dp0config\.config\spotify.toml"
echo cmdline_bg = "#444444">>"%~dp0config\.config\spotify.toml"
)
:4
if exist "%~dp0config\user.ini" (goto 5)  else (echo No user has been set up&& set /P username="Please enter your username "&& echo %username%>>"%~dp0config\user.ini" && set /A count=%count%+1)
:5
if %count% GTR 0 (echo config successfully build.) else (echo config already build.)
