@echo off
setx NTkLibPath "%cd%"
cd %NTkLibPath%
cls
echo colorama > requirements.txt
echo customtkinter >> requirements.txt
echo start python libraries install script???
echo no - 0
echo yes - 1
set /p userinput=
if %userinput% == 0 echo starting program main... && cls
if %userinput% == 1 echo starting installation program && pip install -r requirements.txt
echo installation program is finished
pause