from Optimization import *
from ROSENBROCK_FUNCTION import *

class RosenbrockOptimization(Optimization):
    gene_lower_bound = -5
    gene_upper_bound = 10
    
    def generate_population(self):
        Optimization.generate_population(self, self.gene_lower_bound, self.gene_upper_bound)

    def fitness(self, chromosome: list[float]):
        result = rosenbrock(chromosome)
        return result
