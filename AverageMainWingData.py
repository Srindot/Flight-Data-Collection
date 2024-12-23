import pandas as pd
import os

def compute_averages(input_dir, output_filename):
    # Initialize a list to store the data
    data = []

    # Read all CSV files in the specified directory
    for i in range(len(os.listdir(input_dir))):
        file_name = os.path.join(input_dir, f'flapping{i}.csv')
        if os.path.exists(file_name):
            # Read the CSV file
            df = pd.read_csv(file_name, header=None)
            # Extract relevant data
            flapping_frequency = df.iloc[0, 0]
            airspeed = df.iloc[0, 1]
            angle_of_attack = df.iloc[0, 2]
            # Compute averages for Lift, Induced Drag, and Pitching Moment
            avg_lift = df.iloc[:, 4].mean()
            avg_induced_drag = df.iloc[:, 5].mean()
            avg_pitching_moment = df.iloc[:, 6].mean()
            # Append the results to the data list
            data.append({
                'Flapping Frequency': flapping_frequency,
                'Airspeed': airspeed,
                'Angle Of Attack': angle_of_attack,
                'Average Lift': avg_lift,
                'Average Induced Drag': avg_induced_drag,
                'Average Pitching Moment': avg_pitching_moment
            })

    # Create a DataFrame from the collected data
    result_df = pd.DataFrame(data)

    # Save the result to the specified output file
    result_df.to_csv(output_filename, index=False)

# Example usage:
compute_averages('Data', 'AverageMainWing.csv')
