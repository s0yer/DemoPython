# Python 3.7
# 113

from reportlab.pdfgen import canvas
from padawandays import datatypeconversion
from aidfunctions import append_elements


def gen_pdf():
    weekdays_list = {'Monday': '1', 'Tuesday': '1', 'Wednesday': '2', 'Thursday': '3', 'Friday': '5', 'Saturday': '8',
                     'Sunday': '13', 'Holiday': '21'}

    try:
        file_name = input("Type the file name for your pdf archive: ")
        pdf = canvas.Canvas('{}.pdf'.format(file_name))

        x = 610

        for day, fiboNum in weekdays_list.items():
            x -= 21
            pdf.drawString(233, x, '{} : {}'.format(day, fiboNum))
        pdf.setTitle(file_name)
        pdf.setFont("Helvetica-Oblique", 13)
        pdf.drawString(233, 650, 'List day Fibonacci')
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(233, 630, 'Day : Fibo_Number')

        pdf.drawString(233, 397, 'Holiday^2')
        pdf.drawString(233, 377, str(datatypeconversion.datatype_conversion()))

        pdf.save()
        ans = '{}.pdf created !!!'.format(file_name)
        print(ans)

        return append_elements('gen_pdf', weekdays_list, ans)

    except:
        string_error = "Error to generate PDF"
        print(string_error)
        return append_elements('gen_pdf', string_error)
