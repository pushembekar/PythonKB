from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I am {script} script")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live?")
city = input(prompt)

print(f"What kind of computer do you own?")
computer = input(prompt)

print(f"""
Alright, so you said "{likes}" about liking me.
You live in {city}. Not sure where that is.
You own a {computer} computer. Nice!
""")
