tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

test_cat = '''
test only
'''

f_test_str1 = "%r"
f_test_str2 = "%s"

# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat
print test_cat
print f_test_str1 %("I use format display 1") 
print f_test_str2 %('I use format display 2')

