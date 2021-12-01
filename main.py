import math
def dal():
    numb = int(input("Enter number: "))
    print("All divisors:", end = " ")
    deviders = []
    for i in range(1, numb + 1):
        if (numb % i == 0):
            deviders.append (i)
            print(i, end = "  ")

    print("\n")

    a = sum(deviders)
    print ("sum of all divisors:")
    print (a)
if __name__ == '__main__':
    dal()
