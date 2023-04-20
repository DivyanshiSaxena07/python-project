from pdfquery import PDFQuery

pdf = PDFQuery('../Python-Durga-Notes.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
# text = [t.text for t in text_elements]

print(text_elements)