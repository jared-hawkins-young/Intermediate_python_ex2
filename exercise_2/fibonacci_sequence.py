# Importing time class
import time

# Constructor of fibonacci sequence
def fib(n):
    # start time
    start = time.time()
    # creating list
    fi = [0] *(n + 1)
    fi[1] = 1
    # looping the fibonacci sequence
    for j in range (2, n + 1):
        fi[j] = fi[j - 1] + fi[j - 2]
    # end time
    end = time.time()
    # find total time
    excTime = end - start
    return fi[n], excTime
    
