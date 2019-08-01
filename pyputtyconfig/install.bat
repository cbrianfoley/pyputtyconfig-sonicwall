@echo off
echo Installing PuTTY
PuTTY.msi /quiet
echo Installing Python and dependencies
Python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=c:\Python
C:\Python\Scripts\pip.exe install pywinauto
C:\Python\Scripts\pip.exe install pywin32
C:\Python\Scripts\pip.exe install pyserial