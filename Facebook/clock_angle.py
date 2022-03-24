# Write a function that when given a time, returns the smallest angle between the minute and hour hands on an analog clock.
# Signature
# double getSmallestClockAngle(String timeString, String unit)
# Input
# timeString: a representation of  the time in a string with format hh:mm
# unit: string which determines if the return value is in degrees or radians
# Output
# an integer for degrees and accurate to 4 decimal places for radians.
# Note: use π (pi) functions provided by the language of choice.
# Example 1:
# Input:     
# timeString = '03:00’ 
# unit = ‘radians’
# Output:  1.5708
# Example 2:
# Input:     
# timeString  = ‘09:30’
# unit = ‘degrees’
# Output:  105
# Reference hints:
# There are 360 degrees in a circle.
# There are 2π radians in a circle
# An analog clock is divided in to 12 sectors, each sector represents 30 degrees (360/12 = 30)

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getSmallestClockAngle(timeString, unit):
  # Write your code here
    hour = int(timeString.split(":")[0])
    minute = int(timeString.split(":")[1])
    minute_hand_angle = minute * (360/60)
    hour_hand_angle = hour * (360/12) + minute * (360/12/60)

    if hour_hand_angle > minute_hand_angle:
        smallest_angle = hour_hand_angle - minute_hand_angle
    else:
        smallest_angle = minute_hand_angle - hour_hand_angle

    if unit == "radians":
        smallest_angle = round(smallest_angle * math.pi / 180, 4) # keep 4 decimal and round up
    
    return smallest_angle

# res = getSmallestClockAngle("09:30", "degrees")
res = getSmallestClockAngle("03:00", "radians")
print(res)