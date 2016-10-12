#! /bin/sh
#PBS -N prueba
#PBS -o /home/prueba.out
#PBS -e /home/prueba.err
#PBS -l walltime=01:00:00
#PBS -M rodolfo.restrepo@udea.edu.co
#PBS -m e
#PBS -m a

date
hostname
sleep 20
date