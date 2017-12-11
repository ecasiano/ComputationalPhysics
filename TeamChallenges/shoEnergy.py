import numpy

def average(list):
    total = 0
    for num in list:
        total += float(num)
    return total/len(list)

with open("LectureChallenges/sho_energy.dat", "r+") as f:
    lines = f.readlines()
    lines[0] = lines[0].replace("#", "")
    k = []
    p = []
    for line in lines:
        line = line.split()
        k.append(line[0])
        p.append(line[1])

keys = [k[0], p[0]]
k.pop(0)
p.pop(0)

values = [k, p]
final = dict(zip(keys, values))
#print(final)
for key in final.keys():
    print(key + ": " + str(average(final[key])))

def energy(t):
    return 0.5/numpy.tanh(1/(2*t))

print("total exact: " + str(energy(0.5)))
