import itertools
import types


def comb(base, length):

	baselist = []
	if isinstance(base, str):
		if "n" in base:
			baselist += range(10)
		if "l" in base:
			baselist += map(chr, range(97, 123))
		if "u" in base:
			baselist += map(chr, range(65, 91))

	if isinstance(base, types.ListType):
		baselist = base

	if type(length) == int:
		length = [length]

	def getGen():
		for l in length:
			for comb in itertools.product(baselist, repeat=l):
				yield "".join(map(str,comb))
	return getGen


def wordlist(pattern):
	
	if len(pattern) == 0:
		yield ""
		return

	first = pattern[0]
	if isinstance(first, str):
		for suffix in wordlist(pattern[1:]):
			yield first + suffix
	if isinstance(first, types.FunctionType):
		for prefix in first():
			for suffix in wordlist(pattern[1:]):
				yield prefix + suffix


def writeWordlist(wl, filename):
	with open(filename, "w") as file:
		file.writelines(map(lambda x: x+"\r\n", wl))

example_pattern = "Ab1",comb("n",2),comb("nlu",2)
