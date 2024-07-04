from fpdf import FPDF

pdf=FPDF('p','mm','A4')
pdf.add_page()
pdf.set_font('times','',12)

pdf.cell(20,10,'Id',1,0,'C') #width, height, text, broder, endline, 'align'
pdf.cell(50,10,'Name',1,0,'C')
pdf.cell(100,5,'Score',1,0,'C')
pdf.cell(20,10,'passing',1,0,'C')
pdf.cell(0,5,'',0,1) #dummy

pdf.cell(70,5,'',0,0) #dummy
pdf.cell(25,5,'q1',1,0,'C')
pdf.cell(25,5,'q2',1,0,'C')
pdf.cell(25,5,'q3',1,0,'C')
pdf.cell(25,5,'q4',1,0,'C')
pdf.cell(20,5,'',0,0)#dummy
pdf.cell(0,5,'',0,1)#dummy for break

pdf.cell(20,5,'194109',1,0,'C')
pdf.cell(50,5,'Pollob Chandra Ray',1,0,'C')
pdf.cell(25,5,'10',1,0,'C')
pdf.cell(25,5,'20',1,0,'C')
pdf.cell(25,5,'30',1,0,'C')
pdf.cell(25,5,'40',1,0,'C')
pdf.cell(20,5,'100',1,0,'C')
pdf.cell(0,5,'',0,1)


pdf.output("table.pdf")
