"""
This module is for finding the
the smallest circle around a cluster of points in 2D
and plotting them against on a 2D Graph
INPUT : [(9, -6), (-14, -15), (-5, 9), (5, 1), (12, -7), (9, -14)]
OUTPUT : Centre : (-3, -6)
         Radius : 15.1
TODO : Usage of numpy for easier manipulation
"""

import math
import random
import os
import matplotlib.pyplot as plt
from datetime import datetime
import time
import warnings

# Global variable declaration for easy maintenance
MINIMUM_INPUT_POINTS = 25
MAXIMUM_INPUT_POINTS = 60
MINIMUM_INPUT_RANGE = -15
MAXIMUM_INPUT_RANGE = 15


# Calculate euclidean distance
# FORMULA: sqrt((x1-x2)^2 + (y1-y2)^2)
def euclidean_distance(x, y):
    return math.sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))


# Check point lies inside or on boundaries of circle
def is_points_inside(c, p):
    return euclidean_distance(c[0], p) <= c[1]


# Check whether circle encloses the points
def check_valid_circle(circle, points):
    for point in points:
        if not is_points_inside(circle, point):
            return False
    return True


# Finds the unique circle with three points
def two_point_circle(x, y):
    # centre is between x and y
    center = [(x[0] + y[0]) / 2.0, (x[1] + y[1]) / 2.0]
    # radius is half of xy
    return [center, euclidean_distance(x, y) / 2.0]


# Finds the unique circle with three points
def three_point_circle(p1, p2, p3):
    # Finding the circle center
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    i = x1 * x1 + y1 * y1
    j = x2 * x2 + y2 * y2
    k = x1 * y2 - y1 * x2
    circle = [(y2 * i - y1 * j) // (2 * k),
              (x1 * j - x2 * i) // (2 * k)]

    # Unique circle having boundary with three points
    circle[0] += p1[0]
    circle[1] += p1[1]
    return [circle, euclidean_distance(circle, p1)]


# Recursively trying to find the circle which encloses all the points
def circle_decision_algorithm(input_points):
    p_length = len(input_points)  # length of the input points
    if p_length <= 3:  # p_length is less than 3, trying to define a minimum enclosing circle
        if not p_length:
            return [[0, 0], 0]
        elif p_length == 1:
            return [input_points[0], 0]
        elif p_length == 2:
            return two_point_circle(input_points[0], input_points[1])

        # Working with two points trying to define a minimum enclosing circle which encloses the points
        for i in range(3):
            for j in range(i + 1, 3):
                c = two_point_circle(input_points[i], input_points[j])
                if check_valid_circle(c, input_points):
                    return c

        # Working with three points trying to define a minimum enclosing circle which encloses the points
        return three_point_circle(input_points[0], input_points[1], input_points[2])

    else:  # p_length is greater than 3, repeat the process
        return enclosed_circle_calculator(input_points, [], len(input_points))


# Acts as a wrapper for the minimum enclosing circle logic
def enclosed_circle_calculator(input_list, result_list, input_list_length):
    # Reading all the input points
    if input_list_length == 0 or len(result_list) == 3:
        return circle_decision_algorithm(result_list)
    # Randomly pick one point from the input points
    index = random.randint(0, input_list_length - 1)
    random_input_point = input_list[index]
    # Swapping the points instead of deleting the input list
    input_list[index], input_list[input_list_length - 1] = input_list[input_list_length - 1], input_list[index]
    # Again process by eliminating the previous random_input_point
    d = enclosed_circle_calculator(input_list, result_list, input_list_length - 1)
    if is_points_inside(d, random_input_point):
        return d
    # Points known to be on boundary
    result_list.append(random_input_point)
    # Return the estimated MEC for known points
    return enclosed_circle_calculator(input_list, result_list, input_list_length - 1)


# Arrange the input list
def input_calculator(input_points):
    input_list = []
    # If no input points from the call statement, take the default random input points
    if not input_points:
        input_points = random.randint(MINIMUM_INPUT_POINTS, MAXIMUM_INPUT_POINTS)
    # Generating a input list with the length of input points
    for points in range(input_points):
        input_list.append((random.randint(MINIMUM_INPUT_RANGE, MAXIMUM_INPUT_RANGE),
                           random.randint(MINIMUM_INPUT_RANGE, MAXIMUM_INPUT_RANGE)))
    return input_list


# Plotting the input points and output circle in a graph
def plot_output(input_list, output):
    plt.title("Minimum Enclosing Circle")  # set title
    subplot = plt.subplot()
    x = [x[0] for x in input_list]
    y = [x[1] for x in input_list]
    # Plot the input points
    subplot.scatter(x, y, s=10, facecolors='none', edgecolors='black')
    # Plot the center point
    subplot.scatter(output[0][0], output[0][1], (round(output[1], 1)), edgecolors='blue')
    # Plot the output circle
    subplot.add_patch(plt.Circle((output[0][0], output[0][1]), (round(output[1], 1)), color='red', fill=False))
    subplot.set_aspect('equal')
    subplot.plot()
    # Save the plot diagram
    file_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + '.png'
    plt.savefig(file_name)
    save_file_path = str(os.getcwd()) + str('\\') + str(file_name)
    # print("Diagram is plotted and saved on the path : {} ".format(save_file_path))
    return save_file_path


# Pilot for the program which guides
def pilot(input_points=0):
    # Ignore warnings
    warnings.filterwarnings("ignore")
    try:
        start = time.time()
        if int(input_points) < 0 or not str(input_points).isdecimal() or str(input_points).isalpha():
            raise ValueError()
        input_list = input_calculator(input_points)  # Generate the input points
        output = enclosed_circle_calculator(input_list, [], len(input_list))  # Calculate the minimum enclosing circle
        centre = (output[0][0], output[0][1])
        radius = (round(output[1], 1))
        output_graph = plot_output(input_list, output)
        end = time.time()
        time_taken = end - start
        response_output = {"message": "Success",
                           "centre": centre,
                           "radius": radius,
                           "time_taken": round(time_taken, 3),
                           "graph_path": output_graph,
                           "input_points": input_list}
        return response_output
    except ValueError:
        response_output = {"message": "Error",
                           "error_description": "Wrong input value...Value must be an Integer and should not "
                                                "have negative value"
                           }
        return response_output
