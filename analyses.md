Dec, 2020
- obtain phased diploid genome assembly from Amanda on scinet.      
```txt
all_p_ctg.fa # primary contig-level assembly
all_h_ctg.fa # haplotigs contig-level assembly
```
- obtain HiC data from NC state lab. 

Jan, 2021
- Transfer the working directory to flora server `/pickett/projects/redbud`.   
```txt
assembly/ # phased genome assembly
raw_data/ # HiC data in fastq
analyses/ # working directory of genomic analyses
```

Do not find raw pacbio subreads from the shared folder but get 130 fasta files in `preads/`. Transfer those files to `/pickett/projects/redbud`.    
Test if those reads map to unzip genome.
```bash
mkdir /pickett/projects/redbud/mapping_pb_202101
cd /pickett/projects/redbud/mapping_pb_202101
nohup /pickett/software/minimap2-2.17_x64-linux/minimap2 -ax map-pb -o Pb_alignment_p.sam -t 20 ../assembly/all_p_ctg.fa ../preads/cns*fasta &
```
