#
# Test the HandleInts.returnTwoMaxFromList method.
#

from handleInts import HandleInts

#
# The tests for each call to HandleInts.returnTwoMaxFromList
#
def testIt (theList, expected1, expected2, expectException):

	print ("")
	print (f"Testing with list = {theList}")

	# Call the method and note any exception
	caughtException = False
	try:
		(actual1, actual2) = HandleInts.returnTwoMaxFromList(theList)
	except ValueError:
		caughtException = True

	# If the exception was not as expected FAIL
	if expectException != caughtException:
		print (f"FAILURE - Caught exception = {caughtException}; Expect exception = {expectException}")
		exit (1)

	# Any exception leaves no actuals so exit PASSED here
	if caughtException:
		print ("Caught exception as expected - test PASSED")
		return (None, None)

	print (f"Expected #1 & #2 = {expected1}, {expected2}")
	print (f"Actual #1 & #2 = {actual1}, {actual2}")

	# Check the first set of values
	if actual1 != expected1:
		print (f"FAILURE; actual1 = {actual1}; expected1 = {expected1}")
		exit (1)

	# Check the secondt set of values
	if actual2 != expected2:
		print (f"FAILURE; actual2 = {actual2}; expected2 = {expected2}")
		exit (1)

	print ("Test PASSED")

#
# The integer lists to test with
#

listOne = [5, 100, 10, 125, 15, 150, 20, 175, 25, 0]
listTwo = [25, 93, 97, 18, 71, 114, 52, 48]
listThree = [-2, 0, 1, 2, 2, 1]
listFour = [5, 5]
listFive = [3]

#
# Run the tests on the above lists
#

testIt (listOne, 175, 150,  False)
testIt (listTwo, 114, 97,  False)
testIt (listThree, 2, 1,  False)
testIt (listFour, 5, None,  False)
testIt (listFive, None, None, True)

