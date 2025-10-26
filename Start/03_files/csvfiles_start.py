# Reading and writing Comma Separate Values files with Python
import csv


# TODO: list the dialects that are available to use
print(csv.list_dialects())

# TODO: Open a CSV file and read each row of data
def reader_sample():
    with open("StockQuotes.csv", "r") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)


# TODO: Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer():
    with open("StockQuotes.csv", "r") as datafile:
        dialect = csv.Sniffer().sniff(datafile.read(1024))
        datafile.seek(0)
        hasheader = csv.Sniffer().has_header(datafile.read(1024))
        datafile.seek(0)
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)
        print(hasheader)



# TODO: Write data to a CSV file
def writer_sample():
    with open("SampleData.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Department", "Location"])
        csvwriter.writerow(["John Doe", "Accounting", "San Francisco, CA"])
        csvwriter.writerow(["John Die", "Accounting", "San Francisco, CA"])
        csvwriter.writerow(["Jne Dae", "Engineering", "Seattle, WA"])
        csvwriter.writerow(["Jim Due", "Marketing", "New York, NY"])


# Exercise the samples
# reader_sample()
writer_sample()
# use_sniffer()
