import pandas as pd
import matplotlib.pyplot as plt
import time

# define the CSV file path and the column names
csv_path = 'data.csv'
x_col = 'voltage'
y_col = 'step'

# initialize the figure
plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

while True:
    # read the CSV file
    df = pd.read_csv(csv_path)

    # plot the data
    ax.clear()
    ax.plot(df[x_col], df[y_col])

    # show the plot
    plt.draw()
    plt.pause(0.01)

    # wait for 1 second before reading the CSV file again
    time.sleep(1)
