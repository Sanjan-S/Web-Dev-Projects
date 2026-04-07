import json
try:
    with open("data.json","r") as f:
        tasks=json.load(f)
except  FileNotFoundError:
    tasks=[]

def save_tasks():
    with open("data.json","w") as f:
        json.dump(tasks,f,indent=4)

while True:
    print("\n---TO DO LIST---")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete")
    print("4.Toggle Task Status")
    print("5.Delete all completed tasks")
    print("6.Exit")

    try:

        choice=int(input("Enter your choice: "))

    except ValueError:
        print("Invalid Input!!\nEnter correct Input")

    else:

        if choice==1:
            new_task=input("Enter the new task: ")
            tasks.append({"title": new_task, "done": False})
            save_tasks()
            print("Task added!")

        elif choice==2:
            if len(tasks)==0:
                print("The to do list is empty")
            else:
                for i,task in enumerate(tasks):
                    status="✅" if task["done"] else "❌"
                    print(f"{i+1}. {task['title']} {status}")
    
        elif choice==3:
            if len(tasks)==0:
                print("The to do list is empty")
                continue
            for i,task in enumerate(tasks):
                status="✅" if task["done"] else "❌"
                print(i+1,".", task["title"], status,sep="")

            while True:
                try:
                    delete=int(input("Enter the task to be deleted: "))
                except ValueError:
                    print("Invalid Input!\n Enter a valid Input")
                else:
                    if 1<=delete<=len(tasks):
                        tasks.pop(delete-1)
                        save_tasks()
                        print(f"successfully deleted")
                        break
                    else:
                        print('Invalid task number! Try again.')

        elif choice == 4:
            if len(tasks) == 0:
                print("The to do list is empty")
                continue

            for i, task in enumerate(tasks):
                status = "✅" if task["done"] else "❌"
                print(f"{i+1}. {task['title']} {status}")

            while True:
                try:
                    mark = int(input("Enter task number to mark as done: "))
                except ValueError:
                    print("Invalid Input!")
                else:
                    if 1 <= mark <= len(tasks):
                        tasks[mark-1]["done"] = not tasks[mark-1]["done"]
                        save_tasks()
                        print("Task status updated!")
                        break
                    else:
                        print("Invalid task number!")

        elif choice==5:
            if len(tasks)==0:
                print("The to do list is empty")
                continue

            completed_tasks=any(task["done"] for task in tasks)

            if not completed_tasks:
                print("No completed tasks to delete")
                continue

            tasks=[task for task in tasks if not task["done"]]
            save_tasks()

            print("All completed tasks are deleted")
   
        elif choice==6:
            print("Thank you!!")
            break

        else:
            print("Invalid Choice!")


