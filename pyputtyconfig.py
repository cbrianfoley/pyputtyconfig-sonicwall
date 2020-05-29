#Requires PuTTY, pyserial, pywinauto, and pywin32. Designed and tested for Windows 10 only

import pywinauto
import time
import serial.tools.list_ports
import os

#variable ID. Use this character to identify what a variable is in your command text file (Example: %serial_number%)
varid = '%'

print('''
Select connection type: \n
1)LAN
2)Console
''')

select = int(input('Selection:'))
while select != (1 or 2):
    select = int(input('Please input a valid selection: '))

if select is 1:
    sship = str(input('Please enter the IP you wish to connect to: '))

if select is 2:
    #display available COM ports and ask user to select
    print('\nAvailable COM devices are: \n')
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        index = ports.index(p)
        print(index, p)
    selectport = int(input('\nChoose a COM port:\n'))
    port = str(ports[selectport])
    port = port[:4]

#display available config files and ask user to select
print("\nAvailable config files:\n")
full_path = os.path.realpath(__file__)
availablefiles = list(os.listdir(os.path.dirname(full_path)+'\commands'))
for i in availablefiles:
    index = availablefiles.index(i)
    print(index, i)
selectfile = int(input("\nChoose the config file you would like to use:\n"))
file = os.path.dirname(full_path)+'\commands\\'+availablefiles[selectfile]

#prompt for old u/p
print('\nPlease enter the current username and password to log into the Sonicwall')
olduser = input('Username:\n')
oldpass = input('Password:\n')

#parse and make the list of commands from the file, prompting for variables along the way
with open(file) as f:
    commands = []
    for line in f:
        line = line.replace('\n','')
        line = line.replace(' ','{SPACE}')
        if varid in line:
            line = line.split(varid) #use .split to separate into a list
            for idx, val in enumerate(line):
                if (idx % 2) == 1: #every other item in this list will be a variable, so prompt for its value
                    val = str(input('Enter value for variable found in command file \"'+val+'\":'))
                    line[idx] = val
            s = ""
            line = s.join(line)
        commands.append(line)

#create the PuTTY window and log in
if select is 1:
    app = pywinauto.Application().start(cmd_line='putty.exe -ssh '+olduser+'@'+sship+' 22')
    putty = app.Putty
    putty.wait('ready')
    time.sleep(5)
    putty.type_keys('{ENTER}')
    time.sleep(1)
    putty.type_keys(oldpass)
    putty.type_keys('{ENTER}')
    time.sleep(1)
    
if select is 2:
    app = pywinauto.Application().start(cmd_line='putty.exe -serial '+port+' -sercfg 115200,8,1,n,N')
    putty = app.Putty
    putty.wait('ready')
    time.sleep(1)
    putty.type_keys('{ENTER}')
    time.sleep(1)
    putty.type_keys(olduser)
    putty.type_keys('{ENTER}')
    time.sleep(1)
    putty.type_keys(oldpass)
    putty.type_keys('{ENTER}')
    time.sleep(1)
                
#type away
for cmd in commands:
    putty.type_keys(cmd)
    putty.type_keys('{ENTER}')
    time.sleep(.4)
