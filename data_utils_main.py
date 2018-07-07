import html2text
import os
import re

# dirname_zengjianchi = "data/round1_train_20180518/增减持/html"
# dirname_dingzeng = "data/round1_train_20180518/定增/html"
# dirname_hetong = "data/round1_train_20180518/重大合同/html"
# dirname_txt_zengjianchi = "data/round1_train_20180518/增减持/txt"
# dirname_txt_dingzeng = "data/round1_train_20180518/定增/txt"
# dirname_txt_hetong = "data/round1_train_20180518/重大合同/txt"
# dirname_txt2_zengjianchi = "data/round1_train_20180518/增减持/txt2"
# dirname_txt2_dingzeng = "data/round1_train_20180518/定增/txt2"
# dirname_txt2_hetong = "data/round1_train_20180518/重大合同/txt2"
# filename_predict_zengjianchi = "data/predict_zengjianchi.utf8"
# filename_predict_dingzeng = "data/predict_dingzeng.utf8"
# filename_predict_hetong = "data/predict_hetong.utf8"
# filename_result_zengjianchi = "data/zengjianchi.txt"
# filename_result_dingzeng = "data/dingzeng.txt"
# filename_result_hetong = "data/hetong.txt"

# data_path = "data/round1_train_20180518"

# def read_data(dirname, dirname_txt):
def read_data(model_name, path_model_name):
    dirname = os.path.join(path_model_name, "html")
    dirname_txt = os.path.join(path_model_name, "txt")
    if not os.path.exists(dirname_txt):
        os.mkdir(dirname_txt)
    h2t = html2text.HTML2Text() #初始化html2text工具
    h2t.ignore_links = True #表示忽略html页面中的链接
    count = 0
    for filename in os.listdir(dirname):
        if filename[-4:] == "html":
            announce_id = filename[:-5]
        else:
            announce_id = filename
        # print(announce_id)
        # print("announce_id:", announce_id)
        filename = os.path.join(dirname, filename)
        filename_txt = os.path.join(dirname_txt, announce_id+".txt")
        with open(filename, "r", encoding="utf-8") as f:
            f = f.read()
            s = h2t.handle(f)   #读取为txt格式的string
            s = s.replace(" ", ""); s = s.replace("\n", "") #去除空格和换行符
            s = re.sub(r"(\[image\].+\))", " ", s)  #去除图像数据的影响
            # print(s)
            s = unit_norm(s)    #对日期和比例等单位进行归一化处理
            s = "公告ID" + announce_id + s #将公告id(announce_id)加入每个相应文件的头部
            if model_name == "dingzeng":
                s = text_cut(s)
            # print(s)
            # count += 1
            # if count>50: break
            with open(filename_txt, "w", encoding="utf-8") as f_txt:
                f_txt.write(s)

