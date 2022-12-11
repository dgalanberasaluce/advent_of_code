package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"unicode"
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

type crane struct {
	crates string
	idx    string
}

/*func (c *crane) addCrate(crate string) {
	*crateP
	c.crates += crate
}*/

func (c *crane) addIdx(idx string) {
	c.idx = idx
}

func reverse(s string) string {
	rev := ""
	for _, character := range s {
		rev = string(character) + rev
	}
	return rev
}

func solve(lines []string, rev bool) string {
	re1 := regexp.MustCompile(`^[ ]*(\[[A-Z]\][ ]*)+$`)
	re2 := regexp.MustCompile(`^[ ]*([1-9][ ]*)+$`)
	re3 := regexp.MustCompile(`^move ([1-9]+[0-9]*) from ([0-9]) to ([0-9])$`)

	cranes := map[string]string{}
	stacks := map[string]string{}

	for _, line := range lines {
		matchesRe1 := re1.FindAllStringSubmatch(line, -1)
		if len(matchesRe1) > 0 {
			for i, crate := range line {
				if unicode.IsLetter(crate) {
					cranes[strconv.Itoa(i)] += string(crate)
				}
			}
		}

		matchesRe2 := re2.FindAllStringSubmatch(line, -1)
		if len(matchesRe2) > 0 {
			for i, stack := range line {
				if unicode.IsDigit(stack) {
					stacks[string(stack)] = strconv.Itoa(i)
				}
			}
		}

		matchesRe3 := re3.FindAllStringSubmatch(line, -1)
		if len(matchesRe3) > 0 {
			movements, _ := strconv.Atoi(matchesRe3[0][1])
			var src_stack = matchesRe3[0][2]
			var dst_stack = matchesRe3[0][3]

			if len(cranes[stacks[src_stack]]) >= movements {
				if rev {
					cranes[stacks[dst_stack]] = reverse(cranes[stacks[src_stack]][:movements]) + cranes[stacks[dst_stack]]
				} else {
					cranes[stacks[dst_stack]] = cranes[stacks[src_stack]][:movements] + cranes[stacks[dst_stack]]
				}
				cranes[stacks[src_stack]] = cranes[stacks[src_stack]][movements:]
			}
		}
	}

	var final_word string
	for i := 1; i <= len(stacks); i++ {
		final_word += string(cranes[stacks[strconv.Itoa(i)]][0])
	}

	return final_word
}

func Part1(lines []string) string {
	return solve(lines, true)
}

func Part2(lines []string) string {
	return solve(lines, false)
}

func main() {
	var lines = ReadFromFile("input.txt")
	fmt.Println(Part1(lines)) // QMBMJDFTD
	fmt.Println(Part2(lines)) // NBTVTJNFJ
}
