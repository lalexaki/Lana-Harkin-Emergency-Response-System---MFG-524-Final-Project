"""
                                                        Lana Harkin - MFG 524 - Final Semester Project
---------------------------------------------------------------------------------------------------------------------------------------------------------------------_
                                                                Real Time Emergency Response System
---------------------------------------------------------------------------------------------------------------------------------------------------------------------_
Problem Overview:
In emergencies, every second counts. An ambulance dispatch system must quickly determine
which ambulance is closest to an accident location so that help can be dispatched as soon
as possible.

This script implements an EmergencyResponseSystem class that uses a divide-and-conquer
strategy (similar in spirit to binary search) to rapidly locate the nearest available
ambulance from a list of ambulances positioned on a 2D plane.

Given a dictionary of ambulance coordinates and a single accident location (x, y),
the system returns the ambulance key-value pair that is nearest to the accident.
"""

# ------------------------------------------------------------------------------
# STEP 1: Import mathematical functions from library:
# ------------------------------------------------------------------------------
from math import sqrt #Imported "sqrt()" to compute square roots
'''                     Extra notes: needed for the Euclidean distance formula. '''


# ------------------------------------------------------------------------------
# Emergency Response CLASS: Class Definition and Initializer:
# ------------------------------------------------------------------------------
class EmergencyResponseSystem:
    ''' Extra notes: A system for finding the nearest ambulance to an accident location. '''
    

    # ------------------------------------------------------------------------------
    # Emergency Response System CLASS: STEP 1: Initialize the system with ambulance data:
    # ------------------------------------------------------------------------------
    def __init__(self, ambulances): #Create a new EmergencyResponseSystem instance.
        '''                              Extra notes: ambulances  A dictionary mapping ambulance labels to (x, y)
                                                      coordinates. For example: {'A': (2, 4), 'B': (10, 3),...} '''
        
        self._ambulances = ambulances #Stores the ambulance dictionary as an instance variable so all methods in the class can access it.
        '''                            Extra notes: The underscore prefix on "_ambulances" is a naming convention
                                                    indicating this is a private attribute. '''
        
    # ------------------------------------------------------------------------------
    # Emergency Response System CLASS: STEP 2: Helper method: compute Euclidean distance:
    # ------------------------------------------------------------------------------
    def _euclidean_distance(self, coord1, coord2):
        ''' Extra notes: Compute and return the Euclidean distance between two (x, y) coordinate
                         tuples.
                         coord1  the first (x, y) coordinate tuple
                         coord2  the second (x, y) coordinate tuple
                         Returns the straight-line distance between coord1 and coord2 as a float. '''
        
        dx = coord1[0] - coord2[0] #Computes the difference in x-coordinates between the two points.
        dy = coord1[1] - coord2[1] #Computes the difference in y-coordinates between the two points.
        distance = sqrt(dx ** 2 + dy ** 2) #Applies the Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2).
        return distance #Returns the computed distance value as a float.

    # ------------------------------------------------------------------------------
    # Emergency Response System CLASS: STEP 3: Helper method: divide-and-conquer search:
    # ------------------------------------------------------------------------------
    def _divide_and_conquer(self, sorted_list, accident_location, low, high):
        ''' Extra Notes: Recursively apply divide-and-conquer to find the nearest ambulance.
                         Split the list in half, find the best candidate in each half, then
                         compare them to return the overall nearest. 
                         sorted_list: a list of (key, (x, y)) tuples sorted by x-coordinate.
                         accident_location: the (x, y) tuple of the accident location.
                         low: the starting index of the current sublist (inclusive).
                         high: the ending index of the current sublist (inclusive). '''
        
        #BASE CASE: only one ambulance remains in this portion of the list; Return it immediately since there is nothing left to compare against.
        if low == high: #Checks if the current sublist has been reduced to a single element.
            return sorted_list[low] #Returns that single ambulance as the best (only) candidate in this sublist.

        #DIVIDE: find the midpoint index to split the list into two halves.
        mid = (low + high) // 2 #Computes the midpoint index using integer division, splitting the sublist into left and right halves.
        '''                      Extra notes: "//" is Python's integer (floor) division operator.
                                              It discards any remainder, giving a whole-number index. '''
        
        #CONQUER: Repetativly find the nearest ambulance in the left half.
        left_best = self._divide_and_conquer(sorted_list, accident_location, low, mid) #Repetativly searches the left half for the nearest ambulance.
        '''                                                                             Extra notes: indices low to mid. '''
        
        #CONQUER: Repetativly find the nearest ambulance in the right half.
        right_best = self._divide_and_conquer(sorted_list, accident_location, mid + 1, high) #Repetativly searches the right half for the nearest ambulance.
        '''                                                                                   Extra notes: indices mid+1 to high. '''
        
        #COMBINE: Compute the distance from each half's best candidate to the accident.
        left_distance = self._euclidean_distance(left_best[1], accident_location) #Computes the distance from the left half's best candidate to the accident location.
        right_distance = self._euclidean_distance(right_best[1], accident_location) #Computes the distance from the right half's best candidate to the accident location.

        #COMBINE: Compare the two distances and return whichever candidate is closer.
        #If distances are equal I return the ambulance with the lexicographically smaller key.
        if left_distance < right_distance: #Checks if the left candidate is strictly closer to the accident.
            return left_best #Returns the left candidate as the overall nearest for this sublist.
        elif right_distance < left_distance: #Checks if the right candidate is strictly closer to the accident.
            return right_best #Returns the right candidate as the overall nearest for this sublist.
        else:
            #Tie: If both candidates are the same distance away; pick the one.
            #Whose label is lexicographically smaller.
            if left_best[0] < right_best[0]: #Compares ambulance label strings (e.g. 'A' < 'B') to break the tie predictably.
                return left_best #Returns left candidate because its label comes first alphabetically.
            else:
                return right_best #Returns right candidate because its label comes first alphabetically (or they are equal).

    # ------------------------------------------------------------------------------
    # Emergency Response System CLASS: STEP 4: Main method: find nearest ambulance
    # ------------------------------------------------------------------------------
    def find_nearest_ambulance(self, accident_location):
        ''' Extra notes: Find and return the nearest ambulance to the given accident location.
                         Uses a divide-and-conquer approach:
                            1. Convert the ambulance dictionary into a list of (key, (x, y)) tuples.
                            2. Sort that list by x-coordinate (following the professor's Hint #1).
                            3. Apply the recursive divide-and-conquer search to find the nearest ambulance.
                            4. Return the result as a dictionary {key: (x, y)}.
                         accident_location  a (x, y) tuple representing the accident coordinates.
                         Returns a single-item dictionary, e.g., {'D': (7, 1)}, of the nearest ambulance. '''
        
        #STEP 4a: Convert the dictionary into a list of (key, value) tuples so it can be sorted and indexed for the divide-and-conquer search.
        ambulance_list = list(self._ambulances.items()) #Converts the ambulance dictionary into a list of (key, (x,y)) tuples using the .items() method.
        '''                                              Extra notes: Converting to a list of items gives me a structure I can
                                                                      sort and access by index. '''
        
        #STEP 4b: Sort the ambulance list by x-coordinate: "consider sorting by x-coordinate to apply a binary-search-like process."
        ambulance_list.sort(key=lambda ambulance: ambulance[1][0]) #Sorts the list in ascending order of each ambulance's x-coordinate using a lambda function.
        '''                                                        Extra notes: ambulance[1] accesses the (x,y) tuple, and [0] pulls the x value.
                                                                   Sorting by x-coordinate organizes the data so the divide step
                                                                   splits the ambulances into a "left region" and a "right region". '''
        
        #STEP 4c: Call the divide-and-conquer helper with the full list.
        nearest = self._divide_and_conquer(ambulance_list, accident_location, 0, len(ambulance_list) - 1)#Runs the divide-and-conquer search across the entire sorted list.
        ''' Extra notes: indices 0 to last. '''

        #STEP 4d: Return the result as a dictionary with one key-value pair.
        return {nearest[0]: nearest[1]} #Packages the result as a dictionary {label: (x, y)} and returns it.

