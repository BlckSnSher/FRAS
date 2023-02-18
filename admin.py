import pymysql.connections
import csv
import tkinter

root = tkinter.Tk()
root.title("Student Details")
root.configure(background='grey80')

db = pymysql.connect(host="localhost", user="username", passwd=" ", db="Admin")
cursor = db.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
cursor.execute(query)
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

cs = 'C:/FRAS/Student Details/StudentDetails1.csv'
with open(cs, newline="") as file:
        reader = csv.reader(file)
        r = 0

        for col in reader:
            c = 0
            for row in col:
                            # i've added some styling
                label = tkinter.Label(root, width=10, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="white", text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
                r += 1
            root.mainloop()