
def triangleArea(base, height):
    area = base*height/2
    print(area)
    return area
n = 5
m = 5
areaList = []
for b in range(0,n):
    for h in range(0,m):
        areaList.append(triangleArea(b,h))

print(areaList)


