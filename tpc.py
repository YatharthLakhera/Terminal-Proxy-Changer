#!/usr/bin/python3

import sys, os, re

## System Information Paths(Path of Files)-----------------------------------------------


## If you want to change the path of the environment or apt files location
## then change the location or path here in the below variables

path_environment = "/etc/environment"
path_apt = "/etc/apt/apt.conf.d"

if os.path.exists(path_environment): pass
else:
    print("Default path to environment file '/etc/environment' does not exist.")
    print("Please change the variable 'path_environment' in the file to correct path of environment file.")
    print("For more information please read README.txt file.")
    sys.exit(0)

if os.path.exists(path_apt): pass
else:
    if os.path.exists("/etc/apt/apt.conf"): path_apt = "/etc/apt/apt.conf"
    else:
        print("Default path to apt directory '/etc/apt/apt.conf' does not exist.")
        print("Please change the variable 'path_apt' in the file to correct path of apt.conf file or directory.")
        print("For more information please read README.txt file.")
        sys.exit(0)

## Command Line Arguments--------------------------------------------------------------

cmdargs = sys.argv 


if len(cmdargs)>2: 
    print("Usage: tpc [-option]")
    print("where option include:\n   -r\treset the proxy settings to its original configuration")
    print("    -v\tversion of script\n    -help\thelp")
    sys.exit(0)

if len(cmdargs)>1:

    if cmdargs[1]=='-v' or cmdargs[1]=="-version":
        print("Terminal Proxy Changer version 1.0")
        sys.exit(0)

    elif cmdargs[1]=='-help':
        print("Usage: tpc [-option]")
        print("where option include:\n    -r\treset the proxy settings to its original configuration")
        print("    -v\tversion of script\n    -help\thelp")
        sys.exit(0)

    ## Reseting Proxy configuration-------------------------------------

    elif cmdargs[1]=='-r':
        fr_environment = open(path_environment,"r")
        data = ""
        for line in fr_environment:
            line = line.strip()
            if re.search('^[hHfF][tT]+[pP]_[pP][rR][oO][xX][yY]=http://.*/', line) or re.search('^[hHfF][tT]+[pP][sS]_[pP][rR][oO][xX][yY]=http://.*/', line) or re.search('^[nN][oO]_[pP][rR][oO][xX][yY]=.*', line):
                continue
            data += line+"\n" 
        fr_environment.close()
        fw_environment = open(path_environment,"w")
        fw_environment.write(data)
        fw_environment.close()

        if os.path.exists(path_apt+"/proxy"):
            os.remove(path_apt+"/proxy")
        sys.exit(0)
 
    else:
        print("Unrecognized option:",cmdargs[1])
        print("Error: A fatal exception has occurred. Program will exit.")
        sys.exit(0)
 
## User Inputs-----------------------------------------------------------------

print("Terminal Proxy Changer version 1.0")

user = input("Username: ")
pas =  input("Password: ")
prox = input("Proxy   : ")
port = input("Port    : ")

if user=="" and pas=="":
    net = prox+":"+port
else:
    net = user+":"+pas+"@"+prox+":"+port

## Changing Environment Variables------------------------------------


fr_environment = open(path_environment,"r")
data = ""
for line in fr_environment:
    line = line.strip()
    if re.search('^[hHfF][tT]+[pP]_[pP][rR][oO][xX][yY]=http://.*/', line) or re.search('^[hHfF][tT]+[pP][sS]_[pP][rR][oO][xX][yY]=http://.*/', line) or re.search('^[nN][oO]_[pP][rR][oO][xX][yY]=.*', line):
        continue
    data += line+"\n" 
fr_environment.close()

fw_environment = open(path_environment,"w")
fw_environment.write(data)
fw_environment.write("http_proxy=http://"+net+"/\n")
fw_environment.write("https_proxy=http://"+net+"/\n")
fw_environment.write("ftp_proxy=http://"+net+"/\n")
fw_environment.write('no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"\n')
fw_environment.write("HTTP_PROXY=http://"+net+"/\n")
fw_environment.write("FTP_PROXY=http://"+net+"/\n")
fw_environment.write("HTTPS_PROXY=http://"+net+"/\n")
fw_environment.write('NO_PROXY="localhost,127.0.0.1,localaddress,.localdomain.com"\n')
fw_environment.close()


## Changing apt proxy configuration--------------------------------

fw_apt = open(path_apt+"/proxy","w")
fw_apt.write('Acquire::http::proxy "http://'+net+'/";\n') 
fw_apt.write('Acquire::https::proxy "https://'+net+'/";\n') 
fw_apt.write('Acquire::ftp::proxy "ftp://'+net+'/";\n') 
    

