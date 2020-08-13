"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# creating list of unique call numbers &non-telemarketers
callers = []
non_telemarketers = []
for call in calls:
    callers.append(call[0])
    non_telemarketers.append(call[1])
#print(len(call_numbers))
callers = list(set(callers))
print(len(callers))

# creating list of unique text numbers
for text in texts:
   non_telemarketers.append(text[0])
   non_telemarketers.append(text[1])

# Now Non-Telemarketers are those numbers who have recieved calls or sent a text  or recieved a text

non_telemarketers = list(set(non_telemarketers))
# print(len(non_telemarketers))

telemarketers=[]
for caller in callers:
    if caller not in non_telemarketers:
        telemarketers.append(caller)

print(f"Following callers could be possible telemarketers: \n {caller}")
        
        