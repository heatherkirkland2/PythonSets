'''
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
'''
# Define the sets of flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# Destinations unique to your airline
unique_our_routes = our_routes.difference(competitor_routes)

# Check if there are any destinations that neither airline shares
no_common_destinations = our_routes.isdisjoint(competitor_routes)

# Display the results
print(f"Common destinations: {common_destinations}")
print(f"Destinations unique to our airline: {unique_our_routes}")
print(f"No common destinations: {no_common_destinations}")
