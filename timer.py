import time

x0 = 0
x = int(input("Coloque o tempo para aguardar: "))
count = 0.001

print(x)
time.sleep(0.001)
while x > x0:
    x -= count
    print("{:.3f}".format(x))
    time.sleep(0.001)