# 主要方法

1. 主要用了两种方法，第一种方法为直接用原数据训练命名实体识别模型，然后对测试文本进行实体识别，然后将识别出的实体进行结构化的输出，为端对端的方法；第二种方法为先对html进行解析，得到结构化的表格数据，然后对非结构化的文本数据进行命名实体识别。
2. main_IE为主要运行文件，用main_app方法对zengjianchi数据进行信息抽取，用main_IE方法对hetong和dingzeng数据进行信息抽取。

# 基本目录信息

1. ChineseNER：中文NER模型代码；
2. config: 解析html表格数据的json配置文件；
3. docparser： 对文档进行解析
4. extract: 基于docparser解析后的结果进行信息抽取
5. ltp_data_v3.4:ltp模型
6. ner:命名实体识别工具
7. result:信息抽取结果
8. test_data：测试数据