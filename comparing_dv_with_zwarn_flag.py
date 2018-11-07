import sys, os
import argparse

import numpy as np
import scipy.constants
import matplotlib.pyplot as plt
import fitsio
from astropy.table import Table,Column

plt.rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
plt.rc("text", usetex=True)

g_xlabel = "$z_{in}$"
g_ylabel = "$dv$ (km/s)"

g_fontsize_legend = 13
g_fontsize_xlabel = 25
g_fontsize_ylabel = 25

g_file_dpi = 200
g_plot_dpi = 75

g_xlim = [1.0, 4.0]
g_ylim = [-600, 600]

c = (scipy.constants.speed_of_light/1000.) # km/s

parser=argparse.ArgumentParser(description='Define parameters different runs to compare')

parser.add_argument('--path',type=str,default='/Users/lgarcia/desi/mocks/lya_forest',required=True, help="Define path to files")
parser.add_argument('--version', type=float, default=2.0, required=True, help="London mocks (either 1.0 or 2.0)")
parser.add_argument('--run1', type=float,required=True,help="Run number")
#parser.add_argument('--run2', type=float,required=True,help="Run number to compare with run 1")
parser.add_argument('--number', type=int, default=8, required=True, help="Integer number with the first number of the directory file (e.g. 8 or 16)")
parser.add_argument('--dirnum', type=int, default=845,required=True, help="Directory and file number (for instance, 845)")
#parser.add_argument('--pathred', type=str,default='/Users/lgarcia/desi/mocks/lya_forest',required=True, help="Path the redrock output")

args = parser.parse_args()

path_file_1 = '{}/london/v{}/quick-{}/spectra-16/{}/{}/zbest-16-{}.fits'.format(args.path,args.version,args.run1,args.number,args.dirnum,args.dirnum)
path_file_2 = '{}/london/v{}/quick-{}/spectra-16/{}/{}/output_{}_redrock.fits'.format(args.path,args.version,args.run1,args.number,args.dirnum,args.run1)

#title = 'Comparison runs {} and {} (including BALs balprob 0.12)'.format(args.run1,args.run2)
title = 'Comparison run {} (redrock and zbest) -cell {}-'.format(args.run1,args.dirnum)
outputfile = '/Users/lgarcia/Desktop/BAL/redrock_comparisons/zin_vs_dv_{}.png'.format(args.run1)

def main():

    data_1 = Table.read(path_file_1)
    data_2 = Table.read(path_file_2)

    print(path_file_1)
    print(path_file_2)

    z_1 = data_1['Z']
    z_err_1 = data_1['ZERR']
    z_warn_1 = data_1['ZWARN']
    spec_type_1 = data_1['SPECTYPE']

    z_mock = data_2['Z']
    z_err_mock = data_2['ZERR']
    z_warn_mock = data_2['ZWARN']
    spec_mock = data_2['SPECTYPE']
    #print(z_warn_mock)
    
    catastrophic = np.where(spec_mock != 'QSO')
    boo_x = z_1[catastrophic]
    ind_x = np.nonzero(z_1[catastrophic])
    boo_y = z_mock[catastrophic]
    ind_y = np.nonzero(z_mock[catastrophic])
    err_y = z_err_mock[catastrophic]

    num_red = len(z_1)
    num_red_mock = len(z_mock)

    red_diff = []    
    for i in range(num_red):
        red_diff.append(z_1[i] - z_mock[i])

    red_diff_array = np.asarray(red_diff)

    tolerance = 0.1
    sub1 = (red_diff_array > tolerance)
    sub2 = (red_diff_array < -tolerance)
    #sub = ((np.where(red_diff_array > tolerance)) or (np.where(red_diff_array < - tolerance)))
    print(sub1,sub2)

    good = []
    for i in range(len(z_mock)):
        if((sub1[i] == False or sub2[i]== False) and z_warn_mock[i] == 0):
            good.append(i)
    print(good)

    #catastropic failures
    fail = []

    bad redshift and ZWARN==0

    #missed opportunities
    miss = []

    correct redshift ZWARN!=0

    #wrong but we spotted them
    lost = []

    wrong redshift ZWARN!=0 

    #repeat recipe for fail, loss and miss categories!

    """
    YYY = c*((z_1-z_mock)/(1.0+z_1))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlim(g_xlim)
    ax.set_ylim(g_ylim)
    plt.title(title, fontsize=18)
    ax.set_xlabel(g_xlabel, fontsize=g_fontsize_xlabel)
    ax.set_ylabel(g_ylabel, fontsize=g_fontsize_ylabel)

    ax.scatter(z_1,YYY,color='blue',lw=1,zorder=1)
    ax.scatter(boo_x,boo_y,color='red',lw=1,zorder=10)
    ax.plot([0,5],[0.0,0.0],color='black',lw=1,linestyle='-.',zorder=-10)
    
    #(_, caps, _) = ax.errorbar(z_1, z_mock, yerr=[z_err_mock, z_err_mock],fmt="None", ecolor='blue', elinewidth=3, capsize=3)
    #(_, caps, _) = ax.errorbar(boo_x, boo_y, yerr=[err_y, err_y],fmt="None", ecolor='red', elinewidth=3, capsize=3)
    
    #for cap in caps:
        #cap.set_markeredgewidth(2)

    # Setup legend.
    legend_lines = []
    legend_labels = []
    legend_lines.append(plt.Line2D((0, 0), (0, 0), linewidth=0, color='blue', marker="o", markersize=5, markeredgewidth=1.5, markeredgecolor='blue'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), linewidth=0, color='red', marker="o", markersize=5, markeredgewidth=1.5, markeredgecolor='red'))
    legend_labels.append("Spectype $=$ QSO")
    legend_labels.append("Spectype $=$ other")
    ax.legend(legend_lines, legend_labels, loc="best", numpoints=1, ncol=1, fontsize=g_fontsize_legend, handlelength=1.0, frameon=False)    

    plt.savefig(outputfile, bbox_inches="tight", dpi=g_file_dpi)

    plt.show()
    """

if __name__ == "__main__":
    main()
    
