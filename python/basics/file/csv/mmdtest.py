import csv


fm = ['id', 'name', 'bad_credit', 'fake_application', 'court_blacklist']

writer = csv.writer(file('your.csv', 'wb'))
writer.writerow(fm)
lines = [range(5) for i in range(5)]
for line in lines:
    writer.writerow(line)
