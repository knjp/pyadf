const progHeader = `\
from sys import argv
import adfsimulation as asim
import adflms
import adfnlms
import adfrls
import spmisc
import unknownlinear
import unknownLTV
`;

const progLast = `
s = asim.ADFsimulation(order, nlen, algos, unknown, ensemble)
eall = s.simulation()
names =  []
for i in range(len(algos)):
	names.append(algos[i]._name)

b = spmisc.SPmisc()
b.plotMSE(eall, names)
`;

function initProg(){

var progMain = `\
order = ${forder.value}
nlen = ${nlength.value}
ensemble = ${ensemble.value}
lms = adflms.LMSalgorithm(order)
lms.mu = ${mu1.value}
lms._name = "LMS (" + str(lms.mu)  + ")"
lms2 = adflms.LMSalgorithm(order)
lms2.mu = ${mu2.value}
lms2._name = "LMS (" + str(lms2.mu)  + ")"
nlms = adfnlms.NLMSalgorithm(order)
rls = adfrls.RLSalgorithm(order)
algos = [nlms, lms, lms2, rls]

unknown = unknownLTV.Unknown(order)
unknown.arcoef = ${arcoef.value}
unknown.snr = ${snr.value} # SNR in dB
unknown.changetime = ${changetime.value} # SNR in dB
`
	editarea.textContent = progMain;
}

function initProg2(){
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
	let prog = progHeader + text + progLast;
	fs.writeFileSync('py/z1.py', prog);
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
