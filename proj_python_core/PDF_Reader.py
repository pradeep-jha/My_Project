import pdfplumber
input_path="C:\\Users\\pradeep\\Desktop\Pycharm_PDFreader\\input\\REFUND RULES wef 12-Nov-15.pdf"

with pdfplumber.open(input_path) as pdf:
    print(len(pdf.pages))
    with open("C:\\Users\\pradeep\\Desktop\Pycharm_PDFreader\\input\\output.text", "w+") as f:
        for page in pdf.pages:
            #pages=pdf.pages[page]
            text=page.extract_text()

            f.write(text)
            #tables=page.extract_tables()
            #print(tables)
            for lines in text.split('\n'):
                if 'refund'.lower() in lines.lower():
                  print(lines)


