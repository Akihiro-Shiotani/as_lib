#%%
import os
import sys
import __main__

#exeファイル、pyファイルに依らず実行ファイルのパスを取得
def getpath():
    path = sys.argv[0]
    if os.path.splitext(path)[1] == '.py':
        path = __main__.__file__
    return path