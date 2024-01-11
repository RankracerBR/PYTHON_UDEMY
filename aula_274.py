from datetime import datetime
import time
from pytz import timezone

# data_str = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)

# data = datetime.now()
# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
data = datetime.now()
# data = datetime.now(timezone('Asia/Tokyo'))
print(data.timestamp())
print(data.fromtimestamp(1704985080.21999))