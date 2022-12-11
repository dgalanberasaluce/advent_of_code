package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func Part1(lines []string) int {
	var res = 0
	var parsed []int

	for _, line := range lines {
		parsed = parseString(line)
		if fullContains(parsed[0:2], parsed[2:4]) {
			res += 1
		}
	}

	return res
}

func Part2(lines []string) int {
	var res = 0
	var parsed []int

	for _, line := range lines {
		parsed = parseString(line)
		if contains(parsed[0:2], parsed[2:4]) {
			res += 1
		}
	}

	return res
}

func contains(list1, list2 []int) bool {

	return (list1[0] <= list2[1] && list1[1] >= list2[0]) ||
		(list2[0] <= list1[1] && list2[1] >= list1[0])
}

func fullContains(list1, list2 []int) bool {
	return (list1[0] <= list2[0] && list1[1] >= list2[1]) || (list1[0] >= list2[0] && list1[1] <= list2[1])
}

func parseString(line string) []int {
	re := regexp.MustCompile(`^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$`)
	matches := re.FindAllStringSubmatch(line, -1)

	res := []int{0, 0, 0, 0}
	var number_int int

	for i, number_s := range matches[0][1:] {
		number_int, _ = strconv.Atoi(number_s)
		res[i] = number_int
	}

	return res
}

func ReadFromFile(path string) []string {

	f, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)

	var total []string

	for fileScanner.Scan() {

		var line = fileScanner.Text()
		total = append(total, line)
	}

	f.Close()

	return total
}

func main() {
	var lines = ReadFromFile("input.txt")

	fmt.Println(Part1(lines)) // 547
	fmt.Println(Part2(lines)) // 843
}
