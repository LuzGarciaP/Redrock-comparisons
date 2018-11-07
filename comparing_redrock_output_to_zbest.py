import numpy as np
import matplotlib.pyplot as plt
import fitsio
from astropy.table import Table

plt.rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
plt.rc("text", usetex=True)

g_xlabel = "$z_{in}$"
g_ylabel = "$z_{out}$"

g_fontsize_legend = 13
g_fontsize_xlabel = 25
g_fontsize_ylabel = 25

g_file_dpi = 200
g_plot_dpi = 75

g_xlim = [0.3, 3.7]
g_ylim = [0.3, 3.7]

def main():
    data_real = Table.read('/directory_zbest/zbest.fits')
    data_redrock = Table.read('/directory_output_redrock/output_redrock.fits')

    z_real = data_real['Z']
    z_err_real = data_real['ZERR']
    z_warn_real = data_real['ZWARN']
    spec_type_real = data_real['SPECTYPE']

    z_mock = data_redrock['z']
    z_err_mock = data_redrock['zerr']
    spec_mock = data_redrock['spectype']
    
    catastrophic = np.where(spec_mock != 'QSO')
    boo_x = z_real[catastrophic]
    ind_x = np.nonzero(z_real[catastrophic])
    boo_y = z_mock[catastrophic]
    ind_y = np.nonzero(z_mock[catastrophic])
    err_y = z_err_mock[catastrophic]

    #print(boo_x)
    print(boo_y)
    #print(ind_x)
    print(ind_y)
    print(err_y)
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlim(g_xlim)
    ax.set_ylim(g_ylim)
    plt.title('20 QSOs -with BALs and fixed seed-', fontsize=25)
    ax.set_xlabel(g_xlabel, fontsize=g_fontsize_xlabel)
    ax.set_ylabel(g_ylabel, fontsize=g_fontsize_ylabel)

    ax.scatter(z_real,z_mock,color='blue',lw=1,zorder=1)
    ax.scatter(boo_x,boo_y,color='red',lw=1,zorder=10)
    ax.plot(z_mock,z_mock,color='black',lw=1,linestyle='--',zorder=-10)

    (_, caps, _) = ax.errorbar(z_real, z_mock, yerr=[z_err_mock, z_err_mock],fmt="None", ecolor='blue', elinewidth=3, capsize=3)
    (_, caps, _) = ax.errorbar(boo_x, boo_y, yerr=[err_y, err_y],fmt="None", ecolor='red', elinewidth=3, capsize=3)
    
    for cap in caps:
        cap.set_markeredgewidth(2)

    # Setup legend.
    legend_lines = []
    legend_labels = []
    legend_lines.append(plt.Line2D((0, 0), (0, 0), linewidth=0, color='blue', marker="o", markersize=5, markeredgewidth=1.5, markeredgecolor='blue'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), linewidth=0, color='red', marker="o", markersize=5, markeredgewidth=1.5, markeredgecolor='red'))
    legend_labels.append("Spectype $=$ QSO")
    legend_labels.append("Spectype $=$ other")
    ax.legend(legend_lines, legend_labels, loc="best", numpoints=1, ncol=1, fontsize=g_fontsize_legend, handlelength=1.0, frameon=False)    

    plt.savefig("/output_directory/name_of_the_plot.png", bbox_inches="tight", dpi=g_file_dpi)

    plt.show()
    

if __name__ == "__main__":
    main()
