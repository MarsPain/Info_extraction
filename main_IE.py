from data_utils_main import read_data, process_data, output_data
from main import main_ner

# is_train = True
# is_train = False

def main_IE():
    # model_names = ["zengjianchi", "hetong", "dingzeng"]
    model_names = ["zengjianchi"]
    for model_name in model_names:
        #从html文件中读取文本并进行加工处理
        # read_data(model_name)
        #用最大正向匹配进行自动标注
        pass
        #将被标注的文件分割成train、dev、test三个文件
        # process_data(model_name)
        #对训练集进行训练
        # main_ner(True, model_name)
        #对测试集进行预测
        # main_ner(False, model_name)
        #将命名实体识别结果进行结构化的输出
        # output_data(model_name)

if __name__ == "__main__":
    main_IE()