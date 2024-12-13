from collections import Counter

def solve(puzzle_input):
    l, r = zip(*[map(int, l.split('   ')) for l in puzzle_input])
    l = sorted(l)
    r = sorted(r)
    distances = [abs(pair[0] - pair[1]) for pair in zip(l, r)]
    return sum(distances)


def solve_part_two(puzzle_input):
    l, r = zip(*[map(int, l.split('   ')) for l in puzzle_input])
    c = Counter(r)
    similarities = [x * c[x] for x in l]
    return sum(similarities)

def test():
    puzzle_input = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()
    print(solve(puzzle_input.split('\n')))
    print(solve_part_two(puzzle_input.split('\n')))

test()

with open('day01.txt', 'r') as puzzle_input:
    #print(solve(puzzle_input))
    print(solve_part_two(puzzle_input))

