from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
from pathlib import Path
import getpass

def get_destination_filepath(source_file_path):
    source_file = Path(source_file_path)
    destination_str = str(Path.joinpath(source_file.parent.absolute(), source_file.stem)) + '_enc.pdf'
    return destination_str

def get_password():
    password = ''
    while len(password)==0:
        password = getpass.getpass('Enter password:')
    password_confirmed = ''
    for i in range(3):
        password_confirmed = getpass.getpass('Confirm password:')
        if (password_confirmed == password):
            break
    if ( password != password_confirmed):
        print('Could not confirm password. Exiting')
        return None
    return password

def encrypt_pdf(source_file_str, password):
    source_file = Path(source_file_str)
    if not source_file.exists():
        print("File does not exist:"+str(source_file_str))
        return
    source_pdf = PdfFileReader(source_file_str)
    destination_pdf = PdfFileWriter()
    for page_number in range(source_pdf.numPages):
        destination_pdf.addPage(source_pdf.getPage(pageNumber=page_number))
    destination_pdf.encrypt(password)
    with open(get_destination_filepath(source_file),'wb') as destination_file:
        destination_pdf.write(destination_file)

def routine():
    if len(sys.argv) == 0:
        print('No paths specified. Exiting')
        return
    paths = sys.argv[1:]
    password = get_password()
    if not password:
        return
    for a_path in paths:
        encrypt_pdf(a_path, password)

if __name__ == '__main__':
    routine()
    print('Done')
