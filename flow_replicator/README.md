## IPv4 Flow Replicator

### Description:
Might be useful to replicate sFlow or cFlow to multiple targets on custom ports.
Each datagram is send to every target.

#### How to use:
* Install Python modules using the command:
```sh
# sudo pip install logging daemonize
```
* Adjust the 'Inline configuration' section in the script.
* Make file executable and run it.

### IMPORTANT:
* Has not been tested with Python 3.
* The script is a Linux Daemon. The service controls via SysV or Systemd has not been implemented.
