import numpy as np
import os

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from scripts.test.Projection.projection_base import ProjectionBase
from scripts.utils.config_utils import config
from scripts.utils.data_utils import Data

DATANAME = config.breast_cancer

def plot_tsne():
    dataname = DATANAME
    d = ProjectionBase(dataname)
    d.t_sne(show=True)

def plot_pca():
    d = ProjectionBase(DATANAME)
    d.pca(show=True)

def exploration_3d():
    d = Data(dataname=DATANAME)
    X_train = d.X_train
    plt_X = d.X_train[:,[1,23,24]]
    y_train = d.y_train
    color_map = plt.get_cmap("tab10")(y_train.astype(int))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(plt_X[:,0], plt_X[:,1], plt_X[:,2], s=3, c=color_map)
    plt.show()


if __name__ == '__main__':
    plot_tsne()
    # plot_pca()
    # exploration_3d()
