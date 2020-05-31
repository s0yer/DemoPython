
from reportlab.pdfgen import canvas
from PadawanDays import dataTypeConversion

def genPDF():

    list = {'Monday': '1', 'Tuesday': '1', 'Wednesday': '2', 'Thursday': '3', 'Friday': '5', 'Saturday': '8', 'Sunday': '13', 'Holiday': '21'}
    list_log = ['genPDF']
    try:
        fileName = input("Type the file name for your pdf archive: ")
        pdf = canvas.Canvas('{}.pdf'.format(fileName))

        x = 610

        for day, fiboNum in list.items():
            x -= 21
            pdf.drawString(233,x, '{} : {}'.format(day,fiboNum))
        pdf.setTitle(fileName)
        pdf.setFont("Helvetica-Oblique", 13)
        pdf.drawString(233, 650, 'List day Fibonacci')
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(233, 630, 'Day : Fibo_Number')

        pdf.drawString(233, 397, 'Holiday^2')
        pdf.drawString(233, 377, str(dataTypeConversion.dtConversion()))

        pdf.save()
        print('{}.pdf created !!!'.format(fileName))

        list_log.append(list)
        return list_log

    except:
        string_error = "Error to generate PDF"
        print(string_error)
        return  string_error



