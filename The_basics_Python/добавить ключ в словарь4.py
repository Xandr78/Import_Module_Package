if __name__ == '__main__':

	dictionary = {'A': 1, 'B': 2, 'C': 3}
	key, value = 'D', 4

	dictionary.update({key: value})
	print(dictionary)		# {'A': 1, 'B': 2, 'C': 3, 'D': 4}
