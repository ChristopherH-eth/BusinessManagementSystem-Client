# Imports
from enum import Enum

##
# @file funcUtil.py
# @author 0xChristopher
# @brief
##

class FuncUtil(Enum):
    addEmployee = 100
    removeEmployee = 101
    updateEmployee = 102

    # Functions
    # @brief The isValid() function checks if a function id is valid
    # @param cls The enum class containing function ids
    # @param fId The function id number
    def isValid(cls, fId):
        convertedFId = 0
        
        try:
            convertedFId = int(fId)
        except:
            pass

        values = set(item.value for item in FuncUtil)
        return convertedFId in values