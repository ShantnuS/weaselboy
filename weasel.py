import random
import time

target = "methinks it is like a weasel" #This is what the individuals aspire to be

def list_to_string(list_to_convert):
    return ''.join(list_to_convert)

def string_to_list(string_to_convert):
    return list(string_to_convert)

def create_individual(size):
    individual = [] 
    for _ in range(size):
        ascii_index = random.randint(32,126)
        individual.append(str(chr(ascii_index))) 
    return individual

def calculate_fitness(individual):
    fitness = 0
    for index, item in enumerate(individual):
        if item == target[index]:
            fitness += 1
    return fitness

def mutate_individual(individual, size):
    child = []
    for index, item in enumerate(individual):
        random_value = random.uniform(0,1)
        if random_value < 1/size:
            mutation = str(chr(random.randint(32,126)))
            child.append(mutation)
        else:
            child.append(item)
    return child

def run_mutation_hill_clumber(size):
    individual_A = create_individual(size)
    fitness_A = calculate_fitness(individual_A)

    while(fitness_A != size):
        individual_B = mutate_individual(individual_A, size)
        # print(list_to_string(individual_B))
        fitness_A = calculate_fitness(individual_A)
        fitness_B = calculate_fitness(individual_B)
        if fitness_B > fitness_A: 
            individual_A = individual_B
            fitness_A = fitness_B

        print(list_to_string(individual_A) + " = " +str(fitness_A))

def main():
    size = len(target) #This is how long the individuals will be 

    start = int(round(time.time() * 1000))

    run_mutation_hill_clumber(size)
    
    end = int(round(time.time() * 1000))
    time_taken = end - start
    print("The run took %dms" % time_taken)

    # #Create some individuals
    # individual1 = create_individual(size)
    # individual2 = create_individual(size)

    # print(calculate_fitness(individual1))

    # print("Mutating 100 times")
    # for _ in range(100):
    #     individual1 = mutate_individual(individual1, size)
    #     print(list_to_string(individual1) + " " + str(calculate_fitness(individual1)))
    

if __name__ == "__main__": main()
