'''problema 1'''

def is_palindrome(n):
    '''
    determina daca un nr e palindrom
    :param n: numarul care trebuie verificat
    :return: daca e palindrom sau nu
    '''
    copie1 = n
    invers = 0
    while(n > 0):
        ultima_cifra = n%10
        invers = invers*10+ultima_cifra
        n = n//10
    if(copie1 == invers):
        return"E palindrom"
    else:
        return"Nu e palindrom"

def test_is_palindrome():

    assert is_palindrome(898) == 1
    assert is_palindrome(234) == 0


'''problema 2'''


def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def is_superprime(n):
    '''
    determina daca un nr e superprim
    :param n: un numar intreg
    :return: True or False
    '''
    k = 1
    while (n  > 0):
        if isPrime(n):
            k = 1
            n = n//10
        else:
            k == 0
    if k == 1:
        return"E superprim"
    elif k == 0:
        return"Nu e superprim"

def test_is_superprime():

    assert is_superprime(237) ==1
    assert is_superprime(239) ==1
    assert is_superprime(88) ==0


'''problema 3'''

def lastPrimeNumber(n):
    '''
    determina cel mai apropiat numar prim de n
    :param n: numarul dat
    :return: cel mai mare numar prim mai mic ca n
    '''
    for i in range (2, n):
        if isPrime(i):
            prim=i
    return(prim)


def test_lastPrimeNumber():
    assert lastPrimeNumber(14) == 13
    assert lastPrimeNumber(2) == 2
    assert lastPrimeNumber(20) == 19


'''Meniu'''

def printMenu():
    print("1. Determină dacă un număr dat este palindrom.")
    print("2. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, 233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.")
    print("3. Găsește ultimul număr prim mai mic decât un număr dat.")
    print("4.Exit")

def main():
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            n = int(input("E palindrom?: "))
            print(is_palindrome(n))
        elif optiune == "2":
            n = int(input("E superprim?: "))
            print(is_superprime(n))
        elif optiune == "3":
            n=int(input("Dati numarul: "))
            print(lastPrimeNumber(n))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati!")

main()