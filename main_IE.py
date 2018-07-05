from data_utils_main import read_data, process_data, output_data

def main_IE():
    model_names = ["zengjianchi", "hetong", "dingzeng"]
    # model_names = ["zengjianchi"]
    for model_name in model_names:
        read_data(model_name)
        process_data(model_name)
        output_data(model_name)

if __name__ == "__main__":
    main_IE()