# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

def write_tag(path,char_list,tag_list):
    with open(path, 'w', encoding='utf8') as file:
        for i,char in enumerate(char_list):
            if(tag_list[i]==[]):
                tag_list[i].append('O')
            file.write(char+'\t'+'\t'.join(tag_list[i])+'\n')
def make_tag(tag_list,start, word_len, tag_type):
    tag_list[start].append('B-' + str(tag_type))
    tag_list[start + word_len - 1].append('E-' + str(tag_type))
    if (word_len > 2):
        for i in range(1, word_len - 1):
            tag_list[start + i].append('I-' + str(tag_type))
    return tag_list
def check_duplicate(tag_list,start,word_len):
    flag = 0
    for i in range(word_len):
        for j in tag_list[start + i]:
            if (j in tags):
                flag = 1
    return flag
# if __name__ == '__main__':
def match_by_row(model_name):
    # txt_dir = 'dingzeng/'#'' 'hetong/'
    # train_dir = 'dingzeng/dingzeng.train'   #'zengjianchi.train' 'hetong/hetong.train'
    txt_dir = os.path.join("data/round1_train_20180518", model_name+"/")
    train_dir = os.path.join("data/round1_train_20180518", model_name+"/"+model_name+".train")
    df = pd.read_csv(train_dir, encoding='utf8', sep='\t', header=None)
    df = df.replace(np.nan, '')
    df = df.drop(2,axis=1)
    global tags
    tags = []
    for i in [1,2,3,4,6,5,7,8]:
        tags.append('B-'+str(i))
        tags.append('E-' + str(i))
        tags.append('I-' + str(i))
    num = 0
    file_str= None
    for row in df.itertuples(index=True, name='Pandas'):
        if(num != row[1]):
            if(file_str!=None):
                write_tag(txt_dir+'txt2/t_'+str(num)+'.txt',char_list,tag_list)
            num = row[1]
            with open(txt_dir+'txt/'+str(num)+'.txt','r',encoding='utf8') as f:
                file_str = f.read()
            char_list = list(file_str)
            tag_list = [[]for i in range(len(char_list))]
        for col in range(1,7):
            word = str(row[col])
            if((col==3)|(col==4)|(col==5)):#对数字的处理 222.0改为222
                if(word.endswith('.0')):
                    word = word.replace('.0','')
            if(word==''):
                continue
            start = 0
            first = 1#是否第一次查找
            word_len = len(word)
            while (True):
                if (first):
                    start = file_str.find(word)
                    # if start == -1:
                    #     print('未找到：',word)
                    #     if (col==3)|(col==4):
                    #         if '.' in word:
                    #             print('小数，尝试删除一位查找')
                    #             word = word[:,-1]
                    first = 0
                else:
                    start = file_str.find(word, start + word_len)
                if (start == -1):#找不到退出循环，开始下个词
                    break
                else:
                    # 检查是否有本词典的其他标记
                    flag = check_duplicate(tag_list,start,word_len)
                    if flag:
                        continue
                    tag_list = make_tag(tag_list,start, word_len, col)

    write_tag(txt_dir+'txt2/t_' + str(num) + '.txt', char_list, tag_list)
    pass



