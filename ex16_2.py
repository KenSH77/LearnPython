from sys import argv

script, filename = argv

txt = open(filename)

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Good bye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# if (FALSE) {target.write(line1) target.write("\n") target.write(line2)
# target.write("\n") target.write(line3) target.write("\n") }

allline = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(allline)

print "And finally, we close it."
target.close()



