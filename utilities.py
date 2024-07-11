import logging
import inspect
from main import logger

def Is_Even(i) -> bool:
    logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}:{i}")
    result = (i%2 == 0)
    logger.debug(f"       result={result}")
    return result 

def Is_Odd(i) -> bool:
    logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}:{i}")    
    result =  ( i%2 != 0)
    logger.debug(f"       result={result}")
    return result
 
def Get_Sign(num):
    logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}:{num}")
    result = 0
    if num > 0:
        result =  "+"
    elif num < 0:
        result = "-"
    else:
        result = "0"

    logger.debug(f"       result={result}")
    return result    
