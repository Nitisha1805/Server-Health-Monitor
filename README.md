# Server Health Monitor

## Project Overview
This project is a Server Health Monitoring System built using Python. It continuously monitors CPU, memory, and disk usage of a system. If usage exceeds predefined threshold values, the system automatically sends an email alert to the administrator.

## Features
- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Automatic email alerts
- Custom threshold values
- Continuous monitoring at fixed intervals

## Technologies Used
- Python
- psutil
- smtplib
- EmailMessage

## Project Structure
```text
Server-Health-Monitor/
│── server_monitor.py
│── requirements.txt
│── README.md
│── .gitignore
│── Screenshots/
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Nitisha1805/Server-Health-Monitor.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python server_monitor.py
```

## Configuration

Update the following values inside `server_monitor.py`:

- Email sender
- App password
- Email receiver
- Threshold values
- Check interval

Example:

```python
CPU_THRESHOLD = 90
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 90

CHECK_INTERVAL = 60
```
```python
Case-2   
Changing threshold so email alerts work
CPU_THRESHOLD = 20
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

CHECK_INTERVAL = 60
```

## Screenshots

Add screenshots inside the `Screenshots` folder.

Example:
- Running script output
- Email alert received

## Learning Outcome
This project helped me understand:
- System monitoring
- Automation using Python
- Email alert integration
- Basic IT infrastructure monitoring

## Future Improvements
- SMS alerts
- Dashboard for monitoring
- Log file generation
- Real-time graphs