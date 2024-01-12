import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_PT')
# Get-WinSystemLocale
print(calendar.calendar(2024))
print(locale.getlocale())