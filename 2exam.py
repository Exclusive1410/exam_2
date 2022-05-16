#Task 1. Write a program that given an array of integers determines if it is sorted in "ascending" order, "descending" order or "not sorted" at all.
A=[10,9,8,3,1,0]
B=[1,9,18,33,41,50]
C=[1, 1, 1, 1, 1]
D= [1]
E=[1, 2, 3, 2, 1]

def order(List):
    results = [True if second >= first else False for first, second in zip(List, List[1:])]
    if any(results) and all(results):
        return "ascending order"
    elif not any(results) and not all(results):
        return "descending order"
    else:
        return "not sorted"
print(order(A))
print(order(B))
print(order(C))
print(order(D))
print(order(E))

print('--------------')
#Write the function morse_number() for encryption of a number in a three-digit format in Morse code.

print('--------------')

#Task 3. Write a function using recursion to check if a number n is prime
def isPrime(n, i=2):
    if (n <= 2):
        return True if (n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True

    return isPrime(n, i + 1)

n = int(input('Input number : '))
if (isPrime(n)):
    print('Is Prime')
else:
    print('Not Prime')

print('--------------')
#Task 4. Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others.
def iq_test(numbers):
    nums = [int(num)%2 for num in numbers.split(" ")]
    if nums.count(0)>1:
        return nums.index(1)+1
    else:
        return nums.index(0)+1

a=iq_test('2 4 7 8 10')
print(a)

print('--------------')
#Task 5. Given an array of ones and zeroes, convert the equivalent binary value to an integer
binary=[1,0,1,1]
acc=0
for b in binary:
    acc=acc*2+b
print('Integer value is',acc)
