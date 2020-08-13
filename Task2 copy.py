"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# create a set of unique numbers from the calls csv
phone_numbers = []
for call in calls:
    phone_numbers.append(call[0])
    phone_numbers.append(call[1])
    
unique_numbers = list(set(phone_numbers))
#print(unique_numbers)
#print(calls[:5])

# Calculate the longest call to or from the numbers
durations = [0]*len(unique_numbers)
for key in range(len(unique_numbers)):
    for value in calls:
        if value[0]== unique_numbers[key] or value[1] == unique_numbers[key]:
            durations[key] += int(value[3])
#print(durations)
longest_caller = unique_numbers[durations.index(max(durations))]
longest_call = max(durations)

print(f"{longest_caller} spent the longest time, {longest_call} seconds, on the phone during September 2016")