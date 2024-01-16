"""
TASK 1   -  TO-DO LIST
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
"""


list = []
num =0
def display():
    for i in list:
        print(i)

def insert():
    global num
    print ("How many task you want to enter")
    answer = int(input())
    for answer in range(answer):
        line = input('>')
        num+=1
        list.append(f"{num}. {line} ")


while True:
        
    print(""" What do you want to do 
        create    - for creating a todo list
        update    - for updating your todo list
        display   - for track/display the todo list
        """)
    answer = input()

    #Creating list..
    if answer.lower() == 'create':
        insert()
        print("List is successfully created")


    #updation of list...
    elif answer.lower() == 'update':
        print("This is the list ")
        display()
        print("What do you want to do insertion/deletion ??")
        if input().lower().startswith('i'):
            insert()
            
        else:
            print("inter the list no to delete")
            index =int(input())
            list.pop(index-1)
        
        print("List is successfully updated")

        

    elif answer.lower() == 'display':
        display()

    else:
        print("Please enter the right input")

    print("Do you want to continue....")
    if not input().lower().startswith('y'):
        break
    
print("Bye BYe .....")
    

