import microbit
import time


offset = 580


def read():
    read = float(microbit.cmd('print(pin2.read_analog())'))
    return max(0, read - offset)


def running_time():
    return time.time()


def wait_for_double_clap(timeout=1000, spread=500, sensitivity=75):
    sensitivity = 105 - sensitivity

    clap_one_time = None

    start_time = running_time()
    while running_time() - start_time < timeout:
        if read() > sensitivity:
            while read() > sensitivity:
                pass
            microbit.sleep(100)
            if clap_one_time is not None and running_time() - clap_one_time < spread:
                return True
            else:
                clap_one_time = running_time()

    return False

def wait_for_clap(timeout=1000, sensitivity=75):
    sensitivity = 105 - sensitivity

    start_time = running_time()
    while running_time() - start_time < timeout:
        #if int(running_time() - start_time) % 2 == 0:
        sound_level = read()
        if sound_level > sensitivity:
            print(sound_level)
            return True

    return False

if __name__ == "__main__":
    while True:
        clap_status = "YESS" if wait_for_clap() else "NOO"
        microbit.sleep(100)
        microbit.display.show(clap_status)