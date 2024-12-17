code:-
import numpy as np
import math
import random

def objective_function(x):
    """Objective function to minimize: f(x) = x^2"""
    return x ** 2

def simulated_annealing(initial_state, initial_temp, cooling_rate, max_iterations):
    """Simulated Annealing algorithm to find the minimum of the objective function."""
    
    current_state = initial_state
    current_energy = objective_function(current_state)
    best_state = current_state
    best_energy = current_energy
    
    temp = initial_temp
    
    for iteration in range(max_iterations):
        # Generate a new candidate state by perturbing the current state
        candidate_state = current_state + random.uniform(-1, 1)
        candidate_energy = objective_function(candidate_state)
        
        # Calculate energy difference
        energy_diff = candidate_energy - current_energy
        
        # If the candidate state is better, or accepted with a certain probability
        if energy_diff < 0 or random.uniform(0, 1) < math.exp(-energy_diff / temp):
            current_state = candidate_state
            current_energy = candidate_energy
            
            # Update best state found
            if current_energy < best_energy:
                best_state = current_state
                best_energy = current_energy
        
        # Cool down the temperature
        temp *= cooling_rate
        
        # Print the current state and temperature for debugging
        print(f"Iteration {iteration + 1}: Current State = {current_state:.4f}, Current Energy = {current_energy:.4f}, Temperature = {temp:.4f}")

    return best_state, best_energy

# Get user input for parameters
try:
    initial_state = float(input("Enter the initial state (starting point): "))
    initial_temp = float(input("Enter the initial temperature: "))
    cooling_rate = float(input("Enter the cooling rate (between 0 and 1): "))
    max_iterations = int(input("Enter the number of iterations: "))
    
    # Validate cooling rate
    if cooling_rate <= 0 or cooling_rate >= 1:
        raise ValueError("Cooling rate must be between 0 and 1.")
    
    # Execute the simulated annealing algorithm
    best_state, best_energy = simulated_annealing(initial_state, initial_temp, cooling_rate, max_iterations)

    # Output the best state and energy found
    print(f"Best State: {best_state:.4f}, Best Energy: {best_energy:.4f}")

except ValueError as e:
    print(f"Invalid input: {e}")
