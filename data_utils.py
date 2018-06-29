import html2text
import os
import re

dirname_zengjianchi = "data/round1_train_20180518/增减持/html"
dirname_dingzeng = "data/round1_train_20180518/定增/html"
dirname_hetong = "data/round1_train_20180518/重大合同/html"
dirname_txt_zengjianchi = "data/round1_train_20180518/增减持/txt"
dirname_txt_dingzeng = "data/round1_train_20180518/定增/txt"
dirname_txt_hetong = "data/round1_train_20180518/重大合同/txt"

def read_data(dirname, dirname_txt):
    h2t = html2text.HTML2Text() #初始化html2text工具
    h2t.ignore_links = True #表示忽略html页面中的链接
    count = 0
    for filename in os.listdir(dirname):
        filename_txt = os.path.join(dirname_txt, filename[:-5]+".txt")
        filename = os.path.join(dirname, filename)
        with open(filename, "r", encoding="utf-8") as f:
            f = f.read()
            s = h2t.handle(f)   #读取为txt格式的string
            s = s.replace(" ", ""); s = s.replace("\n", "") #去除空格和换行符
            s = unit_norm(s)    #对日期和比例等单位进行归一化处理
            count += 1
            if count>100: break
            with open(filename_txt, "w", encoding="utf-8") as f_txt:
                f_txt.write(s)

def unit_norm(s):
    # s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"  #测试pattern
    pattern = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+%)")
    def replace(matchobj):
        if matchobj[0][-1] == "%":
            value = 0.01*int(matchobj[0][:-1])
            matchobj = re.sub(matchobj[0], str(value), matchobj[0])
        else:
            year = matchobj[0][:4]
            matchobj = re.sub("至", "至"+year+"年", matchobj[0])
            matchobj = re.sub("年|月", "-", matchobj)
            matchobj = re.sub("日", "", matchobj)
        return matchobj
    s = re.sub(pattern, replace, s)
    return s


if __name__ == "__main__":
    read_data(dirname_zengjianchi, dirname_txt_zengjianchi)