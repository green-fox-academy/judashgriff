# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

for i in range(len(boys)):
    if i < len(girls):
        order.append(girls[i])
    order.append(boys[i])


print(order)