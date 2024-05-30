@echo off
setlocal EnableDelayedExpansion

rem Websites to block
set websites=example.com www.example.com facebook.com www.facebook.com

rem Hosts file location
set hosts_file=%SystemRoot%\System32\drivers\etc\hosts

rem Take ownership of the hosts file
takeown /f %hosts_file% >nul
icacls %hosts_file% /grant %username%:F >nul

rem Add entries to the hosts file
for %%A in (%websites%) do (
    echo 127.0.0.1 %%A >> %hosts_file%
)

rem Flush DNS cache
ipconfig /flushdns

echo Websites blocked successfully.
pause
