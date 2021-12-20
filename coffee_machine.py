msg_ = [""] * 30
msg_[0] = "Starting to make a coffee"
msg_[1] = 'Grinding coffee beans'
msg_[2] = 'Boiling water'
msg_[3] = 'Mixing boiled water with crushed coffee beans'
msg_[4] = 'Pouring coffee into the cup'
msg_[5] = 'Pouring some milk into the cup'
msg_[6] = "Coffee is ready!"
msg_[7] = 'Write how many cups of coffee you will need:'
msg_[8] = "For {} cups of coffee you will need:"
msg_[9] = "water"
msg_[10] = "milk"
msg_[11] = "coffee beans"
msg_[12] = "Write how many ml of water you want to add:"
msg_[13] = "Write how many ml of milk you want to add:"
msg_[14] = "Write how many grams of coffee beans you want to add:"
msg_[15] = "I have enough resources, making you a coffee!"
msg_[16] = "(and even {} more than that)"
msg_[17] = "No, I can make only {} cups of coffee"
msg_[18] = "Write how many disposable coffee cups you want to add:"
msg_[19] = "The coffee machine has:"
msg_[20] = "Write action ({}):"
msg_[21] = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:"
msg_[22] = "disposable cups"
msg_[23] = "money"
msg_[24] = "I gave you ${}"
msg_[25] = "Sorry, not enough {}!"
# msg_[2] = ""
temp = '''
'''

recept = {}
recept["espresso"] = {'water':250, "milk":0, "beans":16, "money":4}
recept["latte"] = {'water':350, "milk":75, "beans":20, "money":7}
recept["cappuccino"] = {'water':200, "milk":100, "beans":12, "money":6}

has = {'water':400, "milk":540, "beans":120, "cups":9, "money":550}
qua = {'water':msg_[12], "milk":msg_[13], "beans":msg_[14],
       "cups":msg_[18]}
nam = {'water':msg_[9], "milk":msg_[10], "beans":msg_[11],
       "cups":msg_[22], "money":msg_[23]}
can = {'water':0, "milk":0, "beans":0, "cups":0}

def cup_can(x):
    for i in recept[x]:
        can[i] = (has[i] - recept[x][i]) > 0
        # can[i] = int(has[i] / recept[x][i])
    # can["cups"] = has["cups"] - 1 if has["cups"] else 0
    # return min(can.values())
    can["cups"] = has["cups"] - 1 > 0
    return all(can.values())

def take():
    print(msg_[24].format(has["money"]))
    has["money"] = 0

def fill():
    for i in qua:
        print(qua[i])
        has[i] += int(input())

def input_action(m, c):
    a = ""
    while a not in c:
        print(m.format(", ".join(c)))
        a = input().lower()
    return a

def buy():
    c = input_action(msg_[21], ['1', '2', '3', "back"])
    if c == "back": return
    c = int(c) - 1
    r = ('espresso', 'latte', 'cappuccino')[c]
    if cup_can(r):
        for i in recept[r]:
            has[i] -= recept[r][i]
        has["money"] += recept[r]["money"] * 2
        has["cups"] -= 1
        print(msg_[15])
    # elif cups == cup_max:
        # print(msg_[15].format(cups))
    else:
        print(msg_[25].format(", ".join([k for k,v in can.items() if not v])))
        # print(msg_[15], msg_[16].format(cup_max - cups))

def print_has():
    print(msg_[19])
    for i in has:
        print(has[i], "of", nam[i])

def stop():
    global go
    go = False

action = {}
action['buy'] = buy
action['fill'] = fill
action['take'] = take
action['remaining'] = print_has
action['exit'] = stop

def main():
    u = input_action(msg_[20], action.keys())
    print()
    action[u]()
    print()
"""    if u == 'buy':
        print()
        buy()
        print()
    elif u == 'fill':
        print()
        fill()
        print()
    elif u == 'take':
        print()
        take()
        print()
    elif u == 'remaining':
        print()
        print_has()
        print()
    elif u == 'exit':
        # global go
        go = False
"""

go = True
while go:
    main()

# print(msg_[8].format(cups))
# print(one['water'] * cups, msg_[9])
# print(one['milk'] * cups, msg_[10])
# print(one['beans'] * cups, msg_[11])
