import PyPDF2
import pyttsx3

# Ask the user to input the path of the PDF file
pdf_path = input("Enter the path of the PDF file: ")

pdfreader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
speaker = pyttsx3.init()

full_text = ""  # Variable to hold the entire text extracted from the PDF

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    full_text += clean_text + " "  # Concatenation of text extracted from each page

print(full_text)

# Ask the user to input the name of the output audio file (without extension)
output_file = input("Enter the name of the output audio file (without extension): ") + ".mp3"
speaker.save_to_file(full_text, output_file)
speaker.runAndWait()

speaker.stop()
