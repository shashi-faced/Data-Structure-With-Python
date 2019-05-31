n = int(input())
arr = []
for i in range(0,n):
    arr.append(int(input()))
maxx = max(arr)
print(maxx)
arr.remove(maxx)
print(max(arr))
