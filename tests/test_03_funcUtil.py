from Util.funcUtil import funcUtil
from HR.employee import employee
from Network.tcp import newTcp

'''
@file test_03_funcUtil.py
@author 0xChristopher
@brief This file tests the FuncUtil module.
'''

## @brief Test the IsValid() function. It should return true if the function id is valid.
def test_IsValid():
    fId = "100"
    result = funcUtil.IsValid(fId)

    assert result == True

## @brief Test the IsValid() function with an invalid function id - should return false
def test_IsValidFalse():
    fId = "99"
    result = funcUtil.IsValid(fId)

    assert result == False

## TODO: Test DirectInput()

## @brief Test the WaitForReply() function
def test_WaitForReply():
    username = ""
    password = ""

    employee.Login(username, password)
    result = funcUtil.WaitForReply()
    newTcp.Receive()

    assert result == True

## @brief Test the WaitForReply function timeout - should return false
def test_WaitForReplyTimeout():
    result = funcUtil.WaitForReply()

    assert result == False