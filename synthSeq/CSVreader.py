import csv
import time

# The CSV file to read
csv_file = 'synthSeq/file.csv'

# The BPM to use for timing
bpm = 120

# Calculate the time (in seconds) between each row
time_between_beat = 60 / bpm
time_between_rows = time_between_beat / 4 # resolution of 16th note


# Open the CSV file for reading
with open(csv_file, 'r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)
    # Loop through each row in the CSV file
    for row in reader:
        # Do something with the row (e.g. print it)
        print(row, end='')
        #test if row is divisable by 4
        if int(row[0]) % 4 == 0:
            #if true, send to arduino
            print("beat")
        print()
        # Wait for the calculated time between rows
        time.sleep(time_between_rows)
