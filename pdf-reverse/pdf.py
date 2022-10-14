import pynput
from pynput.keyboard import Controller, Key, Listener
from pynput.mouse import Button

def on_click(x, y, button, pressed):
    # 实例化键盘
    kb = Controller()

    # 使用键盘输入一个字母
    kb.press(Key.ctrl)
    kb.press(Key.alt)
    kb.press('.')
    kb.release(Key.ctrl)
    kb.release(Key.alt)
    kb.release('.')
    kb.pressed(Key.ctrl,Key.alt,'.')
    if button == Button.right:
        print("关闭")
        return False·
    with pynput.mouse.Listener(
    on_click=on_click,) as listener:
    listener.join()


def get_file_name(file_dir):
    '''
    获取指定目录下所有文件名称
    :param file_dir:指定目录
    :return:返回文件名列表
    '''
    for root, dirs, files in os.walk(file_dir):
        # return root#当前目录路径
        # return dirs#当前路径下所有子目录
        return files  # 当前路径下所有非目录子文件


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


if __name__ == '__main__':
    filenames = get_file_name(file_dir)
    print(filenames)
    conver_img()