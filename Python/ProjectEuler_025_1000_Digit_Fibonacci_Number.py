# https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = b = count = 1
    
while True:
    a, b = b, a + b
    count += 1
    if len(str(a)) == 1000:
        print(count) # 4782
        break