import re
import time

class Solution:
    def solve1(self, filename):
        invalid_ids_sum = 0
        
        # <firstId - lastId>,<...>
        with open(filename, 'r') as f:
            line = f.readline()

            for code in line.split(","):
                start_interval, end_interval = code.split("-")

                for i in range(int(start_interval), int(end_interval)+1):
                    i_s = str(i)

                    if i_s[:len(i_s)//2] == i_s[len(i_s)//2:]:
                        invalid_ids_sum += i

        return invalid_ids_sum

    def _is_repetition(self,digit):
        digit_s = str(digit)
        length = len(digit_s)

        for part_size in range(1,(length // 2) + 1):
            if len(digit_s) % part_size == 0:
                divide_string = [digit_s[i:i+part_size] for i in range(0, len(digit_s), part_size)]

                if len(set(divide_string)) == 1:
                    return True

        return False
        
    def _is_repetition_optimized(self, digit):
        digit_s = str(digit)
        length = len(digit_s)

        for part_size in range(1, (length // 2) + 1):
            if len(digit_s) % part_size == 0:
                pattern = digit_s[:part_size]
                repeats = length // part_size

                if pattern * repeats == digit_s:
                    return True
        
        return False

    '''
    "When you double a string(s + s), you create every possible "rotation" of that string
    - If a string is periodic (like "1212", rotating it by its period (shifting it by 2 spots) results in the exact same string)
    - By finding s inside the doubled version (excluding the trivial start and end positions), you prove
    that there is a non-trivial rotation that matches the original string - which is only possible
    if the string repeats
    '''
    def _is_repetition_optimized_pro(self, digit):
        digit_s = str(digit)
        return len(digit_s) > 1 and digit_s in (digit_s + digit_s)[1:-1]

    def solve2(self, filename):
        invalid_ids_sum = 0
        
        # <firstId - lastId>,<...>
        with open(filename, 'r') as f:
            line = f.readline().strip()

            for code in line.split(","):
                start_interval, end_interval = code.split("-")

                for digit in range(int(start_interval), int(end_interval)+1):
                    if self._is_repetition(digit):
                        invalid_ids_sum += digit
        return invalid_ids_sum


def part1():
    sol_c = Solution() 
    sol = sol_c.solve1("sample.txt")
    expected = 1227775554
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")

    print(f"Solution Test: {sol_c.solve1("input.txt")}")


def part2():
    sol_c = Solution() 
    sol = sol_c.solve2("sample.txt")
    expected = 4174379265
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")

    start_time = time.time()
    print(f"Solution Test: {sol_c.solve2("input.txt")}")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    # part1()
    part2()