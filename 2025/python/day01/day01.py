class Solution():
    
    STARTING_POINT = 50

    def solve1(self, filename):
        final_point = self.STARTING_POINT
        zero_crossings = 0
        
        with open(filename, 'r') as f:
            for line in f:
                if line.strip():
                    direction = line[0]
                    steps = int(line[1:])

                    if direction.lower() == "r":
                        final_point += steps
                    else:
                        final_point -= steps
                    
                    final_point %= 100

                    zero_crossings += 1 if final_point == 0 else 0
        
        return zero_crossings



    def solve2(self, filename):
        current_position = self.STARTING_POINT
        zero_crossings = 0
        
        with open(filename, 'r') as f:
            for line in f:
                if line.strip():
                    direction = line[0].lower()
                    steps = int(line[1:])

                    if direction == "r":
                        zero_crossings += ( current_position + steps) // 100
                        current_position = (current_position + steps) % 100

                    elif direction == "l":
                        distance_to_zero = current_position if current_position > 0 else 100

                        if steps >= distance_to_zero:
                            zero_crossings += 1
                            remaining_steps = steps - distance_to_zero
                            zero_crossings += remaining_steps // 100

                        current_position = (current_position - steps) % 100

        return zero_crossings

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve1("day01.txt"))
    print(sol.solve2("day01.txt"))

