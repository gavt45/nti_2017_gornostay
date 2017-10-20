from re import compile, match
num = input()
pattern=re.compile("[A-Z][0-9][0-9][0-9][A-Z][A-Z]")
if pattern.match(num):
	print "Yes"
else:
	print "No"
