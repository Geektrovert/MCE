import os

import numpy as np
import pandas as pd
from bokeh.io import export_png, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure

data_path = os.path.join(os.getcwd(), 'data')
dev_bg_path = os.path.join(data_path, 'dev_background.csv')
dev_bl_path = os.path.join(data_path, 'dev_blacklist.csv')
trn_bg_path = os.path.join(data_path, 'trn_background.csv')
trn_bl_path = os.path.join(data_path, 'trn_blacklist.csv')
dev_bg_data = dev_bg_name = dev_bl_data = dev_bl_name = None
trn_bg_data = trn_bg_name = trn_bl_data = trn_bl_name = None
dev_bg_mean = dev_bl_mean = trn_bg_mean = trn_bl_mean = None
dev_bg_max = dev_bl_max = trn_bg_max = trn_bl_max = None
dev_bg_min = dev_bl_min = trn_bg_min = trn_bl_min = None


def plot_show():
    index = [i for i in range(0, 600)]

    f11 = figure(plot_width=500, plot_height=250, title='dev_background_data_1', y_range=(-5, 5))
    f11.line(index, dev_bg_data[:1][0], line_width=1)
    f12 = figure(plot_width=500, plot_height=250, title='dev_background_data_2', y_range=(-5, 5))
    f12.line(index, dev_bg_data[1:2][0], line_width=1)

    f21 = figure(plot_width=500, plot_height=250, title='dev_blacklist_data_1', y_range=(-5, 5))
    f21.line(index, dev_bl_data[:1][0], line_width=1)
    f22 = figure(plot_width=500, plot_height=250, title='dev_blacklist_data_2', y_range=(-5, 5))
    f22.line(index, dev_bl_data[1:2][0], line_width=1)

    f31 = figure(plot_width=500, plot_height=250, title='trn_background_data_1', y_range=(-5, 5))
    f31.line(index, trn_bg_data[:1][0], line_width=1)
    f32 = figure(plot_width=500, plot_height=250, title='trn_background_data_2', y_range=(-5, 5))
    f32.line(index, trn_bg_data[1:2][0], line_width=1)

    f41 = figure(plot_width=500, plot_height=250, title='trn_blacklist_data_1', y_range=(-5, 5))
    f41.line(index, trn_bl_data[:1][0], line_width=1)
    f42 = figure(plot_width=500, plot_height=250, title='trn_blacklist_data_2', y_range=(-5, 5))
    f42.line(index, trn_bl_data[1:2][0], line_width=1)

    m1 = figure(plot_width=500, plot_height=250, title='dev_background_data_mean', y_range=(-1, 1))
    m1.line(index, dev_bg_mean, line_width=1)
    m2 = figure(plot_width=500, plot_height=250, title='dev_blacklist_data_mean', y_range=(-1, 1))
    m2.line(index, dev_bl_mean, line_width=1)
    m3 = figure(plot_width=500, plot_height=250, title='trn_background_data_mean', y_range=(-1, 1))
    m3.line(index, trn_bg_mean, line_width=1)
    m4 = figure(plot_width=500, plot_height=250, title='trn_blacklist_data_mean', y_range=(-1, 1))
    m4.line(index, trn_bl_mean, line_width=1)

    mx1 = figure(plot_width=500, plot_height=250, title='dev_background_data_max', y_range=(-10, 10))
    mx1.line(index, dev_bg_max, line_width=1)
    mx2 = figure(plot_width=500, plot_height=250, title='dev_blacklist_data_max', y_range=(-10, 10))
    mx2.line(index, dev_bl_max, line_width=1)
    mx3 = figure(plot_width=500, plot_height=250, title='trn_background_data_max', y_range=(-10, 10))
    mx3.line(index, trn_bg_max, line_width=1)
    mx4 = figure(plot_width=500, plot_height=250, title='trn_blacklist_data_max', y_range=(-10, 10))
    mx4.line(index, trn_bl_max, line_width=1)

    mn1 = figure(plot_width=500, plot_height=250, title='dev_background_data_min', y_range=(-10, 10))
    mn1.line(index, dev_bg_min, line_width=1)
    mn2 = figure(plot_width=500, plot_height=250, title='dev_blacklist_data_min', y_range=(-10, 10))
    mn2.line(index, dev_bl_min, line_width=1)
    mn3 = figure(plot_width=500, plot_height=250, title='trn_background_data_min', y_range=(-10, 10))
    mn3.line(index, trn_bg_min, line_width=1)
    mn4 = figure(plot_width=500, plot_height=250, title='trn_blacklist_data_min', y_range=(-10, 10))
    mn4.line(index, trn_bl_min, line_width=1)

    data = gridplot([[f11, f12],
                     [f21, f22],
                     [f31, f32],
                     [f41, f42]
                     ],
                    toolbar_location=None)

    mean = gridplot([[m1, m2],
                     [m3, m4]
                     ],
                    toolbar_location=None)

    mx = gridplot([[mx1, mx2],
                   [mx3, mx4]],
                  toolbar_location=None)

    mn = gridplot([[mn1, mn2],
                   [mn3, mn4]
                   ],
                  toolbar_location=None)

    f = gridplot([[f11, f12],
                  [f21, f22],
                  [f31, f32],
                  [f41, f42],
                  [m1, m2, m3, m4],
                  [mx1, mx2, mx3, mx4],
                  [mn1, mn2, mn3, mn4]
                  ], toolbar_location=None)
    export_png(f, filename='DataVis_full.png')
    export_png(data, filename='DataVis.png')
    export_png(mean, filename='MEAN.png')
    export_png(mx, filename='MAX.png')
    export_png(mn, filename='MiN.png')
    show(f)


