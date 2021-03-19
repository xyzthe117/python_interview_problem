#Python 3.8.6
#   Natchapol Shinno E-mail: nathnath2542@hotmail.com Tel. 082-333-6264

# Easy Question - 1
#
#   Prints the numbers from 1 to 100
#       - Multiples of three print “Fizz”
#       - Multiples of five print “Buzz”
#       - Multiples of both three and five print “FizzBuzz”
def fizznBuzz():
    print("\n1. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.\n")
    while True:
        isStart = input("Do you want to start to run this task? (Y/N): ")
        if isStart == "Y":
            for x in range(1,101):
                if x % 3 == 0 and x % 5 == 0:
                    print("FizzBuzz")
                elif x % 3 == 0:
                    print("Fizz")
                elif x % 5 == 0:
                    print("Buzz")
                else :
                    print(x)
            while True :
                confirmation = input("\nConfirm task completed (Y/N): ")
                if confirmation == "Y" :
                    return True
                elif confirmation == "N" :
                    return False
                else :
                    print("Invalid, Please input only Y or N\n")
        elif isStart == "N" :
            return False
        else :
            print("Invalid, Please input only Y or N\n")

# Easy Question - 2
#   Determine integer input is a leap year or not
#       - Rule 1: A year is called leap year if it is divisible by 400.
#       - Rule 2: If year is not divisible by 400 as well as 100 but it is divisible by 4 then that year are also leap year.
#
#   Another reference source (https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year)
#       1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#       2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#       3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#       4. The year is a leap year(it has 366 days).
#       5. The year is not a leap year(it has 365 days).
def determineLeapYear():
    print("\n2. Determine  integer input is a leap year.\n")
    while True :
        year = input("Enter Year (Press 'ENTER' to exit) : ")
        if len(year) <= 0 :
            break
        else :
            year = int(year)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leapYear = True
                else :
                    leapYear = False
            else :
                leapYear = True
        else :
            leapYear = False
        print(year, "-> TRUE\n") if leapYear else print(year, "-> FALSE\n")
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.1
#   Right Triangle Star Pattern
#       Rows  - run an outer loop from 1 to n+1.
#       Columns - run an inner loop from 1 to i.
#       Inside the inner loop print star.
#       After printing all columns of a row move to next line then print new line.
def rightTriangle():
    while True :
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n+1) :
            for j in range(i) :
                print("*", end = ''),
            print()
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.2
#   Mirrored Right Triangle Star Pattern
#       Rows  - run an outer loop from 1 to n+1.
#       Columns - print spaces if j <= n-i else print star.
#       After printing all columns of a row, move to next line then print new line.
def mirroredRightTriangle():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n+1):
            for j in range(n+1):
                if(j <= n - i):
                    print(' ', end='')
                else:
                    print('*', end='')
            print()
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.3
#   Mirrored Right Triangle Star Pattern
#       Rows  - run an outer loop from 1 to n+1.
#       Columns - print spaces and staying in the same line then print star in the start (j==0) and the end (j ==2*i) of each line.
#       After printing all columns of a row, move to next line then print new line.
def hollowPyramid():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n):
            for j in range(n-i):
                print(' ', end='')  
            for j in range(2*i+1):
                if j == 0 or j == 2*i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print() 
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.4
#   Cross Star Pattern
#       Rows  - run an outer loop from 1 to n.
#       Columns - print star if i equal j or n-j-1 equal i other else print spaces.
#       After printing all columns of a row, move to next line then print new line.
def crossStar():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n):
            for j in range(n):
                if i == j or n - j - 1 == i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.5
