import zipfile
myZip = zipfile.ZipFile("./channel.zip")

changedfile ="90052.txt"
readme = ""
while(1):
    filename = "./channel/" + changedfile
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()
        num = data.split("nothing is ")[1]
        zp_info = myZip.getinfo(changedfile)
        comment = zp_info.comment.decode('utf-8')
        print(comment, end='')
        changedfile = num + ".txt"