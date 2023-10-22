from main import simulated_annealing, G, E, W, Dv, A, initial_temp, cooling_rate

# Define a vehicle class with a current_position attribute
class Vehicle:
    def __init__(self, current_position):
        self.current_position = current_position



# Test the simulated_annealing function
def test_simulated_annealing():
    vehicle = Vehicle(W)
    best_solution = simulated_annealing(G, E, vehicle, Dv, A, initial_temp, cooling_rate)
    print("Best solution:", best_solution)

if __name__ == "__main__":
    test_simulated_annealing()
