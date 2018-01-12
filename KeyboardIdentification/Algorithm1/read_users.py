def letter_number(letter):
	return ord(letter) - ord('a')


def create_matrix():
	matrix = []

	for i in range(26):
		matrix.append([])
		for j in range(26):
			matrix[i].append([])

	return matrix


def read_user(file_name):
	print(file_name)
	matrix = create_matrix()

	input = open(file_name, 'r')

	
	for line in input:
		parsed = line.split()
		matrix[letter_number(parsed[0][0])][letter_number(parsed[0][1])] = [int(x) for x in parsed[2:]]

	for i in range(26):
		for j in range(26):
			matrix[i][j].sort()

	input.close()

	return matrix


if __name__ == "__main__":
	main()