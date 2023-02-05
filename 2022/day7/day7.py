
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2022/day7/day_7input.txt', 'r') as f:
        input_lines = [x.strip() for x in f.readlines()]
    return input_lines

sample_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
sample_input = [x.strip() for x in sample_input.splitlines(keepends=True)]


class file:
    def __init__(self, parent, filename, size) -> None:
        self.filename = filename
        self.parent = parent
        self.isDir = True if size == 0 else False
        self.size = size
        self.files = dict()
    def __str__(self):
        return self.filename

def print_filesystem(root_dir:file) -> None:
    systemTree = f'- {root_dir.filename} (dir, size={root_dir.size})\n'
    def list_dir(dir:file, depth:int=0) -> str:
        dir_contents = ''
        indent = ' ' * depth
        for file in dir.files.values():
            file_type = 'dir' if file.isDir else 'file'
            dir_contents += f'{indent}- {file.filename} ({file_type}, size={file.size})\n'
            if file.isDir:
                dir_contents += list_dir(file, depth+1)
        return dir_contents
    systemTree += list_dir(root_dir)
    print(systemTree)

def _calc_dir_sizes(root_dir:file):
    def dir_dfs(cur_dir:file):
        cur_size = 0
        for file in cur_dir.files.values():
            if file.isDir:
                cur_size += dir_dfs(file)
            else:
                cur_size += file.size
        cur_dir.size = cur_size
        return cur_size
    dir_dfs(root_dir)

def process_filesystem(command_lines:list) -> file:
    cur_dir = None
    root_dir = None
    for line in command_lines:
        tokens = line.split()
        isCmd = tokens[0] == '$'
        if isCmd:
            cmd = tokens[1]
            if cmd == 'cd':
                filename = tokens[2]
                if cur_dir is None: # Root dir
                    new_dir = file(cur_dir, filename, 0)
                    root_dir = new_dir
                    cur_dir = root_dir
                    continue
                if filename == '..':
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = cur_dir.files[filename]
            else: # cmd == 'ls'
                continue
        else: # is ls output
            size = 0
            filename = tokens[1]
            if tokens[0].isdigit():
                size = int(tokens[0])

            new_file = file(cur_dir, filename, size)
            cur_dir.files[filename] = new_file
    _calc_dir_sizes(root_dir)
    return root_dir

def sum_small_dirs(root_dir:file) -> int:
    def sum_dfs(cur_dir:file) -> int:
        total_size = 0
        if cur_dir.size < 100000:
            total_size += cur_dir.size
        for file in cur_dir.files.values():
            if file.isDir:
                total_size += sum_dfs(file)
        return total_size
    return sum_dfs(root_dir)

def find_min_dir_size(root_dir:file, minimum_size:int) -> int:
    def size_dfs(cur_dir:file, minimum_size:int, dirs=[]) -> list:
        if cur_dir.size > minimum_size:
            dirs.append(cur_dir.size)
        for file in cur_dir.files.values():
            if file.isDir:
                size_dfs(file, minimum_size, dirs)
        return dirs
    return min(size_dfs(root_dir, minimum_size))

if __name__ == "__main__":
    input_lines = read_input()

    # input_lines = sample_input
    root_dir = process_filesystem(input_lines)
    print_filesystem(root_dir)
    # Part 1 output
    print(sum_small_dirs(root_dir))
    
    # Part 2
    TOTAL_DISK_SPACE = 70000000
    SPACE_NEEDED = 30000000
    space_used = root_dir.size
    min_size = abs(TOTAL_DISK_SPACE - SPACE_NEEDED - space_used)
    print(find_min_dir_size(root_dir, min_size))

