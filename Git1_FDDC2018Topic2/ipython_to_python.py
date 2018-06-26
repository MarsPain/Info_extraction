#this code is for extracting text for training
# coding=utf-8
import sys
import os.path
import re

import logging
# from bs4 import BeautifulSoup
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)

def prase_all(file_dir, test_file_number):
    print("Yes!!!!!!!!")
    pathDir = os.listdir(file_dir)
    file_path_list = list()
    for allDir in pathDir:
        child = os.path.join('%s%s' % (file_dir, allDir))
        file_path_list.append(child)
    for filename in file_path_list:
        print(filename)
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
            results = re.sub(r'\s+', '', results)
            #results = results.replace('/n', ' ')
            #print(file_path)
            #print(results)
            txt_path = file_path
            f = open(txt_path.replace('pdf', 'txt'),'wb')
            f.write(bytes(results, encoding = "utf-8"))
            file.close()

if __name__ == '__main__':
    prase_all('data', -1)
    #path = u'F:\\FDDC2018data\\round1_train_20180518\\重大合同\\pdf\\1008828.pdf'
    #pdf2TxtManager = CPdf2TxtManager()
    #pdf2TxtManager.changePdfToText(path)