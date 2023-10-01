if __name__ == '__main__':

	first = {'A': 1, 'B': 2, 'C': 3}
	second = {'D': 4}

	dictionary = {**first, **second}
	print(dictionary)			# {'A': 1, 'B': 2, 'C': 3, 'D': 4}
