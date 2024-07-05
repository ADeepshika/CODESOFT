print("Calculator.")

print("Enter the operation to perform:")
print("1.Add")
print("2.Subtrct")
print("3.Multiply")
print("4.Divide")

operation=input("Enter your choice:")
if (operation== "1"):
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The sum is:", num1 + num2)
elif (operation=="2"):
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The difference is:", num1 - num2)
elif (operation=="3"):
     num1=int(input("Enter the first number:"))
     num2=int(input("Enter the second number:"))
     print("The Product sum is:", num1 * num2)
elif (operation=="4"):
     num1=int(input("Enter the first number:"))
     num2=int(input("Enter the second number:"))
     print("The division sum is:",num1 / num2)
else:
     print("The Value is Invalid.")








