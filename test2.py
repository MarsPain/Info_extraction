# coding=gbk

# a = [1, 2, 3, 4, 5, 6,7]
# print(a[2:-2])

import re
# pattern = re.compile(r"\d{4}"+"年"+r"\d{1,2}"+"月"+r"\d{1,2}"+"日")
# s = "他的生日是2016年12月12日，他在2017年8月7日去大学了集中竞价	2018年2月5日d s"
# print(re.findall(pattern,s))
# def test(matchobj):
#     #以下方法不知道为什么不再适用了
#     # print(matchobj)
#     # print(type(matchobj[0]))
#     # matchobj = re.sub("年|月", "-", matchobj[0])
#     # matchobj = re.sub("日", "", matchobj)
#     # return matchobj
#     #新的方法
#     matchobj = matchobj.group(0)
#     matchobj = re.sub("年|月", "-", matchobj)
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

# s = "证券代码：002065证券简称：东华软件公告编号：2014-021东华软件股份公司关于持股5%以上股东减持股份的公告本公司及董事会全体成员保证信息披露内容的真实、准确和完整，没有虚假记载、误导性陈述或重大遗漏。东华软件股份公司（以下简称“公司”）2014年1月27日收到公司控股股东北京东华诚信工业设备有限公司（以下简称“工业设备”）减持股份的通知，工业设备于2010年9月14日至2014年1月27日通过二级市场集中竞价方式累计减持公司无限售流通股股份4,879,336股，具体减持情况如下：股东名称|减持方式|减持时间|减持均价(元/股)|减持股数（股）|占总股本比例（%）|总股本（股）---|---|---|---|---|---|---北京东华诚信工业设备有限公司|集中竞价交易|2010.9.14|31.82|600,510|0.1410%|425,985,0902012.6.28|22.19|112,800|0.0213%|530,744,0002012.7.3|23.46|697,671|0.2880%|530,744,0002012.7.4|22.75|831,050|530,744,0002012.9.3|18.17|333,905|0.1362%|689,967,2002012.9.4|18.40|2,615|689,967,2002012.9.5|18.35|169,400|689,967,2002012.9.6|18.84|5,000|689,967,2002012.9.7|18.89|323,250|689,967,2002012.9.11|18.60|105,475|689,967,200||2014.1.8|34.13|167,400|0.2445%|694,334,8102014.1.9|35.13|183,800|694,334,8102014.1.23|34.28|485,000|694,334,8102014.1.24|36.80|541,460|694,334,8102014.1.27|39.59|320,000|694,334,810合计|||4,879,336||工业设备历年持股及变动情况：（1）公司股票于2006年8月23日上市，工业设备持有公司股票12,752,643股，占公司总股本86,236,687股的14.79%。（2）2007年5月31日，公司实施2006年年度利润分配方案，向全体股东每10股转增5股，公司总股本增加至129,355,687股，工业设备持股比例不变。（3）2008年2月29日，公司发行股份购买资产收购北京联银通科技有限公司100%股权，股本增加至141,995,030股；2008年5月29日，公司实施2007年年度利润分配方案，向全体股东每10股转增10股，总股本增加至283,990,060股。增发前占公司总股本的14.79%，增发后工业设备持股比例为13.47%，持股比例被摊薄1.32%。（4）2009年5月22日，公司实施2008年年度利润分配方案，向全体股东每10股送2股转增3股，派1元红利（含税），公司股本增加至425,985,090股，工业设备持股比例不变。（5）2010年9月14日，工业设备累计减持600,510股，占公司总股本425,985,090股的0.1410%，减持后占公司总股本13.33%。（6）2011年2月27日，公司发行股份购买资产收购北京神州新桥科技有限公司100%股权，股本增加至442,286,667股，增发前占公司总股本13.33%，增发后占公司总股本12.84%，持股比例被摊薄0.49%。（7）2011年2月13日，公司实施2010年年度利润分配方案，向全体股东每10股送2股，派1元红利（含税），公司股本增加至530,744,000股，工业设备持股比例不变。（8）2012年6月28，工业设备累计减持112，800股，占公司总股本530,744,000的0.0213%；2012年7月18日，公司因实施2011年度利润分配方案，向全体股东每10股送3股，总股本增加至689,967,200股，工业设备于2012年3日-2012年9月11日期间，累计减持939,645股，占公司总股本689,967,200股的0.1362%。（9）2014年1月8日至2014年1月27日期间，工业设备累计减持1,697,660股，占公司总股本694,334,810股的0.2445%。综上所述，工业设备通过证券交易所集中竞价交易减持所持公司股份的比例为0.8309%，公司因2008年、2011年实施发行股份购买资产，股份被摊薄1.81%。本次变动后，工业设备仍持有公司股份81,495,379股，占公司目前总股本694,334,810股的11.74%，目前工业设备所持股份不存在被质押、冻结等情况。股东名称|股份性质|本次减持前持有股份|本次减持后持有股份---|---|---|---股份（股）|占股本比例|股数（股）|占股本比例工业设备|合计持有股份|12,752,643|14.79%|81,495,379|11.74%其中：无限售条件股份|12,752,643|14.79%|81,495,379|11.74%有条件限售股份||||1、本次减持未违反《上市公司解除限售存量股份转让指导意见》等有关规定，其间任意30天减持数量均未超过1%。2、本次减持未违反《上市公司收购管理办法》、《深圳证券交易所中小企业板上市公司规范运作指引》等有关法律、法规、规章、业务规则等规定。3、本次减持的股东未在相关文件中做出过最低减持价格等承诺。4、本次权益变动后，投资公司仍为持有本公司5%以上股份的股东。特此公告。东华软件股份公司2014年1月30日"
# pattern1 = re.compile(r"(\d{1,2}月)|(\d{1,2}日)")
# def replace1(matchobj):
#     matchobj = matchobj.group(0)
#     if len(matchobj) == 2:
#         # print(type(matchobj[0]), matchobj[0])
#         matchobj = "0" + matchobj
#         print(matchobj)
#         return matchobj
#     else:
#         return matchobj
# s = re.sub(pattern1, replace1, s)

