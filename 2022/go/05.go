package main

import (
	"fmt"
	"bufio"
	"os"
	"regexp"
	"strconv"
)

func main() {
	////// build the moves
	movesText, _ := os.Open("../data/05-moves.txt")	
	movesScanner := bufio.NewScanner(movesText)
	reMoves, _ := regexp.Compile("move (\\d+) from (\\d+) to (\\d+)")

	var movesList [][]string
	for movesScanner.Scan() {
		matches := reMoves.FindStringSubmatch(movesScanner.Text())
		matches = matches[1:]
		movesList = append(movesList, matches)
		//fmt.Println(matches)
	}

	////// build the stacks
	stacksText, _ := os.Open("../data/05-crates.txt")
	stacksScanner := bufio.NewScanner(stacksText)
	stacks := make([][]rune, 9)
	for stacksScanner.Scan() {
		for i, r := range stacksScanner.Text() {
			if r != ' ' && r!= '[' && r!= ']' && i%4 == 1 {
				stacks[i/4] = append(stacks[i/4], r)
			}
		}
	}
	// the stacks are in reverse order
	//fmt.Println(stacks)
	// initial state
	for _, stack := range stacks {
		fmt.Printf("%c", stack[0])
	}
	fmt.Println("")
	part2Stacks := make([][]rune, 9)
	copy(part2Stacks, stacks)
	//fmt.Println(part2Stacks)

	for i := 0; i < len(movesList); i++ {
		moves := movesList[i]
		count, _ := strconv.Atoi(moves[0])
		from, _ := strconv.Atoi(moves[1])
		from -= 1
		to, _ := strconv.Atoi(moves[2])
		to -= 1
		for i := 0; i < count; i++ {
			//// part 1 work
			// add to the 'to'
			stacks[to] = append([]rune{stacks[from][0]}, stacks[to]...)
			// take away from the 'from'
			stacks[from] = stacks[from][1:]

			//// part 2 work
			// similar to part 1, still add them 1 at a time, but in the reverse order
			part2Stacks[to] = append([]rune{part2Stacks[from][(count-1)-i]}, part2Stacks[to]...)
		}
		// only do this once per move
		part2Stacks[from] = part2Stacks[from][count:]
	}
	// part 1 answer
	for _, stack := range stacks {
		fmt.Printf("%c", stack[0])
	}

	fmt.Println("")

	// part 2 answer
	for _, stack := range part2Stacks {
		fmt.Printf("%c", stack[0])
	}
}