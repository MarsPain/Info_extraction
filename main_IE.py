from data_utils_main import read_data, process_data, output_data
from ChineseNER.main import main_ner
from match_by_row3 import match_by_row, sort_by_row
import os

# is_train = True
# is_train = False

path = "data/round1_train_20180518"
test_path = "./test_data"
# test_path = "./test_dataB"

def main_IE():
    # model_names = ["zengjianchi", "hetong", "dingzeng"]
    model_names = ["zengjianchi"]
    for model_name in model_names:
        #训练和验证
        path_model_name = os.path.join(path, model_name)
        maps_path = path_model_name
        pass
        #从html文件中读取文本并进行加工处理
        # read_data(model_name, path_model_name)
        #用最大正向匹配进行自动标注
        # match_by_row(model_name, path_model_name)
        #将被标注的文件分割成train、dev、test三个文件
        # process_data(model_name, path_model_name, True)
        #对训练集进行训练
        #若导入了已训练好的模型参数，需要删除data_train中的字典maps_pkl并重新生成，否则可能出现标签种类数量（tensor）无法对齐的问题
        #若要重新训练，则需要删除model_ckpt下面已经保存好的相应模型参数
        # main_ner(True, model_name, path_model_name, maps_path)
        #对验证集进行预测并输出预测结果
        main_ner(False, model_name, path_model_name, maps_path)  #不要轻易使用该函数，会覆盖result中的预测
        #将上一步输出的命名实体识别结果进行结构化的输出
        # output_data(model_name, path_model_name)

        #对官方测试集进行预测
        test_path_model_name = os.path.join(test_path, model_name)
        # read_data(model_name, test_path_model_name)
        # sort_by_row(model_name, test_path_model_name)
        # process_data(model_name, test_path_model_name, False)
        maps_path = path_model_name   #训练时生成的字典的路径
        # main_ner(False, model_name, test_path_model_name, maps_path)    #若模型有大的变化，需要删除model_ckpt下面的模型参数以及data_train中的字典并重新训练，否则可能出现标签种类数量无法对齐的问题
        # output_data(model_name, test_path_model_name)

if __name__ == "__main__":
    main_IE()