def format_datetime(value, format=None):
    if format is None: 
        format = "%Y년 %m월 %d일"
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    else:
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    return formatted