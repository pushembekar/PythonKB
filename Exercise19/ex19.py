def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for the party!")

print("We can give the function numbers directly")
cheese_and_crackers(20, 30)

print("OR, we can use variables in our script")
amount_of_cheese = 15
amount_of_crackers = 33

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside too")
cheese_and_crackers(10+20, 40+80)

print("And we can combine all")
cheese_and_crackers(amount_of_cheese * 2, amount_of_crackers * 3)
