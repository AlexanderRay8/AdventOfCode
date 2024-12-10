# imports



# Sample Input
sample_input = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day5/day_5input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def process_input(input_lines):
    is_page_ordering = True
    page_ordering = dict()
    page_updates = []
    for line in input_lines:
        if line == "":
            is_page_ordering = False
            continue
        if is_page_ordering:
            required_page, page = line.split('|')
            if page in page_ordering.keys():
                page_ordering[page].add(required_page)
            else:
                page_ordering[page] = {required_page}
        else:
            page_updates.append(line.split(','))
    return page_ordering, page_updates

if __name__ == "__main__":
    input_lines = read_input(True)
    page_ordering, page_updates = process_input(input_lines)
    print(page_ordering)
    middle_page_sum = 0
    for update in page_updates:
        is_update_valid = True
        i = 0
        while i < len(update):
            after_pages = set(update[i:])
            if update[i] not in page_ordering.keys():
                i += 1
                continue
            wrong_updates = page_ordering[update[i]].intersection(after_pages)
            if wrong_updates:
                is_update_valid = False
                for j in range(i, len(update)):
                    if update[j] in wrong_updates:
                        update[i], update[j] = update[j], update[i]
                        break
            else:
                i += 1
                
        if not is_update_valid:
            middle_page_sum += int(update[len(update) // 2])
    print(middle_page_sum)
    