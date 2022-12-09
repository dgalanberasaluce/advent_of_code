package main

import (
	"bufio"
	"fmt"
	"os"
)

func GetTotalPriority(word_list []string) int {
	cont := 0

	for _, word := range word_list {
		cont += getPriority(word)
	}

	return cont
}

func getPriority(word string) int {
	return priority(getCommonCharacter(word[:len(word)/2], word[len(word)/2:]))
}

func priority(char byte) int {

	if char < 'a' {
		return 1 + int(char) + 58 - 'a'
	}

	return 1 + int(char) - 'a'
}

func getCommonCharacter(item1, item2 string) byte {
	item1_byte := []byte(item1)
	item2_byte := []byte(item2)

	for i := 0; i < len(item1_byte); i++ {
		for j := 0; j < len(item2_byte); j++ {
			if item1_byte[i] == item2_byte[j] {
				return item1_byte[i]
			}
		}
	}

	return 0
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

		var words = fileScanner.Text()
		total = append(total, words)
	}

	f.Close()

	return total
}

func part1() int {
	var input []string = ReadFromFile("input.txt")
	return GetTotalPriority(input)
}

func getBadge(algo []string) byte {
	algo_b_0 := []byte(algo[0])
	algo_b_1 := []byte(algo[1])
	algo_b_2 := []byte(algo[2])
	for i := 0; i < len(algo_b_0); i++ {
		for j := 0; j < len(algo_b_1); j++ {
			if algo_b_0[i] == algo_b_1[j] {
				for k := 0; k < len(algo_b_2); k++ {
					if algo_b_1[j] == algo_b_2[k] {
						return algo_b_0[i]
					}
				}
			}
		}
	}
	return 0
}

func part2() int {
	var input []string = ReadFromFile("input.txt")
	count := 0

	for i := 0; i < len(input); i += 3 {
		count += priority(getBadge(input[i : i+3]))
	}

	return count
}

func main() {

	fmt.Println(part2())

}
