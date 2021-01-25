# Linux

## 1. Fish Tar 
Please provide the command to create a tar archive named fish.tar.gz that contains all files from the “fish” directory. 
Be sure the resulting file is compressed.

`tar -czvf fish.tar.gz fish`


## 2. Connections Exhausted
You are responsible for a server program that has been written to handle 5000 parallel open connections and requests. 
Unfortunately, at around 1000 connections, it stops accepting new connections. No CPU or RAM limits have been hit, and 
the server continues to be underutilized, but the program still stops around 1000 connections. Describe the methods and 
procedures you would use to troubleshoot. Include commands and theories as to what may be the root cause.



## 3. Bash my Keyboard
Bash, KSH, and CSH are all examples of what? How does one change their preference for one vs another?

Bash, KSH, and CSH are all examples of shells in Linux. 

## 4. System Examination
Provide examples of 4 commands and arguments that can be used to examine utilized system resources on a linux machine. 
Explain what each one does.

`cat /proc/meminfo` - used to check real time information about system's memory utilization

`free` - displays the amount of physical and swap memory used

`vmstat` - provides the general information of memory and CPU activity

`top` - used to check memory and CPU usage per activity


## 5. OpenSSH Authentication
Describe the process for enabling public key authentication to a user account on linux. 
Explain the difference between the two keys utilized.

1. First we need to generate a SSH key pair on the local machine of a user account using `ssh-keygen`. 
2. After that, we need to enable SSH based authentication on the server (if not already enabled).
3. Add the public key that is generated using `ssh-keygen` inside the `.ssh` directory on the remote server. 

The two types of keys utilized are public and private keys. The public key is basically stored on the remote server 
and establishes a link to local machine using the inherent private key that is only stored on a local machine. 
