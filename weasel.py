import random

size = 28
target = "methinks it is like a weasel"

def list_to_string(list_to_convert):
    return ''.join(list_to_convert)

def string_to_list(string_to_convert):
    return list(string_to_convert)

def create_individual(size):
    individual = [] 
    for index in range(size):
        ascii_index = random.randint(32,127)
        individual.append(str(chr(ascii_index)))
    print("Created the individual: " + list_to_string(individual))    
    return individual

def main():
    individual1 = create_individual(size)
    individual2 = create_individual(size)

if __name__ == "__main__": main()
