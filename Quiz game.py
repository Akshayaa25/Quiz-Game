#Quiz Game

import pymysql
from tabulate import tabulate

connection = pymysql.connect(host="localhost", user="root", password='', db="QuizGame")
cursor = connection.cursor()


class Teacher:
    def signup(self):
        self.username = input("Enter the username : ")
        self.password = input("Enter the password : ")
        column = (self.username,self.password)
        cmd = "insert into teacher(username,password) values(%s,%s)"
        cursor.execute(cmd,column)
        print()
        teacher.after_login()

    def login(self):
        self.username = input("Enter the username : ")
        self.password = input("Enter the password : ")
        cmd = "select * from teacher where username='%s' and password='%s'" %(self.username,self.password)
        cursor.execute(cmd)
        data = cursor.fetchall()
        if len(data) > 0:
            print("Login Successfully")
            print()
            teacher.after_login()
        else:
            print("Invalid User")
        print()

    def after_login(self):
        while True:
            print("1.Question Details \n2.Student Scores \n3.Exit")
            ch = int(input("Enter the choice number : "))
            print()
            if ch==1:
                teacher.question_details()
            elif ch == 2:
                teacher.student_scores()
            else:
                break
            print()    

    def question_details(self):
        while True:
            print("1.Add Questions \n2.View Questions \n3.Delete all questions \n4.Exit")
            ch = int(input("Enter the choice number : "))
            print()
            if ch == 1:
                teacher.add_question()
            elif ch == 2:
                teacher.view_question()
            elif ch == 3:
                teacher.deleteall_question()
            else:
                break
            print()  
        
    def add_question(self):
        self.n = int(input("How many questions do you want to add? "))
        for i in range(self.n):
            self.question = input("Enter the question : ")
            self.opt_a = input("Enter the option 1 : ")
            self.opt_b = input("Enter the option 2 : ")
            self.opt_c = input("Enter the option 3 : ")
            self.opt_d = input("Enter the option 4 : ")
            self.answer = int(input("Enter the answer (option number) : "))
            column = (self.question,self.opt_a,self.opt_b,self.opt_c,self.opt_d,self.answer)
            cmd = "insert into questions(question,opt_a,opt_b,opt_c,opt_d,answer) values (%s,%s,%s,%s,%s,%s)"
            cursor.execute(cmd,column)
        print()

    def view_question(self):
        cmd = "select * from questions"
        cursor.execute(cmd)
        data = cursor.fetchall()
        for row in data:
            print("{}.{}".format(row[0],row[1]))
            print("Option 1 : ",row[2])
            print("Option 2 : ",row[3])
            print("Option 3 : ",row[4])
            print("Option 4 : ",row[5])
            print("Answer :",row[6])
            print()

    def deleteall_question(self):
        print("Are you sure you want to delete all questions?")
        print("1.Yes\t2.No")
        confirmation = int(input("Enter the choice number : "))
        if (confirmation == 1):
            cmd = "truncate table questions"
            cursor.execute(cmd)
            print("Deleted all contacts successfully")
        print()

    def student_scores(self):
        cmd = "select username,score from student"
        cursor.execute(cmd)
        data = cursor.fetchall()
        headers = ["Student Name","Score"]
        print(tabulate(data, headers, tablefmt="fancy_grid",numalign="center", stralign="center"))
        print()
        

class Student:
    def login(self):
        self.username = input("Enter the username : ")
        self.password = input("Enter the password : ")
        column = (self.username,self.password)
        cmd = "insert into student(username,password) values(%s,%s)"
        cursor.execute(cmd,column)
        print()

    def instructions(self):
        print("Read the following questions carefully.")
        print("You have only one chance to answer the questions.")
        print("Answer all the questions.")
        print("Enter the option number for answer.")
        print("All the best!")
        print()

    def question(self):
        cmd = "select * from questions"
        cursor.execute(cmd)
        data = cursor.fetchall()
        self.mark = 0
        self.noq = 0
        for row in data:
            self.noq += 1
            print("{}.{}".format(row[0],row[1]))
            print("Option 1 : ",row[2])
            print("Option 2 : ",row[3])
            print("Option 3 : ",row[4])
            print("Option 4 : ",row[5])
            self.ans = int(input("Answer : "))
            if self.ans == row[6]:
                self.mark+=1
                print("Correct Answer!")
            else:
                print("Wrong Answer!")
            print()

    def score(self):
        # column = (self.mark,self.username)
        cmd = "update student set score='%s' where username='%s'" %(self.mark,self.username)
        cursor.execute(cmd)
        print("Your Score : {}/{}".format(self.mark,self.noq))
        print()

    def viewans(self):
        cmd = "select * from questions"
        cursor.execute(cmd)
        data = cursor.fetchall()
        for row in data:
            print("{}.{}".format(row[0],row[1]))
            print("Option 1 : ",row[2])
            print("Option 2 : ",row[3])
            print("Option 3 : ",row[4])
            print("Option 4 : ",row[5])
            print("Answer :",row[6])
            print()


teacher = Teacher()
student = Student()


while True:
    print("*****Welcome to the Quiz Game*****")
    print("1.Teacher \n2.Student \n3.Exit")
    choice = int(input("Enter the choice number : "))
    print()
    if choice==1:
        print("1.Login \t 2.Signup \t 3.Exit")
        ch = int(input("Enter the choice number : "))
        print()
        if ch == 1:
            teacher.login()
        elif ch == 2:
            teacher.signup()
        else:
            break

    if choice==2:
        print("Do you want to play?")
        print("1.Yes \t 2.No")
        ch = int(input("Enter the choice number : "))
        if ch == 1:
            student.login()
            student.instructions()
            student.question()
            student.score()
            print("Do you want want view answers?")
            print("1.Yes \t 2.No")
            ch = int(input("Enter the choice number : "))
            if ch == 1 :
                student.viewans()
                print("*****Thank You*****")
            else:
                print("*****Thank You*****")
        else:
            break

    else:
        break

connection.commit()
connection.close()