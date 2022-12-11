package main

import (
	"bufio"
	"fmt"
	"os"
)

/*func isRepeated(items []byte) bool {
	return items[0] == items[1] || items[0] == items[2] || items[0] == items[3] ||
		items[1] == items[2] || items[1] == items[3] ||
		items[2] == items[3]
}*/

func isRepeated(items []byte) bool {
	for i, item1 := range items {
		for _, item2 := range items[i+1:] {
			if item1 == item2 {
				return true
			}
		}
	}
	return false
}

func findIndex(items []byte, n int) int {
	for idx := n; idx <= len(items); idx++ {
		if !isRepeated(items[idx-n : idx]) {
			return idx
		}
	}
	return -1

}
func Part1(line string) int {
	items := []byte(line)
	return findIndex(items, 4)
}

func Part2(line string) int {
	items := []byte(line)
	return findIndex(items, 14)
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

	fmt.Println(Part1(lines[0])) // 1760

	fmt.Println(Part2(lines[0])) //

}
