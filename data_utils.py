import html2text
import os
import re

dirname_zengjianchi = "data/round1_train_20180518/增减持/html"
dirname_dingzeng = "data/round1_train_20180518/定增/html"
dirname_hetong = "data/round1_train_20180518/重大合同/html"
dirname_txt_zengjianchi = "data/round1_train_20180518/增减持/txt"
dirname_txt_dingzeng = "data/round1_train_20180518/定增/txt"
dirname_txt_hetong = "data/round1_train_20180518/重大合同/txt"
dirname_txt2_zengjianchi = "data/round1_train_20180518/增减持/txt2"
dirname_txt2_dingzeng = "data/round1_train_20180518/定增/txt2"
dirname_txt2_hetong = "data/round1_train_20180518/重大合同/txt2"

def read_data(dirname, dirname_txt):
    h2t = html2text.HTML2Text() #初始化html2text工具
    h2t.ignore_links = True #表示忽略html页面中的链接
    count = 0
    for filename in os.listdir(dirname):
        announce_id = filename[:-5]
        # print("announce_id:", announce_id)
        filename = os.path.join(dirname, filename)
        filename_txt = os.path.join(dirname_txt, announce_id+".txt")
        with open(filename, "r", encoding="utf-8") as f:
            f = f.read()
            s = h2t.handle(f)   #读取为txt格式的string
            s = s.replace(" ", ""); s = s.replace("\n", "") #去除空格和换行符
            s = unit_norm(s)    #对日期和比例等单位进行归一化处理
            s = "公告ID" + announce_id + s #将公告id(announce_id)加入每个相应文件的头部
            # print(s)
            count += 1
            # if count>10: break
            with open(filename_txt, "w", encoding="utf-8") as f_txt:
                f_txt.write(s)

def process_data(dirname):
    announce_train = "data/round1_train_20180518/增减持/announce.train"
    announce_dev = "data/round1_train_20180518/增减持/announce.dev"
    announce_test = "data/round1_train_20180518/增减持/announce.test"
    all_filenames = os.listdir(dirname)
    # print(all_filenames)
    num_filenames = len(all_filenames)
    # num_filenames = 20
    count = 0
    announce_txt = ""
    for filename in all_filenames:
        filename = os.path.join(dirname, filename)
        count += 1
        with open(filename, 'r', encoding="utf-8") as f:
            announce_txt = announce_txt + f.read() + "\n"
            # print(announce_txt)
            if count==6*(num_filenames//10):
                with open(announce_train, 'w', encoding="utf-8") as train:
                    train.write(announce_txt)
                    announce_txt = ""
            elif count==8*(num_filenames//10):
                with open(announce_dev, 'w', encoding="utf-8") as dev:
                    dev.write(announce_txt)
                    announce_txt = ""
            elif count==num_filenames:
                with open(announce_test, 'w', encoding="utf-8") as test:
                    test.write(announce_txt)

def unit_norm(s):
    # s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"  #测试pattern
    pattern = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+\.?\d+%)")
    def replace(matchobj):
        if matchobj[0][-1] == "%":
            value = 0.01*float(matchobj[0][:-1])
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
    # process_data(dirname_txt2_zengjianchi)