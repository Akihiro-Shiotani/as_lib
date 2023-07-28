#%%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def setting():
    plt.rcParams['font.family'] ='Meiryo'#使用するフォント
    plt.rcParams['xtick.direction'] = 'in' #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in' #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.5 #x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.5 #y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 14 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.5 # 軸の線幅edge linewidth。囲みの太さ
    
def make_hist(dfs, column, xlabel=0, labels=0, bins=20, alpha=1, ran=0):
    plt.figure(dpi=400)
    if xlabel == 0:
        xlabel = column
    plt.xlabel(xlabel)
    plt.ylabel('度数')
    if labels == 0:
        labels = [i for i in range(len(dfs))]
    xs = []
    mins = []
    maxs = []
    for df in dfs:
        x = df[column].to_numpy()
        x = x[~np.isnan(x)]
        xs.append(x)
        try:
            mins.append(np.nanmin(x))
            maxs.append(np.nanmax(x))
        except:
            pass
    try:
        ran = [min(mins), max(maxs)]
        for x, label in zip(xs, labels):
            plt.hist(x, bins=bins, alpha=alpha, label=label, range=ran)
        if len(dfs) > 1:
            plt.legend()
        plt.show()
    except:
        plt.clf()

def correlation(df, x_column, y_column, reg=True):
    x = df[x_column].to_numpy()
    y = df[y_column].to_numpy()
    plt.figure(dpi=400)
    plt.xlim([np.nanmin(x)*0.95, np.nanmax(x)*1.05])
    plt.plot(x, y, 'o')

    if reg:
        model_lr = LinearRegression()
        model_lr.fit(x.reshape(-1, 1), y)
        a = model_lr.coef_
        b = model_lr.intercept_
        x_reg = np.array([np.nanmin(x)*0.95, np.nanmax(x)*1.05])
        y_reg = a * x_reg + b
        plt.plot(x_reg, y_reg, linestyle='dashed')
    plt.show()
    plt.clf()
    
    df_std = df.loc[:, [x_column, y_column]].groupby(x_column).aggregate(['mean', 'std'])
    x = df_std.index.to_numpy()
    y = df_std[y_column]['mean'].to_numpy()
    y_err = df_std[y_column]['std'].to_numpy()
    plt.figure(dpi=400)
    plt.xlim([np.nanmin(x)*0.95, np.nanmax(x)*1.05])
    plt.errorbar(x, y, yerr=y_err, capsize=3, fmt='o', markersize=5)
    
    if reg:
        model_lr = LinearRegression()
        model_lr.fit(x.reshape(-1, 1), y)
        a = model_lr.coef_
        b = model_lr.intercept_
        x_reg = np.array([np.nanmin(x)*0.95, np.nanmax(x)*1.05])
        y_reg = a * x_reg + b
        plt.plot(x_reg, y_reg, linestyle='dashed')
    plt.show()
    plt.clf()