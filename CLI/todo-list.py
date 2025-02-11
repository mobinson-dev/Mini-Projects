import time
import os
import sys
import platform

Filename = "tasks.txt"

def save_tasks():
    with open(Filename,"w") as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks():
    try:
        with open(Filename,"r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_tasks():
    print("Tasks : ")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task}")
        time.sleep(0.05)
    print()

def open_new_terminal():
    system = platform.system()

    if os.getenv("RUNNING_IN_TERMINAL") is None:
        os.environ["RUNNING_IN_TERMINAL"] = "1"

        if system == "Windows":
            os.system(f'start cmd /k python "{sys.argv[0]}"')
        elif system == "Linux":
            terminal = os.environ.get("TERMINAL", "gnome-terminal") # sudo apt update && sudo apt install gnome-terminal -y
            os.system(f'{terminal} -- python3 "{sys.argv[0]}"')  
        elif system == "Darwin":  # macOS
            os.system(f'osascript -e \'tell application "Terminal" to do script "python3 {sys.argv[0]}"\'')
        
        sys.exit()

open_new_terminal()

tasks = load_tasks()

while True:
    print("\nTo do list :")
    time.sleep(0.5)
    print("1. Enter a task")
    time.sleep(0.2)
    print("2. View all tasks")
    time.sleep(0.2)
    print("3. Update a task")
    time.sleep(0.2)
    print("4. Delete a task")
    time.sleep(0.2)
    print("5. Exit\n")
    time.sleep(0.2)

    try:
        menu_option = int(input("Enter your option : "))
    except ValueError:
        clear_screen()
        print("\nInvalid option! Enter a number between 1-5.")
        time.sleep(1.5)
        continue

    print()

    if menu_option == 1:
        clear_screen()
        print_tasks()
        while True:
            if not tasks:
                print("\n[Empty]\n")
            print("[type 'exit' to return to main menu]")
            task = input("Enter your task : ")
            if task.lower() == 'exit':
                print("\nReturning to menu...")
                time.sleep(0.5)
                clear_screen()
                break
            if task:
                tasks.append(task)
                save_tasks()
                print("\nTask added.")
                time.sleep(1)
                clear_screen()
                print_tasks()
            else:
                print("\nTask cannot be empty!")
                time.sleep(1)
                print("\nReturning to menu...")
                time.sleep(1)
                clear_screen()
                continue

    elif menu_option == 2:
        clear_screen()
        if not tasks:
            print("\nThere are no tasks.")
            time.sleep(2)
            print("\nReturning to menu...")
            time.sleep(1)
            clear_screen()
        else:
            print_tasks()

    elif menu_option == 3:
        clear_screen()
        if not tasks:
            print("\nThere are no tasks.")
            time.sleep(1)
            print("\nReturning to menu...")
            time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print_tasks()
            return_to_menu = False
            while not return_to_menu:
                print("[type 'exit' to return to main menu]")
                modify = input("Please enter the task number to modify : ")
                if modify == 'exit':
                    print("\nReturning to menu...")
                    time.sleep(0.5)
                    clear_screen()
                    break
                try :
                    modify = int(modify)
                    if 1 <= modify <= len(tasks):
                        modify_task = input("\nEnter the modified task : ")
                        if modify_task:
                            tasks[modify -1] = modify_task
                            save_tasks()
                            print("\nTask updated.")
                            time.sleep(1)
                            clear_screen()
                            print_tasks()
                        else:
                            print("\nTask cannot be empty!")
                            time.sleep(1)
                            print("\nReturning to menu...")
                            time.sleep(1)
                            clear_screen()
                            return_to_menu = True
                            break
                    else:
                        print("\nInvalid task number. Try again.")
                        time.sleep(0.5)
                except ValueError:
                    clear_screen()
                    print("Enter a valid task number!\n")
                    time.sleep(0.5)
                    print_tasks()
                    continue


    elif menu_option == 4:
        while True:
            clear_screen()
            if not tasks:
                print("\nNo tasks to delete.")
                time.sleep(1)
                print("\nReturning to menu...")
                time.sleep(1)
                clear_screen()
                break
            else:
                print_tasks()
                print("[type 'exit' to return to main menu]")
                delete = input("Enter the task number you want to delete : ")
                if delete == 'exit':
                    print("\nReturning to menu...")
                    time.sleep(0.5)
                    clear_screen()
                    break
                try:
                    delete = int(delete)
                    if 1 <= delete <= len(tasks):
                        del tasks[delete -1]
                        save_tasks()
                        print("\nTask deleted.")
                        time.sleep(1)
                        if not tasks:
                            clear_screen()
                            print("\nNo more tasks available")
                            time.sleep(1)
                            print("\nReturning to menu...")
                            time.sleep(1)
                            clear_screen()
                            break
                    else:
                        print("\nInvalid task number. Try again")
                        time.sleep(0.5)
                except ValueError:
                    clear_screen()
                    print("Enter a valid task number!\n")
                    time.sleep(0.5)
                    print_tasks()
                    continue
    
    elif menu_option == 5:
        print("Exiting...\n")
        time.sleep(1.5)
        system = platform.system()
        if system == "Windows":
            os.system(f"taskkill /F /PID {os.getppid()} ")
        elif system == "Linux" or system == "Darwin":
            os.system("kill $PPID")
        sys.exit()

    elif 6 <= menu_option or menu_option <= 0:
        clear_screen()
        print("\nInvalid option! Enter a number between 1-5.")
        time.sleep(1.5)