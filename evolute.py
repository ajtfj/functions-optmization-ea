from Optimization import Optimization

def evolute(instance: Optimization, max_generation=100000, μ=30, λ=200, optimal_solution=0):
    instance.generate_population()

    _, best_solution = instance.best_solution()
    offspring = []
    generation = 0
    while best_solution != optimal_solution and generation < max_generation:
        parents = instance.select_parents()
        generated_offspring = instance.crossover(parents)
        generated_offspring = instance.mutate(generated_offspring)
        offspring.append(generated_offspring)
        instance.update_success_rate(parents, generated_offspring)

        if len(offspring) == λ:
            instance.survival_selection_elitist(offspring, μ)
            offspring = []

        generation += 1

    print(f"Search completed in {generation} generations")

    best_chromosome, best_solution = instance.best_solution()
    mean, std = instance.fitness_statistics()
    print(f"The best chromosome found has fitness of {best_solution}")
    print(f"Chromosome: {best_chromosome}")
    print(f"The population mean fitness is {mean} with standard deviation of {std}")
