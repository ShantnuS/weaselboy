import random

target = "methinks it is like a weasel" #This is what the individuals aspire to be

def list_to_string(list_to_convert):
    return ''.join(list_to_convert)

def string_to_list(string_to_convert):
    return list(string_to_convert)

def create_individual(size):
    individual = [] 
    for _ in range(size):
        ascii_index = random.randint(32,127)
        individual.append(str(chr(ascii_index)))
    print("Created the individual: " + list_to_string(individual))    
    return individual

def main():
    size = len(target) #This is how long the individuals will be 

    #Create some individuals
    individual1 = create_individual(size)
    individual2 = create_individual(size)

if __name__ == "__main__": main()
