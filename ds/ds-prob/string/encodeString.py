def encodeString(str) :
	prev = str[0]
	length = 1

	for i in range(1, len(str)) :
		if str[i] == prev :
			length += 1
		else :
			print('%d%s' % (length, prev), end="")
			prev = str[i]
			length = 1
	print('%d%s' % (length, prev))

encodeString("AAAABBBCCD")

encodeString("AAAABBBCCDAADC")

