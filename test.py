# a = [1, 2, 3, 4, 5, 6,7]
# print(a[2:-2])

import re
# pattern = re.compile(r"\d{4}"+"年"+r"\d{1,2}"+"月"+r"\d{1,2}"+"日")
# s = "他的生日是2016年12月12日，他在2017年8月7日去大学了"
# print(re.findall(pattern,s))
# def test(matchobj):
#     print(1)
#     print(type(matchobj[0]))
#     matchobj = re.sub("年|月", "-", matchobj[0])
#     matchobj = re.sub("日", "", matchobj)
#     return matchobj
# s = re.sub(pattern, test, s)
# print(s)

# pattern2 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)")
# s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了"
# # print(re.findall(pattern,s))
# def test2(matchobj):
#     print(1)
#     print(type(matchobj[0]))
#     year = matchobj[0][:4]
#     matchobj = re.sub("至", "至"+year+"年", matchobj[0])
#     matchobj = re.sub("年|月", "-", matchobj)
#     matchobj = re.sub("日", "", matchobj)
#     return matchobj
# s = re.sub(pattern2, test2, s)
# print(s)

# pattern3 = re.compile(r"(\d+%)")
# s = "我50%"
# def test3(matchobj):
#     print("matchobj", matchobj[0])
#     value = 0.01*int(matchobj[0][:-1])
#     print(value)
#     matchobj = re.sub(matchobj[0], str(value), matchobj[0])
#     return matchobj
# s = re.sub(pattern3, test3, s)
# print(s)

# s = "50%"
# s = int(s[:-1])
# print(s)

pattern4 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+%)")
s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"
# print(re.findall(pattern,s))
def test4(matchobj):
    print(1)
    print(type(matchobj[0]))
    if matchobj[0][-1] == "%":
        value = 0.01*int(matchobj[0][:-1])
        print(value)
        matchobj = re.sub(matchobj[0], str(value), matchobj[0])
        return matchobj
    else:
        year = matchobj[0][:4]
        matchobj = re.sub("至", "至"+year+"年", matchobj[0])
        matchobj = re.sub("年|月", "-", matchobj)
        matchobj = re.sub("日", "", matchobj)
    return matchobj
s = re.sub(pattern4, test4, s)
print(s)
