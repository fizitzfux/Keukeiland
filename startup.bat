@ECHO off
date /T>"%~dp0temp\date.var"&& time /T>"%~dp0temp\time.var"
SET /P date=<"%~dp0temp\date.var" && SET /P time=<"%~dp0temp\time.var"
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set localip=%%a
for /f %%a in ('powershell Invoke-RestMethod api.ipify.org') do set publicip=%%a
echo ^<mark name="START"/^> >>"%~dp0temp\startup.voice"
echo ^<speak^> >>"%~dp0temp\startup.voice"
echo ^<p^> >>"%~dp0temp\startup.voice"
echo ^<s^> >>"%~dp0temp\startup.voice"
echo Welcome to ^<say-as interpret-as="characters"^> Keukeiland ^</say-as^> . >>"%~dp0temp\startup.voice"
echo ^</s^> >>"%~dp0temp\startup.voice"
echo ^<s^> >>"%~dp0temp\startup.voice"
echo Your version number is ^<say-as interpret-as="characters"^>%1^</say-as^> . >>"%~dp0temp\startup.voice"
echo Today is ^<say-as interpret-as="date" format="ddmmyyyy" detail="2"^> %date% ^</say-as^> , at ^<say-as interpret-as="time" format="hhmm" detail="1"^> %time% ^</say-as^> . >>"%~dp0temp\startup.voice"
echo ^</s^> >>"%~dp0temp\startup.voice"
echo ^</speak^> >>"%~dp0temp\startup.voice"
echo ^</mark name="END"/^> >>"%~dp0temp\startup.voice"
call "%~dp0soundengine.bat" "%~dp0temp\startup.voice"
erase /F "%~dp0temp\startup.voice"