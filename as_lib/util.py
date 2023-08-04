#%%
import os
import sys
import shutil
import __main__

#exeファイル、pyファイルに依らず実行ファイルのパスを取得
def getpath():
    path = sys.argv[0]
    if os.path.splitext(path)[1] == '.py':
        path = __main__.__file__
    return path

#ディレクトリ作成関数
def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

#ディレクトリを消して作成
def renewdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)

#ディレクトリ削除
def deldir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

if __name__ == '__main__':
    path = getpath()
    print(path)
    dir_path = os.path.dirname(path)+r'\test'
    mkdir(dir_path)
    renewdir(dir_path)
    deldir(dir_path)
    