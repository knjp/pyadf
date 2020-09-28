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

function reloadProg(){	
var progAlgos = `\
order = ${forder.value}
nlen = ${nlength.value}
ensemble = ${ensemble.value}

lms = adflms.LMSalgorithm(order)
lms2 = adflms.LMSalgorithm(order)
nlms = adfnlms.NLMSalgorithm(order)
rls = adfrls.RLSalgorithm(order)

lms.mu = ${mu1.value}
lms._name = "LMS (" + str(lms.mu)  + ")"
lms2.mu = ${mu2.value}
lms2._name = "LMS (" + str(lms2.mu)  + ")"
algos = [nlms, lms, lms2, rls]

unknown = unknownLTV.Unknown(order)
unknown.arcoef = ${arcoef.value}
unknown.snr = ${snr.value} # SNR in dB
unknown.changetime = ${changetime.value} # SNR in dB
`;
	return progAlgos;
}

function writeProg(){
	const fs = require('fs');
	//let text = editarea.value
	let text = reloadProg();
	let prog = progHeader + text + progLast;
	fs.writeFileSync('py/z1.py', prog);
}

btnwrite.addEventListener('click', ()=>{
	writeProg();
});

function openChildWindow(){
	const url = 'edit.html';
	window.open(url, '', 'width=800,height=500')
}

child.addEventListener('click', function(clickEvent) {
	openChildWindow()
})