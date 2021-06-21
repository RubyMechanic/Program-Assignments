
def triangleArea(base, height):
    area = base*height/2
    print(area)
    return area
n = 5
m = 5
areaList = [0]*n*m
i=0
for b in range(0,n):
    for h in range(0,m):
        areaList[i] = triangleArea(b,h)
        i += 1
print(areaList)


