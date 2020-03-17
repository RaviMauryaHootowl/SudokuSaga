let sudo = {}

// reads the input from the HTML Table
function getData() {
    const tableObj = document.querySelector('#sudoku-table');
    for (let i = 0; i < 9; i++) {
        sudo[i] = [];
        for (let j = 0; j < 9; j++) {
            let cellData = tableObj.rows[i].cells[j].innerText;
            if (cellData == "") {
                cellData = "0";
            }
            sudo[i].push(cellData);
        }
    }
}

// Fills the solved sudoku in the HTML Table
function fillData(jsonInput) {
    const tableObj = document.querySelector('#sudoku-table');
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (tableObj.rows[i].cells[j].innerText == "") {
                tableObj.rows[i].cells[j].innerText = jsonInput[i][j];
                tableObj.rows[i].cells[j].style.backgroundColor = '#363636';
                tableObj.rows[i].cells[j].style.fontWeight = "500";
            }
        }
    }
}

// On button click sends AJAX Request to '/solve' route
const errorLabel = $('#error-label');
errorLabel.css('display', 'none');
const solveBtn = $('#solve-btn');
solveBtn.click(function () {
    getData()
    $.ajax({
        type: 'POST',
        url: '/solve',
        data: JSON.stringify(sudo),
        contentType: 'application/json',
        dataType: "json",
        success: function (data) {
            console.log(data)
            // Do something with retured data
            if (!(data['error'] == 'yes')) {
                fillData(data);
                errorLabel.css('display', 'none');
            } else {
                errorLabel.css('display', 'block');
            }
        },
        error: function (error) {
            console.log(error);
        }
    })
})

// Clears the HTML Table
const clearBtn = $('#clear-btn');
clearBtn.click(function () {
    errorLabel.css('display', 'none');
    const tableObj = document.querySelector('#sudoku-table');
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            tableObj.rows[i].cells[j].innerText = "";
            tableObj.rows[i].cells[j].style.backgroundColor = '#1e1e1e';
            tableObj.rows[i].cells[j].style.fontWeight = "700";
        }
    }
})