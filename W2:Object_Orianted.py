

class Student():
    def __init__(self):
        print("""************
        1- Create an Account
        2- Delete an Account
        3- Get Information
        4- Exit
        """)

    def register(self):
        name=input("Enter the name:")
        surname=input("Enter the surname:")
        ID=input("Enter the student ID:")
        cla=input("Enter the class")
        age=input("Enter the age")
        gender=input("Enter the gender")

        information=(ID,"\t",name,"\t",surname,"\t",cla,"\t",age,"\t",gender)


        with open("ogrenci.txt","a",encoding= "utf-8") as file:
            for i in information:
                file.write(i)
            file.write("\n")
    def remove(self):
        print("**********\nStudent deletion")
        ID_control=input("Enter the ID")
        f = open("ogrenci.txt","r")
        lines = f.readlines()
        f.close()
        f = open("ogrenci.txt","w")
        for line in lines:
            if ID_control not in line:
                f.write(line)
        f.close()
    def info(self):
        ID_control=input("Enter the student ID")
        f = open("ogrenci.txt","r")
        lines = f.readlines()
        for line in lines:
            if ID_control in line:
                print(line.split("\t"))


ogrenci=Student()
while True:
    process=int(input("Choose the process:"))
    if process==1:
        ogrenci.register()
    if process==2:
        ogrenci.remove()
    if process==3:
        ogrenci.info()
    if process==4:
        break