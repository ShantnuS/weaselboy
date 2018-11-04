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

def create_population(individual_size,pop_size):
    population = []
    for _ in range(pop_size):
        population.append(create_individual(individual_size))

    return population

def crossover_individuals(size, individual_A, individual_B):
    child = []
    for i in range(size):
        random_value = random.uniform(0,1)
        if random_value < 0.5:
            child.append(individual_A[i])
        else:
            child.append(individual_B[i])
    
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

def run_ga_without_crossover(size, pop_size):
    population = create_population(size, pop_size)
    best_fitness = 0
    while (best_fitness != size): 
        #Find best parent
        individual_A = random.choice(population)
        individual_B = random.choice(population)

        if calculate_fitness(individual_A) > calculate_fitness(individual_B):
            parent = individual_A
        else:
            parent = individual_B
        
        #Create mutant child
        child = mutate_individual(parent, size)
        best_fitness = calculate_fitness(child)

        #Remove some rando
        individual_A = random.choice(population)
        individual_B = random.choice(population)

        if calculate_fitness(individual_A) > calculate_fitness(individual_B):
            population.remove(individual_B)
        else:
            population.remove(individual_A)

        population.append(child)
        print(list_to_string(child) + " = " +str(best_fitness))
            
def run_ga_with_crossover(size, pop_size):
    population = create_population(size, pop_size)
    best_fitness = 0
    while (best_fitness != size): 
        #Find parent 1
        individual_A = random.choice(population)
        individual_B = random.choice(population)

        if calculate_fitness(individual_A) > calculate_fitness(individual_B):
            parent1 = individual_A
        else:
            parent1 = individual_B

        #Find parent 2
        individual_A = random.choice(population)
        individual_B = random.choice(population)

        if calculate_fitness(individual_A) > calculate_fitness(individual_B):
            parent2 = individual_A
        else:
            parent2 = individual_B

        #Crossover and find child
        result_of_crossover = crossover_individuals(size, parent1, parent2)
        child = mutate_individual(result_of_crossover, size)
        best_fitness = calculate_fitness(child)

        #Remove randos 
        individual_A = random.choice(population)
        individual_B = random.choice(population)

        if calculate_fitness(individual_A) > calculate_fitness(individual_B):
            population.remove(individual_B)
        else:
            population.remove(individual_A)

        population.append(child)
        print(list_to_string(child) + " = " +str(best_fitness))


def main():
    size = len(target) #This is how long the individuals will be 
    pop_size = 10

    start = int(round(time.time() * 1000))

    #run_mutation_hill_clumber(size)
    #run_ga_without_crossover(size, pop_size)
    run_ga_with_crossover(size, pop_size)

    '''
    indA = create_individual(size)
    indB = create_individual(size)
    child = crossover_individuals(size, indA, indB)
    print(list_to_string(indA) + " = " +str(calculate_fitness(indA)))
    print(list_to_string(indB) + " = " +str(calculate_fitness(indB)))
    print(list_to_string(child) + " = " +str(calculate_fitness(child)))
    '''


    end = int(round(time.time() * 1000))
    time_taken = end - start
    print("The run took %dms" % time_taken)

    

if __name__ == "__main__": main()
