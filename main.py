import datetime

user_intput = input("Enter your goal and deadline\n")
input_list = user_intput.split(":")

goal = input_list[0]
deadline = input_list[1]

Deadline_time = datetime.datetime.strptime(deadline, "%d.%m.%Y")
Today = datetime.datetime.today()

Time_remaining = Deadline_time-Today

print(f"This is your remaining time: {Time_remaining} and your {goal}")


# print("Your Goal + goal + and your deadline is + deadline")
