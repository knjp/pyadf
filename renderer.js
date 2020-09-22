
var {PythonShell} = require('python-shell');
PythonShell.defaultOptions = { pythonOptions: ['-u'] };


function pytest(){
	let options = {
		puthonOptions: ['-u'],
		args: [input.value]
	}
	let pyshell = new PythonShell('./py/z1.py', options);
 
	// sends a message to the Python script via stdin
	pyshell.send('John');
	pyshell.on('message', function (message) {
	  // received a message sent from the Python script (a simple "print" statement)
	  console.log(message);
	  tt = tarea.value;
	  tarea.textContent = tt + message + '\n';
	  tarea.scrollTop = tarea.scrollHeight;
	})

	pyshell.end(function (err,code,signal) {
		if (err) throw err;
		ss = ('The exit code was: ' + code + '\n');
		ss = ss + ('The exit signal was: ' + signal + '\n');
		ss = ss + ('finished');
		tt = tarea.value;
		tarea.textContent = tt + ss + '\n'
	  	tarea.scrollTop = tarea.scrollHeight;
	});
}

btn.addEventListener('click', ()=>{
	tarea.textContent = '';
	pytest();
});

//btn.dispatchEvent(new Event('click'));

quit.addEventListener('click', function(clickEvent) {
	window.close()
})


function openChildWindow(){
	const url = 'edit.html';
	window.open(url, '', 'width=800,height=800')
}

child.addEventListener('click', function(clickEvent) {
	openChildWindow()
})