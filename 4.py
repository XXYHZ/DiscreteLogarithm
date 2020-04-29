from random import randint
from time import time
from math import gcd
from math import sqrt
from operator import itemgetter

def eulerFunction(n):
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

def pollardRho(a, b, p, q):
    u, v = (randint(2, p-1) % p), (randint(2, p-1) % p)
    logc, logd = 2, 2
    logc_x, logd_x = 2, 2
    c = pow(a, u, p) * pow(b, v, p) % p
    d = c
    count = 0
    half_p = p//2
    while(1):
        print("\nstep = ", count)
        print("c =", c)
        print("d =", d)
        print("log(c) = ", logc_x, "x + ", logc)
        print("log(d) = ", logd_x, "x + ", logd, "\n")

        # f(c) function
        if c < half_p:
            c = a*c % p
            logc += 1
        else:
            c = b*c % p
            logc_x += 1

        # f(f(d)) function
        if d < half_p:
            d = a*d % p
            logd += 1
        else:
            d = b*d % p
            logd_x += 1
        if d < half_p:
            d = a*d % p
            logd += 1
        else:
            d = b*d % p
            logd_x += 1
        count += 1
        if c == d:
            break
    a, b = (logc_x - logd_x) % q, (logd - logc) % q
    print(logc, " + ", logc_x, "x", " = ", logd, " + ", logd_x, "x", " (mod ", q, ")")
    x = (pow(a, eulerFunction(q) - 1, q)*b) % q
    print("x ≡ ", x, " (mod ", q, ")")
    print("step count =", count)
    return

#a = 3
#b = 5
#p = 799454910203247398939
#q = 399727455101623699469

a = 2
b = 7
p = 137
q = 68

#start_time = time()
pollardRho(a, b, p, q)
#print("time:", time() - start_time, "sec.")

def gelfond(a, b, p, q):
    s = int(sqrt(q) + 1)
    
    start_time = time()
    base = {}
    idx = pow(a, s, p)
    help_a = idx
    base[idx] = 1   
    for i in range(2, s + 1):
        idx = pow(help_a * idx, 1, p)
        base[idx] = i
    keys_b = sorted(list(base.keys()))
    #print("keys_b:", keys_b)
    #print("base:", base)
    print("base calculation time: ", time() - start_time)

    step = 0
    start_time = time()
    for i in range(0, s + 1):
        a_i = pow(a, i, p)
        a_i = pow(a_i * b, 1, p)
        #print(a_i)
        for j in range(s):
            step += 1
            if keys_b[j] == a_i:
                x = (base[keys_b[j]]*s - i) % p
                print("\nx ≡ ", keys_b[j], " * ", s, " - ", i, " = ", x, " ( mod ", p, ")")
                print("calculation time", time() - start_time)
                print("step count =", step)
                return

#a = 3
#b = 5
#p = 799454910203247398939
#q = 399727455101623699469

#a = 5
#b = 3
#p = 23
#q = 16

#a = 2
#b = 7
#p = 137
#q = 68

#start_time = time()
#gelfond(a, b, p, q)
#print("time:", time() - start_time, "sec.")
