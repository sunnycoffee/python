import math


def main():
    rate = 0.049 / 12.0
    print(rate)
    s =  540000 * rate * (1 + rate) ** 360 / ((1 + rate) ** 360 - 1) 
    print(s)


def main2(s):
    rate = 0.049 / 12.0
    total =  s *  ((1 + rate) ** 360 - 1) /(rate * (1 + rate) ** 360 )
    print(total)


def conver_img():
    for filename in filenames:
        # pdf_name = os.path.splitext(pdf)[0]
        print(filename)

        doc = fitz.open(f'{file_dir}/{filename}')

        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            # pm.writePNG('%s.png' % pg)
            pm.writePNG(f'jpg/{pg}.jpg')


def main3(s):
    rate = 0.049 / 12.0
    total =  s *  ((1 + rate) ** 360 - 1) /(rate * (1 + rate) ** 360 )
    print(total)


def main4(s):
    rate = 0.049 / 12.0
    total =  s *  ((1 + rate) ** 360 - 1) /(rate * (1 + rate) ** 360 )
    print(total)


def main5(s):
    rate = 0.049 / 12.0
    total =  s *  ((1 + rate) ** 360 - 1) /(rate * (1 + rate) ** 360 )
    print(total)

main()
