#%%
import os
import logging
import logging.handlers
import function

def log_setting(outpath='Default', n=30, unit='D'):
    #ログファイル出力ディレクトリに移動
    if outpath == 'Default':
        outpath = os.path.dirname(function.getpath())
    if os.path.isdir(outpath) == False:
        os.mkdir(outpath)
    os.chdir(outpath)
    
    filename = os.path.basename(os.path.splitext(function.getpath())[0])+'.log'
    
    #ログ出力設定
    formatter = '[%(asctime)s] %(levelname)s : %(message)s'
    #コンソール表示設定
    stream_handler = logging.StreamHandler()
    # ログレベルの設定
    stream_handler.setLevel(logging.INFO)
    # ログ出力フォーマットを設定
    stream_handler.setFormatter(logging.Formatter(formatter))

    #ファイル出力設定
    file_handler = logging.handlers.TimedRotatingFileHandler(filename, when=unit, interval=n, backupCount=5)
    # ログレベルの設定
    file_handler.setLevel(logging.INFO)
    # ログ出力フォーマットを設定
    file_handler.setFormatter(logging.Formatter(formatter))
    
    logging.basicConfig(level=logging.INFO, handlers=[stream_handler, file_handler])
