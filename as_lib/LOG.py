#%%
import os
import logging
import logging.handlers
from as_lib import util

def test():
    config(level=logging.INFO)
    logging.debug('テスト')

def config(outpath='Default', level=logging.INFO, n=30, unit='D'):
    #出力ディレクトリの設定
    if outpath == 'Default':
        outpath = os.path.dirname(util.getpath())
    util.mkdir(outpath)
    
    #ログファイル名の設定
    logname = os.path.basename(os.path.splitext(util.getpath())[0])+'.log'
    
    #ログ出力設定
    formatter = '[%(asctime)s] %(levelname)s : %(message)s'
    #コンソール表示設定
    stream_handler = logging.StreamHandler()
    # ログレベルの設定
    stream_handler.setLevel(level)
    # ログ出力フォーマットを設定
    stream_handler.setFormatter(logging.Formatter(formatter))
    #ファイル出力設定
    file_handler = logging.handlers.TimedRotatingFileHandler(logname, when=unit, interval=n, backupCount=5)
    # ログレベルの設定
    file_handler.setLevel(level)
    # ログ出力フォーマットを設定
    file_handler.setFormatter(logging.Formatter(formatter))
    
    #ログ出力設定
    logging.basicConfig(level=level, handlers=[stream_handler, file_handler], force=True)

if __name__ == '__main__':
    test()