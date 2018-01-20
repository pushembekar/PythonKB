# This one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 = {arg1}, arg2 = {arg2}")

# Ok, this *args is pointless... we can just do This
def print_two_again(arg1, arg2):
    print(f"arg1 = {arg1}, arg2 = {arg2}")

# This just takes 1 argument
def print_one(arg1):
    print(f"arg1 = {arg1}")

# This one takes no argument
def print_non():
    print("I got nothing")


print_two("Pushkar", "Shembekar")
print_two_again("Maithili", 'Saoji')
print_one("Arya")
print_non()
