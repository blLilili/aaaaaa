import random

def item10():
    number = []
    for i in range(10):
        number.append(random.randint(1, 100))
    return number

def decide(listyy :list, value :int):
    return value in listyy


def main():
    
    current_list = list()
    message = "done." if decide(current_list, 24) else "Nince."