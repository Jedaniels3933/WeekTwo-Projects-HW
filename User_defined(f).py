#user defined 

#Syntax
# def = define function_name():
    # code block executed when called

def devi():
    print("=" * 100)

devi()
  # Calls the function 

def greeting():
    print("Hello, Buddy!")

greeting()  # Calls the function
devi()
greeting()
devi()
#Can also do this

def devi2():
    return '+' * 100

print(devi2())  # wont do anything unless printed since it did not print anything
devi2() , greeting() 

#Function witH VARIABLES    
def personal_greeting(name):
    print(f"Hello {name}, Welcome!!")

personal_greeting("John Doe")
# prints out Hello John Doe, Welcome!!

person = "Eric"
personal_greeting(person)  

devi()

def class_info(teacher, students):
    print(f"This class is taught by {teacher}!")
    class_size = len(students)
    print(f"It has {class_size} students")
    for i in students:
        print(i)
students = ["Joe","Barry","Billy","Peter"] 
class_info("Mr Brewster", students)

devi()
class_info("Mr. Daniels", students)

def book_info(thing1, thing2):
    print(f"The author is {thing1}")
    print(f"The book is called {thing2}")

book_info("GRR Martin", "Game of Thrones")

def Vgame_info(thing1, thing2):
    print(f"The developer is {thing1}")
    print(f"The game is called {thing2}")

Vgame_info("From Software","Elden Ring")









