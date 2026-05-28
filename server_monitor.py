import psutil
import smtplib
from email.message import EmailMessage
import ssl
import time

# ---------------- SETTINGS ---------------- #

CPU_THRESHOLD = 20
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 90

CHECK_INTERVAL = 60  # seconds

EMAIL_SENDER = "nitishasom2000@gmail.com"
EMAIL_PASSWORD = "xobj aimg qnzw meaj"

EMAIL_RECEIVER = "nitishasom1805@gmail.com"

# ---------------- EMAIL FUNCTION ---------------- #

def send_alert(subject, message):

    email = EmailMessage()

    email["From"] = EMAIL_SENDER
    email["To"] = EMAIL_RECEIVER
    email["Subject"] = subject

    email.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:

        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)

        smtp.send_message(email)

# ---------------- MONITOR FUNCTION ---------------- #

def monitor_system():

    while True:

        # CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Memory Usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        # Disk Usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")

        # ---------------- ALERT CHECKS ---------------- #

        if cpu_usage > CPU_THRESHOLD:

            send_alert(
                "HIGH CPU USAGE ALERT",
                f"CPU usage is critically high: {cpu_usage}%"
            )

        if memory_usage > MEMORY_THRESHOLD:

            send_alert(
                "HIGH MEMORY USAGE ALERT",
                f"Memory usage is critically high: {memory_usage}%"
            )

        if disk_usage > DISK_THRESHOLD:

            send_alert(
                "HIGH DISK USAGE ALERT",
                f"Disk usage is critically high: {disk_usage}%"
            )

        print("System checked successfully.\n")

        # Wait before next check
        time.sleep(CHECK_INTERVAL)

# ---------------- START PROGRAM ---------------- #
if __name__== '__main__':
    monitor_system()