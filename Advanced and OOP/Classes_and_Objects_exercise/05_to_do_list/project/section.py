from task import Task


class Section:
    def __init__(self, name: str):
        self.tasks = []
        self.name = name
        self.completed_task = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                self.completed_task.append(task)
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = len(self.completed_task)
        self.completed_task = []
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        output = ""
        output += f"Section {self.name}:\n"
        for i in self.tasks:
            output += f"{i.details()}\n"
        return output

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())


section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
section.complete_task("Make bed")
print(section.clean_section())
print(section.view_section())




