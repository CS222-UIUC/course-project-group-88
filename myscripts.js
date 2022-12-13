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
});

let show = document.getElementById('show');
show.addEventListener('click', event => {
    var classTable = [
        [['Intro Computing: Engrg & Sci 101'], ['Laboratory-Discussion', '04:00PM - 05:50PM ; M', '06:00PM - 07:50PM ; M', '01:00PM - 02:50PM ; T', '06:00PM - 07:50PM ; W', '05:00PM - 06:50PM ; R', '03:00PM - 04:50PM ; F']], 
        [['Little Bits to Big Ideas 102'], ['Laboratory', '04:00PM - 05:15PM ; R', '05:30PM - 06:45PM ; W']], 
        [['Intro Computing: Non-Tech 105'], ['Laboratory-Discussion', '11:00AM - 12:20PM ; M', '05:00PM - 06:20PM ; M', '01:00PM - 02:20PM ; T', '03:00PM - 04:20PM ; T']], 
        [['Data Science Discovery 107'], ['Laboratory-Discussion', '05:00PM - 06:20PM ; W', '05:00PM - 06:20PM ; W']], 
        [['Introduction to Computer Science I 124'], ['Discussion/ Recitation', '01:00PM - 01:50PM ; T', '01:00PM - 01:50PM ; T', '02:00PM - 02:50PM ; T', '02:00PM - 02:50PM ; T', '03:00PM - 03:50PM ; T', '03:00PM - 03:50PM ; T']], 
        [['Introduction to Computer Science II 128'], ['Laboratory-Discussion', '03:30PM - 04:50PM ; F', '05:00PM - 06:20PM ; F', '06:30PM - 07:50PM ; F', '03:30PM - 04:50PM ; F', '05:00PM - 06:20PM ; F', '06:30PM - 07:50PM ; F', '03:30PM - 04:50PM ; F', '05:00PM - 06:20PM ; F', '06:30PM - 07:50PM ; F', '03:30PM - 04:50PM ; F', '05:00PM - 06:20PM ; F', '06:30PM - 07:50PM ; F']], 
        [['Undergraduate Open Seminar in Computer Science 199'], ['Laboratory-Discussion', '12:30PM - 01:45PM ; W'], ['Online', '05:00PM - 05:50PM ; M', '05:00PM - 06:50PM ; R'], ['Lecture', '07:00PM - 07:50PM ; W', '05:00PM - 06:00PM ; W']], 
        [['Software Design Lab 222'], ['Laboratory-Discussion', '01:00PM - 01:50PM ; W']], [['System Programming 341'], ['Laboratory-Discussion', '05:00PM - 06:20PM ; R', '12:30PM - 01:50PM ; W', '05:00PM - 06:20PM ; W']], 
        [['Probability & Statistics for Computer Science 361'], ['Discussion/ Recitation', '11:00AM - 11:50AM ; M', '12:00PM - 12:50PM ; M', '01:00PM - 01:50PM ; M', '04:00PM - 04:50PM ; M']], 
        [['Embedded Systems 431'], ['Laboratory', '05:00PM - 06:50PM ; W']], 
        [['Computer Security I 461'], ['Discussion/ Recitation', '12:00PM - 12:50PM ; W', '01:00PM - 01:50PM ; W']], 
        [['Seminar 491'], ['Lecture', '05:15PM - 06:15PM ; M']]];
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
