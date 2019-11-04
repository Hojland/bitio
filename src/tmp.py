import time
import microbit
import utils
import logging
from envirobit import sound

utils.create_logging('.')


def show_txt(txt):
    microbit.display.show(txt)


if __name__ == "__main__":
    logger = logging.getLogger()
    for i in range(0, 100):
        got_clap = sound.wait_for_clap()
        #logger.info('the temperature is %s degrees celsius' % temp)
        logger.info('I got a clap now, that is %s' % got_clap)
        time.sleep(1)