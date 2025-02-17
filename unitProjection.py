import numpy as np

u = input("Enter the numerator vector of the unit vector u: ")
denom = input("Enter the denominator of the unit vector u. Write sqrt() for square root: ")
v = input("Enter the vector to project: ")

u = np.array(list(map(float, u.replace('[', '').replace(']', '').split(','))))
if 'sqrt(' in denom:
    denom = np.sqrt(float(denom[5:-1]))
else:
    denom = float(denom.replace('sqrt(', '').replace(')', ''))
u = u / denom

v = np.array(list(map(float, v.replace('[', '').replace(']', '').split(','))))

projection = np.dot(u, v) * u

print("The projection of v onto u is:", projection)
