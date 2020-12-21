import logging
from logging.handlers import RotatingFileHandler

import mysql.connector
import config
########################################################################################################################
# PROCEDURES:
# Step 1: Select all space from tbl_spaces
# Step 2: Print the result
########################################################################################################################
def main(logger):
    # TODO
    mydb =mysql.connector.connect(**config.config)
    mycursor = mydb.cursor()
    query=("SELECT id, name, uuid, area from tbl_spaces" )
    mycursor.execute(query)
    for (id, name, uuid, area) in mycursor:
        print("id:%s,name:%s,uuid:%s,area:%s" % (id, name, uuid, area))
    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    """main"""
    # create logger
    logger = logging.getLogger('mysql-connector-demo')
    # specifies the lowest-severity log message a logger will handle,
    # where debug is the lowest built-in severity level and critical is the highest built-in severity.
    # For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL
    # messages and will ignore DEBUG messages.
    logger.setLevel(logging.ERROR)
    # create file handler which logs messages
    fh = logging.handlers.RotatingFileHandler('mysql-connector-demo.log', maxBytes=1024 * 1024, backupCount=1)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(fh)

    main(logger)
