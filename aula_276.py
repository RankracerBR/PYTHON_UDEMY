from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2024 08:20:20', fmt)

delta = timedelta(days=10, hours=2)
delta2 = relativedelta(data_fim, data_inicio)
print(delta2)
print(data_fim - delta)
print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10))
print(delta2.days, delta2.years)


# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)

# print(data_fim - data_inicio)
# print(data_fim > data_inicio)