def count_lines_in_file(file_path):
    answer = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            answer += 1
        return answer
    
print(count_lines_in_file("c:\projects\m.txt"))     