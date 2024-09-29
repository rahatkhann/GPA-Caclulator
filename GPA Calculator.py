# instructions
def print_instructions():
  print("Welcome to GPA Calculator!")
  print()
  print("You will be asked to input your total number of classes.")
  print()
  print("Then you will be asked to input your class name,")
  print("grade recieved and type of class.")
  print()
  print("After you input everything your report card will")
  print("be printed with your weighted and unweighted gpa.")
  print("---------------------------------------------------------")

# call instructions function
print_instructions()

# variables
types = ["AP", "Honors", "Regular"]
total_classes = 0
class_grade = [] 
class_names = []
class_type = []

# ask for total number of classes
total_classes = int(input("How many classes are you taking? "))
print("---------------------------------------------------------")

# ask for all the information
for  i in range(total_classes):
  name = input("What is the name of the class? ")
  grade = input("What grade did you get in that class? ")
  print("1 = AP, 2 = Honors, 3 = Regular")
  diff = int(input("What type of class? "))
  type = types[diff - 1]
  class_type.append(type)
  class_grade.append(grade)
  class_names.append(name)

# calculate weighted gpa
def weighted_calc_gpa(classes):
    points = 0
    for i in range(classes):
        if class_grade[i] == "A" or class_grade[i] == "a":
            points += 4
        elif class_grade[i] == "B" or class_grade[i] == "b":
            points += 3
        elif class_grade[i] == "C" or class_grade[i] == "c":
            points += 2
        elif class_grade[i] == "D" or class_grade[i] == "d":
            points += 1
        elif class_grade[i] == "F" or class_grade[i] == "f":
            points += 0
        else:
            points += 0
        if class_type[i] == "AP": 
          points += 1
        elif class_type[i] == "Honors": 
          points += 0.5
    return points / classes

# calculate unweighted gpa
def unweighted_calc_gpa(classes):
    points = 0
    for i in range(classes):
        if class_grade[i] == "A" or class_grade[i] == "a":
            points += 4
        elif class_grade[i] == "B" or class_grade[i] == "b":
            points += 3
        elif class_grade[i] == "C" or class_grade[i] == "c":
            points += 2
        elif class_grade[i] == "D" or class_grade[i] == "d":
            points += 1
        elif class_grade[i] == "F" or class_grade[i] == "f":
            points += 0
        else:
            points += 0
    return points / classes

print("---------------------------------------------------------")

# calls function to calculates and rounds the unweighted and weighted gpa to 3 decimals 
u_gpa = unweighted_calc_gpa(total_classes)
u_gpa = round(u_gpa, 3)
w_gpa = weighted_calc_gpa(total_classes)
w_gpa = round(w_gpa,3)

# print report card
def print_results(u_gpa, w_gpa):
  print("Class Type         Class Name               Class Grade ")
  for i in range(total_classes):
    print("{:<18} {:<15} {:>15} ".format(class_type[i], class_names[i], class_grade[i]))
  print()
  print("Your unweighted gpa is " +str(u_gpa)+"!")
  print("Your weighted gpa is " +str(w_gpa)+"!")
  
# call function
print_results(u_gpa, w_gpa)