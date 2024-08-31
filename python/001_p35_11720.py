# 자료구조 - 배열과 리스트
a = int(input());
b = list(input());
# print(a);
# print(b);
answer = 0
for i in b :
    '''
    Python의 주석은 들여쓰기 필요 
    형변환 : int, float, str, chr, bool
    '''
    answer = answer + int(i);
    
print(answer);


