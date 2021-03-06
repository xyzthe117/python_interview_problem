
#Easy 1
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

#Easy 2
def ex2():
    while(1):
        val = input("Enter your value(Press Enter to Exit): ") 
        if(val==''):
            exit()
        year=int(val)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("-> True")
                else:
                    print("-> False")
            else:
                print("-> True")
        else:
            print("-> False")
    

#Easy 3.1
def ex31():
    while(1):
        n = int(input("Enter your value(Press Enter to Exit): "))
        if(n==''):
            exit()
        for i in range(0, n):
            for j in range(0, i+1):
            # printing stars
                print("* ",end="")
                
            # ending line after each row
            print("\r")

#Easy 3.2
while(1):
  val = input("Enter your value(Press Enter to Exit): ") 
  if(val==''):
    exit()
  n=atoi(val)
# number of spaces
  k = 2*n - 2
  # outer loop to handle number of rows
  for i in range(0, n):
      # inner loop to handle number spaces
      # values changing acc. to requirement
      for j in range(0, k):
          print(end=" ")
      # decrementing k after each loop
      k = k - 2
      # inner loop to handle number of columns
      # values changing acc. to outer loop
      for j in range(0, i+1):
          # printing stars
          print("* ", end="")
      # ending line after each row
      print("\r")

#Easy 3.3
while(1):
  val = input("Enter your value(Press Enter to Exit): ") 
  if(val==''):
    exit()
  n=atoi(val)
  k = 0
  for i in range(1,n+1) : #row 6 
      # Print spaces 
      for j in range(i,n) : 
          print(' ', end='') 
        
      # Print # 
      while (k != (2 * i - 1)) : 
          if (k == 0 or k == 2 * i - 2) : 
              print('#', end='') 
          else : 
              print(' ', end ='') 
          k = k + 1
      k = 0; 
      print ("") # print next row 
        
#Easy 3.4
# def ex34():
while(1):
    val = input("Enter your value(Press Enter to Exit): ") 
    if(val==''):
        exit()
    n=atoi(val)
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
    
  
  
#Not Easy 3.5
while(1):
    n = int(input("Enter the Number: "))
    for i in range(n+1) :
        if i%2!=0 :
            val = (n - i) // 2
            print(" "*val + "*"*(i) + " "*val)
    for j in range(n-1, 0, -1) :
        if j%2!=0 :
            val = (n-j)//2
            print(" "*val + "*"*(j) + " "*val)

# Not Easy 3.6
while(1):
    n = int(input("Enter the Number: "))
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
# Medium
while(1):
    val = input("Enter your value(Press Enter to Exit): ") 
    if(val==''):
      exit()
    n=atoi(val)
    print(n,"->",end=" ")
    for num in range(0, n + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num,end=" ")
    print()

def main():
  choice ='0'
  while choice =='0':
    print("Main Choice: Choose 1 of 5 choices")
    print("Choose 1 for something")
    print("Choose 2 for something")
    print("Choose 3 for something")
    print("Choose 4 for something")
    print("Choose 5 to go to another menu")

    choice = input ("Please make a choice: ")

    if choice == "5":
        print("Go to another menu")
        main()
    elif choice == "4":
        print("Do Something 4")
    elif choice == "3":
        ex31()
        choice ='0'
        main()
    elif choice == "2":
        ex2()
        choice ='0'
        main()
    elif choice == "1":
        ex1()
        choice ='0'
        main()
    else:
        print("I don't understand your choice.")

main()
