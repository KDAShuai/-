from PIL import Image



# 剪裁图片的指定范围
def CropImage(filein, fileout, x1, y1, x2, y2):
    img = Image.open(filein)
    out = img.crop((x1, y1, x2, y2))
    out.save(fileout)
    
    
# 批量剪裁文件夹下所有的图片
def CropAllImage(folderpath, x1, y1, x2, y2):
    target = FindTargetIMage(folderpath)
    for tar in target:
        try:
            CropImage(folderpath + '/' + tar, folderpath + '/' + 'Croped-' + tar, x1, y1, x2, y2)
        except ():
            print('图片“%s”转换失败' % tar)
  

# 调整图片尺寸
def ResizeImage(filein, fileout, length, width):
    img = Image.open(filein)
    out = img.resize((length, width), Image.ANTIALIAS)  # ANTIALIAS为抗锯齿
    out.save(fileout)

    
# 批量调整文件夹下所有图片的尺寸
def ResizeAllImage(folderpath, length, width):
    target = FindTargetIMage(folderpath)
    for tar in target:
        if os.path.isfile(tar):
            try:
                ResizeImage(folderpath + '\\' + tar, folderpath + '\\' + tar, length, width)
            except ():
                print('图片“%s”转换失败' % tar)
    
    
# 垂直合并图片
def MergeImage_Vertical(img1, img2, spacing=20):
    i1 = Image.open(img1)
    i2 = Image.open(img2)
    i3 = Image.new(i1.mode, (max(i1.width, i2.width), i1.height + i2.height + spacing), 'white')
    i3.paste(i1, (0, 0))
    i3.paste(i2, (0, spacing + i1.height))
    return i3


# 水平合并图片
def MergeImage_Horizontal(img1, img2, spacing=20):
    i1 = img1
    i2 = img2
    i3 = Image.new(i1.mode, (i1.width + i2.width + spacing, max(i1.height, i2.height)), 'white')
    i3.paste(i1, (0, 0))
    i3.paste(i2, (spacing + i1.width, 0))
    return i3
