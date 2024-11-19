CONVERSION_FaCTOR = 0.6214
START_SPEED = 60
END_SPEED = 131
INCREMENT = 10

for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FaCTOR
    print(kph, "\t", format(mph, ".1f"))