# a = "abd cdf ede kdof diknd"
# print(type(a))
#
# b = [x for x in a.split(" ")[:-1]]
# print(b)
# print(type(b))
#
# k = "my home"
#
# print(f"제가 있는 장소는 {k}")



## 단어간 동일성 비교 테스트

print("절단"=="절단")
print("절단"=="절단기")

print("절단"in"절단")
print("절단"in"절단기")

print("-"*30)

target = ["절단기", "절단장비"]

def including_check(k):
    if k in [x for x in target][0]:
        print("Included")
    else:
        print("Not Included")

including_check("절단기")
including_check("절단")