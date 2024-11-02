import math


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


# Example readings from the magnetometer (X, Y, Z)
x, y, z = 128, -230, 410  # Replace with actual sensor readings

# Calculate the compass heading
heading = calculate_heading(x, y)
direction = get_compass_direction(heading)

print(f"Compass Heading: {heading:.2f}° ({direction})")
