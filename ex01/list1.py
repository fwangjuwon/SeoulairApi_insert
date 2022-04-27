# 리스트, 슬라이싱
print('='*80)

#리스트 만들기
list1 = [1,2,3,4]
list2 = ['1',2,'3',4]

print(list1[0])
print(list2[0])

#리스트 추가하기
list1.append(5)
print(list1)

#리스트 요소 제거
del list1[0]
print("0번지 제거", list1)

#리스트 정렬
list3=[4,2,6,7,3]
list3.sort()
print(list3)
list3.reverse()
print(list3)

#리스트 값 찾기
print(list3.index(2)) #2라는 값은 몇번지에 있나? 

#문자열 슬라이싱
str1 = "안녕하세요"
print(str1[0])
print(str1[1:3]) #시작~끝-1
print(str1[-1]) #끝 인덱스 
print(str1[1:]) #1~끝가지