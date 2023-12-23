#exercise 12.
# not aproved

print("Time Converter")
x = int(input('Enter seconds: '))
days = x//86400
hours = (x//3600) - (days*24)
minutes = (x//60) - (x//3600 * 60)
seconds = x % 60
print(f"Converted time in D:HH:MM:SS format")
print(f"{days}:{hours}:{minutes}:{seconds}")