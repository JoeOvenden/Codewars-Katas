# In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) 
# of a numeric array.

# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

# The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. 
# If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent 
# in other languages)

# All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, 
# we don't know what is after and before and therefore, we don't know if it is a peak or not).

# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. 
# In case of a plateau-peak, please only return the position and value of the beginning of the plateau. 
# For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

from math import copysign

def pick_peaks(arr):
    peaks = {"pos": [], "peaks": []}
    
    if arr == []:
        return peaks
    
    direction = 0                   # 1 for upwards, -1 for downards, 0 start with
    prev_number = arr[0]
    potential_peak_location = -1    # Used to mark starts of plateaus
    
    for i in range(1, len(arr)):
        current_number = arr[i]
        
        # We only want to consider the first number in a plateau as the peak so skip the rest of the plateau
        if current_number == prev_number:
            continue
        
        # Get the direction, note from the above if clause that this direction will never be 0
        new_direction = int(copysign(1, current_number - prev_number))
        
        # If the direction changes from uphill to downhill, i.e. a peak, then add the peak stats
        if direction == 1 and new_direction == -1:
            peaks["pos"].append(potential_peak_location)
            peaks["peaks"].append(prev_number)
            
        # If the current number is larger than the previous, then store this as a potential peak location    
        if current_number > prev_number:
            potential_peak_location = i
            
        prev_number = current_number
        direction = new_direction
            
    return peaks