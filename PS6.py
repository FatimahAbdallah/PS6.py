"""
Course     : CMPSC 131, Summer 2025
File       : PS6.py 

Name       : Fatimah Abdallah
GitHub User: Fatimah_Abdallah11
Collaboration Statement: I did all the code by myself.
"""


def sum_of_rows(filename):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            values = line.strip().split(',')
            total = 0
            for val in values:
                if val:
                    total += float(val)
            results.append(round(total, 2))
    return results

def sum_of_columns(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for val in line.strip().split(','):
                if val:
                    row.append(float(val))
            matrix.append(row)
    longest = 0
    for row in matrix:
        if len(row) > longest:
            longest = len(row)
    output = []
    for col in range(longest):
        col_sum = 0
        for row in matrix:
            if col < len(row):
                col_sum += row[col]
        output.append(round(col_sum, 2))
    return output

def is_magic_square(filename):
    with open(filename, 'r') as f:
        matrix = []
        for line in f:
            row = []
            for val in line.strip().split(','):
                if val:
                    row.append(int(val))
            matrix.append(row)

    size = len(matrix)
    for row in matrix:
        if len(row) != size:
            return False

    target = sum(matrix[0])

    for row in matrix:
        if sum(row) != target:
            return False

    for i in range(size):
        s = 0
        for j in range(size):
            s += matrix[j][i]
        if s != target:
            return False

    if sum(matrix[i][i] for i in range(size)) != target:
        return False
    if sum(matrix[i][size - i - 1] for i in range(size)) != target:
        return False

    return True

def buy_ticket(filename, seat):
    row_letter = seat[0:1]
    ascii_code = ord(row_letter)
    if ascii_code >= 97:  # lowercase to uppercase manually
        row_letter = chr(ascii_code - 32)

    col_index = int(seat[1:]) - 1
    row_index = ord(row_letter) - ord('A')

    with open(filename, 'r') as file:
        lines = file.read().split("\n")

    matrix = []
    for line in lines:
        line = line.strip()
        if line:
            matrix.append(line.split())

    if row_index >= len(matrix) or col_index >= len(matrix[row_index]):
        return False

    if matrix[row_index][col_index] == 'O':
        matrix[row_index][col_index] = 'X'
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join(row) + '\n')
        return True

    return False

def product_of_digits(n):
    if n == 0:
        return 1
    last = n % 10
    rest = n // 10
    if last == 0:
        return product_of_digits(rest)
    return last * product_of_digits(rest)

def near_by_unique(n):
    return near_by_unique_helper(n, -1)

def near_by_unique_helper(n, prev):
    if n == 0:
        return 0
    digit = n % 10
    rest = n // 10
    if digit == prev:
        return near_by_unique_helper(rest, prev)
    return near_by_unique_helper(rest, digit) * 10 + digit

def zero_below(table, threshold):
    zero_below_helper(table, threshold, 0, 0)

def zero_below_helper(table, threshold, row, col):
    if row == len(table):
        return
    if col == len(table[row]):
        zero_below_helper(table, threshold, row + 1, 0)
        return
    if table[row][col] < threshold:
        table[row][col] = 0
    zero_below_helper(table, threshold, row, col + 1)

def remove_evens(lst):
    if not lst:
        return []
    current = lst[0]
    rest = remove_evens(lst[1:])
    if current % 2 == 0:
        return rest
    return [current] + rest

def remove_evens_destructive(lst):
    remove_evens_destructive_helper(lst, 0)

def remove_evens_destructive_helper(lst, index):
    if index == len(lst):
        return
    if lst[index] % 2 == 0:
        del lst[index]
        remove_evens_destructive_helper(lst, index)
    else:
        remove_evens_destructive_helper(lst, index + 1)

def next_double(lst):
    return next_double_helper(lst, 0)

def next_double_helper(lst, i):
    if i >= len(lst) - 1:
        return 0
    count = 1 if lst[i] * 2 == lst[i + 1] else 0
    return count + next_double_helper(lst, i + 1)

################################################################################

def main():
    print("product_of_digits(4052):", product_of_digits(4052))  # 40
    print("near_by_unique(1222333):", near_by_unique(1222333))  # 123

    table = [[5, 2, 7], [9, 3, 6]]
    zero_below(table, 5)
    print("zero_below:", table)  # [[5, 0, 7], [9, 0, 6]]

    print("remove_evens([1, 2, 4, 7, 9, 10]):", remove_evens([1, 2, 4, 7, 9, 10]))  # [1, 7, 9]

    values = [2, 4, 5, 6, 7, 8]
    remove_evens_destructive(values)
    print("remove_evens_destructive:", values)  # [5, 7]

    print("next_double([1, 2, 2, 4, 3, 6, 7]):", next_double([1, 2, 2, 4, 3, 6, 7]))  # 3

if __name__ == "__main__":
    main()
