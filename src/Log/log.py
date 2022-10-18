# Imports
import logging

##
# @file log.py
# @author 0xChristopher
# @brief
##

class Log:
    # Functions
    # @brief The setLogger() function sets the logger config
    def setLogger():
        logger = logging.getLogger("BMS_Client")
        logger.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        fh = logging.FileHandler(filename = "daily.txt")
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter("[%(asctime)s %(levelname)s] %(name)s:%(message)s", 
            datefmt = "%m/%d/%Y %I:%M:%S %p")
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger

    def getLogger():
        return logger

# Initialize logger
logger = Log.setLogger()