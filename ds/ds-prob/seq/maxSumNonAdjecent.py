def sol(l) :
	max_nasum_im2 = l[0]
	max_nasum_im1 = max(l[0], l[1])

	res = 0

	for i in range(2, len(l)) :
		max_nasum_i = max(max_nasum_im2+l[i], max_nasum_im1)
		res = max(max_nasum_i, res)

		max_nasum_im2 = max_nasum_im1
		max_nasum_im1 = max_nasum_i

	print(res)

sol([5, 5, 10, 100, 10, 5])
