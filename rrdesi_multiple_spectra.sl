#!/bin/bash -l

#SBATCH --partition=debug
#SBATCH --account=desi
#SBATCH --nodes=12
#SBATCH --time=00:5:00
#SBATCH --job-name=rrdesi
#SBATCH --output=rrdesi.log
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=lgarciap@ecci.edu.co
#SBATCH -C haswell

export OMP_NUM_THREADS=1

idir=/global/project/projectdirs/desi/mocks/lya_forest/london/v2.0/quick-1.7/spectra-16

logdir=/global/project/projectdirs/desi/mocks/lya_forest/london/v2.0/quick-1.7/logs/rr

if [ ! -d $logdir ] ; then

    mkdir -p $logdir

fi

echo "get list of spectra  to analize ..."

files=`\ls -1 $idir/*/*/spectra-16*.fits`

nfiles=`echo $files | wc -w`

echo "n files =" $nfiles

for infile  in $files ; do

    name=${infile##*-}

    outdir=${infile%/*}

    if [ ! -f $outdir/zbestrr-16-$name ] ; then

    command="srun -N 12 -n 384 -c 1 rrdesi_mpi  --zbest $outdir/zbestrr-16-$name $infile"

        $command >& $logdir/$name.log &
        wait
    fi
    echo "done with file:" $name
done

wait
echo "END"
