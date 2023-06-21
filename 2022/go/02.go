package main

import (
	"fmt"
	"os"
	"bufio"
)

func main() {
	file, _ := os.Open("../data/02-1.txt")
	scanner := bufio.NewScanner(file)

	score1 := 0
	score2 := 0

	scoreDict1 := map[string]int{
		"A X": 4,
		"A Y": 8,
		"A Z": 3,
		"B X": 1,
		"B Y": 5,
		"B Z": 9,
		"C X": 7,
		"C Y": 2,
		"C Z": 6,
	}
	scoreDict2 := map[string]int{
		"A X": 3,
		"A Y": 4,
		"A Z": 8,
		"B X": 1,
		"B Y": 5,
		"B Z": 9,
		"C X": 2,
		"C Y": 6,
		"C Z": 7,
	}
	for scanner.Scan() {
		// fmt.Println(scanner.Text())
		score1 += scoreDict1[scanner.Text()]
		score2 += scoreDict2[scanner.Text()]
	}
	// part 1 answer
	fmt.Println(score1)
	// part 2 answer
	fmt.Println(score2)
}