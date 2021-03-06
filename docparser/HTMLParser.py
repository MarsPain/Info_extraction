#-*- coding: utf-8 -*-

import codecs

from bs4 import BeautifulSoup

from utils import TextUtils


class HTMLParser(object):

    def __init__(self):
        pass

    def parse_content(self, html_file_path):
        """
        解析 HTML 中的段落文本
        按顺序返回多个 paragraph 构成一个数组，
        每个 paragraph 是一个 content 行构成的数组
        :param html_file_path:
        :return:
        """
        rs = []
        with codecs.open(html_file_path, encoding='utf-8', mode='r') as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")
            paragraphs = []
            for div in soup.find_all('div'):
                div_type = div.get('type')
                #添加div_type == 'paragraph'的div块中的文本
                if div_type is not None and div_type == 'paragraph':
                    paragraphs.append(div)
            for paragraph_div in paragraphs:
                has_sub_paragraph = False   #判断paragraph中是否有子paragraph
                for div in paragraph_div.find_all('div'):
                    div_type = div.get('type')
                    if div_type is not None and div_type == 'paragraph':
                        has_sub_paragraph = True
                if has_sub_paragraph:
                    continue    #若存在子paragraph则continue，因为后面会遍历到该paragraph
                rs.append([])   #每个paragraphs中的content保存在rs的子列表中
                #将paragraph中的content添加到列表中
                for content_div in paragraph_div.find_all('div'):
                    div_type = content_div.get('type')
                    if div_type is not None and div_type == 'content':
                        rs[-1].append(TextUtils.clean_text(content_div.text))
        paragraphs = []
        for content_list in rs:
            if len(content_list) > 0:
                paragraphs.append(''.join(content_list))    #每个content_list结合在一起成为一个字符串
        return paragraphs

    def parse_table(self, html_file_path):
        """
        解析 HTML 中的 table
        返回一个二维表
        :param html_file_path:
        :return:
        """
        rs_list = []
        with codecs.open(html_file_path, encoding='utf-8', mode='r') as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")
            for table in soup.find_all('table'):
                table_dict, is_head_two_rowspan = self.parse_table_to_2d_dict(table)
                row_length = len(table_dict)
                if table_dict is not None:
                    if is_head_two_rowspan and row_length > 2:
                        try:
                            new_table_dict = {}
                            head_row = {}
                            col_length = len(table_dict[0])
                            for col_idx in range(col_length):
                                head_row[col_idx] = table_dict[0][col_idx] + table_dict[1][col_idx]
                            new_table_dict[0] = head_row    #第一行是表头
                            for row_idx in range(2, row_length):
                                new_table_dict[row_idx - 1] = table_dict[row_idx]
                            rs_list.append(new_table_dict)
                        except KeyError:
                            rs_list.append(table_dict)
                    else:
                        rs_list.append(table_dict)
        return rs_list

    @staticmethod
    def parse_table_to_2d_dict(table):
        rs_dict = {}
        row_index = 0
        is_head_two_rowspan, is_head = False, True
        for tr in table.find_all('tr'): #tr为表格的一行
            col_index, cur_col_index = 0, 0
            for td in tr.find_all('td'):    #查找每一行中每个单元中的数据
                rowspan = td.get('rowspan') #列方向的单元跨越行数（所占行数），即一个单元格的元素对应多行数据
                rowspan = int(rowspan) if (rowspan is not None and int(rowspan) > 1) else 1
                colspan = td.get('colspan') #行方向的单元跨越行数（所占列数）
                colspan = int(colspan) if (colspan is not None and int(colspan) > 1) else 1
                if is_head:
                    if rowspan > 1 or colspan > 1:  #is_head_two_rowspan和is_head具体有什么意义？
                        is_head_two_rowspan = True
                    is_head = False
                for r in range(rowspan):
                    if (row_index + r) not in rs_dict:  #每一行创建一个字典存储一行的信息
                        rs_dict[row_index + r] = {}
                    for c in range(colspan):
                        cur_col_index = col_index
                        while cur_col_index in rs_dict[row_index + r]:
                            cur_col_index += 1
                        #将信息添加到每一行的字典中，键值对为列索引和具体的文本
                        rs_dict[row_index + r][cur_col_index] = TextUtils.remove_blank_chars(td.text)   #这里是双重字典
                        cur_col_index += 1
                col_index = cur_col_index
            row_index += 1
        return rs_dict, is_head_two_rowspan
