
RED_GPIO = 18
BLUE_GPIO = 23
GREEN_GPIO = 24

FIFO = open('/dev/pi-blaster', 'w', buffering=0)

def set(gpio, value):
    s = "%s=%s\n" % (gpio, value)
    FIFO.write(s)

