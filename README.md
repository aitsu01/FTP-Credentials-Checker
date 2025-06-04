# FTP Credentials Checker

A fast and simple Python script to test multiple FTP login credentials from lists of servers, usernames, and passwords.



Uno strumento desktop sviluppato in Python per testare la connessione a un server FTP, verificare le credenziali tramite upload di un file di test e salvare i dati in un file `.env`.

##  Funzionalità

-  Verifica connessione FTP con `ftplib`
-  Upload di un file di test ("credenziali.txt")
-  Salvataggio delle credenziali verificate in un file `.env`
-  Integrazione con una DLL esterna per elaborazioni avanzate via `ctypes`
-  Interfaccia semplice con `tkinter`


![ftp6](https://github.com/user-attachments/assets/4acbe3a5-e6aa-4156-ae33-fe916746365f)




##  Tecnologie usate ##

- Python 3.x
- `tkinter`
- `ftplib`
- `ctypes`
- C++ (DLL)

## 🌐 Live Demo

Try the live web version here:  
👉 [https://aitsu01.github.io/FTP-Credentials-Checker](https://aitsu01.github.io/FTP-Credentials-Checker)

##  Avvio rapido ##

```bash
git clone https://github.com/tuo-username/ftp-verifier.git
cd ftp-verifier
python ftp_verifier.py




## Assicurati di avere FtpBackend.dll nella stessa cartella dello script ##
