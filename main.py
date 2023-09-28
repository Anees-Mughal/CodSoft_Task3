from tkinter import *

# calculator main page
root = Tk()
root.geometry("150x150+500+150")
#input number from the user
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

# Calcultion

function = input("enter + for Addition \n - for Subtraction \n "
                     "* for Multiplication \n / for Division \n ")
if (function == "+"):
    cal = (first_num+second_num)
    print_fun = "The answer is = ", cal
    label = Label(root, text= print_fun)
    print("The additon of ", first_num, "and" , second_num , "Is = " , cal)
elif (function=="-"):
    cal = (first_num - second_num)
    print_fun = "The answer is = ", cal
    label = Label(root, text=print_fun)
    print("The subtration of ", first_num, "and", second_num, "Is = ", cal)
elif (function=="*"):
    cal = (first_num * second_num)
    print_fun = "The answer is = ", cal
    label = Label(root, text=print_fun)
    print("The multiplication of ", first_num, "and", second_num, "Is = ", cal)
elif (function=="/"):
    cal = (first_num / second_num)
    print_fun = "The answer is = ", cal
    label = Label(root, text=print_fun)
    print("The division of ", first_num, "and", second_num, "Is = ", cal)
else:
    print_fun = "You enter the invalid value"
    label = Label(root, text=print_fun)
    print("You enter the invalid value")
label.pack()
root.mainloop()