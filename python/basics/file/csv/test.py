import csv
import codecs


# csv.writer
fobj = open('my.csv', 'wb')
fobj.write(codecs.BOM_UTF8)
writer = csv.writer(fobj)
writer.writerow(['Column1', 'Column2', 'Column3'])
lines = [range(3) for i in range(5)]

for line in lines:
    writer.writerow(line)

fobj.close()


# csv.reader
csvfile = file('my.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close()


# csv.DictReader
for d in csv.DictReader(open('my.csv', 'rb')):
    print d


# csv.DictWriter
fobj = open('my1.csv', 'wb')
fobj.write(codecs.BOM_UTF8)
FIELDS = ['Column1', 'Column2', 'Column3']
writer = csv.DictWriter(fobj, fieldnames=FIELDS)
lines = [dict(zip(FIELDS, xrange(3))) for _ in xrange(5)]

lines.insert(0, dict(zip(FIELDS, FIELDS)))

for line in lines:
    writer.writerow(line)

fobj.close()
