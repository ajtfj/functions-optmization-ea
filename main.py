from evolute import evolute
from AckleyOptimization import AckleyOptimization
from RastriginOptimization import RastriginOptimization
from RosenbrockOptimization import RosenbrockOptimization
from SchwefelOptimization import SchwefelOptimization

def main():
    print("Optimizing the Ackley function")
    ackleyOptimization = AckleyOptimization(
        population_size=1000, 
        dimension=30, 
        c=0.8
    )
    evolute(ackleyOptimization)

    print("Optimizing the Rastrigin function")
    rastriginOptimization = RastriginOptimization(
        population_size=1000, 
        dimension=30, 
        c=0.8
    )
    evolute(rastriginOptimization)

    print("Optimizing the Rosenbrock function")
    rosenbrockOptimization = RosenbrockOptimization(
        population_size=1000, 
        dimension=30, 
        c=0.8
    )
    evolute(rosenbrockOptimization)

    print("Optimizing the Schwefel function")
    schwefelOptimization = SchwefelOptimization(
        population_size=1000, 
        dimension=30, 
        c=0.8
    )
    evolute(schwefelOptimization)

if __name__ == "__main__":
    main()