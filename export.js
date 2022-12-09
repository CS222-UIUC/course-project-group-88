const spawner = require('child_process').spawn;

const information = 'ur mom';
console.log('Data sent to python script:', information);
  
const python_process = spawner('python', ['./receive.py', information]);

python_process.stdout.on('data', (data) => {
    console.log("finale:", data.toString());
});