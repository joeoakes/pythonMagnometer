import math
import time


def calculate_heading(x, y):
    # Calculate the heading in radians and convert it to degrees
    heading = math.atan2(y, x) * (180 / math.pi)

    # Normalize the heading to a range of 0-360 degrees
    if heading < 0:
        heading += 360

    return heading


def get_compass_direction(heading):
    # Determine the compass direction based on the heading
    if (heading >= 337.5 or heading < 22.5):
        return "N"
    elif (22.5 <= heading < 67.5):
        return "NE"
    elif (67.5 <= heading < 112.5):
        return "E"
    elif (112.5 <= heading < 157.5):
        return "SE"
    elif (157.5 <= heading < 202.5):
        return "S"
    elif (202.5 <= heading < 247.5):
        return "SW"
    elif (247.5 <= heading < 292.5):
        return "W"
    elif (292.5 <= heading < 337.5):
        return "NW"


# Function to simulate reading from a data stream
def read_magnetometer_stream():
    # Simulated stream of magnetometer data (X, Y, Z)
    data_stream = [
        (128, -230, 410),
        (130, -225, 415),
        (120, -240, 400),
        (135, -220, 405),
        (140, -210, 420),
        # Add more tuples for continuous data
    ]
    for data in data_stream:
        yield data


# Process the data stream
for x, y, z in read_magnetometer_stream():
    heading = calculate_heading(x, y)
    direction = get_compass_direction(heading)

    # Print the X, Y, Z readings along with the heading and direction
    print(f"Magnetometer Readings -> X: {x}, Y: {y}, Z: {z}")
    print(f"Compass Heading: {heading:.2f}° ({direction})")

    # Wait for a short interval to simulate real-time data processing
    time.sleep(1)
