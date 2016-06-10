tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#testing
print "gatico tabby1 %r" % tabby_cat
print "gatico tabby2 %s" % tabby_cat
print "gato persa1 %r" % persian_cat
print "gato persa2 %s" % persian_cat
print "Wakatta!"

# Infinite loop cyclying the array of escape characters... fooled..

#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,