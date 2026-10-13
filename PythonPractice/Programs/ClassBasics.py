class Student:
    college_City = "Pune"    #class variables
    college_pincode = 411025
    
    @staticmethod
    def welcome(): # static method
        print("Welcome to VIT college")
    
    def __init__ (self, name, marks):   #paramaterized constructor
        self.name = name
        self.marks = marks
     
    def get_avg(self): # method
        sum = 0
        for i in self.marks:
            sum = sum + i 
        return sum/3
               

stu1 = Student("Rupesh",[97,98,99]) # object
print("************************")
Student.welcome()
print(Student.college_City,Student.college_pincode)
print (stu1.name, stu1.marks)   
print ("Avg score is: ",stu1.get_avg())

stu2 = Student("VJ",[97,98,99])
print("************************")
Student.welcome()
print(Student.college_City, Student.college_pincode)
print(stu2.name, stu2.marks) 
print("Avg score is: ",stu2.get_avg())