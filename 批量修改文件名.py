import os


# 转换jpg为png
def TransferFormat_fromJPGtoPNG(path):
    if path[-1] != '\\':
        path += '\\'
    for i in os.listdir(path):
        os.rename(path + i, path + i.replace('jpg', 'png'))

        
# 批量修改文件名
def RenameFile():
    path = r'C:\Users\KDA帅\Desktop\HR\证件照'
    name = os.listdir(path)
    for i in name:
        if '1' in i:
            os.rename(path + '\\' + i, path + '\\' + i.replace('1', '-身份证正面'))
        if '2' in i:
            os.rename(path + '\\' + i, path + '\\' + i.replace('2', '-身份证反面'))
