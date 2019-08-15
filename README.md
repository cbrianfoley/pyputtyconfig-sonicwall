#pyputtyconfig-sonicwall

Just a script to automate configuration of a Sonicwall over the console port using windows, python, and putty

Requires Python3, PuTTY, pyserial, pywinauto, and pywin32. Designed and tested for Windows 10 only

Text files in 'commands' folder are selected from. Commands are piped into a putty window. 
Variables can exist inside of the command file, and should be identified by surrounding variable with '%' (Example: %serial_number%)

Unfortunately, other tasks can't be done while script is running, as all the script is doing is emulating mouse/keyboard actions.