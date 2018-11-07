# Redrock-comparisons

We have made different tests to compare the results from redrock and quickquasars script (zbest or ztrue??).

First, one checks that BALs features are produced in the QSO spectra (BALs with 0.12 probability). There are two quick runs in version 2.0 that introduced these broad lines: quick 1.7 and 1.8 (also includes random DLAs).

As a second step, one can actually check redrock routine performance with respect to the predicted redshift of the QSO (z_in). Redrock compares each synthetic spectrum with templates of different objects and predicts a redshift according to the most probable object (z_out). If the predicted object spectrum does not look like a QSO, a flag will be generated and the discrepancy in redshift will be obviously large (associated with the dispersion velocity or dv).

* The runs we have used so far include:

/global/project/projectdirs/desi/mocks/lya_forest/london/v2.0/quick-1.8/spectra-16

Version 2.0/ quick 1.0 to 1.8: first tests in local (especifically, 8, subpixel 845). Further tests have been focused on quick 1.0, 1.7 and 1.8.

/global/project/projectdirs/desi/mocks/lya_forest/london/v3.0
Version 3.0/ quick 0.1 and 0.2: tests to run redrock in parallel with a modified version of Alma' script. (logs in cluster).

* Ways to run redrock:
 
 Serial mode: 
 rrdesi spectra-number-subpixel.fits --zbest output_redrock.fits
 
 Parallel mode in an interactive job: 
 srun -N 1 -n 32 -C haswell rrdesi_mpi /global/project/projectdirs/desi/mocks/lya_forest/london/v2.0/quick-1.8/spectra-16/18/1876/spectra-number-subpixel.fits --zbest output-redrock.fits
 
 Parallel mode in a background job:
 sbatch rrdesi.sl
 
Right now the script rrdesi.sl is in my scratch directory at Cori. The code is a variation of Alma' script that produces the output and its corresponding logs in the directory of the spectrum.





