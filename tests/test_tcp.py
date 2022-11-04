from Network.tcp import Tcp

'''
@file test_tcp.py
@author 0xChristopher
@brief This file tests the Tcp module.
'''

## @brief Test the Tcp() object constructor
def test_CreateTcp():
    tcp = Tcp()

    assert tcp

## @brief Test the GetHost() function
def test_GetHost():
    tcp = Tcp()
    host = tcp.GetHost()

    assert host == "127.0.0.1"

## @brief Test the Send() function
def test_Send():
    tcp = Tcp()
    fId = "100"
    json = "{\"username\": \"\", \"password\": \"\"}"
    msg = fId + " " + json
    tcp.Send(msg)

    assert tcp.Receive()