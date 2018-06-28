# a = [1, 2, 3, 4, 5, 6,7]
# print(a[2:-2])

import re
pattern = re.compile(r"\d{4}"+"年"+r"\d{1,2}"+"月"+r"\d{1,2}"+"日")
s = "他的生日是2016年12月12日，他在2017年8月7日去大学了"
print(re.findall(pattern,s))
def test(matchobj):
    print(1)
    print(type(matchobj[0]))
    matchobj = re.sub("年|月", "-", matchobj[0])
    matchobj = re.sub("日", "", matchobj)
    return matchobj
s = re.sub(pattern, test, s)
print(s)
