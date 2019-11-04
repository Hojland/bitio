import microbit
import time
import utils


name_1 = 'HEART'
name_2 = 'HEART_SMALL'


if __name__ == "__main__":
    for i in range(0, 100):
        utils.show_pic(name_1)
        time.sleep(0.5)
        utils.show_pic(name_2)
        time.sleep(0.5)