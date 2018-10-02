### IPv4 UDP Replicator. 
### Could be used to replicate sFlow or cFlow to multiple targets on custom ports.

#### How to use:
* Install python modules using the command:
```sh
# sudo pip install logging daemonize
```
* Adjust the 'Inline configuration' section in the script.
* Make file executable and run it.

### IMPORTANT:
* Has not been tested with Python 3.
* The script is a Linux Daemon. The service controls via SysV or Systemd have not been implemented.
