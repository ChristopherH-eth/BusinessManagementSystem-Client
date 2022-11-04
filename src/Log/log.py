# Imports
import logging

'''
@file log.py
@author 0xChristopher
@brief This file sets and initializes the client side logger.
'''

class Log:
    ##
    # Functions
    ##

    ## @brief Log constructor
    def __init__(self):
        self.logger = logging.getLogger("BMS_Client")
        self.logger.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        fh = logging.FileHandler(filename = "daily.txt")
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter("[%(asctime)s %(levelname)s] %(name)s:%(message)s", 
            datefmt = "%m/%d/%Y %I:%M:%S %p")
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

# Initialize log object
log = Log()