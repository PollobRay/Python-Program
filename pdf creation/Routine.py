from fpdf import FPDF



ls = ['lab\nCSE-2823\nVisual Baisc\nSumaya\nAbu Bakkar\nRoom - ICT LAB','2','3','4','CSE - 1015\nDigital\nOmar Farue\n-\nCSE - 7019 B','6','7','8']
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday']

'''
pdf=FPDF('p','mm','A4')
pdf.add_page()
#header
pdf.set_font('times','',13)
pdf.cell(190,16,'DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING',0,0,'C')
pdf.ln(8)
pdf.set_font('times','',13)
pdf.cell(190,16,'Dhaka University of Engineering & Technology, Gazipur',0,0,'C')
pdf.ln(8)
pdf.cell(190,16,'Gazipur-1707, Bangladesh',0,0,'C')
pdf.line(35,40,175,40)
pdf.image('DUET.png',18,16,20,20)
pdf.ln(20)
pdf.set_font('times','',12)
pdf.cell(190,8,'CLASS ROUTINE',0,0,'C')
pdf.ln(8)
pdf.cell(190,8,'2nd Year 2nd Sem B Section',0,0,'C')
pdf.ln(15)
pdf.set_font('times','',7)

#content
#class Time
pdf.cell(20,10,'Day / Time',1,0,'C') #width, height, text, broder, endline, 'align'
pdf.cell(21,10,'8.00 - 8.30',1,0,'C')
pdf.cell(21,10,'8.30 - 9.30',1,0,'C')
pdf.cell(21,10,'9.30 - 10.30',1,0,'C')
pdf.cell(1,10,' ',1,0,'C')  # tea break
pdf.cell(21,10,'10.45 - 11.45',1,0,'C')
pdf.cell(21,10,'11.45 - 12.45',1,0,'C')
pdf.cell(1,10,' ',1,0,'C') # launch break
pdf.cell(21,10,'1.45 - 2.45',1,0,'C')
pdf.cell(21,10,'2.45 - 3.45',1,0,'C')
pdf.cell(21,10,'3.45 - 4.30',1,0,'C')
pdf.cell(0,10,'',0,1) #dummy


for i in range(5):
    pdf.cell(20, 30, day[i], 1, 0, 'C')  # width, height, text, broder, endline, 'align'

    j=0
    counter = 0
    while j<10:

        x = pdf.get_x()
        y = pdf.get_y()
        u = int(1)
        if j==3 or j==6:
            pdf.cell(1,30,'',1,0,'C')
            j = j+1
            continue
        courseDtl = ls[counter].count('\n') + 1
        if courseDtl == 6:
            pdf.multi_cell(21*3, 5, ls[counter],1, 'C')
            u = int(3)

        elif courseDtl == 5:
            pdf.multi_cell(21, 6, ls[counter], 1, 'C')

        else:
            pdf.cell(21,30,' - '+str(j),1,0,'C')
        #move to position
        pdf.set_xy(x+21*u,y) #20 for day + 10 for left margin width
        j = j + u
        counter = counter + 1

    pdf.cell(0, 30, '', 0, 1)  #  for line break
pdf.ln(30)


#signature line of course coordinator sir & head sir
y = pdf.get_y()
dotLine = '------------------------------'
courseC = 'Course Coordinator'
head = 'Head'
CourseCoordinatorSir = 'Dr. Md. Jakirul Islam, Assistant Professor, Dept of CSE'
HeadSir = 'Prof. Dr. Md. Obaidur Rahman, Dept of CSE'
pdf.cell(60,4,dotLine,0,0,'C')
pdf.set_xy(140,y)
pdf.cell(60,4,dotLine,0,0,'C')
pdf.ln(4)
pdf.set_font('times','B',7)
pdf.cell(60,6,courseC,0,0,'C')
pdf.set_xy(140,y+4)
pdf.cell(60,6,head,0,0,'C')
pdf.ln(6)
pdf.set_font('times','',7)
pdf.cell(60,6,CourseCoordinatorSir,0,0,'C')
pdf.set_xy(140,y+4+6)
pdf.cell(60,6,HeadSir,0,0,'C')


pdf.output("table.pdf")
'''
 #landscape
