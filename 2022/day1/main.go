package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func GetCalories(total [][]int) int {
	var max int = 0
	var total_row *int

	for _, row := range total {
		total_row = new(int)
		for _, element := range row {
			*total_row += element
		}

		if max < *total_row {
			max = *total_row
		}
	}
	return max
}

func min(s []int) (int, int) {
	min := s[0]
	pos := 0
	for i := 1; i < len(s); i++ {
		if min > s[i] {
			min = s[i]
			pos = i
		}
	}
	return pos, min
}

func GetCaloriesTop3(total [][]int) int {
	max := []int{0, 0, 0}
	var total_row *int

	for _, row := range total {
		total_row = new(int)
		for _, element := range row {
			*total_row += element
		}

		var pos, min_value = min(max)
		if min_value < *total_row {
			max[pos] = *total_row
		}
	}

	var result int = 0
	for _, elem := range max {
		result += elem
	}

	return result
}

func ReadFromFile(path string) [][]int {
	f, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []int
	var word_i int
	var total [][]int
	var count int = 0

	for fileScanner.Scan() {
		var word = strings.TrimSpace(fileScanner.Text())

		if word != "" {
			word_i, err = strconv.Atoi(word)
			fileLines = append(fileLines, word_i)
		} else {
			//months[i] = make([]int, days[i])
			total = append(total, fileLines)
			fileLines = nil
			count += 1
		}
	}

	f.Close()

	return total
}

func main() {
	var input [][]int = ReadFromFile("input.txt")

	calories := GetCalories(input)

	fmt.Println(calories)

	calories_top3 := GetCaloriesTop3(input)

	fmt.Println(calories_top3)

}
