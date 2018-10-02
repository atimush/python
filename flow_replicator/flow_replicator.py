#!/usr/bin/env python

__author__ = 'Andrei Timush'

import logging
from daemonize import Daemonize
import socket
import sys

# Inline configuration
listen_ip = '198.51.100.5' # Local IP
listen_port = 2055  # Local Port

destinations = [
                {'dst': '198.51.100.10', 'port': 2055},  # 1st Flow Collector
                {'dst': '198.51.100.20', 'port': 2056}  # 2nd Flow Collector
               ]

pid = "/var/run/flow_replicator.pid"  # Process PID
log_file = "/var/log/flow_replicator.log"  # Process Log file

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')
fh = logging.FileHandler(log_file, "a")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
pr_files = [fh.stream.fileno()]


def main():
    logger.info('Daemon Started')
    # Create Datagram(UDP) socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        logger.info("Socket succesfully created")
    except socket.error, msg:
        logger.error("Failed to create socket. Error Code: %s Message: %s" % (str(msg[0]), msg[1]))
        sys.exit(2)

    # Bind socket to local IP and port
    try:
        s.bind((listen_ip, listen_port))
        logger.info("Starting UDP Listener on %s:%s" % (listen_ip, listen_port))
    except socket.error, msg:
        logger.error("Bind failed. Error Code: %s Message: %s" % (str(msg[0]), msg[1]))
        sys.exit(2)

    # Replicate data to destinations
    sources = []
    while 1:
        data, addr = s.recvfrom(32768)
        src = addr[0]
        if src not in sources:
            sources.append(src)
            logger.info("Replicating data from %s to %s" % (src, str(destinations)))
        for destination in destinations:
            s.sendto(data, ('%s' % destination['dst'], destination['port']))


daemon = Daemonize(app="flow_replicator", pid=pid, action=main, keep_fds=pr_files)
daemon.start()
