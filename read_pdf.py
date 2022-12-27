from PyPDF2 import PdfReader

reader = PdfReader('resources/docs-pytest-org-en-latest.pdf')
print(len(reader.pages))
page = reader.pages[0]
text = page.extract_text()
print(text)
assert 'Jul 14' in text
