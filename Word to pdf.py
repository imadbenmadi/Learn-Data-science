import os
import win32com.client  # Windows Only

def convert_docx_to_pdf(directory):
    word_app = win32com.client.Dispatch("Word.Application")
    word_app.Visible = False
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".docx") and not file.startswith("~"):  # Ignore temporary Word files
                docx_path = os.path.join(root, file)
                pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
                
                doc = word_app.Documents.Open(docx_path)
                doc.SaveAs(pdf_path, FileFormat=17)  # 17 is the PDF format code
                doc.Close()
                print(f"Converted: {docx_path} -> {pdf_path}")
    
    word_app.Quit()

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    convert_docx_to_pdf(directory)
    print("Conversion completed.")
