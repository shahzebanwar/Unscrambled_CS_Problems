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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_numbers= []

for text in texts:
    phone_numbers.append(text[0])
    phone_numbers.append(text[1])
    
for call in calls:
    phone_numbers.append(call[0])
    phone_numbers.append(call[1])

#Using the combination of set and lenth funtion to display unique records
print(f"There are {len(set(phone_numbers))} different telephone numbers in the records.")
