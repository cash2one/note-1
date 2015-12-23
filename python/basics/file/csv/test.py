import csv, codecs


fobj = open('my.csv', 'wb')
fobj.write(codecs.BOM_UTF8)
writer = csv.writer(fobj)
writer.writerow(['Column1', 'Column2', 'Column3'])
lines = [range(3) for i in range(5)]
for line in lines:
    writer.writerow(line)


# fobj = open(filename, 'wb')
# fobj.write(codecs.BOM_UTF8)
# writer = csv.writer(fobj)
# writer.writerow(headers)


csvfile = file('csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close()
