import PyPDF2 
import sys
import os

merger = PyPDF2.PdfWriter()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("CombinedPDF.pdf")

    # Istruzioni: 
    
    # 1) Inserisci i pdf che vuoi unire all'interno della cartella di questo progetto
    
    # 2) Avviare il terminale e attivare l'ambiente virtuale scrivendo: env-merger-pdf/Scripts/activate
    
    # 3) Aprire il terminale e far partire il programma scrivendo python main.py 

    # 4) Il tuo nuovo pdf contenente i due pdf uniti, si trova nella cartella del progetto col nome "CombinedPDF.pdf"
    
    # 5) IMPORTANTE : Ricordati di rimuovere i pdf presenti dalla cartella del progetto una volta finito il merge!!     