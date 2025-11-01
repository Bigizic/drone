#!/usr/bin/env python3
from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import os
import sys
import time
import socket
# import exceptions
import math
# ./connection_template --connect 127.0.0.1:{PORT}

def connectCopter() -> None:
    """
    function to connect to the drone
    """
    connection_string = sys.argv[1]
    vehicle = connect(connection_string, wait_ready=True)
    return vehicle
if __name__ == '__main__':
    v = connectCopter()
    # print([x for x in dir(v)])
