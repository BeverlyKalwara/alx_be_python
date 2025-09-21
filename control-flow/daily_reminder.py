task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = print(f"Reminder: '{task}' is a HIGH priority task")
    case "medium":
        reminder = print(f"Reminder:'{task}' is a MEDIUM priority task")
    case "low":
        reminder = print(f"Note: '{task}' is a LOW priority task")
    case _:
        reminder = print(f"'{task}' is an UNKNOWN priority task.")

# Check if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print final customized reminder
print(reminder)