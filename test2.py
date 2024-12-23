import numpy as np
import matplotlib.pyplot as plt

def generate_test_data(flapping_period, num_cycles=3):
    points_per_second = 120  # Updated based on the new information
    points_per_cycle = int(points_per_second * flapping_period)
    total_points = points_per_cycle * num_cycles
    
    # Generate sample data for each array
    time = np.linspace(0, num_cycles * flapping_period, total_points)
    angle_of_flapping = np.sin(2 * np.pi * (1/flapping_period) * time)
    lift = np.cos(2 * np.pi * (1/flapping_period) * time) + np.random.normal(0, 0.1, total_points)
    pitching_moment = np.sin(4 * np.pi * (1/flapping_period) * time) + np.random.normal(0, 0.05, total_points)
    induced_drag = np.abs(np.sin(2 * np.pi * (1/flapping_period) * time)) + np.random.normal(0, 0.02, total_points)
    
    return np.array([angle_of_flapping]), np.array([lift]), np.array([pitching_moment]), np.array([induced_drag])

def extract_second_cycle(data, flapping_period):
    points_per_second = 120  # Updated based on the new information
    points_per_cycle = int(points_per_second * flapping_period)
    
    start_index = points_per_cycle
    end_index = 2 * points_per_cycle
    
    return data[0, start_index:end_index]

# Test the functions
flapping_period = 0.2  # 0.2 seconds per cycle

# Generate test data
angle_of_flapping, lift, pitching_moment, induced_drag = generate_test_data(flapping_period)

print(f"Original data shape: {angle_of_flapping.shape}")

# Extract second cycle for each array
angle_of_flapping_2nd = extract_second_cycle(angle_of_flapping, flapping_period)
lift_2nd = extract_second_cycle(lift, flapping_period)
pitching_moment_2nd = extract_second_cycle(pitching_moment, flapping_period)
induced_drag_2nd = extract_second_cycle(induced_drag, flapping_period)

print(f"Truncated data shape: {angle_of_flapping_2nd.shape}")

# Plot the results
plt.figure(figsize=(12, 8))
plt.plot(angle_of_flapping[0], label='Full Data')
plt.plot(range(len(angle_of_flapping[0])//3, 2*len(angle_of_flapping[0])//3), 
         angle_of_flapping_2nd, label='Second Cycle', linewidth=2)
plt.title('Angle of Flapping: Full Data vs Second Cycle')
plt.legend()
plt.show()