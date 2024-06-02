# import sys
# sys.path.append("D:/Automation Testing/Selenium-Python---First-Project/Library")
# from Lib_Excel import LibExcel
# from datetime import datetime
# import os
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.colors import Color, PCMYKColor, DeviceGray
# from reportlab.platypus import Image, Paragraph
# from reportlab.lib.units import inch

# class LibPDF:
#     document = None
#     pdf = None
#     fontColor = None
#     fontColor2 = None
#     fontColor3 = None
#     fontColor4 = None
#     transparentColor = None
#     pageSize = None
#     tempProjectDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     projectDir = tempProjectDir.replace("\\", "/")
#     globalExcelFilePath = projectDir + "/File Excel/Global_Report.xlsx"
#     tableOfContent = []
#     startEndDate = []
#     verticalPosition = None
#     centerX = None
#     marginLeftRight = None
#     marginTop = None
#     red = 49
#     green = 132
#     blue = 155
#     red2 = 227
#     green2 = 108
#     blue2 = 10
#     red3 = 146
#     green3 = 205
#     blue3 = 220

#     @staticmethod
#     def InitializeDocument(excelPath, excelSheet):
#         # LibPDF.tempProjectDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#         # LibPDF.projectDir = LibPDF.tempProjectDir.replace("\\", "/")
#         # LibPDF.globalExcelFilePath = LibPDF.projectDir + "/File Excel/Global_Report.xlsx"
        
#         reportDir = os.path.join(LibPDF.tempProjectDir, "Report")
#         todayReportDir = os.path.join(reportDir, datetime.now().strftime("%Y%m%d"))
#         mainDir = todayReportDir.replace("\\", "/")

#         if not os.path.exists(reportDir):
#             os.makedirs(reportDir)

#         if not os.path.exists(todayReportDir):
#             os.makedirs(todayReportDir)

#         pdfPath = mainDir + "/" + LibExcel.getDataExcel(excelPath, "TC_ID", excelSheet) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"

#         LibPDF.document = Canvas(pdfPath, pagesize=A4)
#         LibPDF.page_size = A4
#         LibPDF.margin_left_right = 70
#         LibPDF.margin_top = 130
#         LibPDF.vertical_position = A4[1] - LibPDF.margin_top
#         LibPDF.font_color = Color(46/255, 132/255, 155/255)  # Biru
#         LibPDF.font_color2 = Color(227/255, 108/255, 10/255)  # Orange
#         LibPDF.font_color3 = Color(146/255, 205/255, 220/255)  # Biru Muda
#         LibPDF.font_color4 = Color(0, 128/255, 0)  # Green
#         LibPDF.transparent_color = PCMYKColor(0, 0, 0, 0)  # Transparent Color
#         LibPDF.center_x = A4[0] / 2


#     def CreateCover():
#         pageSize = A4
#         LibPDF.startEndDate.append(datetime.now().strftime("%d %b %Y %H:%M:%S"))  # start testing date
#         centerY = (pageSize[1] / 2) + 90

#         headerText = LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "COVER_TITLE", "Global")
#         headerText2 = LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "COVER_SUBTITLE", "Global")
#         headerText3 = LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "PROJECT_CODE", "Global")
#         headerText4 = LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "HEADER_DESCRIPTION", "Global")
#         headerText5 = "Prepared By " + LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "AUTHOR", "Global")
#         headerText6 = datetime.now().strftime("%Y-%m-%d")
#         headerText7 = "COPYRIGHT NOTICE"
#         headerText8 = "Copyright " + datetime.now().strftime("%Y") + " by " + LibExcel.getDataExcel(LibPDF.globalExcelFilePath, "CREATOR", "Global")

#         logo = Image(LibPDF.projectDir + "/Assets/MainImage.jpg", width=75, height=50)
#         logo.drawWidth = 75
#         logo.drawHeight = 50
#         logo.hAlign = 'LEFT'
#         logo.vAlign = 'BOTTOM'
#         logo.wrapOn(pdf, pageSize[0], pageSize[1])
#         logo.drawOn(pdf, marginLeftRight, centerY - 330)

#         header = formatted_paragraph(headerText, fontColor, 'RIGHT', 34, centerX, centerY, True)
#         header2 = formatted_paragraph(headerText2, fontColor2, 'RIGHT', 22, centerX - 25, centerY - 25, True)
#         header3 = formatted_paragraph(headerText3, Color(0, 0, 0), 'RIGHT', 20, centerX - 50, centerY - 50)
#         header4 = formatted_paragraph(headerText4, Color(0, 0, 0), 'LEFT', 18, marginLeftRight, centerY - 250)
#         header5 = formatted_paragraph(headerText5, Color(0, 0, 0), 'LEFT', 12, marginLeftRight, centerY - 265)
#         header6 = formatted_paragraph(headerText6, Color(0, 0, 0), 'LEFT', 11, marginLeftRight, centerY - 280)
#         header7 = formatted_paragraph(headerText7, Color(0.5, 0.5, 0.5), 'LEFT', 11, marginLeftRight, centerY - 350)
#         header8 = formatted_paragraph(headerText8, Color(0.5, 0.5, 0.5), 'LEFT', 10, marginLeftRight, centerY - 365, True)

#         document.drawRightString(pageSize[0] - inch, pageSize[1] - inch / 2, startEndDate[0])
#         document.drawRightString(pageSize[0] - inch, inch / 2, startEndDate[1])

#         document.add(header)
#         document.add(header2)
#         document.add(header3)
#         document.add(header4)
#         document.add(header5)
#         document.add(header6)
#         document.add(logo)
#         document.add(header7)
#         document.add(header8)

#     # Format Paragraf untuk Header
#     def formatted_paragraph(text, font_color, alignment, font_size, position_x, position_y, bold=False):
#         paragraph = Paragraph(text, textColor=font_color, alignment=alignment, fontSize=font_size)

#         if bold:
#             paragraph.style.bold = True

#         paragraph.wrapOn(pdf, pageSize[0], pageSize[1])
#         paragraph.drawOn(pdf, position_x, position_y)

#         return paragraph
