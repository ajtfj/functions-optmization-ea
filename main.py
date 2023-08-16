from Optimization import *
from AckleyOptimization import *
import numpy as np

def find_solution():
    population_size = 1000
    n = 30
    max_generation = 200000
    μ = 30
    λ = 200
    optimal_solution = 0
    c = 0.8

    best_fitness_by_generation = []

    ackley_evolutionary_strategy = AckleyOptimization(population_size, n, c)
    ackley_evolutionary_strategy.generate_population()

    best_chromosome, best_solution = ackley_evolutionary_strategy.best_solution()
    best_fitness_by_generation.append(best_solution)
    generation = 0
    children = []

    print(f"The chromosome in generation {generation} is with fitness {best_solution}")
    print(f"Chromosome: {best_chromosome}")
    print()

    while best_solution != optimal_solution and generation < max_generation:
        parents = ackley_evolutionary_strategy.select_parents()
        child = ackley_evolutionary_strategy.crossover(parents)
        child = ackley_evolutionary_strategy.mutate(child)
        children.append(child)
        ackley_evolutionary_strategy.update_success_rate(parents, child)

        if len(children) == λ:
            ackley_evolutionary_strategy.survival_selection_elitist(children, μ)
            children = []

        generation += 1
        last_best_solution = best_solution
        best_chromosome, best_solution = ackley_evolutionary_strategy.best_solution()
        best_fitness_by_generation.append(best_solution)

        if best_solution < last_best_solution:
            print(f"A new promising chromosome was found in generation {generation} with fitness {best_solution}")
            print(f"Chromosome: {best_chromosome}")
            print()

    print(f"Search completed in {generation} generations")
    print(f"The best chromosome found has fitness of {best_solution}")
    print(f"Chromosome: {best_chromosome}")

find_solution()