def debug():
    print(dev_bl_name[:1].shape)
    print(dev_bl_data[:1].shape)
    # print(dev_bl_name[:1])
    # print(dev_bl_data[:1])
    ll = [i for i in dev_bl_data[:1:][0]]
    print(ll)


if __name__ == '__main__':

    # READING DATA
    dev_bg_data = pd.read_csv(dev_bg_path, sep=',', skiprows=1, header=None)
    dev_bl_data = pd.read_csv(dev_bl_path, sep=',', skiprows=1, header=None)
    trn_bg_data = pd.read_csv(trn_bg_path, sep=',', skiprows=1, header=None)
    trn_bl_data = pd.read_csv(trn_bl_path, sep=',', skiprows=1, header=None)

    # FORMATTING DATA
    dev_bg_name = dev_bg_data.iloc[:, :1]
    dev_bg_data = dev_bg_data.iloc[:, 1:]
    dev_bl_name = dev_bl_data.iloc[:, :1]
    dev_bl_data = dev_bl_data.iloc[:, 1:]
    trn_bg_name = trn_bg_data.iloc[:, :1]
    trn_bg_data = trn_bg_data.iloc[:, 1:]
    trn_bl_name = trn_bl_data.iloc[:, :1]
    trn_bl_data = trn_bl_data.iloc[:, 1:]
    dev_bg_data = dev_bg_data.values
    dev_bl_data = dev_bl_data.values
    trn_bg_data = trn_bg_data.values
    trn_bl_data = trn_bl_data.values

    # MEAN
    dev_bg_mean = np.mean(dev_bg_data, axis=0)
    dev_bl_mean = np.mean(dev_bl_data, axis=0)
    trn_bg_mean = np.mean(trn_bg_data, axis=0)
    trn_bl_mean = np.mean(trn_bl_data, axis=0)

    # MAX
    dev_bg_max = np.amax(dev_bg_data, axis=0)
    dev_bl_max = np.amax(dev_bl_data, axis=0)
    trn_bg_max = np.amax(trn_bg_data, axis=0)
    trn_bl_max = np.amax(trn_bl_data, axis=0)

    # MIN
    dev_bg_min = np.amin(dev_bg_data, axis=0)
    dev_bl_min = np.amin(dev_bl_data, axis=0)
    trn_bg_min = np.amin(trn_bg_data, axis=0)
    trn_bl_min = np.amin(trn_bl_data, axis=0)

    plot_show()
