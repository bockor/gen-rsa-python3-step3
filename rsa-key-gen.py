'''

Summary:            RSA Key Generation Principle
		
Author:             bruno.on.the.road@gmail.com
Version:            0.3
Date:               17 Oct 2018
Platform:           Ubuntu Server 18.04 LTS
python version:     3.6

RSA Key Generation Principle
----------------------------

1. Generate two large random primes, p and q, of approximately equal size
such that their product n = pq is of the required bit length, e.g. 1024 bits.

2. Compute n = pq and (φ) phi = (p-1)(q-1).

3. Choose an integer e, 1 < e < phi, such that gcd(e, phi) = 1.

4. Compute the secret exponent d, 1 < d < phi, such that ed ≡ 1 (mod phi).
   -modular arithmetics or congruences theorem-

5. The public key is (n, e) and the private key is (n, d).
Keep all the values d, p, q and phi secret.

* n is known as the modulus.

* e is known as the public exponent or encryption exponent or
just the exponent.

* d is known as the secret exponent or decryption exponent.

'''

from random import randrange
from math import gcd

def print_title():
    ''' print title '''
    print()
    print('Simple RSA encryption example')
    print( '-' * 29 )
    print()
 
def input_primes():
    '''  Select two primes and return these in a tuple '''
    p = int(input('Select prime p: '))
    q = int(input('Select prime q: '))
    print()
    return (p,q)

def calc_modulus(primes):
    ''' calculate modulus n 
        33 is actually the smallest possible value for the modulus n for which
        the RSA algorithm works.
    '''
    p,q = primes[0], primes[1]
    n = p * q
    print('modulus n = p * q =  {}'.format(n))
    return n

def calc_phi(primes):
    ''' calculate phi '''
    p,q = primes[0], primes[1]
    phi = (p - 1) * ( q - 1)
    print('phi = (p - 1) * (q - 1) =  {}'.format(phi))
    print()
    return phi

def pick_public_key(phi):
    ''' Pick a public key e '''
    gcd_is_one = False
    while not gcd_is_one:
        e = randrange( 2, phi )
        if gcd(e,phi) == 1:
            gcd_is_one = True
    print('Choose Public key e: {}'.format(e)) 
    print('[*] {} and {} have no common factors except 1'.format(e,phi))        
    print()
    return e

def calc_private_key(e,phi,n):
    ''' Compute d such that ed ≡ 1 (mod phi) '''
    for d in range( 1, n - 1 ):
        if (e * d - 1) % phi == 0:
            break
    print('Computed Private key d: {}'.format(d))    
    print('[*] {} * {} mod {} = 1'.format(e,d,phi))
    print()
    return d

def input_message():
    ''' Enter a test message m (int type < modulus) ''' 
    m = int(input('Select message m: '))
    print()
    return m

def encrypt_message(e,n,m):
    ''' Encrypt the message m to c '''
    #c = m ** e % n
    c  = pow(m,e,n)
    print('Encrypted message c = m ** e % n = {}'.format(c)) 
    return c

def decrypt_message(d,n,c):
    ''' Decrypt c to mm '''
    #mm = c ** d % n 
    mm = pow(c,d,n) 
    print('Decrypted message mm = c ** d % n = {}'.format(mm))
    print()
    return mm

def verify_message(m, mm):
    ''' Is m == mm ? '''
    print('[*] Is m == mm ? ... ', end= "")
    msg = 'OK WORKING EXAMPLE' if m == mm else 'NOT OK -- CHECK FOR ANY ERROR'
    print(msg) 
    print()

def main():
    ''' top level code '''
    print_title()    
    my_primes = input_primes()
    n = calc_modulus(my_primes)
    phi = calc_phi(my_primes)
    e = pick_public_key(phi)
    d = calc_private_key(e,phi,n)
    m = input_message()
    c = encrypt_message(e,n,m)
    mm = decrypt_message(d,n,c)
    verify_message(m,mm)  
    

if __name__ == '__main__':
    main()
