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

#initializing Dictionary
durations = dict((el,0) for el in unique_numbers)

for call in calls:
    durations[call[0]] += int(call[3])
    durations[call[1]] += int(call[3])
#print(durations)
longest_caller = max(durations, key=durations.get)

print(f"{longest_caller} spent the longest time, {durations[longest_caller]} seconds, on the phone during September 2016")