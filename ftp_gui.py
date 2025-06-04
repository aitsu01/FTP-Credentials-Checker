import tkinter as tk
from tkinter import messagebox
import ctypes
import os
import ftplib
import io

# Percorso della DLL (assicurati che FtpBackend.dll sia nella stessa cartella dello script)
DLL_PATH = os.path.join(os.path.dirname(__file__), "FtpBackend.dll")

# Carica la DLL utilizzando ctypes
try:
    ftp_dll = ctypes.CDLL(DLL_PATH)
except Exception as e:
    messagebox.showerror("Errore", f"Impossibile caricare la DLL: {e}")
    exit(1)

# Imposta il prototipo della funzione export RunBackend
ftp_dll.RunBackend.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
ftp_dll.RunBackend.restype = ctypes.c_int

def save_env_file(server, user, password):
    """Crea il file .env con le credenziali verificate nella stessa cartella dello script."""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    try:
        with open(env_path, "w") as f:
            f.write(f"ftpServer={server}\n")
            f.write(f"ftpUser={user}\n")
            f.write(f"ftpPassword={password}\n")
        print(f"File .env creato in: {env_path}")
    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile salvare il file .env: {e}")

def upload_credentials_file(server, user, password):
    """
    Prova ad eseguire l'upload sul server FTP di un file di verifica.
    Se l'upload ha successo, viene visualizzato un messaggio di conferma.
    """
    content = "your FTP settings are working and verificated!!"
    file_obj = io.BytesIO(content.encode('utf-8'))
    try:
        print(f"Tentativo di connessione a: {server}")
        ftp = ftplib.FTP(server, timeout=10)
        ftp.login(user, password)
        ftp.storbinary("STOR credenziali.txt", file_obj)
        ftp.quit()
        messagebox.showinfo("Upload FTP", "Il file di verifica è stato caricato con successo!")
        return True
    except Exception as e:
        messagebox.showerror("Upload FTP", f"Connessione o spazio host non disponibile: {e}")
        return False
    


def test_connection():
    """
    Raccoglie le credenziali dalla GUI, testa la connessione FTP utilizzando ftplib e, 
    se il test ha successo, chiama la funzione RunBackend della DLL, esegue l'upload del file di verifica
    e crea il file .env; altrimenti mostra un messaggio di errore e interrompe l'operazione.
    """
    # Recupera le credenziali dalla GUI (elimina eventuali spazi in eccesso)
    ftpServer = server_entry.get().strip()
    ftpUser = user_entry.get().strip()
    ftpPassword = pass_entry.get().strip()

    # Controlla che tutti i campi siano compilati
    if not ftpServer or not ftpUser or not ftpPassword:
        messagebox.showerror("Errore", "Tutti i campi devono essere compilati!")
        return

    # Primo test: prova a connetterti con ftplib per verificare la connessione FTP
    try:
        ftp = ftplib.FTP(ftpServer, timeout=10)
        ftp.login(ftpUser, ftpPassword)
        ftp.quit()
    except Exception as e:
        messagebox.showerror("Test FTP", f"Errore durante la connessione: {e}")
        return

   
    server_b = ftpServer.encode('utf-8')
    user_b = ftpUser.encode('utf-8')
    password_b = ftpPassword.encode('utf-8')

    result = ftp_dll.RunBackend(server_b, user_b, password_b)
    if result != 0:
        # Se la funzione RunBackend restituisce un valore non previsto, segnala un errore.
        messagebox.showerror("Test FTP", "Errore durante il test della connessione FTP tramite DLL!")
        return

    # Altrimenti, se i test hanno avuto successo:
    messagebox.showinfo("Test FTP", "Connessione FTP testata con successo!")
    
    # Esegui l'upload del file di verifica sul server FTP
    if upload_credentials_file(ftpServer, ftpUser, ftpPassword):
        # Se l'upload ha successo, crea il file .env con le credenziali verificate
        save_env_file(ftpServer, ftpUser, ftpPassword)


   

# Configurazione della GUI con Tkinter
root = tk.Tk()
root.title("Configurazione Credenziali FTP")

tk.Label(root, text="FTP Server:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
server_entry = tk.Entry(root, width=30)
server_entry.grid(row=0, column=1, padx=5, pady=5)
server_entry.insert(0, "ftp.example.com")



tk.Label(root, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
user_entry = tk.Entry(root, width=30)
user_entry.grid(row=1, column=1, padx=5, pady=5)
user_entry.insert(0, "tuo_username")

tk.Label(root, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
pass_entry = tk.Entry(root, width=30, show="*")
pass_entry.grid(row=2, column=1, padx=5, pady=5)
pass_entry.insert(0, "tua_password")

test_button = tk.Button(root, text="Testa e Salva Credenziali", command=test_connection)
test_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
