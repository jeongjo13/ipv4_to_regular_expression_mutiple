count = int(input("IP 개수: "))
ip_list = []
w = 0
while w < count : 
    a = input("CIDR 입력: ") # CIDR 입력 받기
    b = a.split(".", 3)
    c = b[3].split("/", 2)
    d = b + c
    del d[3]
    print(d)
    ip_list.append(d)
    w += 1
print("현재 추가된 아이피 리스트: ", end="")
print(ip_list)

for i in ip_list :
    if i[4] == "32" :
        print("정규식 차단이 필요하지 않은 아이피")
    elif i[4] == "24" :
        print("%s\\.%s\\.%s(\\.[0-9]{1,3})" % (i[0], i[1], i[2]))
    elif i[4] == "16" :
        print("%s\\.%s(\\.[0-9]{1,3}){2}" % (i[0], i[1]))
    elif i[4] == "8" :
        print("%s(\\.[0-9]{1,3}){3}" % i[0])
'''
if d[4] == "36" :
    print("정규식 차단이 필요하지 않습니다.")
elif d[4] == "24" :
    print("%s\\.%s\\.%s(\\.[0-9]{1,3})" % (d[0], d[1], d[2]))
elif d[4] == "16" :
    print("%s\\.%s(\\.[0-9]{1,3}){2}" % (d[0], d[1]))
elif d[4] == "8" :
    print("%s(\\.[0-9]{1,3}){3}" % d[0])
'''

