import numpy as np
import matplotlib.pyplot as plt
import fitsio

plt.rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
plt.rc("text", usetex=True)

g_xlabel = "$\lambda (\AA)$"
g_ylabel = "$F (units)$"

g_fontsize_xlabel = 30
g_fontsize_ylabel = 28

g_file_dpi = 200
g_plot_dpi = 75

fin = fitsio.FITS('/init_directory_spectra_with_BALs/spectra_with_BAL.fits')

wave = fin[2].read()
flux = fin[3].read()

plt.xlabel(g_xlabel, fontsize=g_fontsize_xlabel)
plt.ylabel(g_ylabel, fontsize=g_fontsize_ylabel)

plt.plot(wave,flux[28,:],color='blue',lw=1,zorder=10)
plt.plot(wave,flux[29,:],color='orange',lw=1,zorder=5)

plt.savefig("directory/name_plot.png", bbox_inches="tight", dpi=g_file_dpi)

plt.show()
