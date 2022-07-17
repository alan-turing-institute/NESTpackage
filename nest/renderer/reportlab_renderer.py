import os
from pathlib import Path
from nest.renderer import base_renderer
from reportlab.lib import styles, utils
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate
from reportlab.platypus import Table, Spacer, TableStyle
import importlib.util
import datetime
from io import BytesIO
from matplotlib import pylab

# from
# https://stackoverflow.com/questions/5327670/image-aspect-ratio-using-reportlab-in-python
def __get_image__(path, width=1*cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))


class reportlabRenderer(base_renderer.baseRenderer):
    def __init__(self,filename,name,options):
        self.name = name
        self.filename = name
        self.options = options
        self.my_doc = SimpleDocTemplate(filename + ".pdf")
        self.flowables = []
        self.style = getSampleStyleSheet()
        self.__makeFrontPage__()

    def __makeFrontPage__(self):

        # make a local reference to avoid having self
        # on every line
        flowables = self.flowables

        titlePageStyle = ParagraphStyle(
            name='titlePageStyle',
            fontSize=40,
            spaceAfter=40,
            alignment=styles.TA_CENTER
        )
        flowables.append(Spacer(7*cm, 7*cm))
        title = Paragraph('Network Statistic Report', titlePageStyle)
        flowables.append(title)
        title = Paragraph(self.name, titlePageStyle)
        flowables.append(title)
        flowables.append(Spacer(1*cm, 1*cm))
        p1 = Path(__file__)
        logopath = os.path.join(os.path.dirname(p1),"logo.png")
        flowables.append(__get_image__(logopath, width=6*cm))
        if importlib.util.find_spec('git'):
            import git
            repo = git.Repo(search_parent_directories=True)
            sha = repo.head.object.hexsha
            flowables.append(Spacer(1*cm, 1*cm))
            date = str(datetime.date.today())
            dateTxt = Paragraph('Date: ' + date, self.style['Heading2'])
            txt = 'Code Version: '
            txt += sha[:15]
            txt += '(Clean='
            txt += str(not repo.is_dirty())
            txt += ')'
            codeVerTxt = Paragraph(txt, self.style['Heading2'])
            flowables.append(dateTxt)
            if 'version' in self.options:
                versionTxt = Paragraph('Version: ' + str(self.options['version']),
                                    self.style['Heading2'])
                flowables.append(versionTxt)
            flowables.append(codeVerTxt)
        else:
            print('gitpython not found')
            flowables.append(Spacer(3*cm, 3*cm))
            date = str(datetime.date.today())
            dateTxt = Paragraph('Date: ' + date, self.style['Heading2'])
            flowables.append(dateTxt)
            if 'version' in self.options:
                versionTxt = Paragraph('Version: ' + str(self.options['version']),
                                    self.style['Heading2'])
                flowables.append(versionTxt)

        flowables.append(PageBreak())


    def addSectionPage(self, text):
        statText = Paragraph(text, self.style['title'])
        self.flowables.append(statText)

    def addHeading(self,level,text):
        if level==1:
            s1 = self.style['Heading1']
        elif level==2:
            s1 = self.style['Heading2']
        elif level==3:
            s1 = self.style['Heading3']
        else:
            Exception('Level not defined')
        text = Paragraph(text, s1)
        self.flowables.append(text)

    def addText(self,text):
        statText = Paragraph(text, self.style['Heading4'])
        self.flowables.append(statText)

    def addTable(self,text):
        t1 = Table(text)
        self.flowables.append(t1)

    def addTableFromDict(self, data, options={}):
        l1 = [['Statistics', ]]+list(data.items())
        t = Table(l1)
        # https://pairlist2.pair.net/pipermail/reportlab-users/2012-February/010385.html
        t.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, 1), 14),
            ('FONTSIZE', (0, 1), (-1, len(l1)+1), 14),
            ('FONTSIZE', (0, 2), (-1, len(l1)+1), 14),
            ('TEXTFONT', (0, 0), (-1, len(l1)+1), 'Times-Bold'),
            ('TEXTFONT', (0, 1), (-1, len(l1)+1), 'Times-Bold'),
            ('RIGHTPADDING', (2, 2), (-1, -1), 20), ]))
        self.flowables.append(t)

    def addPlot(self,figureHandle):
        fakeFile = BytesIO()
        figureHandle.savefig(fakeFile, format='tiff',bbox_inches='tight')
        pylab.close('all')
        t = Image(fakeFile)
        self.flowables.append(t)

    def addPageBreak(self):
        self.flowables.append(PageBreak())

    def render(self):
        self.my_doc.build(self.flowables)

