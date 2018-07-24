import time
# this script demonstrates an infinite loop function
def loop():
    while   True:
        print 'Hello World!'
        time.sleep(1)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print 'Good Bye'
