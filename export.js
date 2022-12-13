const spawner = require('child_process').spawn;

const information = 'ur mom';
console.log('Data sent to python script:', information);
  
const python_process = spawner('python', ['./receive.py', information]); //sends information (a string) to python file "receive.py"

python_process.stdout.on('data', (data) => { //reads the python output
    console.log("finale:", data.toString());
});