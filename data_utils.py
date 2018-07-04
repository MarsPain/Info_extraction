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
filename_predict_zengjianchi = "data/predict_zengjianchi.utf8"
filename_predict_dingzeng = "data/predict_dingzeng.utf8"
filename_predict_hetong = "data/predict_hetong.utf8"
filename_result_zengjianchi = "data/zengjianchi.txt"
filename_result_dingzeng = "data/dingzeng.txt"
filename_result_hetong = "data/hetong.txt"

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
            # count += 1
            # if count>50: break
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
    pattern1 = re.compile(r"(\d{1,2}月|\d{1,2}日)")
    def replace1(matchobj):
        if len(matchobj[0]) == 2:
            # print(type(matchobj[0]), matchobj[0])
            matchobj = "0" + matchobj[0]
            # print(matchobj)
            return matchobj
        else:
            return matchobj[0]
    s = re.sub(pattern1, replace1, s)
    # s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"  #测试pattern2
    pattern2 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+\.?\d+%)")
    def replace2(matchobj):
        if matchobj[0][-1] == "%":
            value = 0.01*float(matchobj[0][:-1])
            matchobj = re.sub(matchobj[0], str(value), matchobj[0])
        else:
            year = matchobj[0][:4]
            matchobj = re.sub("至", "至"+year+"年", matchobj[0])
            matchobj = re.sub("年|月", "-", matchobj)
            matchobj = re.sub("日", "", matchobj)
        return matchobj
    s = re.sub(pattern2, replace2, s)
    return s

def output_data(filename_ner, filename_result_zengjianchi):
    result = ""
    with open(filename_ner, "r", encoding="utf-8") as f:
        flag = True
        temp_result = ["\t" for i in range(8)]   #用于保存一行结构化的实体
        entity = "" #用于保存一个实体
        for line in f:
            # print(line)
            char_tag_predict = line.split()
            # print(char_tag_predict)
            # print(len(char_tag_predict))
            if len(char_tag_predict) != 3:
                continue
            if char_tag_predict[-1] == "O":
                # print(char_tag_predict[0])
                continue
            else:
                predict = char_tag_predict[-1]
                char = char_tag_predict[0]  #被标注预测的字符
                predict_loc = predict[0]    #被标注预测的在实体中的位置（B、I、O等）
                predict_type = predict[-1]  #被标注预测的在实体类型（0-7，标注还是得从0而不是1开始，方便输出）
                # print(type(predict_type))
                # print("char:", char, "predict_loc:", predict_loc, "predict_type:", predict_type)
                if predict_loc == "B" or predict_loc == "I":
                    entity += char
                elif predict_loc == "E":
                    entity += char
                    #如果是新的公告id实体，则说明属于新的公告文本，将上一个temp_result加入result并换行，
                    # 然后重新初始化temp_result并用entity对公告id赋值。
                    if int(predict_type) == 0:
                        result = result + "\t".join(temp_result) + "\n"
                        temp_result = ["\t" for i in range(8)]
                        temp_result[0] = entity
                        entity = ""
                    #如果是当前公告中的一条结构化信息，则只要对该行数据的temp_result赋值即可
                    elif temp_result[int(predict_type)-1] == "\t":
                        temp_result[int(predict_type)-1] = entity
                        entity = ""
                    #该实体依然在当前的公告文本中，但是属于另一条结构化信息，所以先从当前temp_result
                    # 中取出公告id，然后将temp_result加入result中，再换行，
                    # 重新初始化temp_result，并对公告id和当前的检测到的实体entity赋值
                    else:
                        announce_id = temp_result[0]
                        result = result + "\t".join(temp_result) + "\n"
                        temp_result = ["\t" for i in range(8)]
                        temp_result[0] = announce_id
                        temp_result[int(predict_type)-1] = entity
                        entity = ""
    with open(filename_result_zengjianchi, "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    read_data(dirname_dingzeng, dirname_txt_dingzeng)
    # process_data(dirname_txt2_zengjianchi)
    # output_data(filename_ner, filename_result_zengjianchi)