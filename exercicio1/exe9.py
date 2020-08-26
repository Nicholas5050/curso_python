from datetime import datetime, timedelta
today = datetime.now()
print('hoje eh: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Ontem foi: ' + str(yesterday))