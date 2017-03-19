from sys import argv

script, filename = argv

file16 = open(filename)

confile16 = file16.read()

print "%s" % confile16

file16.close()

