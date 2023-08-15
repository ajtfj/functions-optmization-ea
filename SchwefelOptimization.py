from Optimization import *
from SCHWEFEL_FUNCTION import *

class SchwefelOptimization(Optimization):
    gene_lower_bound = -500
    gene_upper_bound = 500

    def generate_population(self):
        Optimization.generate_population(self, -500, 500)

    def fitness(self, chromosome: list[float]):
        result = schwefel(chromosome)
        return result
