import os


# 转换jpg为png
def TransferFormat_fromJPGtoPNG(path):
    if path[-1] != '\\':
        path += '\\'
    for i in os.listdir(path):
        os.rename(path + i, path + i.replace('jpg', 'png'))

        
# 批量替换文件夹下所有文件的名称
def RenameFile(filepath, old_str, new_str):
    path = filepath  # 文件夹路径
    name = os.listdir(path)
    for i in name:
        if old_str in i:
            os.rename(path + '\\' + i, path + '\\' + i.replace(old_str, new_str))


