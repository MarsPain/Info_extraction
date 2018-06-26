import html2text
import os

dirname_zengjianchi = "data/round1_train_20180518/增减持/html"
dirname_dingzeng = "data/round1_train_20180518/定增/html"
dirname_hetong = "data/round1_train_20180518/重大合同/html"

def read_data(dirname):
    # filename = dirname + "/6927.html"
    h2t = html2text.HTML2Text() #初始化html2text工具
    h2t.ignore_links = True #表示忽略html页面中的链接
    count = 0
    for filename in os.listdir(dirname):
        filename = os.path.join(dirname, filename)

        with open(filename, "r", encoding="utf-8") as f:
            f = f.read()
            while count<100:
                print(h2t.handle(f))
                count += 1

if __name__ == "__main__":
    read_data(dirname_zengjianchi)