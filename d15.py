from time import time

start = time()

G1 = 277
G2 = 349
#G1 = 65
#G2 = 8921
c1 = 16807
c2 = 48271
inthing = 2147483647

counter = 0
s1 = []
s2 = []
while min(len(s1), len(s2)) < 5000000:
    G1 = (G1 * c1) % inthing
    G2 = (G2 * c2) % inthing
    if G1 & 3 == 0:
        s1.append(G1)
    if G2 & 7 == 0:
        s2.append(G2)

iter = min(len(s1), len(s2))
for i in range(iter):
    a = s1[i]
    b = s2[i]
    if a & (65535) == b & (65535):
        counter += 1

end = time()

print(counter)
print(end - start)