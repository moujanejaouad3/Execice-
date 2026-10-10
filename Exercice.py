p = 7  # bar
n = 5  # moles
v = 3  # m3
R = 8.314

T = p * 100000 * v / (n * R)
print("Temperature =", T, "K")