'''
Phan tich xml voi sax api
'''

import xml.sax

class StudentHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ''
        self.ids         = ''
        self.name        = ''
        self.date        = ''

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'student':
            print('==== Student ====')
            ids = attributes['id']
            print('ID:', ids)

    def endElement(self, tag):
        if self.CurrentData == 'id':
            print('ID:', self.ids)
        elif self.CurrentData == 'name':
            print('Name:', self.name)
        elif self.CurrentData == 'date':
            print('Date:', self.date)
        self.CurrentData = ''

    def characters(self, content):
        if self.CurrentData == 'id':
            self.id = content
        elif self.CurrentData == 'name':
            self.name = content
        elif self.CurrentData == 'date':
            self.date = content

if __name__ == '__main__':
    
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = StudentHandler()
    parser.setContentHandler(Handler)
    parser.parse('student.xml')
    
    