def process_data(model_name, path_model_name, is_train):
    if is_train:
        dirname = os.path.join(path_model_name, "txt2")
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        announce_train = os.path.join(path_model_name, "announce.train")
        announce_dev = os.path.join(path_model_name, "announce.dev")
        announce_test = os.path.join(path_model_name, "announce.test")
    else:
        dirname = os.path.join(path_model_name, "txt2")
        announce_test = os.path.join(path_model_name, "announce.test")
    # print("===========Yes==============")
    all_filenames = os.listdir(dirname)
    # print(all_filenames)
    num_filenames = len(all_filenames)
    # print(num_filenames)
    # num_filenames = 20
    count = 0
    announce_txt = ""
    for filename in all_filenames:
        filename = os.path.join(dirname, filename)
        count += 1
        if is_train:
            with open(filename, 'r', encoding="utf-8") as f:
                announce_txt = announce_txt + f.read() + "\n"
                # print(announce_txt)
                if count==8*(num_filenames//10):
                    with open(announce_train, 'w', encoding="utf-8") as train:
                        print("===========Yes==============")
                        train.write(announce_txt)
                        announce_txt = ""
                elif count==num_filenames:
                    with open(announce_dev, 'w', encoding="utf-8") as dev:
                        dev.write(announce_txt)
                    with open(announce_test, 'w', encoding="utf-8") as test:
                        test.write(announce_txt)
        else:
            with open(filename, 'r', encoding="utf-8") as f:
                announce_txt = announce_txt + f.read() + "\n"
                if count==num_filenames:
                    with open(announce_test, 'w', encoding="utf-8") as test:
                        test.write(announce_txt)

def unit_norm(s):
    pattern1 = re.compile(r"(\d{1,2}月)|(\d{1,2}日)")
    def replace1(matchobj):
        matchobj = matchobj.group(0)
        # if len(matchobj[0]) == 2:
        if len(matchobj) == 2:
            # print(type(matchobj[0]), matchobj[0])
            # matchobj = "0" + matchobj[0]
            matchobj = "0" + matchobj
            # print(matchobj)
            return matchobj
        else:
            return matchobj[0]
    s = re.sub(pattern1, replace1, s)

    # s = "他的生日是2016年12月12日，他在2017年8月7日至9月10日去大学了，有50%的学生"  #测试pattern2
    pattern2 = re.compile(r"(\d{4}年\d{1,2}月\d{1,2}日-\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日至\d{1,2}月\d{1,2}日)|(\d{4}年\d{1,2}月\d{1,2}日)|(\d+\.?\d+%)")
    def replace2(matchobj):
        matchobj = matchobj.group(0)
        # if matchobj[0][-1] == "%":
        #     value = 0.01*float(matchobj[0][:-1])
        #     matchobj = re.sub(matchobj[0], str(value), matchobj[0])
        if matchobj[-1] == "%":
            value = 0.01*float(matchobj[:-1])
            matchobj = re.sub(matchobj, str(value), matchobj)
        # else:
        #     year = matchobj[0][:4]
        #     matchobj = re.sub("至", "至"+year+"年", matchobj[0])
        #     matchobj = re.sub("-", "至"+year+"年", matchobj)
        #     matchobj = re.sub("年|月", "-", matchobj)
        #     matchobj = re.sub("日", "", matchobj)
        else:
            year = matchobj[:4]
            matchobj = re.sub("至", "至"+year+"年", matchobj)
            matchobj = re.sub("-", "至"+year+"年", matchobj)
            matchobj = re.sub("年|月", "-", matchobj)
            matchobj = re.sub("日", "", matchobj)
        return matchobj
    s = re.sub(pattern2, replace2, s)

    pattern3 = re.compile(r"(\d{1,}.\d{3}.\d{3}.\d{3})|(\d{1,}.\d{3}.\d{3})|(\d{1,}.\d{3})|(\d+.\d+)")
    def replace3(matchobj):
        matchobj = matchobj.group(0)
        # string = matchobj[0].replace(",", "")
        string = matchobj.replace(",", "")
        string = string.replace("，", "")
        return string
    s = re.sub(pattern3, replace3, s)

    pattern4 = re.compile(r"(\d+\.?\d+万)")
    def replace4(matchobj):
        matchobj = matchobj.group(0)
        # num = matchobj[0][:-1]
        num = matchobj[:-1]
        new_num = float(num) * 10000
        return str(new_num)
    s = re.sub(pattern4, replace4, s)

    return s


def output_data(model_name, path_model_name):
    filename_predict = os.path.join("result", model_name+"_predict.utf8")
    filename_result = os.path.join("result", model_name+".txt")
    if model_name == "zengjianchi":
        result = "公告id	股东全称	股东简称	变动截止日期	变动价格	变动数量	变动后持股数	变动后持股比例"
    elif model_name == "hetong":
        result = "公告id	甲方	乙方	项目名称	合同名称	合同金额上限	合同金额下限	联合体成员"
    elif model_name == "dingzeng":
        result = "公告id  增发对象    增发数量	增发金额	锁定期	认购方式"
    elif model_name == "test":
        result = ""
    with open(filename_predict, "r", encoding="utf-8") as f:
        flag = True
        temp_result = ["\t" for i in range(8)]   #用于保存一行结构化的实体
        temp2_result = []    #保存临时重复出现的实体
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
                    if int(predict_type) == 1:
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
                    # 这个地方还是没处理好，很多不应该存在的多余的结构化数据，而且导致一些实体数据被分散在多余的结构化数据中。
                    # 有两个思路，第一个思路是在遍历到下一个公告之前，同一个公告的信息用嵌套列表存储，然后重复出现的实体依次往后放
                    # 在下一个子列表中，然后添加实体的时候从最前面的列表开始检索相应位置是否是空着的，如果空着的就填入，最后把长度不够的子列表去除！
                    # 更好的思路是用一个临时列表temp2_result保存重复的实体，不重复的实体先放在当前temp_result，当temp2_result中非空的元素长度与
                    # temp_result相同时（根据规律，文本中出现的重复结构化数据多为列表表示，所以实体数量基本相等），
                    # 则认为是属于同一个公告的结构化数据,temp_result添加到最终result中，temp2_result中的值转移到temp_result中，
                    # 然后自身赋值为空数组
                    # elif temp_result[int(predict_type)-1] == "\t":
                    #     if temp2_result == []:  #如果出现了重复实体且temp2_result为空
                    #         count1, count2 =0, 0
                    #         announce_id = temp_result[0]
                    #         temp2_result = ["\t" for i in range(8)]
                    #         temp2_result[0] = announce_id
                    #         temp2_result[int(predict_type)-1] = entity
                    #         entity = ""
                    #     else:
                    #         if temp2_result[int(predict_type)-1] == "\t":
                    #             temp2_result[int(predict_type)-1] = entity
                    #         entity = ""  #如果出现的重复实体在临时列表中已经重复了，则忽略
                    #     for e in temp_result:
                    #         if e != "\t":
                    #             count1 += 1
                    #     for e in temp2_result:
                    #         if e != "\t":
                    #             count2 += 1
                    #     if count1 == count2:    #如果实体数量相同了
                    #         result = result + "\t".join(temp2_result) + "\n"
                    #         temp2_result = []

                    #下面的方法是简单粗暴地出现重复的公司名称时就认为是另一条结构化数据
                    elif int(predict_type) == 2 and temp_result[1] != "\t":
                        announce_id = temp_result[0]
                        result = result + "\t".join(temp_result) + "\n"
                        temp_result = ["\t" for i in range(8)]
                        temp_result[0] = announce_id
                        temp_result[int(predict_type)-1] = entity
                        entity = ""
                    else:
                        entity = ""
    with open(filename_result, "w", encoding="utf-8") as f:
        f.write(result)

def text_cut(s):
    # s = "dhasjdh jklasd打开就好撒考虑到认购大开大合就卡死好dsdsadd认购的数据爱可登拉丝机贷款了"
    # print(s)
    index_list = []
    interval_id = Interval(0, 20)
    index_list.append(interval_id)
    length_s = len(s)
    pattern = re.compile(r"(认购)")
    matchobj = re.search(pattern, s, flags=0)
    if matchobj:
        index = matchobj.start()
        index_list.append(Interval(index, index+2))
    while matchobj:
        last_index = index + 2
        matchobj = re.search(pattern, s[last_index:], flags=0)
        if not matchobj:
            break
        index = matchobj.start()
        index = index + last_index
        # index_list.append(Interval(index, index+2)) #原始区间
        index_list.append(Interval(index-1000, index+1000)) #区间膨胀
    index_list = merge(index_list)
    new_s = ""
    for interval in index_list:
        start = interval.start
        end = interval.end
        if start < 0:
            start = 0
        if end > length_s-1:
            end = length_s-1
        new_s += s[start:end]
    return new_s

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    intervals.sort(key = lambda x:x.start)
    len1 = len(intervals)
    res = []
    for i in range(len1):
        if res == []:
            res.append(intervals[i])
        else:
            len2 = len(res)
            if res[len2-1].start <= intervals[i].start <= res[len2-1].end :
                res[len2-1].end = max(intervals[i].end, res[len2-1].end)
            else:
                res.append(intervals[i])
    return res

if __name__ == "__main__":
    pass
    # read_data(dirname_zengjianchi, dirname_txt_zengjianchi)
    # process_data(dirname_txt2_zengjianchi)
    # output_data(filename_predict_zengjianchi, filename_result_zengjianchi)

    # read_data(dirname_hetong, dirname_txt_hetong)
    # process_data(dirname_txt2_hetong)
    # output_data(filename_predict_hetong, filename_result_hetong)

    # read_data(dirname_dingzeng, dirname_txt_dingzeng)
    # process_data(dirname_txt2_dingzeng)
    # output_data(filename_predict_dingzeng, filename_result_dingzeng)

    # model_names = ["zengjianchi", "hetong", "dingzeng"]