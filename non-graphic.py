import time
import math
import random

def check_overlap(circle1, circle2):
    distance_between_centers = math.sqrt((circle2['x'] - circle1['x'])**2 + (circle2['y'] - circle1['y'])**2)
    combined_radii = circle1['radius'] + circle2['radius']
    return distance_between_centers < combined_radii

def generate_random_coordinates(large_radius, small_radius):
    x = center_x + (random.random() - 0.5) * (large_radius - small_radius) * 2
    y = center_y + (random.random() - 0.5) * (large_radius - small_radius) * 2
    return {'x': x, 'y': y}

# Set properties for the large circle
center_x = 0
center_y = 0
large_circle_radius = 1000

# Set properties for the small circles
small_circle_radius = 20

number_of_small_circles = 2
count = 1
def simulate():
    global number_of_small_circles
    global count
    with open('example.csv', 'a') as file:
      # Write content to the file
      file.write(str(count) + ","+str(math.log10(number_of_small_circles)) + ",\n")
    count = count + 1
    # Draw and check for overlap for each small circle
    circles = []
    for _ in range(number_of_small_circles):
        random_coordinates = generate_random_coordinates(large_circle_radius, small_circle_radius)
        circle = {
            'x': random_coordinates['x'],
            'y': random_coordinates['y'],
            'radius': small_circle_radius
        }

        # Check for overlap with previous circles
        for previous_circle in circles:
            if check_overlap(circle, previous_circle):
                # print("Overlap")
                number_of_small_circles += 1
                # break

        # Store the current circle for future checks
        circles.append(circle)

while True:
    simulate()
    # time.sleep(1)  # Sleep for 1 second