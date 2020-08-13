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
callers = set()
receivers = set()
for call in calls:
    callers.add(call[0])
    receivers.add(call[1])

text_senders = set()
text_receivers = set()
for text in texts:
   text_senders.add(text[0])
   text_receivers.add(text[1])


telemarketers = sorted(callers - (text_receivers | text_senders | receivers))
# print(len(non_telemarketers))


print(f"Following callers could be possible telemarketers: ")
print('\n'.join(telemarketers))
        