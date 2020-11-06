import os
import tkinter as tk
from tkinter import filedialog

from PyPDF4 import PdfFileReader

root = tk.Tk()
root.withdraw()

filenames = filedialog.askopenfilenames(
                                        initialdir= os.getcwd(),
                                        title= "Please select pdfs to be sized",
                                        filetypes=[("PDFs", "*.pdf")]
)

with open(os.path.join(os.getcwd(), "PDF sizes.txt"), "+w") as out:
    for filename in filenames:
        fileparts=os.path.splitext(filename.lower())
        if fileparts[1] == ".pdf":
            if os.path.exists(filename):
                with open(filename, 'rb') as fl:
                    reader=PdfFileReader(fl)
                    print(filename+":   "+str(reader.getNumPages()), file=out)

