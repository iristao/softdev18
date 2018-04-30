wordlist = ['list','of','words','temp','list','list','hey','hey']

# Find the frequency of a single word
def frequency(story, target):
	match = [x for x in story if x == target]
	return reduce(lambda x, y: x +1, match, 0)

print frequency(wordlist,'hey')

# Find the total frequency of a group of words
# def totalFreq(story, targetlist):
# 	alltargets = [x for x in 

# 	allmatch = reduce(lambda x, y: [] ,targetlist)


