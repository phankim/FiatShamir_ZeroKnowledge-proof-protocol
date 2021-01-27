import random

def MillerRabin(n):
        if n!=int(n):
            return False
        n=int(n)
        #Miller-Rabin test for prime
        if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
            return False 
        if n==2 or n==3 or n==5 or n==7:
            return True
        s = 0
        d = n-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == n-1)
 
        def trial_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True   
        for i in range(8):#number of trials 
            a = random.randrange(2, n)
            if trial_composite(a):
                return False 
        return True 
def mod(a,p):                 #приведение по модулю
    mod = (a % p + p) % p
    return mod

def fast_pow(a, w, n):
    s = 1
    v = w
    c = a
    while not v == 0:
        if mod(v,2) == 1:
            s = mod(s*c,n)
            v = (v-1)//2
            c = mod(c**2,n)
        else:
            v = v//2
            c = mod(c*c,n)
    return s

len = int(input("Enter length bits of p, q -> "))
l_s=int(len/12.8)
s_p=random.randint((2**l_s)/2,(2**l_s)-1)
s_q=random.randint((2**l_s)/2,(2**l_s)-1)
while not MillerRabin(s_p) :
    s_p=random.randint((2**l_s)/2,(2**l_s)-1)
i=1
p=4
q=4
dif =int(len-l_s)
while not MillerRabin(p) : #
    p=s_p*2
    r_p=random.randint((2**dif)//2,(2**dif)-1) #r- нечетное число 
    p=int(p*r_p)+1 # p-1=2*s*r_p
    i+=1
while not MillerRabin(q):
    q=s_q*2
    r_q=random.randint((2**dif)//2,(2**dif)-1) #r- нечетное число 
    q=int(q*r_q)+1 # q-1=2*s*r_q
    i+=1
print ("p=",p)
print("q=",q)


n = p * q
s = random.randint(1, n - 1)  # private key
y = (s**2) % n  # public key
z = 20  # number of rounds
res = []
for i in range(1, z + 1):
    print('--------------------')
    print('Round ', i)
    # prover:
    k = random.randint(1, n - 1)
    u = (k**2) % n
    print('The prover sends a fixator to the verifier: ', format(u, 'x'))
    # verifier:
    r = random.randint(0, 1)
    print('Verifier sent r =', r)
    # prover:
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
