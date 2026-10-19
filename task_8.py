
p = 9739
a = 497
b = 1768

O = None  # Point at infinity

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return O

    if P == Q:
        numerator = (3 * x1**2 + a) % p
        denominator = (2 * y1) % p
    else:
       
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    lam = (numerator * pow(denominator, -1, p)) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)



X = (5274, 2841)
Y = (8669, 740)

assert point_add(X, Y) == (1024, 4440)
assert point_add(X, X) == (7284, 2107)

# Calculate S = P + P + Q + R
P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

S = point_add(point_add(point_add(P, P), Q), R)

print("S =", S)

x, y = S
assert (y**2 - (x**3 + a*x + b)) % p == 0

print("S is on the curve")
