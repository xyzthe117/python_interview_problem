def atoi(str):
    resultant = 0
    for i in range(len(str)):
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))        
    return resultant
    
#Easy 1

# for i in range(100):
#   if((i+1)%15==0):
#     print("FizzBuzz", end =" ")
#   elif((i+1)%3==0):
#     print("Fizz", end =" ")
#   elif((i+1)%5==0):
#     print("Buzz", end =" ")
#   else:
#     print(i+1, end =" ")

#Easy 2

# while(1):
#   val = input("Enter your value(Press Enter to Exit): ") 
#   if(val==''):
#     exit()
#   year=atoi(val)
#   if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("-> True")
#        else:
#            print("-> False")
#    else:
#        print("-> True")
#   else:
#     print("-> False")

#Easy 3.1
# while(1):
#   val = input("Enter your value(Press Enter to Exit): ") 
#   if(val==''):
#     exit()
#   n=atoi(val)
#   for i in range(0, n):
#     for j in range(0, i+1):
#       # printing stars
#       print("* ",end="")
        
#     # ending line after each row
#     print("\r")

#Easy 3.2
# while(1):
#   val = input("Enter your value(Press Enter to Exit): ") 
#   if(val==''):
#     exit()
#   n=atoi(val)
# # number of spaces
#   k = 2*n - 2
#   # outer loop to handle number of rows
#   for i in range(0, n):
#       # inner loop to handle number spaces
#       # values changing acc. to requirement
#       for j in range(0, k):
#           print(end=" ")
#       # decrementing k after each loop
#       k = k - 2
#       # inner loop to handle number of columns
#       # values changing acc. to outer loop
#       for j in range(0, i+1):
#           # printing stars
#           print("* ", end="")
#       # ending line after each row
#       print("\r")

#Easy 3.3
# while(1):
#   val = input("Enter your value(Press Enter to Exit): ") 
#   if(val==''):
#     exit()
#   n=atoi(val)
#   k = 0
#   for i in range(1,n+1) : #row 6 
#       # Print spaces 
#       for j in range(i,n) : 
#           print(' ', end='') 
        
#       # Print # 
#       while (k != (2 * i - 1)) : 
#           if (k == 0 or k == 2 * i - 2) : 
#               print('#', end='') 
#           else : 
#               print(' ', end ='') 
#           k = k + 1
#       k = 0; 
#       print ("") # print next row 
        
#Easy 3.4
def ex34():
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
    return 1111
  
  


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
        second_menu()
    elif choice == "4":
        print("Do Something 4")
    elif choice == "3":
        print("Do Something 3")
    elif choice == "2":
        print("Do Something 2")
    elif choice == "1":
        test=ex34()
    else:
        print("I don't understand your choice.")
    print(test)


main()
