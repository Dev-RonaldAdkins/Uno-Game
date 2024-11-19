total_seconds = float(input("Enter a number of seconds: "))

hours = total_seconds // 3600

minutes = (total_seconds // 60) % 60

seconds = total_seconds % 60

print("The time in hours, minutes, and seconds is:", hours, "hours", minutes, "minutes", seconds, "seconds")