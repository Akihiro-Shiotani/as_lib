#%%
import os 
import cv2
from PIL import Image
import numpy as np

#OpenCVの日本語無効を回避したimread
def imread(path):
    tmp_dir = os.getcwd()
    # 1. 保存するディレクトリに移動
    file_dir = os.path.dirname(path)
    os.chdir(file_dir)
    img = cv2.imread(os.path.basename(path))
    # カレントディレクトリをもとに戻す
    os.chdir(tmp_dir)
    return img

#OpenCVの日本語無効を回避したimwrite
def imwrite(path, img):
    tmp_dir = os.getcwd()
    # 1. 保存するディレクトリに移動
    file_dir = os.path.dirname(path)
    os.chdir(file_dir)
    # 2. 対象ファイルを保存
    tmp_name = "tmp_name.png"
    cv2.imwrite(tmp_name, img)
    os.rename(tmp_name, os.path.basename(path))
    # カレントディレクトリをもとに戻す
    os.chdir(tmp_dir)

#pillowからopencv変換
def pil_to_cv(image):
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image

#opencvからpillow変換
def cv_to_pil(image):
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image