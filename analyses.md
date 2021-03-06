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
Check mapping stats
```bash
spack load samtools@1.10
samtools flagstats Pb_alignment_p.sam
# 99% mapping rate. The entire folder is deleted after. 
```
After loading samtools, the system chose to use python on spack instead of conda, at this time, the packages installed in the conda environments will not function.
To change python back to conda version, need to unload python from spack.
```bash
which python
#/pickett/spack/opt/spack/linux-rhel8-zen/gcc-8.3.1/python-3.8.6-hgew2rvmzrkyygmouqjyfhfat6qoy6ir/bin/python
spack unload python
which python
#/pickett/software/miniconda3/bin/python
```

Feb, 2021     
We blast the genome assembly to chroloplast genome and found a lot of hits. 
Remove chloroplast reads from PacBio reads.
First, the reads were aligned to redbud chloroplast sequences by minimap2 and output results in .paf file.     
Second, used python scripts [filter_paf.py](https://github.com/statonlab/Redbud_genome/blob/main/scripts/filter_paf.py) to extract reads with >90% alignment length to chloroplast.  
```bash
cd /pickett/projects/redbud/version_2/2.0.0/analysis/1_filter_cp
python /pickett/projects/redbud/python_scripts/filter_paf.py /pickett/projects/redbud/version_1/1.0.0/8_reads_to_chloroplast_20210202/redbud_reads_to_chloroplast.paf --rate 0.9
```
This will output two file: 
  - `aligned_read_headers.txt` stored the read headers aligned to cp with >90% length 
  - `unaligned_read_headers.txt` stored read headers aligned to cp with < 90% length.     

Last, remove the reads aligned to cp using python script [extract_seqs.py](https://github.com/statonlab/Redbud_genome/blob/main/scripts/extract_seqs.py). This script takes `aligned_read_headers.txt` and raw reads fasta files as input, and output aligned reads and clean reads into two fasta files provided by users. 
```bash
# need to make sure conda environment contains biopython library
python /pickett/projects/redbud/python_scripts/extract_seqs.py /pickett/projects/redbud/raw_data/pacbio_long_reads/redbud_pacbio_long_reads_concatenated.fasta aligned_read_headers.txt cp_reads.fasta redbud_clean_PBreads.fasta
```
  - `cp_reads.fasta` stored cp reads.
  - `redbud_clean_PBreads.fasta` stored clean reads. You can name the files by your own. 

We think we also need to filter cp reads from HiC data too.
```bash
mkdir /pickett/projects/redbud/analyses_falcon_unzip/10_filter_HiC
spack load bowtie2
bowtie2-build ../7_chloroplast_20210128/redbud_chloroplast_genome.fasta cp_genome
bowtie2 -p 18 \
-x cp_genome \
-1 ../../raw_data/CVFP12_S7_L003_R1_001.fastq.gz \
-2 ../../raw_data/CVFP12_S7_L003_R2_001.fastq.gz \
-S Aligned_cp.sam \
--un-conc HiC_cp_not_aligned.fq >& bowtie2.log &
```
