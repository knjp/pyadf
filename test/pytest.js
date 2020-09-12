let {PythonShell} = require('python-shell')

//import {PythonShell} from 'python-shell';

PythonShell.defaultOptions = { pythonOptions: ['-u'] };
let pyshell = new PythonShell('t1.py');
 
// sends a message to the Python script via stdin
pyshell.send('John');
 
pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});
 
// end the input stream and allow the process to exit
pyshell.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
});