//searchbar funtion
function look_up() {    
    let searchString = document.getElementById('searchbar').value 
    searchString = searchString.toLowerCase();
    let x = document.getElementsByClassName('courses');
    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(searchString)) {
            x[i].style.display="none";
        } else {
            x[i].style.display="list-item";
        }
    }
}

//processing  data from back end
function toArr(data) {
    const twoD = data.split("@");
    for (let arr of twoD) {
        arr = arr.split("+");
        for (let elem of arr) {
            elem = elem.split(",");
        }
    }
    return twoD;
}

let btn = document.getElementById('btn');
btn.addEventListener('click', event => {
    //getting user imput
    var monday = document.getElementById('m').value;
    var tuesday = document.getElementById('t').value;
    var wednesday = document.getElementById('w').value;
    var thursday = document.getElementById('r').value;
    var friday = document.getElementById('f').value;
    var dept = document.getElementById('searchbar').value;
    const user_input = dept + "+" + monday + "+" + tuesday + "+" + wednesday + "+" + thursday + "+" + friday;
    console.log(JSON.stringify(user_input));
    //sending information to the backend
    const information = JSON.stringify(user_input);
    const spawner = require('child_process').spawn;
    const python_process = spawner('python', ['./better_schedule.py', information]); 
    //gettting information from the backend 
    const classInfo = "";
    python_process.stdout.on('data', (data) => { //reads the python output
       classInfo = data.toString();
    }); 
    var classTable = toArr(classInfo); 
    const out = document.getElementById("output");
    let table = document.createElement('table');
    for (let one of classTable) {
        for (let two of one) {
            for (let row of two) {
                table.insertRow();
                for (let cell of row) {
                    let newCell = table.rows[table.rows.length - 1].insertCell();
                    newCell.textContent = cell;
                }
            }
        }
    }
    out.appendChild(table);
});
