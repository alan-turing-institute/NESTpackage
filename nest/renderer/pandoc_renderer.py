import os
from pathlib import Path
from nest.renderer import base_renderer
import importlib.util
import datetime
import random as rd


import pandoc
from pandoc.types import Header, Image, Str, HorizontalRule
from pandoc.types import Para, Pandoc, Meta, RawBlock, Format

def getPara(text):
    return Para([Str(text)])


def tableConverter(listoflists,full=False):
    titl1 =listoflists[0]
    row0 = ' | '.join(str(x) for x in titl1)
    headRow = ''.join(x if x=='|' else "-" for x in row0)
    restOfTab = '\n'.join(' | '.join(str(x) for x in item) for item in listoflists[1:])
    q1 = row0 + "\n" +headRow +"\n" + restOfTab
    q2 = pandoc.read(q1)
    if full:
        return q2
    else:
        return q2[1][0]

def plotWrapper(figure,caption="",fileT = ".png"):
    lc1 = [chr(97+i) for i in range(26)]
    name1 = ''.join(rd.choice(lc1) for x in range(8)) + fileT
    figure.savefig('tempImages/'+name1, format='png',bbox_inches='tight')
    from pandoc.types import Str
    from pandoc.types import Para
    return Para([Image(('', [], []), [Str(caption),], ('tempImages/'+name1, 'fig:'))])

class pandocPdf(base_renderer.baseRenderer):
    def __init__(self,filename,name,options):
        self.name = name
        self.filename = filename
        self.options = options
        self.flowables = []
        self.__makeFrontPage__()
        self.imageT = ".pdf"
        self.headings = []

    def __makeFrontPage__(self):
        # make a local reference to avoid having self
        # on every line

        title = 'Network Statistic Report'
        self.addHeading(1,title)
        self.addHeading(2,self.name)

        p1 = Path(__file__)
        logopath = os.path.join(os.path.dirname(p1),"logo.png")
        self.addImage(logopath,"")
        if importlib.util.find_spec('git'):
            import git
            repo = git.Repo(search_parent_directories=True)
            sha = repo.head.object.hexsha
            date = str(datetime.date.today())
            dateTxt = 'Date: ' + date
            txt = 'Code Version: '
            txt += sha[:15]
            txt += '(Clean='
            txt += str(not repo.is_dirty())
            txt += ')'
            self.addText(dateTxt)
            if 'version' in self.options:
                versionTxt = 'Version: ' + str(self.options['version'])
                self.addText(versionTxt)
            self.addText(txt)
        else:
            date = str(datetime.date.today())
            dateTxt = 'Date: ' + date
            self.addText(dateTxt)
            if 'version' in self.options:
                versionTxt = 'Version: ' + str(self.options['version'])
                self.addText(versionTxt)


    def addSectionPage(self, title):
        statText = Header(1, (title, [], []), [Str(title)])
        self.headings.append([1,title])
        self.flowables.append(statText)

    def addHeading(self,level,text):
        statText = Header(level, (text, [], []), [Str(text)])
        self.headings.append([level,text])
        self.flowables.append(statText)

    def addText(self,text):
        statText = getPara(text)
        self.flowables.append(statText)

    def addTable(self,text):
        t1 = tableConverter(text)
        self.flowables.append(t1)

    def addTableFromDict(self, data, options={}):
        l1 = [['Statistics', ""]]+sorted(list(data.items()))
        t = tableConverter(l1)
        self.flowables.append(t)

    def addPlot(self,figureHandle):
        t = plotWrapper(figureHandle)
        self.flowables.append(t)

    def addImage(self,imagePath,caption=""):
        t = Para([Image(('', [], []), [Str(caption),], (imagePath, 'fig:'))])
        self.flowables.append(t)

    def addImageWidth(self,imagePath,width,caption=""):
        t = Para([Image(('', [], [('width',str(width))]), [Str(caption),], (imagePath, 'fig:'))])
        self.flowables.append(t)

    def addPageBreak(self):
        self.flowables.append(HorizontalRule())

    def render(self):
        print('sdfsdf124')
        pandoc.write(Pandoc(Meta({}),self.flowables),self.filename+".pdf")

def makeSidebar(headings):
    p1 = Path(__file__)
    imagePath = os.path.join(os.path.dirname(p1),"logo.png")
    block2 = Para([Image(('', [], [('width',str(250))]), [Str(""),],
                    (imagePath, 'fig:'))])
    htmlstart = '<div class="sidenav"><ul>'

    block1 = RawBlock(Format("html"),'<div class="sidenav">')
    htmlstart = '<ul>'
    htmlend = '</ul></div>'
    lines = []
    curLevel = 1
    for heading in headings:
        if not heading[1].startswith("Section "):
            continue
        if heading[0]>=3:
            continue
        line1 = ""
        while heading[0]>curLevel:
            line1 +="<ul>"
            curLevel +=1
        while heading[0]<curLevel:
            line1 +="</ul>"
            curLevel -= 1
        line1 += '<li><a href="'
        line1 += '#'
        line1 += heading[1]
        line1 += '" id=toc-"'
        line1 += heading[1]
        line1 += '">'
        if heading[1].startswith("Section "):
            line1 += ' '.join(heading[1].split(' ')[2:])
        else:
            line1 += heading[1]
        line1 += '</a></li>'
        lines.append(line1)
    fullhtml =  htmlstart + '\n'.join(lines) + htmlend
    block3 = RawBlock(Format("html"),fullhtml)
    return [block1,block2,block3]



class pandocHTML(pandocPdf):
    def __init__(self,filename,name,options):
        self.headings = []
        self.name = name
        self.filename = filename
        self.options = options
        self.flowables = []
        self.__makeFrontPage__()
        self.imageT = ".svg"

    def __makeFrontPage__(self):
        # make a local reference to avoid having self
        # on every line

        title = 'Network Statistic Report'
        self.addHeading(1,title+": "+self.name)

        if importlib.util.find_spec('git'):
            import git
            repo = git.Repo(search_parent_directories=True)
            sha = repo.head.object.hexsha
            date = str(datetime.date.today())
            dateTxt = 'Date: ' + date
            txt = 'Code Version: '
            txt += sha[:15]
            txt += '(Clean='
            txt += str(not repo.is_dirty())
            txt += ')'
            self.addText(dateTxt)
            if 'version' in self.options:
                versionTxt = 'Version: ' + str(self.options['version'])
                self.addText(versionTxt)
            self.addText(txt)
        else:
            date = str(datetime.date.today())
            dateTxt = 'Date: ' + date
            self.addText(dateTxt)
            if 'version' in self.options:
                versionTxt = 'Version: ' + str(self.options['version'])
                self.addText(versionTxt)


    def render(self):
        print('sdfsdf123')
        p1 = Path(__file__)
        temp = os.path.join(os.path.dirname(p1),"standard.css")
        temp = str(temp)

        sidebarhtml = makeSidebar(self.headings)
        self.flowables = sidebarhtml + self.flowables
#        pandocSidebar = RawBlock(Format("html"),sidebarhtml)
#        self.flowables.insert(0,pandocSidebar)
        pandoc.write(Pandoc(Meta({}),self.flowables), self.filename+".html",
                     format="html", options=["--standalone",
                                             "--self-contained", "-V",
                                             "lang=en","--css",temp])

#        -c pandoc.css
