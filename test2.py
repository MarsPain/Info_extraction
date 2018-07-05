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

# pattern4 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+%)")
# s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"
# # print(re.findall(pattern,s))
# def test4(matchobj):
#     print(1)
#     print(type(matchobj[0]))
#     if matchobj[0][-1] == "%":
#         value = 0.01*int(matchobj[0][:-1])
#         print(value)
#         matchobj = re.sub(matchobj[0], str(value), matchobj[0])
#         return matchobj
#     else:
#         year = matchobj[0][:4]
#         matchobj = re.sub("至", "至"+year+"年", matchobj[0])
#         matchobj = re.sub("年|月", "-", matchobj)
#         matchobj = re.sub("日", "", matchobj)
#     return matchobj
# s = re.sub(pattern4, test4, s)
# print(s)

# pattern5 = re.compile(r"(\d+\.?\d+%)")
# s = "我50|50%|0.345%"
# def test5(matchobj):
#     print("matchobj", matchobj[0])
#     value = 0.01*float(matchobj[0][:-1])
#     print(value)
#     matchobj = re.sub(matchobj[0], str(value), matchobj[0])
#     return matchobj
# s = re.sub(pattern5, test5, s)
# print(s)


# s = ["\t" for i in range(4)]
# print(s)
# s[0] = "a"; s[2] = "b"
# if s[3] == "\t":
#     print("Yes!!!!")
# print("\t".join(s))

# s = "67.236.244"
# pattern = re.compile(r"(\d{1,3}\.\d{3}\.\d{3}\.\d{3})|(\d{1,3}\.\d{3}\.\d{3})|(\d{1,3}\.\d{3})")
# def test(matchobj):
#     string = matchobj[0].replace(".", "")
#     return string
# s = re.sub(pattern, test, s)
# print(s)

# s = "400万"
# pattern4 = re.compile(r"(\d+万)")
# def replace4(matchobj):
#     num = matchobj[0][:-1]
#     new_num = int(num) * 10000
#     return str(new_num)
# s = re.sub(pattern4, replace4, s)
# print(s)

# s = "州发展![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQsAAAEBCAIAAADgrBdjAAAABmJLR0)adsd"
# s = re.sub(r"(\[image\].*\))", " ", s)
# print(s)

# s = "额为137,630,695元，币共计16928.797540000元（大写：人民币,51，452元"
# pattern = re.compile(r"(\d+.\d+)|(\d{1,}.\d{3}.\d{3})")
# def test(matchobj):
#     string = matchobj[0].replace("，|,|.", "")
#     print(string)
#     return string
# s = re.sub(pattern, test, s)
# print(s)

# s = "dad2017年6月7日-8月8日大萨达撒"
# pattern2 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日-\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+\.?\d+%)")
# def replace2(matchobj):
#     if matchobj[0][-1] == "%":
#         value = 0.01*float(matchobj[0][:-1])
#         matchobj = re.sub(matchobj[0], str(value), matchobj[0])
#     else:
#         year = matchobj[0][:4]
#         matchobj = re.sub("至", "至"+year+"年", matchobj[0])
#         matchobj = re.sub("-", "至"+year+"年", matchobj)
#         matchobj = re.sub("年|月", "-", matchobj)
#         matchobj = re.sub("日", "", matchobj)
#     return matchobj
# s = re.sub(pattern2, replace2, s)
# print(s)

# l1 = ["1sad", "2312", "\t", "sda"]
# l2 = ["1sad", "\t", "\t", "sda"]
# count1, count2 =0, 0
# for i in l1:
#     if i != "\t":
#         count1 += 1
# for i in l2:
#     if i != "\t":
#         count2 += 1
# print(count1, count2)
