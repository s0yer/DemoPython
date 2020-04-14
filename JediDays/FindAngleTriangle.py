import math

ab = int(input())
bc = int(input())
res = str(int(round(math.degrees(math.atan2(ab,bc)))))

print(res+'°')