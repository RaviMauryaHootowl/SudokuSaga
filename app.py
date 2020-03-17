'''
Author : Ravi Maurya
Project Name : Sudoku Saga
Date : 16/March/2020 (COVID-19 Holidays)
'''

from flask import Flask, render_template, request
import json

app = Flask(__name__)


#These are functions which solves the sudoku using Backtracking
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row_and_col(arr, row, col, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False


def check(arr, row, col, num):
    return not used_in_row_and_col(arr, row, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]
    if(not find_empty_location(arr, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if(check(arr, row, col, num)):
            arr[row][col] = num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False


# Home page route
@app.route('/')
def home():
    return render_template('index.html')


# Solve route (Only POST)
@app.route('/solve', methods=['POST'])
def solve():
    if request.method == 'POST':
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        result_grid = {}
        inputJson = request.json
        # convertJsonToArray(inputJson);
        for i in range(9):
            for j in range(9):
                grid[i][j] = int(inputJson.get(str(i))[j])
        if(solve_sudoku(grid)):
            #print("sudo accepted")
            for i in range(9):
                result_grid[str(i)] = []
                for j in range(9):
                    result_grid[str(i)].append(grid[i][j])
        else:
            #print("sudo denied")
            return json.dumps({"error": "yes"})
        return json.dumps(result_grid)


if __name__ == "__main__":
    app.run(debug=True)
