const initprog = `\
from sys import argv
import adfsimulation as asim
import adflms
import adfnlms
import adfrls
import spmisc
import unknownlinear
import unknownLTV

if len(argv) == 2 or len(argv) == 3:
	arg = argv[1]
else:
	arg = 2

if len(argv) == 3:
	arcoef = float(argv[2])
else:
	arcoef = 0.8

order = 131
nlen = 2000
ensemble = int(arg)
lms = adflms.LMSalgorithm(order)
lms.mu = 0.001
lms._name = "LMS (" + str(lms.mu)  + ")"
lms2 = adflms.LMSalgorithm(order)
lms2.mu = 0.005
lms2._name = "LMS (" + str(lms2.mu)  + ")"
nlms = adfnlms.NLMSalgorithm(order)
rls = adfrls.RLSalgorithm(order)

algos = [nlms, lms, lms2, rls]
unknown = unknownLTV.Unknown(order)
unknown.arcoef = arcoef
unknown.snr = 30 # SNR in dB
unknown.changetime = 2500 # SNR in dB
s = asim.ADFsimulation(order, nlen, algos, unknown, ensemble)
eall = s.simulation()

names =  []
for i in range(len(algos)):
	names.append(algos[i]._name)

b = spmisc.SPmisc()
b.plotMSE(eall, names)
`;

function initProg(){
	editarea.textContent = initprog;
}

function readProg(){
	const fs = require('fs');
	let text = fs.readFileSync("py/sptest3.py");
	editarea.textContent = text;
}

function writeProg(){
	const fs = require('fs');
	let text = editarea.value
	fs.writeFileSync('py/z1.py', text);
}

btnedit.addEventListener('click', ()=>{
	initProg();
});

btnwrite.addEventListener('click', ()=>{
	writeProg();
});

btnclose.addEventListener('click', function(clickEvent) {
	window.close()
})

function openChildWindow(){
	const url = 'edit.html';
	window.open(url, '', 'width=800,height=500')
}

child.addEventListener('click', function(clickEvent) {
	openChildWindow()
})
