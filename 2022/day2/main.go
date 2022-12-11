package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func getScore(elem1, elem2 string) int {

	switch elem1 {
	case "A":
		switch elem2 {
		case "X":
			return 4
		case "Y":
			return 8
		case "Z":
			return 3
		}
	case "B":
		switch elem2 {
		case "X":
			return 1
		case "Y":
			return 5
		case "Z":
			return 9
		}
	case "C":
		switch elem2 {
		case "X":
			return 7
		case "Y":
			return 2
		case "Z":
			return 6
		}
	}
	return 0
}

func getTotalScore(strategy [][]string) int {
	var count int = 0

	for _, row := range strategy {
		count += getScore(row[0], row[1])
	}

	return count
}

func getScorePart2(elem1, elem2 string) int {
	switch elem1 {
	case "A":
		switch elem2 {
		case "X":
			return 3
		case "Y":
			return 4
		case "Z":
			return 8
		}
	case "B":
		switch elem2 {
		case "X":
			return 1
		case "Y":
			return 5
		case "Z":
			return 9
		}
	case "C":
		switch elem2 {
		case "X":
			return 2
		case "Y":
			return 6
		case "Z":
			return 7
		}
	}
	return 0
}

func getTotalScorePart2(strategy [][]string) int {
	var count int = 0

	for _, row := range strategy {
		count += getScorePart2(row[0], row[1])
	}

	return count
}

func ReadFromFile(path string) [][]string {
	f, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)

	var total [][]string

	for fileScanner.Scan() {

		var words = strings.Fields(fileScanner.Text())
		total = append(total, words)
	}

	f.Close()

	return total
}

func main() {
	var input [][]string = ReadFromFile("input.txt")

	var total = getTotalScore(input)

	fmt.Println(total)

	var total_2 = getTotalScorePart2(input)

	fmt.Println(total_2)
}
