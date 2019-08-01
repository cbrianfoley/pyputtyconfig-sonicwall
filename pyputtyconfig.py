#Requires PuTTY, pyserial, pywinauto, and pywin32. Designed and tested for Windows 10 only

import pywinauto
import time
import serial.tools.list_ports
import os

#variable ID. Use this character to identify what a variable is in your command text file (Example: +serno+)
varid = '+'

#get available COM ports for serial connection
def check_serial_port(name):
    '''returns valid COM Port.'''
    try:
        cdc = next(serial.tools.list_ports.grep(name))
        return cdc.__str__().split()[0]
    except StopIteration:
        msg = 'device {} not found. '.format(name)
        msg += 'available devices are: '
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            msg += '{},'.format(str(p))
        raise ValueError(msg)

#display available COM ports and ask user to select
msg = 'Available COM devices are: \n'
ports = list(serial.tools.list_ports.comports())
for p in ports:
    msg += '\n{},'.format(str(p))
print(msg)
port = input('\nEnter COM port:\n')
check_serial_port(port)

#display available config files and ask user to select
print("\nAvailable config files:")
full_path = os.path.realpath(__file__)
availablefiles = list(os.listdir(os.path.dirname(full_path)+'\commands'))
for i in availablefiles:
    index = availablefiles.index(i)
    print(index, i)
index = int(input("\nEnter the number corresponding to the file you would like to use:\n"))
print(os.path.dirname(full_path)+'\commands\\'+availablefiles[index])
file = os.path.dirname(full_path)+'\commands\\'+availablefiles[index]

#Get variables from user. These variables should exist in your commands file separated by '+' (Example: +serno+)
############BUG: These variables will be ran through eval() when coming into the script. Some characters will not work#################
olduser = input('\nEnter the current username of the Sonicwall:\n')
oldpass = input('\nEnter the current password of the Sonicwall:\n')
serno = input('\nEnter the serial number of the Sonicwall:\n')
activatekey = input('\nEnter the activation code of the Sonicwall (can be found on the device next to the serial number):\n')
fwname = input('\nEnter the friendly firewall name (Must be 8 characters minimum):\n')
newpass = input('\nEnter password-to-be of the new Sonicwall (Must be 8 characters minimum):\n')
lan = input('\nEnter the LAN IP to-be of the new Sonicwall:\n')

#make the list of commands from the file
with open(file) as f:
        commands = []
        for line in f:
                line = line.replace('\n','')
                line = line.replace(' ','{SPACE}')
                if varid in line:
                    line = line.split(varid)
                    for idx, val in enumerate(line):
                        if (idx % 2) == 1:
                            line[idx] = eval(val)
                    s = ""
                    line = s.join(line)
                commands.append(line)

#create the PuTTY window and log in
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
    time.sleep(.3)