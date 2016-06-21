class MyStuff(object):

  def __init__(self):
    self.tangerine = "And now a thousand years "

  def apple(self):
    print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine

# Getting Things from Things
# 3 ways so far

# dict style
mystuff['apple']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine