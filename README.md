### Terminal-Proxy-Changer

This python script help to change Terminal Proxy so install python3 if you don't have it already.

### Installation

1. First download the python file and move it to a suitable location, open the file and set the path for path_apt and path_environment variable if not correct.

2. Now to make the file executable type the following command in the terminal:

   sudo chmod +x tpc.py

3. Now to open file from terminal directly as command_name(i.e. "tpc") enter following command in terminal
  
   sudo ln -s [filepath from root]/tpc.py /usr/bin/command_name
   
  Example

   ln -s /home/username/Desktop/tpc /usr/bin/tpc

4. Now you can execute it directly from terminal.

   For executing the file use super user with it as follows:

  > sudo tpc
  > sudo tpc -v
  > sudo tpc -r 
  > sudo tpc -help

### Commands available:

> tpc              : Used to change proxies

> tpc -v           : to return its version

> tpc -help        : for help
 
> tcp -r           : to reset proxies


### Licence

[GNU General Public License v3.0](https://github.com/YatharthLakhera/Terminal-Proxy-Changer/blob/master/LICENSE)
