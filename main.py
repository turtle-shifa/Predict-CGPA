from tkinter import *

def calculate_func():
    current_cgpa = currentCGPA.get("1.0",'end-1c')
    completed_credits = completedCredits.get("1.0",'end-1c')
    total_credits = totalCredits.get("1.0",'end-1c')
    goal_cgpa = goalCGPA.get("1.0",'end-1c')


    if current_cgpa!="" and completed_credits!="" and total_credits!="" and goal_cgpa!="":
        current_grade_points = float(current_cgpa) * int(completed_credits)
        total_grade_points_for_target_cgpa = float(goal_cgpa) * int(total_credits)
        grade_points_remain = total_grade_points_for_target_cgpa - current_grade_points
        required_cgpa = round(grade_points_remain / (int(total_credits)-int(completed_credits)),2)

            #calculate.state = "enabled"

        if 0.0<=required_cgpa<=4.0:
            resultBox.delete(0.0, END)
            resultBox.insert(END, f"You would need to achieve an average of approximately {required_cgpa} in your remaining {int(total_credits)-int(completed_credits)} credits to reach a CGPA of {float(goal_cgpa)}.")
        else:
            resultBox.delete(0.0, END)
            resultBox.insert(END, f"To achieve a CGPA of {float(goal_cgpa)} after completing your degree, you would need to achieve an average of approximately {required_cgpa} in your remaining {int(total_credits)-int(completed_credits)} credits. Since the maximum CGPA is typically 4.0, it is not possible to reach a CGPA of {float(goal_cgpa)} with your current performance and remaining credits.")

    else:
        resultBox.delete(0.0,END)
        resultBox.insert(END,"Please fill out the required form.")



window = Tk()
window.geometry('800x500')
window.title("Predict Your CGPA")

#Interface Design
#Software Name
progName = Label(window,font=("Courier New",20,"bold"),text="CGPA Predictor",fg="red")
progName.place(relx=0.35,rely=0.07)

#Current Cgpa Label + text box
c_cgpa = Label(window,font=("Courier New",13,"bold"),text="Current CGPA:",fg="black")
c_cgpa.place(relx=0.25,rely=0.19)
currentCGPA = Text(window,height=1, width=10,font=("Courier New",13,"bold"),fg="blue",bg="LightCyan")
currentCGPA.place(relx=0.42,rely=0.19)

#Completed Credit Label + text box
c_credit = Label(window,font=("Courier New",13,"bold"),text="Completed Credits:",fg="black")
c_credit.place(relx=0.25,rely=0.26)
completedCredits = Text(window,height=1, width=10,font=("Courier New",13,"bold"),fg="blue",bg="LightCyan")
completedCredits.place(relx=0.485,rely=0.26)

#Goal CGPA Label + text box
g_cgpa = Label(window,font=("Courier New",13,"bold"),text="Target CGPA:",fg="black")
g_cgpa .place(relx=0.25,rely=0.33)
goalCGPA = Text(window,height=1, width=10,font=("Courier New",13,"bold"),fg="blue",bg="LightCyan")
goalCGPA.place(relx=0.41,rely=0.33)

#Total Credits Label + text box
t_credits = Label(window,font=("Courier New",13,"bold"),text="Total Credits:",fg="black")
t_credits .place(relx=0.25,rely=0.4)
totalCredits = Text(window,height=1, width=10,font=("Courier New",13,"bold"),fg="blue",bg="LightCyan")
totalCredits.place(relx=0.435,rely=0.4)

#calulate_button
calculate = Button(window,text="Predict Now!",command=calculate_func,font=("Courier New",13,"bold"),fg="blue")
calculate.place(relx=0.43,rely=0.5)

#Result_box
resultBox = Text(window,height=7,width=70,font=("Courier New",12,"bold"),fg="blue",bg="LightCyan")
resultBox.place(relx=0.06,rely=0.6)

#build credit
build = Label(window,font=("Courier New",10),text="Developed by Turtle Shifa",fg="black")
build.place(relx=0.35,rely=0.9)
window.mainloop()
