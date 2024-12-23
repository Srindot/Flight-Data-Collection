import numpy as np
import csv

def save_flapping_data_to_csv(flapping_period, aoas, airspeeds, angles_of_flapping, lifts, pitching_moments, induced_drags, filename="flapping_data.csv"):
    """
    Save the flapping data into a CSV file with columns for Flapping Period, Angle of Attack, Airspeed, 
    Angle of Flapping, Lift, Pitching Moment, and Induced Drag.

    :param flapping_period: List of flapping frequencies
    :param aoas: List of angles of attack
    :param airspeeds: List of airspeeds
    :param angles_of_flapping: Numpy array of angles of flapping (2D, one per time step and configuration)
    :param lifts: Numpy array of lift values (2D, one per time step and configuration)
    :param pitching_moments: Numpy array of pitching moments (2D, one per time step and configuration)
    :param induced_drags: Numpy array of induced drag values (2D, one per time step and configuration)
    :param filename: The name of the CSV file to save the data in
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["Flapping Period", "Angle of Attack", "Airspeed", "Angle of Flapping", "Lift", "Pitching Moment", "Induced Drag"])

        # Loop through the combinations of inputs and corresponding data arrays
        for i, freq in enumerate(flapping_period):
            for j, aoa in enumerate(aoas):
                for k, Va in enumerate(airspeeds):
                    for t in range(len(angles_of_flapping[i][j][k])):
                        writer.writerow([freq, aoa, Va, angles_of_flapping[i][j][k][t], lifts[i][j][k][t], pitching_moments[i][j][k][t], induced_drags[i][j][k][t]])

    print(f"Data successfully saved to {filename}")

# Example usage
# These are dummy values, replace them with actual data
flapping_period = [1.0, 2.0]
aoas = [5.0, 10.0]
airspeeds = [15.0, 20.0]

# Assume each combination has 100 time steps for simplicity (you can adjust the dimension based on T/ts)
time_steps = 100
angles_of_flapping = np.random.rand(len(flapping_period), len(aoas), len(airspeeds), time_steps)  # Replace with actual angle of flapping data
lifts = np.random.rand(len(flapping_period), len(aoas), len(airspeeds), time_steps)  # Replace with actual lift data
pitching_moments = np.random.rand(len(flapping_period), len(aoas), len(airspeeds), time_steps)  # Replace with actual pitching moment data
induced_drags = np.random.rand(len(flapping_period), len(aoas), len(airspeeds), time_steps)  # Replace with actual induced drag data

# Save the data to CSV
save_flapping_data_to_csv(flapping_period, aoas, airspeeds, angles_of_flapping, lifts, pitching_moments, induced_drags, filename="flapping_data.csv")
