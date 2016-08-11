This python script help to change Terminal Proxy

Installation

1. First download the python file and move it to a suitable location, open the file and set the path for path_apt and path_environment variable if not correct.

2. Now to make the file executable type the following command in the terminal:

   sudo chmod +x tpc.py

3. Now to open file from terminal directly as "tpc" enter following command in terminal
  
   sudo ln -s [filepath form root]/tpc.py /usr/bin/tpc
   
  Example

   ln -s /home/username/Desktop/tpc /usr/bin/tpc

4. Now you can execute it directly from terminal.

   For executing the file use super user with it as follows:

     sudo tpc
     sudo tpc -v
     sudo tpc -r
     sudo tpc -help

Commands available:

tpc              : Used to change proxies

tpc -v           : to return its version
    -version

tpc -help        : for help
 
tcp -r           : to reset proxies
