import html2text
import scholarly
import re

class bookParser:

    # convert html file to text file
    def writeHtmlToText(self, fromFile, toFile):
        with open(fromFile, 'r', encoding="utf8") as inp:
            with open(toFile, 'w', encoding="utf8") as res:
                res.write(html2text.html2text(inp.read()))

    # writing to "sch.txt" file from google scholar
    def scholar(self, book):
        query = scholarly.search_pubs_query(book)
        pub = next(query)
        with open('input/sch.txt', 'a', encoding="utf8") as two:
            for citation in pub.get_citedby():
                two.write(citation.bib['title'] + '\n')

    # writing to "elib.txt" file from elibrary
    def elibrary(self):
        self.writeHtmlToText('input\elibrary.html', 'input\elib.txt')
        with open('input/elib.txt', 'r', encoding="utf8") as inp:
            result = re.findall(r'\[\*\*\s[\s\S]+?\*\*\]', inp.read())
            with open('input/elib.txt', 'w', encoding="utf8") as one:
                for name in result:
                    one.write(name.replace('[** ', "").replace('**]', "").replace('\n', " ") + '\n')

