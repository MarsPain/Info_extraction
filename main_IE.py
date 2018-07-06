from data_utils_main import read_data, process_data, output_data
from main import main_ner
from match_by_row2 import match_by_row, sort_by_row
import os

# is_train = True
# is_train = False

path = "data/round1_train_20180518"
test_path = "./test_data"

def main_IE():
    # model_names = ["zengjianchi", "hetong", "dingzeng"]
    model_names = ["zengjianchi"]
    for model_name in model_names:
        #训练和验证
        path_model_name = os.path.join(path, model_name)
        pass
        #从html文件中读取文本并进行加工处理
        # read_data(model_name, path_model_name)
        #用最大正向匹配进行自动标注
        # match_by_row(model_name, path_model_name)
        #将被标注的文件分割成train、dev、test三个文件
        # process_data(model_name, path_model_name, True)
        #对训练集进行训练
        # main_ner(True, model_name, path_model_name)
        #对验证集进行预测并输出预测结果
        # main_ner(False, model_name, path_model_name)  #不要轻易使用该函数，会覆盖result中的预测
        #将上一步输出的命名实体识别结果进行结构化的输出
        # output_data(model_name, path_model_name)

        #对官方测试集进行预测
        test_path_model_name = os.path.join(test_path, model_name)
        # read_data(model_name, test_path_model_name)
        # sort_by_row(model_name, test_path_model_name)
        # process_data(model_name, test_path_model_name, False)
        maps_path =  path_model_name   #训练时生成的字典的路径
        main_ner(False, model_name, test_path_model_name, maps_path)
        # output_data(model_name, test_path_model_name)

if __name__ == "__main__":
    main_IE()