import time
import microbit
import logging


def stop_display():
    #microbit.repl.ctrl_c()
    microbit.display.show(" ")


def show_pic(std_img_name):
    IMG = [microbit.Image.STD_IMAGES[i]
           for i, x in enumerate(microbit.Image.STD_IMAGE_NAMES)
           if x == std_img_name][0]
    return microbit.display.show(IMG)


def create_logging(path):
    ''' Logging '''
    LOG_FILENAME = '%s/logfile.log' % path
    log_format = '%(levelname)s: %(asctime)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)
    logger = logging.getLogger()
    handler = logging.FileHandler(LOG_FILENAME)
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    # add handler to the logger
    logger.addHandler(handler)
    return logger