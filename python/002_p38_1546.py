# 자료구조 - 배열과 리스트
a = int(input());
# b = list(int(input().split(" ")));
b = list(map(int, input().split(" ")));
# print(a);
print(b);
M = max(b);
# M = 0;
# for i in b :
#     if M < int(i) :   
#         M = int(i)
        
print(M);
c = 0;
for i in b :
    c = c + ((int(i) / M) * 100)

print(float(c/a));