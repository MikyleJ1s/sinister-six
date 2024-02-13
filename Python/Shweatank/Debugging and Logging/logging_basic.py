import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
logging.basicConfig(filename='app3.log', filemode='w', format="%(name)s %(levelname)s - %(message)s")

def divide(x,y):
    try:
        out = x/y
    except ZeroDivisionError as e:
        logger.exception("Division by zero issue"+str(e))
    else:
        return out
        
logger = logging.getLogger("mylogger")
 