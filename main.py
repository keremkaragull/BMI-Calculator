from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)

#title
bmi_calculator = Label(text="BMI Calculator", font=("Arial",30), fg="black")
bmi_calculator.pack()


#enterheight
enter_height = Label(text="Enter Height(cm)",font=("Arial",10))
enter_height.pack()

#height
height = Entry()
height.pack()

#enterweight
enter_weight = Label(text="Enter Weight(kg)",font=("Arial",10))
enter_weight.pack()


#weight
weight = Entry()
weight.pack()

#truncate
def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier

#reportfunc
report = Label(text="Please enter a valid number!", font=("Arial", 10))
report1 = Label(text="Enter both weight and height!", font=("Arial",10))

#bmicalculator
result_label = Label()
x_label = Label()

def bmi_calculator():
    report.forget()
    report1.forget()
    global bmi

    user_weight = weight.get()
    user_height = height.get()
    if weight.get() == "" or height.get() == "":
        report1.pack()
    else:
        try:
            bmi = float(user_weight) / ((float(user_height)/100)**2)
            result_label.config(text="Your BMI is {}".format(truncate(n=bmi, decimals=1)), font=("Arial", 10))

        except:
            report.pack()

    if bmi <18.5:
        x = "Underweight"
    elif 18.5<=bmi<=24.9:
        x = "Normalweight"
    elif 24.9<=bmi<=29.9:
        x = "Overweight"
    elif 29.9< bmi:
        x = "Obesity"


    x_label.config(text="You are {}".format(x), font=("Arial", 10))
    result()
    report.forget()
    report1.forget()
#result

def result():
    global x
    global bmiResult
    calculate.forget()
    enter_weight.forget()
    enter_height.forget()
    weight.forget()
    height.forget()
    result_label.pack()
    x_label.pack()
    back.pack()
def back_func():
    global input_weight
    global input_height
    enter_height.pack()
    height.pack()
    enter_weight.pack()
    weight.pack()
    result_label.forget()
    back.forget()
    x_label.forget()
    calculate.pack()

#button
calculate = Button(text="Calculate", command=bmi_calculator)
back = Button(text="Back",command=back_func)
calculate.pack()




window.mainloop()