import csv
#open file.csv and write 1 to 612
with open('synthSeq/file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)#
    #header
    writer.writerow(['INDEX'])
    for i in range(1, 613):
        writer.writerow([i])
