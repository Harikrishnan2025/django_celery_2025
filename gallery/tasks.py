from celery import shared_task
from datetime import datetime

@shared_task
def log_to_file():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Task is running...") 
    with open('task_log.txt', 'a') as f:
        f.write(f'[{timestamp}] Scheduled task ran.\n')