from datetime import datetime, timedelta
from pytz import timezone
from . import korea_datetime

def format_datetime(value: datetime, format=None):
    if format is None: 
        format = "%Y.%m.%d"
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    else:
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    return formatted

def created_datetime(value: datetime):
    now = korea_datetime().replace(tzinfo=None)
    created = value.replace(tzinfo=None)
    sub = now-created
    
    if sub < timedelta(minutes=1):
        return "방금 전"
    if sub < timedelta(hours=1):
        return f"{round(sub.seconds/60)} 분 전"
    if sub < timedelta(days=1):
        return f"{round(sub.seconds/3600)} 시간 전"
    if sub < timedelta(days=7):
        return f"{sub.days} 일 전"
    else:
        return format_datetime(value,"%Y.%m.%d %h:%M")
     