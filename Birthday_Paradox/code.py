import random
import datetime

# List to store birthdays
birthdays = []

# Generate birthdays for 50 candidates
i = 0

while i < 50:

    year = random.randint(1947, 2026)

    # Leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1
    else:
        leap = 0

    month = random.randint(1, 12)

    # Day generation according to month
    if month == 2 and leap == 1:
        day = random.randint(1, 29)

    elif month == 2 and leap == 0:
        day = random.randint(1, 28)

    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)

    else:
        day = random.randint(1, 31)

    # Create date object
    dd = datetime.date(year, month, day)

    # Store full date
    birthdays.append(dd)

    i += 1


# Display all birthdays
print("\nList of Birthdays:\n")

for i in range(len(birthdays)):
    print(f"Candidate {i+1}: {birthdays[i].strftime('%d/%m/%Y')}")


# Check birthday collisions
collision_count = 0
repeated_birthdays = []

checked = []

for i in range(len(birthdays)):

    for j in range(i + 1, len(birthdays)):

        # Compare only day and month
        if (birthdays[i].day == birthdays[j].day and
                birthdays[i].month == birthdays[j].month):

            collision_count += 1

            date_str = birthdays[i].strftime('%d/%m')

            if date_str not in checked:
                repeated_birthdays.append(date_str)
                checked.append(date_str)


# Display collision results
print("\nBirthday Collisions Found:", collision_count)

if collision_count > 0:

    print("\nRepeated Birthdays:")

    for date in repeated_birthdays:
        print(date)

else:
    print("\nNo birthday collisions found.")