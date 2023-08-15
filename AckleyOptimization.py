from Optimization import *
from ACKLEY_FUNCTION import *

class AckleyOptimization(Optimization):
    gene_lower_bound = -32.768
    gene_upper_bound = 32.768

    def generate_population(self):
        Optimization.generate_population(self, self.gene_lower_bound, self.gene_upper_bound)

    def fitness(self, chromosome: list[float]):
        result = ackley(chromosome)
        return result
