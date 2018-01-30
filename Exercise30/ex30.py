people = 30
cars = 40
trucks = 15

if (cars > people):
    print("We should take the cars")
elif (cars < people):
    print("We should walk")
else:
    print("We cannot decide")

if (trucks > cars):
    print("There are too many trucks")
elif (trucks < cars):
    print("Maybe we should take the trucks")
else:
    print("We still can't decide")

if (people > trucks):
    print("Alright, let's just take the trucks")
else:
    print("Fine! Let's just stay home")
