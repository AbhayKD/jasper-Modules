import time
b=0
e=0
#t = raw_input("Enter:")
while True:
    t = raw_input("Enter:")
    if t == "b":
        b = time.time()
    elif t == "e":
        e = time.time()
        print str(e-b)[0:3]
