import os
import xlwings
from PIL import Image, ImageDraw, ImageFont


# 在图片上添加文字并居中显示  alignment=0居中(默认)，-1左对齐，1右对齐
def AddText(target_image, text, text_font, text_size, text_color, alignment=0):
    tar = Image.open(target_image)
    width, height = tar.size
    font = ImageFont.truetype(text_font, text_size)
    w, h = font.getsize(text)
    draw = ImageDraw.Draw(tar)
    if alignment == 0:
        draw.text(((width - w) / 2, (height - h) / 2), text, fill=text_color, font=font)
    if alignment == -1:
        draw.text((0, (height - h) / 2), text, fill=text_color, font=font)
    if alignment == 1:
        draw.text((width - w, (height - h) / 2), text, fill=text_color, font=font)
    tar.save(target_image)


if __name__ == '__main__':
    app = xlwings.App(visible=True, add_book=False)
    wb = app.books.open('员工信息表.xlsx')
    os.makedirs(r'C:\Users\KDA帅\Desktop\WorkSpace\tel', 0o777, True)

    for i in range(2, 51):
        wd = wb.sheets['Sheet1'].range('A' + str(i)).value + '  电话：' + str(
            wb.sheets['Sheet1'].range('F' + str(i)).value)
        name = wb.sheets['Sheet1'].range('A' + str(i)).value + '-电话号码.png'
        bg = Image.new('RGB', (321, 100), 'white')
        bg.save('tel\\' + name)
        AddText('tel\\' + name, wd, 'simsun.ttc', 20, 'black')
    app.kill()  # 强制关闭进程 释放内存
