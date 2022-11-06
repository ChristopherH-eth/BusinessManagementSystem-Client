from Network.tcp import newTcp
from Util.funcUtil import funcUtil

'''
@file test_01_tcp.py
@author 0xChristopher
@brief This file tests the Tcp module.
'''

## @brief Test the Tcp() object constructor
def test_CreateTcp():
    assert newTcp
    assert newTcp.Receive() == "Connected to Business Management Server!"

## @brief Test the GetHost() function
def test_GetHost():
    host = newTcp.GetHost()

    assert host == "127.0.0.1"

## @brief Test the Send() and Receive() functions
def test_SendAndReceive():
    fId = "100"
    json = "{\"username\": \"\", \"password\": \"\"}"
    msg = fId + " " + json
    newTcp.Send(msg)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "Login successful"