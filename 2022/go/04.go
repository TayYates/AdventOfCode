package main

import (
	"fmt"
	"bufio"
	"os"
	"regexp"
	"strconv"
)

func main() {
	file, _ := os.Open("../data/04-1.txt")
	scanner := bufio.NewScanner(file)
	regExp, _ := regexp.Compile("(\\d+)-(\\d+),(\\d+)-(\\d+)")

	count1, count2 := 0, 0
	var a, b, c, d int

	for scanner.Scan() {
		matches := regExp.FindStringSubmatch(scanner.Text())
		a, _ = strconv.Atoi(matches[1])
		b, _ = strconv.Atoi(matches[2])
		c, _ = strconv.Atoi(matches[3])
		d, _ = strconv.Atoi(matches[4])
		if a <= c && b >= d || a >= c && b <= d {
			count1++
		}
		if a >= c && d >= a || c >= a && c <= b {
			count2++
		}
	}
	// part 1 answer
	fmt.Println(count1)
	// part 2 answer
	fmt.Println(count2)
}