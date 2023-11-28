# print("Helo again\nHey")
# print("Hi," + input("Your nice name"))

# name = input("What's your name?")
# print(len(name))

print("Hello. This is a sale card")
item_name = input("Item name, please:\n")
item_price = input(item_name + "'s" + " price, please:\n")
i_price = float(item_price)
print(item_name + " costs " + item_price + " euros")

second_item_name = input("The second one name, please:\n")
second_item_price = input(second_item_name + "'s" + " price, please:\n")
s_i_price = float(second_item_price)
print(second_item_name + " costs " + second_item_price + " euros")

summary = i_price + s_i_price
# print("Your recipe for a " + item_name + " and a " + second_item_name + " is: " + str(summary) + " euros")
print(f"Your recipe for a {item_name} and a {second_item_name} is: {summary} euros")
print("Thank you")



