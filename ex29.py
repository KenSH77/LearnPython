people = 40
cats = 30
dogs = 41

if people < cats:
    print "Too many cats! the world is doomed!"

if people > cats:
    print "Not many cats! the world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry"

dogs +=5

if people >=dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."


print "Now the code is added if elif"

people = 30
cars = 40
buses= 40

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "we cannot decide."

if buses > cars:
    print "Thats too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

