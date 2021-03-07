@echo off
set /P f1="Enter the number of fonts you wish to delete:"
python.exe font_fingerprint.py %f1%
@pause