import sys
input = sys.stdin.readline;

a1, a2 = map(int,input().split());
print(a1, a2);
bList = list(map(int,input().split()));
print(bList);
sumList = [0];
temp = 0;
for i in bList :
    temp = temp + i;
    sumList.append(temp);

print(sumList);
for i in range(a2) :
    start, end = map(int,input().split());
    print(sumList[end] - sumList[start-1]);