package words

import (
	"strings"
)

func GetMostUsedThreeWords(text string) []string {
	array := strings.Split(text, " ")
	dic := make(map[string]int)
	for i := 0; i < len(array); i += 1 {
		if _, ok := dic[array[i]]; ok {
			dic[array[i]] += 1
		} else {
			dic[array[i]] = 1
		}
	}
	return array
}