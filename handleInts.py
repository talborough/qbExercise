#
# A class to handle integers in unusual ways
#
class HandleInts:

	#
	# A static method to return, as a list of 2 elements, the two largest numbers from a passed-in list.
	# If there is no "second largest" number, None is returned.
	# If there are not at least 2 numbers in the list, a ValueError exception is raised and the two returned values are undefined
	#
	def returnTwoMaxFromList (listOfIntegers):

		if len(listOfIntegers) < 2:
			raise (ValueError("Must provide a list of 2 or more elements"))

		listOfIntegers.sort(reverse = True)

		# THe largest is always here
		firstLargest = listOfIntegers[0]

		# Skip possible duplicates to find (possible) next largest
		nextLargest = None
		for anInteger in listOfIntegers:
			if anInteger < firstLargest:
				nextLargest = anInteger
				break

		return (firstLargest, nextLargest)
