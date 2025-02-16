from datetime import datetime
d1 = datetime(2025, 2, 12, 8, 0, 0)
d2 = datetime(2025, 2, 14, 13, 45, 0)
print((d2 - d1).total_seconds())