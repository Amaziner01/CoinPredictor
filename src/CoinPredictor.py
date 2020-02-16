import json
import random
from time import sleep

url = "data/data.json"


def loop(run_state):
    error = 1
    simulations = 1

    while run:

        error_margin = str((error/simulations) * 100) + "%"
        prediction = get_prediction()
        print("Prediction: %s" % prediction)
        print("Error Margin: %s" % error_margin)
        print("Flip the coin and insert your result:\nh = head\nt = tail")
        answer = input()
        comparator = ""

        if answer is "h" or answer is "t":
            if answer == "t":
                write_data(False)
                comparator = "tail"

            elif answer == "h":
                write_data(True)
                comparator = "head"

            simulations += 1

            if comparator != prediction:
                error += 1

        else:
            print("Invalid answer\n")


def get_prediction():
    file = read_file()
    data = file["coin-result"]
    true = 0

    for i in data:
        if i is True:
            true += 1

    head = true/len(data)
    tail = 1-head

    if head + tail == 1:
        rand = random.uniform(0.0, 1.0)

        if head == 1:
            return "head"

        elif tail == 1:
            return "tail"

        elif head > tail:
            if rand > head:
                return "head"
            else:
                return "tail"

        elif head < tail:
            if rand > tail:
                return "tail"
            else:
                return "head"

        elif head == tail:
            rand = random.randint(0, 1)
            if rand == 0:
                return "tail"
            else:
                return "head"


def read_file():
    file = open(url, "r")
    data = json.loads(file.read())
    file.close()
    return data


def write_data(value):
    data = read_file()
    file = open(url, "w")
    data["coin-result"].append(value)
    json.dump(data, file)
    file.close()


def get_answer(answer):
    if answer == "c":
        return "head"
    elif answer == "t":
        return "tail"
    else:
        print("Invalid answer")


# OnRun
run = True
print("Welcome to CoinPredictor\n")
loop(run)


'''

file = open("data/data.json", "w")
data['coin-result'].append(False)
data = json.dump(data, file)
print(data)
file.close()'''
