from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

output_string = StringIO()


with open('C:\\Users\\JoshEarly\\Desktop\\PagesfromDec.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(),
    output_type='html', codec=None)