# s = "dsadasd.html"
# print(s[-4:])

# s = "打开就好撒考虑到认购认购的数据爱可登拉丝机贷款了"
# pattern = re.compile(r"(认购)")
# # matchobj = re.findall(pattern, s)
# # print(type(matchobj), matchobj)
# matchobj = re.search(pattern, s, flags=0)
# print(matchobj.start())
# print(re.search(pattern, s[8+2:], flags=0).start())

# s = "大厦的考拉数据库认购等级考认购试拉道具第三点认购打开的认购的就是卡德加了"
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# index_list = []
# pattern = re.compile(r"(认购)")
# matchobj = re.search(pattern, s, flags=0)
# index = matchobj.start()
# if index:
#     # print(1)
#     index_list.append(Interval(index, index+2))
# while index>0:
#     # print(1)
#     last_index = index + 2
#     print(last_index)
#     print(s[last_index+2:])
#     matchobj = re.search(pattern, s[last_index:], flags=0)
#     if not matchobj:
#         break
#     index = matchobj.start()
#     print(index)
#     index = index + last_index
#     index_list.append(Interval(index, index+2))
#     index_list.append(Interval(index-2, index+4))
# for interval in index_list:
#     print(interval.start, interval.end)
#
# def merge(intervals):
#     intervals.sort(key = lambda x:x.start)
#     len1 = len(intervals)
#     res = []
#     for i in range(len1):
#         if res == []:
#             res.append(intervals[i])
#         else:
#             len2 = len(res)
#             if res[len2-1].start <= intervals[i].start <= res[len2-1].end :
#                 res[len2-1].end = max(intervals[i].end, res[len2-1].end)
#             else:
#                 res.append(intervals[i])
#     return res
#
# new_interval_list = merge(index_list)
# for interval in new_interval_list:
#     print(interval.start, interval.end)

# a = [2,1,2,0,2,3,4]
# #暴力深度搜索
# def dfs(a, result, num, count, flag):
#     if count == 4:
#         result = num if num>result else result
#         return result
#     elif a:
#         for i in range(len(a)):
#             if flag:
#                 result = dfs(a[i+1:], result, num+a[i], count+1, False)
#             else:
#                 result = dfs(a[i+1:], result, num-a[i], count+1, True)
#     return result
# result = -100000
# flag = True
# result = dfs(a, result, 0, 0, flag)
# print(result)

# a = [2,1,5,3,2,7,6,0]
# def quick_sort(a, left, right):
#     i = left; j = right
#     if i>=j:
#         return a
#     key = a[i]
#     while i<j:
#         while i<j and a[j]>=key:
#             j -= 1
#         a[i] = a[j]
#         while i<j and a[i]<=key:
#             i += 1
#         a[j] = a[i]
#     a[i] = key
#     quick_sort(a, left, i-1)
#     quick_sort(a, j+1, right)
#     return a
# left = 0; right = len(a)-1
# a = quick_sort(a, left, right)
# print(a)