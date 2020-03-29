import time, sys
try:
    indent = 0
    increment = True
    while True:
        if(indent <= 50) and increment:
            print(" " *indent, "***  ***")
            indent = indent + 1
            time.sleep(0.05)
        else:
            increment = False
            print(" " *indent, "***  ***")
            indent = indent - 1
            time.sleep(0.1)
            if(indent == 0):
                increment = True
except KeyboardInterrupt:
    sys.exit()
