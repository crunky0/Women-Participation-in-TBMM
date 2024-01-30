import csv

# will be used to fix the csv format if needed

csvfile = open('outfilename.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)

with open('infilename.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
            # Access the row data
            mylist = [row[0].split(";")[0], row[0].split(";")[1], row[0].split(";")[-1]]  # Replace this with your desired processing logic
            print(mylist)
            csvwriter.writerow(mylist)

     