@ECHO off
:Y
date /T>"%~dp0temp\date.var"&& time /T>"%~dp0temp\time.var"
SET /P date=<"%~dp0temp\date.var" && SET /P time=<"%~dp0temp\time.var"
SET datime=%date%%time%
:X
echo %H%
echo.
echo      %G%                %H%     %A%                %H%
echo      %G% %E%     %G%          %H%     %A%                %H%
echo      %G% %E%        %G%       %H%     %A%                %H%
echo      %G% %E%           %G%    %H%     %A%                %H%
echo      %G% %E%              %G% %H%     %A%                %H%
echo      %G% %E%           %G%    %H%     %A%                %H%
echo      %G% %E%        %G%       %H%     %A%   %C% %A%   %C%  %A%   %C% %A%   %H%
echo      %G% %E%     %G%          %H%     %A%     %C% %A%    %C% %A%     %H%
echo      %G%%AA%1 music player%HA%  %H%     %A%%HA%2 spotify%HA%       %H%
echo.
echo.
echo                                                                                         %G%                %H%
echo                                                                                         %G%       %E%  %G%       %H%
echo                                                                                         %G%  %E%   %G%  %E%  %G%  %E%   %G%  %H%
echo                                                                                         %G% %E%   %G%   %E%  %G%   %E%   %G% %H%
echo                                                                                         %G% %E%  %G%    %E%  %G%    %E%  %G% %H%
echo                                                                                         %G% %E%  %G%    %E%  %G%    %E%  %G% %H%
echo                                                                                         %G% %E%   %G%        %E%   %G% %H%
echo                                                                                         %G%  %E%            %G%  %H%
echo                                                                                         %G%%AA%0 exit%HA%          %H%
echo.
echo.
echo.
echo.
echo.
echo.
echo                                                                                                                 %A%A%B%B%C%C%D%D%E%E%F%F%G%G%H%%AA%H%HA%%F%
echo %datime%%B%
choice /C 1234567890rc /N /T 30 /D r
IF %ERRORLEVEL% == 1 (call "%~dp0musicplayer.bat"&& GOTO Y)
IF %ERRORLEVEL% == 2 (call "%~dp0spotify.bat"&& GOTO Y)
IF %ERRORLEVEL% == 3 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 4 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 5 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 6 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 7 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 8 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 9 (call "%~dp0.bat"&& GOTO Y)
IF %ERRORLEVEL% == 10 (echo %A%&& GOTO EOF)
IF %ERRORLEVEL% == 11 (GOTO Y)
IF %ERRORLEVEL% == 12 (echo %A%&& call "%~dp0credits.bat"&& GOTO Y)
IF %ERRORLEVEL% == 0 (echo %A%Process terminated, QUITTING...&& GOTO EOF)
IF %ERRORLEVEL% == 255 (echo %A%ERRROR DETECTED, QUITTING....&& GOTO EOF)
GOTO X
:EOF