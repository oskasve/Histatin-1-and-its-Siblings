mpirun -bind-to core gmx_mpi grompp -f ../step0_minimization.mdp -c ../Hist-1_box_solv_ions.gro -p ../topol.top -o step0.tpr
mpirun -bind-to core gmx_mpi mdrun -v -s step0.tpr -deffnm step1
mpirun -bind-to core gmx_mpi grompp -f ../step1_equilibration.mdp -c step1.gro -r step1.gro -p ../topol.top -o step1.tpr
mpirun -bind-to core gmx_mpi mdrun -v -s step1.tpr -deffnm step2
mpirun -bind-to core gmx_mpi grompp -f ../step2_equilibration.mdp -c step2.gro -r step2.gro -t step2.cpt -p ../topol.top -o step2.tpr
mpirun -bind-to core gmx_mpi mdrun -v -s step2.tpr -deffnm step3
mpirun -bind-to core gmx_mpi grompp -f ../step3_equilibration.mdp -c step3.gro -r step3.gro -t step3.cpt -p ../topol.top -o step3.tpr
mpirun -bind-to core gmx_mpi mdrun -v -s step3.tpr -deffnm step4
mpirun -bind-to core gmx_mpi grompp -f ../step4_production.mdp -c step4.gro -t step4.cpt -p ../topol.top -o step4.tpr
mpirun -bind-to core gmx_mpi mdrun -v -s step4.tpr -deffnm MDrun
