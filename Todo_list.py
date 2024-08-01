import datetime

class Task:
    def __init__(self, description, due_date=None, priority=1):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = '✓' if self.completed else '✗'
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"[{status}] {self.description} (Due: {due_date_str}, Priority: {self.priority})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority=1):
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5.")
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def mark_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].completed = True
            print(f"Task {task_number + 1} marked as completed.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: (x.completed, x.priority, x.due_date or datetime.datetime.max))
            for i, task in enumerate(sorted_tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Deleted task: {removed_task.description}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. View tasks")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            due_date_str = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
            priority = int(input("Enter the priority (1-5): "))
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            try:
                todo_list.add_task(description, due_date, priority)
            except ValueError as e:
                print(e)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_completed(task_number)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
