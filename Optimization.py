import math
import random

class Optimization:
    population = []

    def __init__(self, population_size: int, dimension: int):
        self.population_size = population_size
        self.dimension = dimension
        self.learning_rate = 1/math.sqrt(self.dimension)
        self.min_mutation_step = 1
        
    def generate_population(self, min_gene: float, max_gene: float):
        self.population = []
        for _ in range(self.population_size):
            chromosome = []
            for _ in range(self.dimension):
                gene = random.uniform(min_gene, max_gene)
                chromosome.append(gene)
            mutation_step = self.min_mutation_step
            chromosome.append(mutation_step)
            self.population.append(chromosome)

    def fitness(self):
        raise Exception("Not implemented")

    def select_parents(self):
        parents = (
            self.population[int(random.uniform(0, self.population_size))],
            self.population[int(random.uniform(0, self.population_size))]
        )

        return parents
    
    def crossover(self, parents: tuple[list[float], list[float]]):
        child = []
        for i in range(self.dimension+1):
            gene = random.choice([parents[0][i], parents[1][i]])
            child.append(gene)
        
        return child
    
    def mutate(self, chromosome: list[float]):
        mutation_step = chromosome[-1]
        params = chromosome[:-1]

        mutated_mutation_step = mutation_step * math.exp(random.gauss(0, self.learning_rate))

        if mutated_mutation_step < self.min_mutation_step:
            mutated_mutation_step = self.min_mutation_step
        
        mutated_params = [x+random.gauss(0, mutated_mutation_step) for x in params]
        mutated_chromosome = mutated_params+[mutated_mutation_step]

        return mutated_chromosome

    def survival_selection(self, children: 'list[list[float]]', μ: int) -> None:
        children.sort(key=self.fitness)
        self.population.sort(key=self.fitness)
        self.population[-μ:] = children[:μ]

    def survival_selection_elitist(self, children: 'list[list[float]]', μ: int) -> None:
        children.sort(key=self.fitness)
        self.population.extend(children[:μ])
        self.population.sort(key=self.fitness)
        self.population = self.population[:len(self.population)-μ]

    def best_solution(self):
        self.population.sort(key=self.fitness)
        best_solution = self.fitness(self.population[0])

        return self.population[0], best_solution