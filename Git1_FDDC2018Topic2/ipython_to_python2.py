# coding=utf-8
import sys
import os.path
import re
import logging
from bs4 import BeautifulSoup
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)

def prase_all(file_dir, test_file_number):
    pathDir = os.listdir(file_dir)
    file_path_list = list()
    for allDir in pathDir:
        child = os.path.join('%s%s' % (file_dir, allDir))
        file_path_list.append(child)
    for filename in file_path_list:
        #print(filename)
        pdf2TxtManager = CPdf2TxtManager()
        pdf2TxtManager.changePdfToText(filename)
        test_file_number += -1
        if test_file_number == 0:
            break

class CPdf2TxtManager():
    def __init__(self):
        '''''
        Constructor
        '''
    def changePdfToText(self, file_path):
        file = open(file_path, 'rb')
        praser = PDFParser(file)
        file.close()
        doc = PDFDocument()
        praser.set_document(doc)
        doc.set_parser(praser)
        doc.initialize()
        if not doc.is_extractable:
            #raise PDFTextExtractionNotAllowed
            print(file_path)
            return 0
        else:
            rsrcmgr = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams = laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            results = ""
            for page in doc.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if hasattr(x, "get_text"):
                        results += x.get_text()
            #no_space_results = re.sub(r'\s+', '', results)
            #results = results.replace('/n', ' ')
            #print(no_space_results + '\n')
            return results

def load_file(file_name):
    f = open("F:\\FDDC2018data\\round1_train_20180518\\重大合同\\" + file_name + ".txt","rb")
    lines = f.readlines()
    lines_str = list()
    for item in lines:
        tmp = str(item, encoding = 'utf-8')
        tmp = tmp.replace(' ',' ')
        tmp = tmp.replace(' ','(.+?)')
        tmp = tmp.replace("\r\n", '')
        tmp = tmp.replace("\ufeff", '')
        lines_str.append(tmp)
    return lines_str

def find(keydict, text):
    name = ""
    for item in keydict:
        p = re.compile(r'' + item)
        if len(p.findall(text)):
            if (not ('，' in p.findall(text)[0])) & (not ('。' in p.findall(text)[0])):
                name = p.findall(text)[0]
                break
    return name

def prefix_check(keydict, name):
    for item in keydict:
        if re.match(item, name):
            if re.match(item,name).span(0)[0] == 0:
                name = name.lstrip(item)
                break
    return name

def suffix_check(keydict, name):
    for item in keydict:
        p = re.compile(r'' + item + "$")
        if len(p.findall(name)):
            name = name.rstrip(item)
            break
    return name

def brackets_check(keydict, text):
    name = text
    flag = False
    if re.compile('（(.+?)）').findall(name):
        tmp = re.compile('（(.+?)）').findall(name)
        for item1 in tmp:
            for item2 in keydict:
                if item1.find(item2):
                    p = re.compile('（' + item1 + '）')
                    name = p.sub('', name)
                    flag = True
    if re.compile(r'[(](.+?)[)]').findall(name):
        tmp = re.compile(r'[(](.+?)[)]').findall(name)
        for item1 in tmp:
            for item2 in keydict:
                if item1.find(item2):
                    p = re.compile('[(]' + item1 + '[)]')
                    name = p.sub('', name)
                    flag = True
    if flag == False:
        return text
    else:
        return name

def re_analyse(text):
    no_space_text = re.sub(r'\s+', '', text)
    print(text)
    #id

    #Party A
    party_a = find(party_a_dict, no_space_text)

    if len(party_a):
        eng_re = re.compile(r'[a-zA-Z]')#English Company Name
        if len(re.findall(eng_re, party_a)):
            party_a = find(party_a_dict, text)
            party_a = party_a.strip()
        party_a = prefix_check(cprefix, party_a)
        party_a = suffix_check(csuffix, party_a)
        party_a = brackets_check(cbrk, party_a)

    print("Party A:")
    print(party_a)
    #Party B
    party_b = find(party_b_dict, no_space_text)

    if len(party_b):
        party_b = brackets_check(cbrk, party_b)

    print("Party B:")
    print(party_b)
    #Project Name
    project_name = find(project_name_dict, no_space_text)

    project_name_list = list()
    if len(project_name):
        project_name_list = re.compile('“(.+?)”').findall(project_name)

    print("Project Name:")
    if len(project_name_list):
        for item in project_name_list:
            print(item)
    else:
        print(project_name)
    #print(" ".join(str(i) for i in project_name_list))
    #Contract Name
    contract_name = find(contract_name_dict, no_space_text)
    #if len(contract_name):

    print("Contract Name:")
    print(contract_name)
    #Minimum contract amount
    #Maximum contract amount
    #Consortium members
    member_name = find(member_name_dict, no_space_text)
    if len(member_name):
        member_name.replace('、', '\n')

    print("Member' Name:")
    print(member_name)

if __name__ == '__main__':
    #prase_all('F:\\FDDC2018data\\round1_train_20180518\\重大合同\\pdf\\', 1)
    path = u'F:\\FDDC2018data\\round1_train_20180518\\重大合同\\pdf\\1518.pdf'
    pdf2TxtManager = CPdf2TxtManager()
    text = pdf2TxtManager.changePdfToText(path)
    party_a_dict = load_file("party_a_re")
    party_b_dict = load_file("party_b_re")
    contract_name_dict = load_file("contract_re")
    project_name_dict = load_file("project_re")
    member_name_dict = load_file("members_re")
    cprefix = load_file("correction_prefix")
    csuffix = load_file("correction_suffix")
    cbrk = load_file("correction_brackets")
    re_analyse(text)