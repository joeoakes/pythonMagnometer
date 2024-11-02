import numpy as np


def process_magnetometer_data(data_stream):
    """
    Process a magnetometer data stream and compute magnitudes.

    Parameters:
    - data_stream: a list of tuples/lists, where each tuple contains (x, y, z) readings

    Returns:
    - magnitudes: a list of magnitudes for each data point
    """
    magnitudes = []
    for x, y, z in data_stream:
        magnitude = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        magnitudes.append(magnitude)

    return magnitudes


# Sample data stream (replace with actual data source)
#Timestamp: 2024-11-02 12:00:01
#Magnetometer X: 128  Y: -230  Z: 410
data_stream = [
    (10, 20, 30),
    (15, 25, 35),
    (20, 30, 40),
    # ... more data points
]

# Process the data stream
magnitudes = process_magnetometer_data(data_stream)

# Print results
for i, magnitude in enumerate(magnitudes):
    print(f"Data point {i}: Magnitude = {magnitude:.2f}")
