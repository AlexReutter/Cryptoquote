import sys, os, random

def crypt(a, cryptokey):
	try:
		x = cryptokey[a]
	except KeyError:
		x = a
	return x

def make_key():				# construct the key for cryptoquotes
	alphabet_pool = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
		    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
		    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
		     'o','p','q','r','s','t','u','v','w','x','y','z']
	cryptokey = {}
	for i in range(26):
		element = alphabet_upper[i]
		while ( element==alphabet_upper[i] ):
			element = random.choice(alphabet_pool)		# choose a letter from the pool
		alphabet_pool.remove(element)
		cryptokey[alphabet_upper[i]] = element
		cryptokey[alphabet_lower[i]] = element
	return(cryptokey)
	

def cryptoquote(input_filename, output_filename):

	# initialize key
	cryptokey = make_key()

	# initialize files and variables
	inputfile = open(input_filename, 'r')  # file to read
	outputfile = open(output_filename,'w')	# open the output file

	# do the cryptoquoting
	for line in inputfile.readlines(): 			# iterate over lines in file
		for character in list(line):			# iterate over characters in each line
			if ( character=="*" ):			# change keys at asterisks 
				cryptokey = make_key()
			outputfile.write(crypt(character,cryptokey))

	# close the files
	inputfile.close()
	outputfile.close()


