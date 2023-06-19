package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sort"
)

func main() {

	file, _ := os.Open("../data/01-1.txt")
	scanner := bufio.NewScanner(file)

	sums := []int{}
	currentSum := 0
	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		if scanner.Text() == "" {
			sums = append(sums, currentSum)
			currentSum = 0
		} else {
			newInt,_ := strconv.Atoi(scanner.Text())
			currentSum += newInt
		}
	}
	//fmt.Println(sums)
	sort.Sort(sort.IntSlice(sums))

	// part 1 answer
	fmt.Println(sums[len(sums)-1])

	// part 2 answer
	fmt.Println(sums[len(sums)-1] + sums[len(sums)-2] + sums[len(sums)-3])
}