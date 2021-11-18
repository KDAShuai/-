import os


# 转换jpg为png
def TransferFormat_fromJPGtoPNG(path):
    if path[-1] != '\\':
        path += '\\'
    for i in os.listdir(path):
        os.rename(path + i, path + i.replace('jpg', 'png'))
