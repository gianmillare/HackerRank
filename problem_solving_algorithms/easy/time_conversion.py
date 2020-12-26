# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    # Remove the colons
    s = list(filter((":").__ne__, s))

    # Create a list of characters in pairs of two
    time_array = []
    for i in range(0, len(s), 2):
        time_array.append(s[i] + s[i+1])

    # if last item in time_array is AM or PM, convert
    if time_array[-1] == "AM":
        # if hour is 12, subtract 12
        if time_array[0] == "12":
            converted_hour = str(int(time_array[0]) - 12) + "0"
            time_array[0] = converted_hour
            return ":".join(time_array[0:3])
        # if hour is not 12, leave as is
        else:
            return ":".join(time_array[0:3])
    else:
        # convert the first hour by adding 12 if its not 12 (noon)
        if time_array[0] == "12":
            return ":".join(time_array[0:3])
        else:
            converted_hour = str(int(time_array[0]) + 12)

        # replace the previous hours with the converted hour
        time_array[0] = converted_hour
        return ":".join(time_array[0:3])
    
print(timeConversion("07:05:45AM"))
print(timeConversion("07:05:45PM"))
print(timeConversion("12:40:22AM"))
print(timeConversion("12:40:22PM"))