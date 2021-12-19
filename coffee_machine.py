
msg_ = [""] * 20
msg_[0] = "Starting to make a coffee"
msg_[1] = 'Grinding coffee beans'
msg_[2] = 'Boiling water'
msg_[3] = 'Mixing boiled water with crushed coffee beans'
msg_[4] = 'Pouring coffee into the cup'
msg_[5] = 'Pouring some milk into the cup'
msg_[6] = "Coffee is ready!"
msg_[7] = 'Write how many cups of coffee you will need:'
msg_[8] = "For {} cups of coffee you will need:"
msg_[9] = "ml of water"
msg_[10] = "ml of milk"
msg_[11] = "g of coffee beans"
msg_[12] = "Write how many ml of water the coffee machine has:"
msg_[13] = "Write how many ml of milk the coffee machine has:"
msg_[14] = "Write how many grams of coffee beans the coffee machine has:"
msg_[15] = "Yes, I can make that amount of coffee"
msg_[16] = "(and even {} more than that)"
msg_[17] = "No, I can make only {} cups of coffee"
# msg_[1] = ""
temp = '''
'''

one = {'water':200, "milk":50, "beans":15}
has = {'water':0, "milk":0, "beans":0}
can = {'water':0, "milk":0, "beans":0}

print(msg_[12])
has['water'] = int(input())
print(msg_[13])
has['milk'] = int(input())
print(msg_[14])
has['beans'] = int(input())

for i in has:
    can[i] = int(has[i] / one[i])
cup_max = min(can.values())
# print(cup_max)

print(msg_[7])
cups = int(input())
if cups > cup_max:
    print(msg_[17].format(cup_max))
elif cups == cup_max:
    print(msg_[15].format(cups))
else:
    print(msg_[15], msg_[16].format(cup_max - cups))

# print(msg_[8].format(cups))
# print(one['water'] * cups, msg_[9])
# print(one['milk'] * cups, msg_[10])
# print(one['beans'] * cups, msg_[11])

