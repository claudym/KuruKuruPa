name = 'Raijin'
age = 534 # hundreds of years
height = 250 #cm
weight = 303 #pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats very heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age+height+weight)