pdf=FPDF('l','mm','A3')
pdf.add_page()
#header
pdf.set_font('times','',20)
pdf.cell(400,16,'DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING',0,0,'C')
pdf.ln(10)
pdf.set_font('times','',20)
pdf.cell(400,16,'Dhaka University of Engineering & Technology, Gazipur',0,0,'C')
pdf.ln(10)
pdf.cell(400,16,'Gazipur-1707, Bangladesh',0,0,'C')
pdf.line(120,48,300,48)
pdf.image('DUET.png',80,18,20,20)
pdf.ln(20)
pdf.set_font('times','',16)
pdf.cell(400,8,'CLASS ROUTINE',0,0,'C')
pdf.ln(8)
pdf.cell(400,8,'2nd Year 2nd Sem B Section',0,0,'C')
pdf.ln(15)
pdf.set_font('times','',10)


#content
#class Time
pdf.cell(20,10,'Day / Time',1,0,'C') #width, height, text, broder, endline, 'align'
pdf.cell(47,10,'8.00 - 8.30',1,0,'C')
pdf.cell(47,10,'8.30 - 9.30',1,0,'C')
pdf.cell(47,10,'9.30 - 10.30',1,0,'C')
pdf.cell(2,10,' ',1,0,'C')  # tea break
pdf.cell(47,10,'10.45 - 11.45',1,0,'C')
pdf.cell(47,10,'11.45 - 12.45',1,0,'C')
pdf.cell(2,10,' ',1,0,'C') # launch break
pdf.cell(47,10,'1.45 - 2.45',1,0,'C')
pdf.cell(47,10,'2.45 - 3.45',1,0,'C')
pdf.cell(47,10,'3.45 - 4.30',1,0,'C')
pdf.cell(0,10,'',0,1) #dummy


for i in range(5):
    pdf.cell(20, 30, day[i], 1, 0, 'C')  # width, height, text, broder, endline, 'align'

    j=0
    counter = 0
    while j<10:

        x = pdf.get_x()
        y = pdf.get_y()
        u = int(1)
        if j==3 or j==6:
            pdf.cell(2,30,'',1,0,'C')
            j = j+1
            continue
        courseDtl = ls[counter].count('\n') + 1
        if courseDtl == 6:
            pdf.multi_cell(47*3, 5, ls[counter],1, 'C')
            u = int(3)

        elif courseDtl == 5:
            pdf.multi_cell(47, 6, ls[counter], 1, 'C')

        else:
            pdf.cell(47,30,'Prof. Dr. Md. Obaidur Rahman',1,0,'C')
        #move to position
        pdf.set_xy(x+47*u,y) #20 for day + 10 for left margin width
        j = j + u
        counter = counter + 1

    pdf.cell(0, 30, '', 0, 1)  #  for line break
pdf.ln(29)


#signature line of course coordinator sir & head sir
pdf.set_font('times','',15)
y = pdf.get_y()
dotLine = '------------------------------'
courseC = 'Course Coordinator'
head = 'Head'
CourseCoordinatorSir = 'Dr. Md. Jakirul Islam, Assistant Professor, Dept of CSE'
HeadSir = 'Prof. Dr. Md. Obaidur Rahman, Dept of CSE'
pdf.set_xy(80,y)
pdf.cell(80,4,dotLine,0,0,'C')
pdf.set_xy(260,y)
pdf.cell(80,4,dotLine,0,0,'C')
pdf.ln(3)
pdf.set_font('times','B',15)
pdf.set_xy(80,y+3)
pdf.cell(80,6,courseC,0,0,'C')
pdf.set_xy(260,y+3)
pdf.cell(80,6,head,0,0,'C')
pdf.ln(5)
pdf.set_font('times','',15)
pdf.set_xy(70,y+3+6)
pdf.cell(100,6,CourseCoordinatorSir,0,0,'C')
pdf.set_xy(238,y+3+6)
pdf.cell(120,6,HeadSir,0,0,'C')


pdf.output("table.pdf")
