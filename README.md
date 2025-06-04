# 🔐 FTP Verifier Tool

Uno strumento desktop sviluppato in Python per testare la connessione a un server FTP, verificare le credenziali tramite upload di un file di test e salvare i dati in un file `.env`.

## 🧰 Funzionalità

- ✅ Verifica connessione FTP con `ftplib`
- 📤 Upload di un file di test ("credenziali.txt")
- 🗃️ Salvataggio delle credenziali verificate in un file `.env`
- ⚙️ Integrazione con una DLL esterna per elaborazioni avanzate via `ctypes`
- 💻 Interfaccia semplice con `tkinter`

## 🖼️ Interfaccia GUI
![ftp3](https://github.com/user-attachments/assets/aad10aee-0a88-4242-82c0-8de9e750cae4)



## 🛠️ Tecnologie usate

- Python 3.x
- `tkinter`
- `ftplib`
- `ctypes`
- C++ (DLL)

## 🚀 Avvio rapido

```bash
git clone https://github.com/tuo-username/ftp-verifier.git
cd ftp-verifier
python ftp_verifier.py

## Assicurati di avere FtpBackend.dll nella stessa cartella dello script. ##
