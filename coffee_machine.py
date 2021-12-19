
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
# msg_[1] = ""

one = {'water':200, "milk":50, "beans":15}
# for m in range(7):
#     print(msg_[m])
print(msg_[7])
cups = int(input())
print(msg_[8].format(cups))
print(one['water'] * cups, msg_[9])
print(one['milk'] * cups, msg_[10])
print(one['beans'] * cups, msg_[11])

