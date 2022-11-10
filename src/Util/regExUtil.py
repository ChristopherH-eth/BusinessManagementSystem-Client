# Imports
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from Log.log import log

'''
@file regExUtil.py
@author 0xChristopher
@brief This file contains functions for checks against regular expressions.
'''

class RegExUtil():
    ##
    # Regular Expressions
    ##

    nameRX = qtc.QRegExp("^[A-Za-z]{1,16}$")                # RegExp for names
    dobRX = qtc.QRegExp("^\\d\\d/\\d\\d/\\d\\d\\d\\d$")     # RegExp for dates
    dob1DRX = qtc.QRegExp("^\\d\\d/\\d/\\d\\d\\d\\d$")      # RegExp for dates with single digit day
    dob1MRX = qtc.QRegExp("^\\d/\\d\\d/\\d\\d\\d\\d$")      # RegExp for dates with single digit month
    dob1D1MRX = qtc.QRegExp("^\\d/\\d/\\d\\d\\d\\d$")       # RegExp for dates with single digit day & month

    ##
    # Functions
    ##

    ## @brief The ValidateEmployeeInfo() function uses regular expressions to validate employee information
    #       formats before sending it to the server
    #  @param firstName An employee's first name
    #  @param lastName An employee's last name
    #  @param birthDate An employee's date of birth
    #  @param position An employee's position
    #  @param salary An employee's salary
    #  @param empId An employee's unique Id number
    def ValidateEmployeeInfo(self, firstName, lastName, birthDate, position, salary, empId):
        if (not self.MatchName(firstName)):
            return False
        elif (not self.MatchName(lastName)):
            return False
        elif (not self.MatchBirthDate(birthDate)):
            return False
        else:
            return True

    ## @brief The MatchName() function uses the nameRX regular expression to match name formats
    #  @param name An employee's name
    def MatchName(self, name):
        match = regExUtil.nameRX.exactMatch(name)

        if (not match):
            log.logger.error("Invalid name")
            return False
        else:
            return True

    ## @brief The MatchBirthDate() function uses the dobRX, dob1DRX, and dob1MRX regular expressions to match
    #       date formats
    #  @param birthDate An employee's birth date
    def MatchBirthDate(self, birthDate):
        match = regExUtil.dobRX.exactMatch(birthDate)
        match1D = regExUtil.dob1DRX.exactMatch(birthDate)
        match1M = regExUtil.dob1MRX.exactMatch(birthDate)
        match1D1M = regExUtil.dob1D1MRX.exactMatch(birthDate)

        if (not match and not match1D and not match1M and not match1D1M):
            log.logger.error("Invalid birth date")
            return False
        else:
            return True

# Initialize regExUtil object
regExUtil = RegExUtil()