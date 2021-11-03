from PyPDF2 import PdfFileWriter, PdfFileReader 

def split_pdf_file(pdf_file_path):
    with open(pdf_file_path, 'rb') as input_pdf_file:
        pdf_file = PdfFileReader(input_pdf_file)
        print(f"File has {pdf_file.getNumPages()} pages.")

        # import pdb
        # pdb.set_trace()
        
        # creating a page object
        pageObj = pdf_file.getPage(0)
        
        # extracting text from page
        page_text = pageObj.extractText()
        with open("page.txt", "w", encoding="utf-8") as out_file:
            out_file.write(page_text)
        print(page_text)


        
    
        


if __name__ == "__main__":
    print("[START PROGRAM]")
    pdf_file_path = "./samples/prd/2A2.pdf"
    split_pdf_file(pdf_file_path)

    print("[END   PROGRAM]")

    # infile = PdfFileReader(open(sys.argv[1], 'rb'))
    # for i in xrange(infile.getNumPages()):
    #     page = infile.getPage(i)
    #     if start_new_file:
    #         outfile = PdfFileWriter()
    #     if page.extractText().find(file_terminator) < 0:
    #         outfile.addPage(page)
    #         start_new_file = False
    #     else:
    #         outfile.addPage(page)
    #         with open('student-%02d.pdf' % profile_number, 'wb') as f:
    #             outfile.write(f)
    #             start_new_file = True
    #             profile_number = profile_number + 1
