package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main() {
	file, _ := os.Open("../data/07-1.txt")
	sc := bufio.NewScanner(file)

	var currDir = []string{"root"}
	var uniq = make(map[string]int)

	for sc.Scan() {
		if strings.Contains(sc.Text(), "$ cd") {
			currDir = append(currDir, strings.Split(sc.Text(), " ")[2])

			if strings.Contains(sc.Text(), "..") {
				currDir = currDir[:len(currDir)-2]
			} else {
				uniq[strings.Join(currDir, ",")] = 0
			}
		}
		if !strings.Contains("dir", sc.Text()) && !strings.Contains("ls", sc.Text()) {
			var fileSize, _ = strconv.Atoi(strings.Split(sc.Text(), " ")[0])
			for i := 1; i <= len(currDir); i++ {
				uniq[strings.Join(currDir[:i], ",")] += fileSize
			}
		}
	}
	var ans1 = 0
	for _, v := range uniq {
		if v <= 100000 {
			ans1 += v
		}
		if v >= 30000000 && (70000000 - uniq["root"]) <= v {
			// part 2 answer
			fmt.Println(v)
		}
	}
	// part 1 answer
	fmt.Println(ans1)
}