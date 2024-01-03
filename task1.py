"""
TASK 1   -  TO-DO LIST
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
"""
#underprocess............
def todo_list():
    while True:
        list = []
        print(""" What do you want to do 
            create    - for creating a todo list
            update    - for updating your todo list
            delete    - for deleting the todo list
            """)
        answer = input()
        if answer.lower() == 'create':
            print ("How many task you want to enter")
            answer = int(input())
            for i in range(answer):
                line = input('>')
                list.append(line+"\n")
            print("Your todo list is successfully created")

        elif answer.lower() == 'update':
            line = input('>')
            list.append(line+"\n")
            print("Your todo list is successfully created")

        elif answer.lower() == 'track':
            for i in list:
                print(i)

        else:
            print("Please enter the right input")

        print("Do you want to continue....")
        if not input().lower().startswith('y'):
            break
    

todo_list()


    

