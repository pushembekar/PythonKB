from sys import argv

script, filename = argv

print(f"We are going to erase file: {filename}")
print("If you don't want that hit ctrl+C (^C)")
print("If you do want that hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. GoodBye!")
target.truncate()

print("Now I am going to ask you three lines")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these lines to the file {filename}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And we finally close it")
target.close()
