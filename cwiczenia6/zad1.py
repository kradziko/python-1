f1 = open("tabliczka.txt", "wb")

for x in range(1, 11):
    for y in range(1, 11):
        f1.write("%4i" % (x*y))
    f1.write('\n')
