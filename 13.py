#exercise 13
day = int(input('Enter a day: '))
day %= 7
Week = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
        }
print(Week[day])
