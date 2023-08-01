def how_many_words(frase):
	count = 0
	i = 0

	while i < len(frase):
		if i != 0 and not frase[i].isalnum() and frase[i - 1].isalnum():
			count = count + 1
		i += 1
	if not frase[-1].isalnum():
		count = count - 1
	return count + 1

def reverse_phrase(frase):
	return (frase)
