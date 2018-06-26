import html2text

filename_zengjianchi = "data/round1_train_20180518/增减持/html"
filename_dingzeng = "data/round1_train_20180518/定增/html"
filename_hetong = "data/round1_train_20180518/重大合同/html"

def read_data(filename):
    filename = filename + "/6927.html"
    h2t = html2text.HTML2Text()
    with open(filename, "r", encoding="utf-8") as f:
        f = f.read()
        print(h2t.handle(f))

if __name__ == "__main__":
    read_data(filename_zengjianchi)