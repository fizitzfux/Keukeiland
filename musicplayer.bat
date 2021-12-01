@ECHO off
:X
echo %H%
echo.
echo     %E% A - ^<indev^> Keukeiland remix %H%
echo     %G% B - {null} %H%
echo     %E% C - {null} %H%
echo     %G% D - {null} %H%
echo     %E% E - {null} %H%
echo     %G% F - {null} %H%
echo     %E% G - {null} %H%
echo     %G% H - {null} %H%
echo     %E% I - {null} %H%
echo     %G% J - {null} %H%
echo     %E% K - {null} %H%
echo     %G% L - {null} %H%
echo     %E% M - {null} %H%
echo     %G% N - {null} %H%
echo     %E% O - {null} %H%
echo     %G% P - {null} %H%
echo     %E% Q - {null} %H%
echo     %G% R - {null} %H%
echo     %E% S - {null} %H%
echo     %G% T - {null} %H%
echo     %E% U - {null} %H%
echo     %G% V - {null} %H%
echo     %E% W - {null} %H%
echo     %G% X - {null} %H%
echo     %E% Y - {null} %H%
echo     %G% Z - {null} %H%
echo     %E% 0 - QUIT %H%                                                                                                            %F%
echo %F%%datime%%B%
choice /N /C abcdefghijklmnopqrstuvwxyz0
IF %ERRORLEVEL% == 1 (echo This song is still in dev!, please try again later.&& GOTO X)
IF %ERRORLEVEL% == 2 (GOTO X)
IF %ERRORLEVEL% == 3 (GOTO X)
IF %ERRORLEVEL% == 4 (GOTO X)
IF %ERRORLEVEL% == 5 (GOTO X)
IF %ERRORLEVEL% == 6 (GOTO X)
IF %ERRORLEVEL% == 7 (GOTO X)
IF %ERRORLEVEL% == 8 (GOTO X)
IF %ERRORLEVEL% == 9 (GOTO X)
IF %ERRORLEVEL% == 10 (GOTO X)
IF %ERRORLEVEL% == 11 (GOTO X)
IF %ERRORLEVEL% == 12 (GOTO X)
IF %ERRORLEVEL% == 13 (GOTO X)
IF %ERRORLEVEL% == 14 (GOTO X)
IF %ERRORLEVEL% == 15 (GOTO X)
IF %ERRORLEVEL% == 16 (GOTO X)
IF %ERRORLEVEL% == 17 (GOTO X)
IF %ERRORLEVEL% == 18 (GOTO X)
IF %ERRORLEVEL% == 19 (GOTO X)
IF %ERRORLEVEL% == 20 (GOTO X)
IF %ERRORLEVEL% == 21 (GOTO X)
IF %ERRORLEVEL% == 22 (GOTO X)
IF %ERRORLEVEL% == 23 (GOTO X)
IF %ERRORLEVEL% == 24 (GOTO X)
IF %ERRORLEVEL% == 25 (GOTO X)
IF %ERRORLEVEL% == 26 (GOTO X)
IF %ERRORLEVEL% == 27 (GOTO EOF)
:EOF
