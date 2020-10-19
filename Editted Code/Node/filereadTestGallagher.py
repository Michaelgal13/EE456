# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:31:12 2020

@author: MikeyG
"""
def readDeviceInfo():
    f = open("deviceInfo.txt", "r")
    devID = f.readline().split()
    # print(devID)
    i = 0
    for x in devID:
        devID[i] = int(x, 16)
        i = i + 1
    devID = bytearray(devID)
    # print(bytearray(devID))
    netkey = f.readline().split()
    # print(devID)
    i = 0
    for x in netkey:
        netkey[i] = int(x, 16)
        i = i + 1
    netkey = bytearray(netkey)
    appkey = f.readline().split()
    # print(devID)
    i = 0
    for x in appkey:
        appkey[i] = int(x, 16)
        i = i + 1
    appkey = bytearray(appkey)

    return devID, netkey, appkey

