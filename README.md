# 🛠️ Log Monitor & Archiver Automation Script

This Python script performs three main tasks:
1. **Archives old files** from a specified directory.
2. **Monitors a log file** for error messages.
3. **Sends email alerts** when errors are detected.

---

## 📁 Project Structure

- `automate.py`: The main automation script.
- `README.md`: This documentation file.
- `system.log`: The log file being monitored.
- `test/`: Directory containing files to be monitored.
- `archive/`: Directory where old files are moved.

---

## ⚙️ Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

---

## 🧪 How to Run

1. Make sure the following folders exist in the same directory as `main.py`:
   - `test/` ← the folder to monitor.
   - `archive/` ← where old files will be archived.

2. Ensure there is a `system.log` file (create it if needed).

3. Update the email credentials in the script:
   ```python
   EMAIL_ADDRESS = "your_email@gmail.com"
   EMAIL_PASSWORD = "your_app_password"
   TO_EMAIL = "recipient_email@gmail.com"
