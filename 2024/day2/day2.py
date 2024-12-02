# imports



# Sample Input
sample_input = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day2/day_2input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def is_safe(report:int):
    # all decreasing/increasing
    # AND adjacent values differ by 1-3
    is_increasing = report[0] - report[1] < 0
    for i in range(len(report)-1):
        level = report[i]
        next_level = report[i+1]
        diff = level - next_level
        if ((is_increasing and diff > 0) or (not is_increasing and diff < 0) or 
            (abs(diff) > 3) or (abs(diff) < 1)):
            return False
    return True



if __name__ == "__main__":
    input_lines = read_input(True)
    reports = []
    for line in input_lines:
        reports.append([int(x) for x in line.split()])
    
    safe_report_count = 0
    for report in reports:
        safe_report_count += is_safe(report)

    print(safe_report_count)

    # Part 2
    # going to try brute force first...

    safe_report_count = 0
    for report in reports:
        safe_report = 0
        if (not is_safe(report)):
            for i in range(len(report)):
                removed_level = report.pop(i)
                if (is_safe(report)):
                    safe_report = 1
                    break
                else:
                    report.insert(i, removed_level)
        else:
            safe_report = 1
        safe_report_count += safe_report
    print(safe_report_count)