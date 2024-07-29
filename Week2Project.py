# User Interface Project
def main():
    tasks = []
    while True:
        ans= input('''
"Welcome to the to-do list manager app!!!
Enter an option , please: 
1. Add a task
2. View All Tasks
3. Mark a Task as Complete 
4. Delete a Task
5. Exit                   
''')
        if ans == '1':
            value = task = input("Please enter a task: ")
            tasks.append(value)
            print(f 'Task' {value} added successfully.')
        if ans == '2':  
            print("List of all tasks:")
            print(tasks[0:])     #display by slicing 
        if ans == '3':
            index = int(input("Which task would you like to cross off the list ?: "))
            if 0 < index <= len(tasks):
                tasks[index-1] = f'{tasks[index-1]} (Completed)'
                print(f'Task {tasks[index-1-1]} marked as complete.')
                print(tasks)
        if ans == '4':
            index = int(input("Which task would you like to delete: "))   #Not user-friendly Askin for index to remove
            if 0 < index <= len(tasks):
                del tasks[index-1]
                print(f'Task {tasks[index[-1][-1]]} deleted successfully.')
            else:
                print("Please read the menu again and make a numerical choice .")     
        if ans == '5':
            print("See  ya later aligator - COme back SOon!")
            break
main()     








      
       