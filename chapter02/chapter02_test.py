import time

result = []
start = time.time()
for i in range(10000):
    result = result + [i]
print(len(result),',',time.time()-start)

result2 = []
start = time.time()
for i in range(10000):
    result.append(i)
print(len(result2),',',time.time()-start)
