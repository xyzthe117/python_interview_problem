
#Thanathkitt Paetyathai Tel. 094-550-1140 E-mail: jirapat.krzx@mail.kmutt.ac.th
#This code is for CODIUM internship interview only
#25/3/2021

import pickle

# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
# instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
def ex1():
    for i in range(100):
        if((i+1)%15==0):
            print("FizzBuzz", end =" ")
        elif((i+1)%3==0):
            print("Fizz", end =" ")
        elif((i+1)%5==0):
            print("Buzz", end =" ")
        else:
            print(i+1, end =" ")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
  

# Write a program that determine whether or not an integer input is a leap year.
def ex2():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        if (n % 4) == 0:
            if (n % 100) == 0:
                if (n % 400) == 0:
                    print(n,"-> True")
                else:
                    print(n,"-> False")
            else:
                print(n,"-> True")
        else:
            print(n,"-> False")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
    

    #Write a program that produce the following output giving an integer input n.

    #Star Pattern(Right Triangle)
def ex31():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(0, n):
            for j in range(0, i+1):
                print("* ",end="")
            print("\r")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")


#Star Pattern(Mirrored Right Triangle)
def ex32():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        k = 2*n - 2
        for i in range(0, n):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i+1):
                print("* ", end="")
            print("\r")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
  

#Star Pattern(Hollow Pyramid without base)
def ex33():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        k = 0
        for i in range(1,n+1) : 
            for j in range(i,n) : 
                print(' ', end='') 
            while (k != (2 * i - 1)) : 
                if (k == 0 or k == 2 * i - 2) : 
                    print('#', end='') 
                else : 
                    print(' ', end ='') 
                k = k + 1
            k = 0; 
            print ("")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")


#Star Pattern(X-cross)
def ex34():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        i,j=0,n-1
        while j >= 0 and i < n:
            initial_spaces = ' '*min(i,j)
            middle_spaces = ' '*(abs(i - j) - 1)
            final_spaces = ' '*(n - 1 - max(i,j))
            if j == i:
                print (initial_spaces + '*' + final_spaces)
            else:
                print (initial_spaces + '*' + middle_spaces + '*' + final_spaces)
            i += 1
            j -= 1
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
  

#Star Pattern(Diamond)
def ex35():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(n+1) :
            if i%2!=0 :
                val = (n - i) // 2
                print(" "*val + "*"*(i) + " "*val)
        for j in range(n-1, 0, -1) :
            if j%2!=0 :
                val = (n-j)//2
                print(" "*val + "*"*(j) + " "*val)
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
  

#Alphabet Pattern with + sign
def ex36():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        for i in range(1, n+1):
            for j in range(1, n-i+1):
                print("A", end="")
            for j in range(1, 2*i):
                if j == 1 or j == 2*i-1:
                    print("+", end="")
                else:
                    print("E", end="") 
            for j in range(1, n):
                if(j < i):
                    print('', end='')
                else:
                    print("B", end='')
            print()
        for i in range(n-1, 0, -1):
            for j in range(1, n-i+1):
                print("C", end="")
            for j in range(1, 2*i):
                if j == 1 or j == 2*i-1:
                    print("+", end="")
                else:
                    print("E", end="")
            for j in range(1, n + 1):
                if(j > n - i):
                    print('', end='')
                else:
                    print("D", end='')
            print()
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")


#What is the difference between else and finally in exception handling?
def ex4():
    print("Else: If there is no exception then this block will be executed")
    print("Finally: Finally block always gets executed either exception is generated or not")
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")
  

#Prime Number up to input 
def ex5():
    while(1):
        n = input("\nEnter the Number (Press 'ENTER' to exit) : ")
        if len(n) <= 0:
            break
        else:
            n = int(n)
        print(n,"->",end=" ")
        for num in range(0, n + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num,end=" ")
        print()
    while(1):
        conf = input("\nConfirm task completed (Y/N)*Capital Letter Only: ")
        if conf == "Y":
            return True
        elif conf == "N":
            return False
        else:
            print("Invalid, Please input only Y or N\n")

def resetTask():
    initStatus = {"ex1": False, "ex2": False, "ex31": False, "ex32": False, "ex33": False,"ex34": False, "ex35": False, "ex36": False, "ex4": False, "ex5": False}
    with open('task.pickle', 'wb') as handle:
        pickle.dump(initStatus, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return True

# Status of each task
status = {"ex1": False, "ex2": False, "ex31": False, "ex32": False, "ex33": False,"ex34": False, "ex35": False, "ex36": False, "ex4": False, "ex5": False}

while(1):
    print("Select the tasks (Press 'ENTER' to exit): ")
    print("     Remaining Task: ")
    print("       Reset task [Press 0]")
    print("       Easy 1: 1-100 Fizz&Buzz [Press 1]") if not status["ex1"] else None
    print("       Easy 2: Leap Year Check [Press 2]") if not status["ex2"] else None
    print("       Easy 3.1: Star Pattern(Right Triangle) [Press 3.1]") if not status["ex31"] else None
    print("       Easy 3.2: Star Pattern(Mirrored Right Triangle)[Press 3.2]") if not status["ex32"] else None
    print("       Easy 3.3: Star Pattern(Hollow Pyramid without base)[Press 3.3]") if not status["ex33"] else None
    print("       Easy 3.4: Star Pattern(X-cross)[Press 3.4]") if not status["ex34"] else None
    print("       Not Easy 3.5: Star Pattern(Diamond) [Press 3.5]") if not status["ex35"] else None
    print("       Easy 3.6: Alphabet Pattern with + sign [Press 3.6]") if not status["ex36"] else None
    print("       Easy 4: What is the difference between else and finally in exception handling? [Press 4]") if not status["ex4"] else None
    print("       Medium 5: Prime Number up to input [Press 5]") if not status["ex5"] else None

    task = input("Enter the task number: ")

    if len(task) <= 0:
        with open('task.pickle', 'wb') as handle:
            pickle.dump(status, handle, protocol=pickle.HIGHEST_PROTOCOL)
        quit()

    elif task == "0":
        if(resetTask()):
            print("\nTask Already Reset")
            with open('task.pickle', 'rb') as handle:
                loadfile = pickle.load(handle)
            status = loadfile  

    elif task == "1" and not status["ex1"]:
        if(ex1()) :
            status["ex1"] = True

    elif task == "2" and not status["ex2"]:
        if(ex2()) :
            status["ex2"] = True

    elif task == "3.1" and not status["ex31"]:
        if(ex31()):
            status["ex31"] = True

    elif task == "3.2" and not status["ex32"]:
        if(ex32()):
            status["ex32"] = True

    elif task == "3.3" and not status["ex33"]:
        if(ex33()):
            status["ex33"] = True

    elif task == "3.4" and not status["ex34"]:
        if(ex34()):
            status["ex34"] = True
    
    elif task == "3.5" and not status["ex35"]:
        if(ex35()):
            status["ex35"] = True
    
    elif task == "3.6" and not status["ex36"]:
        if(ex36()):
            status["ex36"] = True
    
    elif task == "4" and not status["ex4"]:
        if(ex4()):
            status["ex4"] = True
    
    elif task == "5" and not status["ex5"]:
        if(ex5()):
            status["ex5"] = True
    
    else :
        print("\nInvalid, Please try to input again")
    print()
    
try:
    with open('task.pickle', 'rb') as handle:
        loadfile = pickle.load(handle)
    status = loadfile
except EOFError:
    status = {"ex1": False, "ex2": False, "ex31": False, "ex32": False, "ex33": False,"ex34": False, "ex35": False, "ex36": False, "ex4": False, "ex5": False}
