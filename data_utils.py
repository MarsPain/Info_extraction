import html2text
import os

dirname_zengjianchi = "data/round1_train_20180518/增减持/html"
dirname_dingzeng = "data/round1_train_20180518/定增/html"
dirname_hetong = "data/round1_train_20180518/重大合同/html"
dirname_txt_zengjianchi = "data/round1_train_20180518/增减持/txt"
dirname_txt_dingzeng = "data/round1_train_20180518/定增/txt"
dirname_txt_hetong = "data/round1_train_20180518/重大合同/txt"

def read_data(dirname, dirname_txt):
    h2t = html2text.HTML2Text() #初始化html2text工具
    h2t.ignore_links = True #表示忽略html页面中的链接
    count = 0
    for filename in os.listdir(dirname):
        filename_txt = os.path.join(dirname_txt, filename[:-5]+".txt")
        filename = os.path.join(dirname, filename)
        with open(filename, "r", encoding="utf-8") as f:
            f = f.read()
            s = h2t.handle(f)
            s = s.replace(" ", ""); s = s.replace("\n", "")
            while count<1:
                print(s)
                count += 1
                with open(filename_txt, "w", encoding="utf-8") as f_txt:
                    f_txt.write(s)

if __name__ == "__main__":
    read_data(dirname_zengjianchi, dirname_txt_zengjianchi)