#   Diamond Star Pattern
#       Rows  - run an outer loop from 1 to n+1.
#           Upper Part of Diamond - print star if (i) is a odd number. After that, move to the next line and check for (i).
#           Lower Part of Diamond - act like an inversed of an upper part. print stars except for the first line that doesn't print.
def diamondStar():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit :) ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n+1) :
            if i % 2 != 0 :
                val = (n - i) // 2
                print(" "*val + "*"*(i) + " "*val, end="\n")
        
        for j in range(n-1, 0, -1) :
            if j % 2 != 0 :
                val2 = (n-j)//2
                print(" "*val2 + "*"*(j) + " "*val2, end="\n")
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 3.6
#   Alphabetical and Hollow Diamond Plus Pattern
def alphabetDiamond():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        # Upper Part
        for i in range(1, n+1):
            # print inverted right triangle of "A"
            for j in range(1, n-i+1):
                print("A", end="")
            # print the hollow diamond plus (upper)
            for j in range(1, 2*i):
                if j == 1 or j == 2*i-1:
                    print("+", end="")
                # filled the diamond with "E" (upper)
                else:
                    print("E", end="")
            # print inverted mirrored right triangle of "B"
            for j in range(1, n):
                if(j < i):
                    print('', end='')
                else:
                    print("B", end='')
            print()
        # Lower Part 
        for i in range(n-1, 0, -1):
            # print right triangle of "C"
            for j in range(1, n-i+1):
                print("C", end="")
            # print the hollow diamond plus (lower)
            for j in range(1, 2*i):
                if j == 1 or j == 2*i-1:
                    print("+", end="")
                # filled the diamond with "E" (lower)
                else:
                    print("E", end="")
            # print mirrored right triangle of"D"
            for j in range(1, n + 1):
                if(j > n - i):
                    print('', end='')
                else:
                    print("D", end='')
            print()
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Easy Question - 4
#   Finds all prime numbers up to n for input n.
def primeNumbers():
    while True:
        n = input("\nPlease Enter the Total Number of Rows (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(0, n+1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    print(i, end=' ')
        print()
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

# Medium Question - 1
#   In Python, what is the difference between else and finally in exception handling?
def elseFinally():
    print("\nelse: If there is no exception then this block will be executed")
    print("\nFinally: Finally block always gets executed either exception is generated or not\n")
    while True:
        confirmation = input("\nConfirm task completed (Y/N): ")
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
# Use pickle to store and load status of each task.
import pickle
#   Reset 
#       - Reset all of store task in pickle
def resetTask():
    initStatus = {"E1": False, "E2": False, "E31": False, "E32": False, "E33": False,
                  "E34": False, "E35": False, "E36": False, "E4": False, "M1": False}
    with open('task.pickle', 'wb') as handle:
        pickle.dump(initStatus, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return True

# Status of each task
taskStatus = {"E1": False, "E2": False, "E31": False, "E32": False, "E33": False,
        "E34": False, "E35": False, "E36": False, "E4": False, "M1": False}

while True:
    print("--------------------------------------------------")
    print("Select the tasks (Press 'ENTER' to exit): ")
    print("     0  - Reset.")
    print("     1  - Easy: Fizz&Buzz") if not taskStatus["E1"] else None
    print("     2  - Easy: Leap Year") if not taskStatus["E2"] else None
    print("    3.1 - Easy: Right Triangle Star") if not taskStatus["E31"] else None
    print("    3.2 - Easy: Mirrored Right Triangle Star") if not taskStatus["E32"] else None
    print("    3.3 - Easy: Hollow Star Pyramid") if not taskStatus["E33"] else None
    print("    3.4 - Easy: Cross Star") if not taskStatus["E34"] else None
    print("    3.5 - Easy: Diamond Star") if not taskStatus["E35"] else None
    print("    3.6 - Easy: Alphabetical & Plus Hollow Diamond") if not taskStatus["E36"] else None
    print("     4  - Easy: Difference between 'else' and 'finally' ") if not taskStatus["E4"] else None
    print("     5  - Medium: Prime Numbers") if not taskStatus["M1"] else None
    print("--------------------------------------------------")
    task = input("Enter the problem number: ")
    if len(task) <= 0:
        with open('task.pickle', 'wb') as handle:
            pickle.dump(taskStatus, handle, protocol=pickle.HIGHEST_PROTOCOL)
        quit()
    elif task == "0":
        if(resetTask()):
            print("\nReset Complete")
            with open('task.pickle', 'rb') as handle:
                loadfile = pickle.load(handle)
            taskStatus = loadfile
    elif task == "1" and not taskStatus["E1"]:
        if(fizznBuzz()) :
            taskStatus["E1"] = True
    elif task == "2" and not taskStatus["E2"]:
        if(determineLeapYear()) :
            taskStatus["E2"] = True
    elif task == "3.1" and not taskStatus["E31"]:
        if(rightTriangle()):
            taskStatus["E31"] = True
    elif task == "3.2" and not taskStatus["E32"]:
        if(mirroredRightTriangle()):
            taskStatus["E32"] = True
    elif task == "3.3" and not taskStatus["E33"]:
        if(hollowPyramid()):
            taskStatus["E33"] = True
    elif task == "3.4" and not taskStatus["E34"]:
        if(crossStar()):
            taskStatus["E34"] = True
    elif task == "3.5" and not taskStatus["E35"]:
        if(diamondStar()):
            taskStatus["E35"] = True
    elif task == "3.6" and not taskStatus["E36"]:
        if(alphabetDiamond()):
            taskStatus["E36"] = True
    elif task == "4" and not taskStatus["E4"]:
        if(elseFinally()):
            taskStatus["E4"] = True
    elif task == "5" and not taskStatus["M1"]:
        if(primeNumbers()):
            taskStatus["M1"] = True
    else :
        print("\nInvalid, Please try to input again")
    print()
    
try:
    with open('task.pickle', 'rb') as handle:
        loadfile = pickle.load(handle)
    taskStatus = loadfile
except EOFError:
    taskStatus = {"E1": False, "E2": False, "E31": False, "E32": False, "E33": False,
                  "E34": False, "E35": False, "E36": False, "E4": False, "M1": False}
