package main

import (
	"fmt"
	"io/ioutil"
)

func unique(input string) bool {
	var m = make(map[rune]bool)
	var uniq = []rune{}
	for _, x := range input {
		if m[x] {
			return false
		}
		uniq = append(uniq, x)
		m[x] = true
	}
	return true
}

func main() {
	file, _ := ioutil.ReadFile("../data/06-1.txt")
	text := string(file)
	
	var ans1, ans2 = 0, 0
	for i, _ := range text {
		// part 1
		if ans1 == 0 {
			if unique(text[i:i+4]) {
				ans1 = i + 4
			}
		}
		// part 2
		if ans2 == 0 {
			if unique(text[i:i+14]) {
				ans2 = i + 14
			}
		}
	}
	// part 1 answer
	fmt.Println(ans1)
	// part 2 answer
	fmt.Println(ans2)
}