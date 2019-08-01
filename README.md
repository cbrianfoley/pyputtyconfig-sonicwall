#puttypyconfig
Just a script to automate configuration of a Sonicwall over the console port using windows, python, and putty

Install files and dependencies are located in pyputtyfiles

Requires PuTTY, pyserial, pywinauto, and pywin32. Designed and tested for Windows only

Text files in 'commands' folder can be selected from. Commands are piped into a putty window. Variables can exist inside of the command file, and should be identified by surrounding variable with '+' (Example: +serno+)

Unfortunately, other tasks can't be done while script is running, as all the script is doing is emulating mouse/keyboard actions.

KNOWN BUGS:
    using eval() is bad practice and can lead to weird issues if your variables contain non-standard characters.