# Create figures in Python that handle LaTeX, and save images to files in my
# preferred formatting. I typically place this code in the root of each of my
# projects, and import using:
# from latexify import *
# which will also run the latexify() function on the import.

# Based on code from https://nipunbatra.github.io/blog/2014/latexify.html

import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from chainconsumer import ChainConsumer

#Back-end to use depends on the system
from matplotlib.backends.backend_pgf import FigureCanvasPgf
matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)
# matplotlib.use('pgf')
# from matplotlib.backends.backend_pgf import FigureCanvasPgf
# matplotlib.backend_bases.register_backend('ps', FigureCanvasPgf)

import seaborn as sns
sns.set_style("white")

colwidth = 3.404 #inches

#my preferred palette. From
#https://seaborn.pydata.org/tutorial/color_palettes.html: "The cubehelix color
#palette system makes sequential palettes with a linear increase or decrease in
#brightness and some variation in hue. This means that the information in your
#colormap will be preserved when converted to black and white (for printing) or
#when viewed by a colorblind individual."

# I typically set the number of colors (below, 8) to the distinct colors I need
# in a given plot, so as to use the full range.
#sns.set_palette(sns.color_palette("cubehelix", 8)) # gamma=.5

sns.set_palette(sns.cubehelix_palette(rot=.2))


# The following is the latexify function. It allows you to create 2 column or 1
# column figures. You may also wish to alter the height or width of the figure.
# The default settings are good for most cases. You may also change the
# parameters such as labelsize and fontsize based on your classfile.
def latexify(fig_width=colwidth, fig_height=None, columns=1, ticksize=8, adjust_font=False):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.
    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples
    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1, 2]) 

    if fig_width is None:
        fig_width = 6.9 if columns == 1 else 13.8  # width in inches #3.39

    if fig_height is None:
        golden_mean = (sqrt(5) - 1.0) / 2.0    # Aesthetic ratio
        fig_height = fig_width * golden_mean  # height in inches

    MAX_HEIGHT_INCHES = 16.0
    if fig_height > MAX_HEIGHT_INCHES:
        print(("WARNING: fig_height too large:" + fig_height +
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches."))
        fig_height = MAX_HEIGHT_INCHES

    if adjust_font:
        params = {
                # 'backend': 'ps',
            #   'pgf.rcfonts': False,
            #   'pgf.preamble': ['\\usepackage{gensymb}', '\\usepackage[dvipsnames]{xcolor}'],
            #   "pgf.texsystem": "pdflatex",
                # 'text.latex.preamble': ['\\usepackage{gensymb}', '\\usepackage[dvipsnames]{xcolor}'],
                'text.latex.preamble': '\\usepackage{mathptmx}',
                #values below are useful defaults. individual plot fontsizes are
                #modified as necessary.
                'axes.labelsize': 8,  # fontsize for x and y labels
                'axes.titlesize': 8,
                'font.size': 8,
                'legend.fontsize': 8,
                'xtick.labelsize': ticksize,
                'ytick.labelsize': ticksize,
                'text.usetex': True,
                'figure.figsize': [fig_width, fig_height],
                'font.family': 'DejaVu Sans',
                'font.serif': 'Times',
                'lines.linewidth': 1.5,
                'lines.markersize':1,
                'xtick.major.pad' : 2,
                'ytick.major.pad' : 2,
                    'axes.xmargin' :  .0,  # x margin.  See `axes.Axes.margins`
                    'axes.ymargin' : .0,  # y margin See `axes.Axes.margins`
                }
    else:
        params = {
                'figure.figsize': [fig_width, fig_height],
                'axes.labelsize': 8,  # fontsize for x and y labels
                'axes.titlesize': 8,
                'font.size': 8,
                'legend.fontsize': 8,
                }

    matplotlib.rcParams.update(params)

def saveimage(name, fig = plt, extension = 'pdf', folder = 'plots/'):
    sns.despine()

    #Minor ticks off by default in matplotlib
    # plt.minorticks_off()

    #grid being off is the default for seaborn white style, so not needed.
    # plt.grid(False, axis = "x")
    # plt.grid(False, axis = "y")
    
    fig.savefig('{}{}.{}'.format(folder,name, extension), bbox_inches = 'tight')

latexify()