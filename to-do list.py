tasks=[]

def addTask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"Task'{task}' Added to the list.")

def listTasks():
    if not tasks:
        print("no task now.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete= int(input("Enter the task to delete:"))
        if taskToDelete >=0 and taskToDelete <len(tasks):
            tasks.pop(taskToDelete)
            print(f"task has been deleted.")
        else:
            print(f"task not found.")
    except:
        print("invalid input.")

if __name__=="__main__":
    print("To Do List:")
    while True:
        print("\n")
        print("please select your choice:-")  
        print("\n")
        print("1. Add a new task.")
        print("2. Delete a task.")
        print("3. List task")
        print("4. Quit")
        
        choice=input("Enter your choice:")
    
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):
            break
        else: 
            print("Invalid Input. Please try again.")
    print("Thank you.") 