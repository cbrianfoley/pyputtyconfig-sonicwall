#pyputtyconfig-sonicwall
Just a script to automate configuration of a Sonicwall over the console port using windows, python, and putty

Install files and dependencies are located in pyputtyfiles
Requires Python3, PuTTY, pyserial, pywinauto, and pywin32. Designed and tested for Windows 10 only

Text files in 'commands' folder are selected from. Commands are piped into a putty window. 
Variables can exist inside of the command file, and should be identified by surrounding variable with '+' (Example: +serno+)

Unfortunately, other tasks can't be done while script is running, as all the script is doing is emulating mouse/keyboard actions.

KNOWN BUGS:
    using eval() in this manner is considered bad practice
    Some characters will not be accepted if they are in one of your variables