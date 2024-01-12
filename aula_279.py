import calendar

#print(calendar.calendar(2024))
# print(calendar.month(2024,1))
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2024,1)
# print(calendar.monthrange(2024,1))
# print(list(enumerate(calendar.day_name)))
print(calendar.day_name[numero_primeiro_dia])
print(calendar.weekday(2022, 12, ultimo_dia))
print(calendar.day_name[calendar.weekday(2024, 1, ultimo_dia)])

for week in calendar.monthcalendar(2024, 1):
    print(list(enumerate(week)))

for week in calendar.monthcalendar(2024, 1):
    for day in week:
        if day == 0:
            continue
        print(day)