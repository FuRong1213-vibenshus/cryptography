# Public Key Generator

import random, sys, os, primeNum, cryptomath

def main():
    # Create a public/private keypair with 1024-bit:
    print('Making key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files made.')


def generateKey(keySize):
    # Creates public/private keys keySize bits in size.
    p = 0
    q = 0
    # Step1: Create two prime numbers, p and q, Calculate n = p*q:
    print('Generating p prime...')
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p*q

    # Step2: Create a number e that is relative prime to (p-1)(q-1):
    print('Generating e that is relatively prime to (p-1)(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2**(keySize-1), 2**(keySize))
        if cryptomath.gcd(e, (p-1)*(q-1)) == 1:
            break

    # Step3: Calculat d, the mod iverse of e:
    print('Calculating d that is mod inverse of e ...')
    d = cryptomath.findModInverse(e, (p-1)*(q-1))

    publicKey = (n,e)
    privateKey = (n,d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x 
    # is the value in name) with the n, e and d,e integers written in them,
    # delimited by a comma.
    publicKey, privateKey = generateKey(keySize)
    print()

    print('The public key is a %s and a %s digit number.' %(len(str(publicKey[0])), len(str(publicKey[1]))))

    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    print()
    print('The private key is a %s and a %s digit number.' %(len(str(publicKey[0])), len(str(publicKey[1]))))

    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()
if __name__ == '__main__':
    main()
