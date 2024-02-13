import logging
import os

class UserRunningProgramFilter(logging.Filter):
    def filter(self, record):
        record.user = os.getenv("User")
        return True
    
if __name__ == '__main__':
    levels = (
        logging.DEBUG, 
        logging.INFO, 
        logging.WARNING, 
        logging.ERROR,
        logging.CRITICAL,
    )
    
    logging.basicConfig(filename='app2.log', filemode='w', level=logging.DEBUG, format="%(asctime)-5s %(levelname)-8s Run by User: %(user)-20s %(message)s",
    )
    
    logger = logging.getLogger("mylogger")
    f = UserRunningProgramFilter()
    logger.addFilter(f)
    logger.debug("A debug message")
    logger.error("An error message")
    logger.critical("A critical message")
    
    logger = logging.getLogger("yourlogger")
    
    f = UserRunningProgramFilter()
    logger.addFilter(f)
    logger.debug("A debug message")
    logger.error("An error message")
    logger.critical("A critical message")
    
    logger = logging.getLogger("yourlogger")
    
    