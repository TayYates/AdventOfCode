package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func findDouble(myLine string) byte {
	part1, part2 := myLine[:len(myLine)/2], myLine[len(myLine)/2:]
	for i := 0; i < len(part1); i++ {
		if strings.Contains(part2, string(part1[i])) {
			return part1[i]
		}
	}
	// will never be reached, but golang requires it to be explicitly declared
	return 'a'
}

func findTriple(myLines []string) byte {
	part1, part2, part3 := myLines[0], myLines[1], myLines[2]
	for i := 0; i < len(part1); i++ {
		if strings.Contains(part2, string(part1[i])) && strings.Contains(part3, string(part1[i])) {
			return part1[i]
		}
	}
	// will never be reached
	return 'a'
}

func asciiValue(myChar byte) int {
	myVal := int(myChar)
	if myVal >= 97 {
		myVal -= 96
	} else {
		myVal -= 38
	}
	return myVal
}

func main() {
	file, _ := os.Open("../data/03-1.txt")
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	sumValues := 0
	for i := 0; i < len(lines); i ++ {
		myDouble := findDouble(lines[i])
		sumValues += asciiValue(myDouble)
	}

	// part 1 answer
	fmt.Println(sumValues)

	sumValues = 0
	for i := 0; i < len(lines); i += 3 {
		myTriple := findTriple(lines[i:i+3])
		sumValues += asciiValue(myTriple)
	}

	// part 2 answer
	fmt.Println(sumValues)
}