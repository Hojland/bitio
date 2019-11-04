import time
import microbit
import logging
import utils
from envirobit.bme280 import bme280


utils.create_logging('.')


if __name__ == "__main__":
    logger = logging.getLogger()
    for i in range(0, 20):
        bme280 = bme280()
        temp = bme280.temperature()
        #logger.info('the temperature is %s degrees celsius' % temp)
        logger.info('The envirobit temperature is %s degrees celsius' % temp)
        time.sleep(5)