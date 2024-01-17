import turtle
import math
import random

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.circle(radius, 360)
    turtle.penup()

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
large_circle_color = "#3498db"

# Set properties for the small circles
small_circle_radius = 20

number_of_small_circles = 2

def simulate():
    global number_of_small_circles
    turtle.clear()

    # Draw and check for overlap for each small circle
    circles = []
    for _ in range(number_of_small_circles):
        small_circle_color = "#e74c3c"
        random_coordinates = generate_random_coordinates(large_circle_radius, small_circle_radius)
        circle = {
            'x': random_coordinates['x'],
            'y': random_coordinates['y'],
            'radius': small_circle_radius
        }

        # Draw the small circle
        draw_circle(circle['x'], circle['y'], circle['radius'], small_circle_color)

        # Check for overlap with previous circles
        for previous_circle in circles:
            if check_overlap(circle, previous_circle):
                print("Overlap")
                number_of_small_circles += 1
                break

        # Store the current circle for future checks
        circles.append(circle)

    turtle.update()
    turtle.ontimer(simulate, 100)

# Set up turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Set up canvas
turtle.setup(width=800, height=800)

# Call the simulate function to start the animation
simulate()

# Keep the window open
turtle.mainloop()
