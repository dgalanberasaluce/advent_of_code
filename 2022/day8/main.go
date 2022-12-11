package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

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

func toMatrix(lines []string) [][]int {
	var matrix [][]int = make([][]int, len(lines))

	for i, line := range lines {
		matrix[i] = make([]int, len(lines[i]))
		for j, s := range line {
			matrix[i][j], _ = strconv.Atoi(string(s))
		}
	}
	return matrix
}

func isVisible(p int, dir []int) bool {
	for i := 0; i < len(dir); i++ {
		if p <= dir[i] {
			return false
		}
	}
	return true
}

func isVisibleColumn(p int, column int, dir [][]int) bool {

	for i := 0; i < len(dir); i++ {
		if p <= dir[i][column] {
			return false
		}
	}
	return true
}

func left(p int, dir []int) int {
	count := 0
	for i := len(dir) - 1; i >= 0; i-- {
		count += 1
		if p <= dir[i] {
			break
		}
	}
	return count
}

func right(p int, dir []int) int {
	count := 0
	for i := 0; i < len(dir); i++ {
		count += 1
		if p <= dir[i] {
			break
		}
	}
	return count
}

func up(p int, column int, dir [][]int) int {
	count := 0

	for i := len(dir) - 1; i >= 0; i-- {
		count += 1
		if p <= dir[i][column] {
			break
		}
	}
	return count
}

func down(p int, column int, dir [][]int) int {
	count := 0

	for i := 0; i < len(dir); i++ {
		count += 1
		if p <= dir[i][column] {
			break
		}
	}
	return count
}

func Part1(lines []string) int {
	m := toMatrix(lines)

	var cont = 0

	for i := 1; i < len(m)-1; i++ {
		for j := 1; j < len(m[i])-1; j++ {
			if isVisible(m[i][j], m[i][:j]) ||
				isVisible(m[i][j], m[i][j+1:]) ||
				isVisibleColumn(m[i][j], j, m[:i]) ||
				isVisibleColumn(m[i][j], j, m[i+1:]) {
				cont += 1
			}
		}
	}
	return 2*(len(m)+len(m[0])) - 4 + cont
}

func Part2(lines []string) int {
	m := toMatrix(lines)

	var max = 0
	for i := 1; i < len(m)-1; i++ {
		for j := 1; j < len(m[i])-1; j++ {
			var cont = left(m[i][j], m[i][:j]) *
				right(m[i][j], m[i][j+1:]) *
				up(m[i][j], j, m[:i]) *
				down(m[i][j], j, m[i+1:])

			if max < cont {
				max = cont
			}
		}
	}
	return max
}

func main() {
	var lines = ReadFromFile("input.txt")

	fmt.Println(Part1(lines)) // 1782
	fmt.Println(Part2(lines)) // 474606

}
