import random
p = 57896044618658097711785492504343953926634992332
820282019728792003956564821041
q = 5789604461865809771178549250434395392708293458372545
0622380973592137631069619
n = p * q
s = random.randint(1, n - 1)  # private key
y = (s**2) % n  # public key
z = 20  # number of rounds
res = []
for i in range(1, z + 1):
    print('--------------------')
    print('Раунд ', i)
    # доказывающий:
    k = random.randint(1, n - 1)
    u = (k**2) % n
    print('The prover sends a fixator to the verifier: ', format(u, 'x'))
    # проверяющий:
    r = random.randint(0, 1)
    print('Verifier sent r =', r)
    # доказывающий:
    w = (k * (s**r)) % n
    k = 0
    print('Prover sends'
          'the value to the verifier for verification: ', format(w, 'x'))
    # vefifier
    if ((w**2) % n == (u * y**r) % n):
        res.append(1)
    else:
        res.append(0)
print('--------------------')
if res.count(0) != 0:
    print('Check failed')
else:
    print('Check ok')

str = str(input())
