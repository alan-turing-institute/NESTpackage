

class baseRenderer:
    def __init__(self):
        Exception('Not implemented')

    def addSectionPage(self, text):
        """ Add a section page to the document in question.

        :param text: Title of the section
        """
        Exception('Not implemented')

    def __makeFrontPage__(self):
        Exception('Not implemented')

    def addHeading(self,level,text):
        """ Add a header to the document in question.

        :param level: Header Level
        :param text: Title of the Header
        """
        Exception('Not implemented')

    def addText(self,text):
        """ Add text to the document in question.

        :param text: Text to be added
        """
        Exception('Not implemented')

    def addTable(self,table):
        """ Add table to the document in question.

        :param table: Table to be added
        """
        Exception('Not implemented')

    def addPlot(self,figureHandle):
        """ Add figure to the document in question.

        :param figureHandle: Matplotlib figure handle to add to the document
        """
        Exception('Not implemented')

    def addImage(self,imagePath,caption):
        """ Add image to the document in question.

        :param imagePath: Path to the image in question
        :param caption: Image Caption
        """
        Exception('Not implemented')

    def addPageBreak(self):
        """ Add page break to the document in question.
        """
        Exception('Not implemented')

    def addTableFromDict(self,data):
        """ Add a table from a dictionary structure
        """
        Exception('Not implemented')

    def render(self):
        """ Save the document to disk.
        """
        Exception('Not implemented')

