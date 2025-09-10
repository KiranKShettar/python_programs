import time, sys

indent = 0
indentation_increasing = True

try:
    while True:
            print(' ' * indent,end = "")
            print('Samarth bit hoga byad')
            time.sleep(0.1)

            if indentation_increasing:
                indent += 1
                if indent >= 20:
                    indentation_increasing = False
            else:
                indent -= 1
                if indent <= 0:
                     indentation_increasing = True
except KeyboardInterrupt:
     sys.exit()
                 