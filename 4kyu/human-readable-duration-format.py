
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    unit_names = ["year", "day", "hour", "minute", "second"]
    amounts = [0] * 5       # Amounts of each unit
    units_in_seconds = [365 * 24 * 3600, 24 * 3600, 3600, 60, 1]
    
    for i in range(5):
        amounts[i] = seconds // units_in_seconds[i]
        seconds %= units_in_seconds[i]
    
    # Work out how many units will be present in the phrase. 
    # i.e. 1 hour, 1 minute and 10 seconds -> 3 units present in phrase.
    unit_count = 5 - amounts.count(0)
    phrase = ""
    
    for i in range(5):
        # Skip units for which amounts are 0
        if amounts[i] == 0:
            continue
            
        # Decrease the number of units, so that now unit_count represents the number
        # of units that come AFTER the current unit.
        unit_count -= 1
            
        # Add number and unit to phrase
        phrase += str(amounts[i]) + " " + unit_names[i]
        
        # Pluralise if needed
        if amounts[i] != 1:
            phrase += "s"
            
        # If there is precisely 1 more unit to come in the phrase, then add and
        if unit_count == 1:
            phrase += " and "
            
        # If there is more than 1 more unit to come in the phrase, then add a comma
        elif unit_count >= 1:
            phrase += ", "
            
    return phrase