"""
======================================================
===================== TESTMODULE =====================
======================================================

Lorem ipsum dolor sit amet, consetetur sadipscing
elitr, sed diam nonumy eirmod tempor invidunt ut
labore et dolore magna aliquyam erat, sed diam
voluptua.

TODO: Find a better text

TODO
Something

At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata
sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore
magna aliquyam erat, sed diam voluptua.

Todo Add topic

At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata
sanctus est Lorem ipsum dolor sit amet.

# Todo New feature1
# todo New feature2
#TODO: Find out who was Jack the Ripper
"""

import sys
# TODO: Make is this needed?
import os

class TestModuleClass:
	"""
	This is the TestModule class
	
	todo: Add the calc method
	"""
	
	def __init__(self, secret_key=1234):
		self.secret_key = secret_key # TODO: Find better name
		
	def do_something(self):
		pass # TODO
		
if __name__ == '__main__':
	# TODO: Add argument parsing
	test = TestModuleClass()
	test.do_something() # Todo - Is this ok?