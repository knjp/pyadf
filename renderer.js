
var {PythonShell} = require('python-shell');

function testPython(){
	let options = {
		mode: 'text',
		pythonOptions: ['-u'],
		args: [input.value]
	}
	PythonShell.run('py/sptest3.py', options, function(err, pyresult){
		if(err) throw err;
		tarea.textContent = pyresult
	})
}


function sendToPython(){
	var python = require('child_process').spawn('python', ['./py/sptest3.py', input.value]);
	result.textContent = ""
	python.stdout.on('data', function(data){
		console.log("Python response: ", data.toString('utf8'));
		result.textContent = data.toString('utf8');
	});

	python.stderr.on('data', (data) => {
		console.error(`stderr: ${data}`);
	});

	python.on('close', (code)=>{
		console.log(`child process exited with code ${code}`);
	});
}

btn.addEventListener('click', ()=>{
	//sendToPython();
	testPython()
	//tp()
});

btn.dispatchEvent(new Event('click'));


