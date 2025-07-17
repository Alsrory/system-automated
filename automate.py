
import os
import shutil
import time
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage

WATCHED_DIR = "test"
ARCHIVE_DIR = "archive"
LOG_FILE = "system.log"
DAYS_OLD = 7

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@gmail.com"

def send_error_email(error_lines):
    msg = EmailMessage()
    msg['Subject'] = '🚨 تنبيه: تم اكتشاف أخطاء في السجل'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg.set_content("تم اكتشاف الأخطاء التالية:\n\n" + "\n".join(error_lines))

    try:
        with smtpllib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ تم إرسال التنبيه إلى البريد.")
    except Exception as e:
        print("❌ فشل في إرسال البريد:", e)

def archive_old_files():
    now = datetime.now()
    for filename in os.listdir(WATCHED_DIR):
        file_path = os.path.join(WATCHED_DIR, filename)
        if os.path.isfile(file_path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if now - modified_time > timedelta(days=DAYS_OLD):
                print(f"📦 أرشفة الملف: {filename}")
                shutil.move(file_path, os.path.join(ARCHIVE_DIR, filename))

def monitor_log():
    keywords = ['error', 'fail']
    error_lines = []

    print("\n🔍 فحص السجلات...\n")
    try:
        with open(LOG_FILE, 'r') as log:
            for line in log:
                if any(keyword in line.lower() for keyword in keywords):
                    print(f"❗ تم اكتشاف مشكلة: {line.strip()}")
                    error_lines.append(line.strip())
    except FileNotFoundError:
        print("❌ ملف السجل غير موجود.")
        return

    if error_lines:
        send_error_email(error_lines)

if __name__ == "__main__":
    print("🚀 بدء الأتمتة...")
    archive_old_files()
    monitor_log()
    print("✅ تم الانتهاء.")
