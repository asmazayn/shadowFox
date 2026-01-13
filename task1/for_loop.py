#----one-----#
import random

rolls = []
six_count = 0
one_count = 0
two_sixes_in_row = 0

previous_roll = None

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1
    if roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1

    previous_roll = roll

print("Dice rolls:", rolls)
print("Number of times rolled 6:", six_count)
print("Number of times rolled 1:", one_count)
print("Number of times two 6s occurred in a row:", two_sixes_in_row)
#---two-----#
# Program 2: Jumping jacks workout

total_jumps = 0

for i in range(10):
    total_jumps += 10
    print("You did 10 jumping jacks")
    print("Total completed:", total_jumps)

    if total_jumps == 100:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print("You completed a total of", total_jumps, "jumping jacks")
            break
    else:
        print(100 - total_jumps, "jumping jacks remaining")
