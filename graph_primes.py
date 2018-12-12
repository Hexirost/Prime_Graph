
import matplotlib
matplotlib.use("TKAgg",warn=False, force=True)
import matplotlib.pyplot as plt

EXTRA_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM  = "100000000"
BASE = "10"

file = ("prime_" + NUM + "_base_" + str(BASE) + ".txt")
freq = {x:0 for x in EXTRA_CHARS[:int(BASE)]}

with open(file) as fp:
    line = "True"
    while (line):
        number = fp.readline().replace("\n","")
        if not number:
            break
        for num in number:
            freq[num] += 1
plt.plot(*zip(*sorted(freq.items())))

plt.xlabel('Digits')
plt.ylabel('Frequency')
plt.title('Prime number distribution')
plt.grid(True)
plt.savefig("test.png")
plt.show()