# ------------------------------------------------------------------------------
# Helper Function: Print the coordinate table and accident location:
# ------------------------------------------------------------------------------
def print_coordinate_table(ambulances, accident_location):
    ''' Extra notes: Print the ambulance coordinate table and accident location.
                     ambulances: the ambulance dictionary {label: (x, y)}.
                     accident_location: the (x, y) tuple of the accident. '''
    
    print("Ambulance Coordinate Table:") #Prints the table header label.
    print(f"  {'Ambulance':<12} {'Location (x, y)'}") #Prints the column headers, left-aligned using an f-string format specifier.
    print(f"  {'-'*12} {'-'*15}") #Prints a divider line under the column headers.
    for label, coords in ambulances.items(): #Loops over each ambulance in the dictionary to print its row.
        print(f"  {label:<12} {str(coords)}") #Prints each ambulance's label and its (x, y) coordinates.
    print(f"Accident Location: X = {accident_location}") #Prints the accident location below the table.

# ==============================================================================
# MFG 524 Given Test Case and All Other Test Cases:
# ==============================================================================
if __name__ == '__main__':

    # ------------------------------------------------------------------------------
    # MFG 524 Given Test Case: The coordinate map given:
    # ------------------------------------------------------------------------------
    print("=" * 55)
    print("MFG 524 Given Test Case:")
    print("=" * 55)

    original_ambulances = { #Defines the ambulance dictionary for the original problem using the coordinate table from the project.
        'A': (2, 4), #Ambulance A is located at coordinates (2, 4).
        'B': (10, 3), #Ambulance B is located at coordinates (10, 3).
        'C': (5, 8), #Ambulance C is located at coordinates (5, 8).
        'D': (7, 1), #Ambulance D is located at coordinates (7, 1).
        'E': (4, 5) #Ambulance E is located at coordinates (4, 5).
    }
    original_accident = (6, 2) #Defines the accident location as a tuple (x, y) = (6, 2).

    print_coordinate_table(original_ambulances, original_accident) #Prints the coordinate table and accident location for the given problem.

    system_original = EmergencyResponseSystem(original_ambulances) #Creates an Emergency Response System instance with the original ambulance data.
    result_original = system_original.find_nearest_ambulance(original_accident) #Calls find_nearest_ambulance() with the accident location to get the nearest ambulance.

    print(f"Nearest Ambulance: {result_original}") #Prints the returned key-value pair of the nearest ambulance.
    print()

    # ------------------------------------------------------------------------------
    # TEST CASE (a): Base test -- verifies core functionality
    # Accident location: (5, 3)
    # Expected nearest: C (5, 5) -- distances: A~3.61, B~3.61 (tie->A by label), C~2.0, but let's confirm
    # ------------------------------------------------------------------------------
    print("=" * 55)
    print("TEST CASE (a): Base Functionality")
    print("=" * 55)

    ambulances_a = { #Defines the ambulance dictionary for test case (a).
        'A': (3, 7), #Ambulance A is located at (3, 7).
        'B': (8, 2), #Ambulance B is located at (8, 2).
        'C': (5, 5) #Ambulance C is located at (5, 5).
    }
    accident_a = (5, 3) #Defines the accident location for test case (a) as (5, 3).

    print_coordinate_table(ambulances_a, accident_a) #Prints the coordinate table and accident location for test case (a).

    system_a = EmergencyResponseSystem(ambulances_a) #Creates a new Emergency Response System instance for test case (a).
    result_a = system_a.find_nearest_ambulance(accident_a) #Finds the nearest ambulance for test case (a).

    print(f"Nearest Ambulance: {result_a}") #Prints the result for test case (a).
    print()

    # ------------------------------------------------------------------------------
    # TEST CASE (b): Edge case -- tie resolution by lexicographically smallest key
    # Ambulances C and D are at the same location (6,3); tie is broken by label ('C' < 'D')
    # Accident location: (5, 3)
    # ------------------------------------------------------------------------------
    print("=" * 55)
    print("TEST CASE (b): Tie Resolution (Lexicographic)")
    print("=" * 55)

    ambulances_b = { #Defines the ambulance dictionary for test case (b).
        'A': (3, 3), #Ambulance A is located at (3, 3).
        'B': (8, 5), #Ambulance B is located at (8, 5).
        'C': (6, 3), #Ambulance C is located at (6, 3).
        'D': (6, 3), #Ambulance D is located at (6, 3) -- same location as C; tie expected.
        'E': (5, 5) #Ambulance E is located at (5, 5).
    }
    accident_b = (5, 3) #Defines the accident location for test case (b) as (5, 3).

    print_coordinate_table(ambulances_b, accident_b) #Prints the coordinate table and accident location for test case (b).

    system_b = EmergencyResponseSystem(ambulances_b) #Creates a new Emergency Response System instance for test case (b).
    result_b = system_b.find_nearest_ambulance(accident_b) #Finds the nearest ambulance for test case (b); tie between C and D should resolve to C.

    print(f"Nearest Ambulance: {result_b}") #Prints the result for test case (b).
    print()

    # ------------------------------------------------------------------------------
    # TEST CASE (c): Single ambulance -- system must return it without error
    # Accident location: (1, 1)
    # ------------------------------------------------------------------------------
    print("=" * 55)
    print("TEST CASE (c): Single Ambulance")
    print("=" * 55)

    ambulances_c = { #Defines the ambulance dictionary for test case (c) with only one entry.
        'A': (5, 5) #Ambulance A is the only available ambulance, located at (5, 5).
    }
    accident_c = (1, 1) #Defines the accident location for test case (c) as (1, 1).

    print_coordinate_table(ambulances_c, accident_c) #Prints the coordinate table and accident location for test case (c).

    system_c = EmergencyResponseSystem(ambulances_c) #Creates a new Emergency Response System instance for test case (c).
    result_c = system_c.find_nearest_ambulance(accident_c) #Finds the nearest ambulance; with only one option, it must return A without error.

    print(f"Nearest Ambulance: {result_c}") #Prints the result for test case (c).
    print()

    # ------------------------------------------------------------------------------
    # TEST CASE (d): Negative and large coordinate values
    # Accident location: (0, 0)
    # Tests that the algorithm handles large numbers and negative coordinates correctly.
    # ------------------------------------------------------------------------------
    print("=" * 55)
    print("TEST CASE (d): Negative and Large Coordinates")
    print("=" * 55)

    ambulances_d = { #Defines the ambulance dictionary for test case (d) with a wide range of coordinate values.
        'A': (-100, -50), #Ambulance A is located at negative coordinates (-100, -50).
        'B': (1e6, 1e6), #Ambulance B is located at very large coordinates (1,000,000, 1,000,000).
        'C': (500, 400), #Ambulance C is located at (500, 400).
        'D': (-200, -300), #Ambulance D is located at large negative coordinates (-200, -300).
        'E': (250, 250) #Ambulance E is located at (250, 250).
    }
    accident_d = (0, 0) #Defines the accident location for test case (d) as the origin (0, 0).

    print_coordinate_table(ambulances_d, accident_d) #Prints the coordinate table and accident location for test case (d).

    system_d = EmergencyResponseSystem(ambulances_d) #Creates a new Emergency Response System instance for test case (d).
    result_d = system_d.find_nearest_ambulance(accident_d) #Finds the nearest ambulance with the wide-range coordinate values.

    print(f"Nearest Ambulance: {result_d}") #Prints the result for test case (d).
    print()













