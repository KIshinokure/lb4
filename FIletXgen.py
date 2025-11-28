def read_filtered_lines(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                yield line.strip()

filtered = read_filtered_lines('data.txt', '')
for result in filtered:
    print(result)