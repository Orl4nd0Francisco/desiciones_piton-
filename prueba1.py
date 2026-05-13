from datetime import datetime

despierta=datetime(2026,4,11,7,30)
duerme=datetime(2026,4,11,23,45)

vigilia=duerme-despierta
print(vigilia.seconds)