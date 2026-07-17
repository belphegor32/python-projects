import sys
import csv

tasks = []
current_id = 1

# check

def main():
    while True:
        choice = int(input(
        "1. Добавить задачу\n" \
        "2. Показать задачи\n" \
        "3. Отметить выполненной\n" \
        "4. Удалить задачу\n" \
        "5. Найти задачу\n" \
        "6. Выйти\n"
        ))

        match choice:
            case 1:
                add_task()
            case 2:
                show_tasks()
            case 3:
                title = input("Title of a task: ")
                mark_as_done(title)
            case 4:
                title = input("Title of a task: ")
                delete_task(title)
            case 5: 
                title = input("Title of a task: ")
                find_task(title)
            case 6:
                exit_manager()
                

def add_task():
    global tasks
    global current_id
    title = input("Название: ")
    subject = input("Предмет: ")
    deadline = input("Дедлайн: ")
    tasks.append({
        "id": current_id,
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "completed": False,
    })
    current_id += 1

def show_tasks():
    global tasks 
    for task in tasks:
        print(f"id: {task['id']}")
        print(f"title: {task['title']}")
        print(f"subject: {task['subject']}")
        print(f"deadline: {task['deadline']}")
        print(f"completed: {task['completed']}")
        print()

def mark_as_done(title):
    global tasks
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True


def delete_task(title):
    global tasks
    for task in tasks:
        if task["title"].lower() == title.lower():
            tasks.remove(task)

def find_task(title):
    global tasks 
    for task in tasks:
        if task["title"].lower() == title.lower():
            print(f"id: {task['id']}")
            print(f"title: {task['title']}")
            print(f"subject: {task['subject']}")
            print(f"deadline: {task['deadline']}")
            print(f"completed: {task['completed']}")

def exit_manager():
    sys.exit("Exited successfully")

if __name__ == "__main__":
    main()