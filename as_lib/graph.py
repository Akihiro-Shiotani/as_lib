#%%
import matplotlib.pyplot as plt

def config():
    plt.rcParams['font.family'] ='Meiryo'#使用するフォント
    plt.rcParams['xtick.direction'] = 'in' #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in' #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.5 #x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.5 #y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 14 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.5 # 軸の線幅edge linewidth。囲みの太さ