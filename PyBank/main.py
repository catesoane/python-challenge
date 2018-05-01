import csv
import os

filename = input("Enter a name of a file")

month_count = 0
total_revenue = 0
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# open csv path
csvpath = os.path.join("raw_data", "filename")
with open (csvpath, 'r', newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  next(csvreader)
  
# gather monthly changes in revenue
  for row in csvreader:
    month_count = month_count + 1
    months.append(row[0])
    this_month_revenue = int(row[1])
    total_revenue = total_revenue + this_month_revenue
    if month_count > 1:
      revenue_change = this_month_revenue - last_month_revenue
      revenue_changes.append(revenue_change)
    last_month_revenue = this_month_revenue
 
#check progress
print(revenue_changes)
print(months)
