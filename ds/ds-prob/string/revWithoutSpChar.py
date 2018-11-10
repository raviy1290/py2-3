def revWithoutSpChar(str) :

	l = len(str)

	i=0
	j=l-1
	str_list = list(str)
	print(str_list)

	while i < j :
		while str_list[i].isalnum() == False :
			i+=1
		while str_list[j].isalnum() == False:
			j-=1

		str_list[i], str_list[j] = str_list[j], str_list[i]
		i+=1
		j-=1

	print(''.join(str_list))

revWithoutSpChar("abs,d")

revWithoutSpChar("abc,sd")