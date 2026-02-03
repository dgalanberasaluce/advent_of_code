import re
import time

class Solution:

    # 811111111111119 -> 89
    # 818181911112111 -> 92
    # 8189819
    def _find_greater_pair(self, bank):
        
        max_voltage_1 = 0
        max_voltage_1_pos = 0

        tage_1 = 0
        max_voltage_2 = 0
        max_voltage_2_pos = 0
        
        #find the greatest number from [start, end)
        for pos, joltage in enumerate(bank[:len(bank)-1]):
            joltage_d = int(joltage)
            if joltage_d > max_voltage_1:
                max_voltage_1 = joltage_d
                max_voltage_1_pos = pos
            
            if joltage_d == 9 or pos == len(bank):
                break

        #find the greatest number from (greatest, end]
        for joltage in bank[max_voltage_1_pos+1:]:
            joltage_d = int(joltage)
            if joltage_d > max_voltage_2:
                max_voltage_2 = joltage_d
            if joltage_d == 9:
                break

        return str(max_voltage_1) + str(max_voltage_2)

    def solve1(self, filename):
        total_voltage = 0
        with open(filename) as f:
            for line in f:
                line = line.strip()
                max_voltage = self._find_greater_pair(line)
                total_voltage += int(max_voltage)
        
        return total_voltage

    def _find_largest_number(self, a):
        ans = 0
        ans_pos = 0
        
        for pos, elem in enumerate(a):
            if elem > ans:
                ans = elem
                ans_pos = pos
        
        return ans, ans_pos


    def _helper_solve2(self, bank, N):
        backup = []

        for pos, digit in enumerate(bank):
            # print(backup)
            while len(backup) > 0 and int(digit) > int(backup[-1]) and len(bank[pos:]) + len(backup) > N:
                backup.pop()
            if len(backup) < N:
                backup.append(digit)

        return "".join(backup[:N])
        

    def solve2(self, filename):
        total_voltage = 0
        with open(filename) as f:
            for line in f:
                line = line.strip()
                max_voltage = self._helper_solve2(line,12)
                # print(f"{line} - {max_voltage}")
                total_voltage += int(max_voltage)
        
        return total_voltage

def part1():
    sol_c = Solution() 
    sol = sol_c.solve1("sample.txt")
    expected = 357
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")

    print(f"Solution Test: {sol_c.solve1("input.txt")}")


def part2():
    sol_c = Solution() 
    sol = sol_c.solve2("sample.txt")
    expected = 3121910778619
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")

    # start_time = time.time()
    print(f"Solution Test: {sol_c.solve2("input.txt")}")
    # print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    # part1()
    part2()

    sol = Solution()
    # print(sol._helper_solve2("598911829", 5))
    # print(sol._helper_solve2("5998911829", 5))
    print(sol._helper_solve2("95887911729", 6))
