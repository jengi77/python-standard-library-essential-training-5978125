# Reading and writing Comma Separate Values files with Python
import csv


# list the dialects that are available to use
print(csv.list_dialects())


# Open a CSV file and read each row of data
def reader_sample():
    with open("StockQuotes.csv") as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            print(row)


# Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer():
    with open("StockQuotes.csv") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        hasHeader = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        print("Headers found: " + str(hasHeader))
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)


# Write data to a CSV file
def writer_sample():
    with open("SampleData.csv", mode="w") as csvfile:
        # create a csv writer
        csvWriter = csv.writer(csvfile)

        # write the header
        csvWriter.writerow(["Name", "Department", "Location"])

        # write a few rows
        csvWriter.writerow(["John Doe", "Accounting", "San Francisco CA"])
        csvWriter.writerow(["Jane Dae", "Engineering", "Seattle WA"])
        csvWriter.writerow(["Jim Due", "Human Resources", "New York NY"])


# Exercise the samples
# reader_sample()
# writer_sample()
# use_sniffer()
