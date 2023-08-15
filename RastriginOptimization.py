from Optimization import *
from RASTRIGIN_FUNCTION import *

class RastriginOptimization(Optimization):
    gene_lower_bound = -5.12
    gene_upper_bound = 5.12

    def generate_population(self):
        Optimization.generate_population(self, self.gene_lower_bound, self.gene_upper_bound)

    def fitness(self, chromosome: list[float]):
        result = rastrigin(chromosome)
        return result
