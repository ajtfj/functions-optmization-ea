import math
import random
import numpy as np

class Optimization:
    population = []

    def __init__(self, population_size: int, dimension: int, c: float):
        self.population_size = population_size
        self.dimension = dimension
        self.global_learning_rate = 1/math.sqrt(2*self.dimension)
        self.fine_tuning_learning_rate = 1/math.sqrt(2*math.sqrt(self.dimension))
        self.min_mutation_step = 1
        self.c = c
        self.successful_mutations = 0
        self.total_mutations = 0
        
    def generate_population(self, min_gene: float, max_gene: float):
        self.population = []
        for _ in range(self.population_size):
            chromosome = []
            for _ in range(self.dimension):
                gene = random.uniform(min_gene, max_gene)
                chromosome.append(gene)
            for _ in range(self.dimension):
                chromosome.append(self.min_mutation_step)
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
        offspring = []
        for i in range(2*self.dimension):
            gene = random.choice([parents[0][i], parents[1][i]])
            offspring.append(gene)
        
        return offspring
    
    def mutate(self, chromosome: list[float]):
        mutation_steps = chromosome[self.dimension:]
        mutated_mutation_steps = []
        for mutation_step in mutation_steps:
            mutated_mutation_step = mutation_step * math.exp(self.global_learning_rate*random.gauss(0, 1) + self.fine_tuning_learning_rate*random.gauss(0, 1))
            
            if mutated_mutation_step < self.min_mutation_step:
                mutated_mutation_step = self.min_mutation_step
        
            if self.get_mutation_success_rate() > 1/5:
                mutated_mutation_step = mutated_mutation_step / self.c
            if self.get_mutation_success_rate() < 1/5:
                mutated_mutation_step = mutated_mutation_step * self.c

            mutated_mutation_steps.append(mutated_mutation_step)
        
        params = chromosome[:self.dimension]
        mutated_params = [
            min(max(gene+random.gauss(0, mutation_step), self.gene_lower_bound), self.gene_upper_bound) 
            for gene, mutation_step in zip(params, mutated_mutation_steps)
        ]
        
        return mutated_params+mutated_mutation_steps

    def survival_selection(self, offspring: 'list[list[float]]', μ: int) -> None:
        offspring.sort(key=self.fitness)
        self.population.sort(key=self.fitness)
        self.population[-μ:] = offspring[:μ]

    def survival_selection_elitist(self, offspring: 'list[list[float]]', μ: int) -> None:
        offspring.sort(key=self.fitness)
        self.population.extend(offspring[:μ])
        self.population.sort(key=self.fitness)
        self.population = self.population[:len(self.population)-μ]
    
    def update_success_rate(self, parents: list[list[float]], offspring: list[float]):
        offspring_fitness = self.fitness(offspring)
        for parent in parents:
            parent_fitness = self.fitness(parent)
            if offspring_fitness > parent_fitness:
                self.successful_mutations += 1
                break

        self.total_mutations += 1
    
    def get_mutation_success_rate(self):
        if self.total_mutations == 0:
            return 0
        return self.successful_mutations / self.total_mutations
    
    def best_solution(self):
        self.population.sort(key=self.fitness)
        best_solution = self.fitness(self.population[0])

        return self.population[0], best_solution
    
    def fitness_statistics(self):
        fitness_population = []
        for individuo in self.population:
            fitness_population.append(self.fitness(individuo))
        return np.mean(fitness_population), np.std(fitness_population)