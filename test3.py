import numpy as np
import csv

def save_flight_data_to_csv(AngleOfAttack, FlappingFrequency, Airspeed, AngleOfFlapping, Lift, PitchingMoment, InducedDrag, file_name):
    # Ensure the input arrays are numpy arrays
    AngleOfFlapping = np.array(AngleOfFlapping)
    Lift = np.array(Lift)
    PitchingMoment = np.array(PitchingMoment)
    InducedDrag = np.array(InducedDrag)
    
    # Calculate the number of data points based on the Flapping Frequency
    num_data_points = 120 * FlappingFrequency

    # Ensure type 2 inputs have the expected dimensions (N = 120 * FlappingPeriod)
    if not (len(AngleOfFlapping) == num_data_points and
            len(Lift) == num_data_points and
            len(PitchingMoment) == num_data_points and
            len(InducedDrag) == num_data_points):
        raise ValueError(f"Type 2 inputs must have {num_data_points} data points.")

    # Create a list of dictionaries for CSV
    data = []
    for i in range(num_data_points):
        row = {
            "AngleOfAttack": AngleOfAttack,
            "FlappingFrequency": FlappingFrequency,
            "Airspeed": Airspeed,
            "AngleOfFlapping": AngleOfFlapping[i],
            "Lift": Lift[i],
            "PitchingMoment": PitchingMoment[i],
            "InducedDrag": InducedDrag[i]
        }
        data.append(row)

    # Save the data into a CSV file
    fieldnames = ["AngleOfAttack", "FlappingFrequency", "Airspeed", "AngleOfFlapping", "Lift", "PitchingMoment", "InducedDrag"]
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {file_name}")

# Example usage:

