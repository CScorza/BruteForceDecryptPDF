import PyPDF2
import hashlib
import time
from datetime import datetime

def calculate_hash(data, hash_type="sha256"):
    hash_object = hashlib.new(hash_type)
    hash_object.update(data)
    return hash_object.hexdigest()

def brute_force_pdf(pdf_path, wordlist_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)

    if not pdf_reader.is_encrypted:
        print("Il file PDF non è protetto da password.")
        return

    wordlist = open(wordlist_path, "r", encoding="utf-8")
    total_words = sum(1 for _ in wordlist)  # Calcola il numero totale di parole nella wordlist
    wordlist.seek(0)  # Torna all'inizio della wordlist

    count = 0
    start_time = time.time()

    # Decrittazione del file PDF
    pdf_reader.decrypt("")

    # Calcola l'hash del documento PDF
    with open(pdf_path, "rb") as file:
        document_data = file.read()
        document_hash = calculate_hash(document_data)

    print("\nBruteForceDecryptPDF")
    print("HackingPDF la decodifica dei documenti PDF protetti da Password")
    print()


    print("CScorza - Investigazioni Telematiche")
    print("Link Telegram: https://t.me/+kP_uYlc6-345Njc8")
    print("Link GitHub: https://github.com/CScorza")
    print("Link Sito Web: https://cscorza.github.io/CScorza/")
    print()

    for password in wordlist:
        count += 1
        password = password.strip().encode("utf-8")

        if pdf_reader.decrypt(password):
            end_time = time.time()
            password_str = password.decode('utf-8')
            password_hash = hashlib.sha256(password).hexdigest()

            print(f"Password trovata: {password_str}")
            print(f"Tipo di hash per la password: SHA256")
            print(f"Hash della password: {password_hash}")

            print(f"Tipo di hash per il documento ({pdf_path}): SHA256")
            print(f"Hash del documento: {document_hash}")

            print(f"Tempo trascorso: {end_time - start_time:.2f} secondi")
            break

        print(f"Progresso: {count}/{total_words} parole - Tempo trascorso: {time.time() - start_time:.2f} secondi", end="\r", flush=True)

    wordlist.close()

    # Calcola e stampa i metadati del documento
    metadata = pdf_reader.metadata
    print("\nMetadati del documento:")
    print(f"Titolo: {metadata.get('/Title')}")
    creation_date = metadata.get('/CreationDate')
    if creation_date:
        creation_date = datetime.strptime(creation_date[2:10], "%Y%m%d").strftime("%d %B %Y")
        print(f"Data di creazione: {creation_date}")
    print(f"Produttore: {metadata.get('/Producer')}")
    # Aggiungi qui altri metadati desiderati

# Esempio di utilizzo:
pdf_file = "relazione.pdf"
wordlist_file = "password.txt"

brute_force_pdf(pdf_file, wordlist_file)
