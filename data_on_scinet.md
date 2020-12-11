All data are compressed in `/lustre/project/gbru/gbru_sharewithjiali/redbud-assembly.tar.gz`.       
Decompressed it and get all the imtermediate and final files in `/lustre/project/gbru/gbru_sharewithjiali/gpfs_backup/ashrafi_data/rishi/redbud/pacbio/assembly`.     

### data directory
* `0-rawreads` - process raw PacBio reads.          
* `1-preads_ovl`
* `2-asm-falcon` - files are empty, all fasta files are 0 byte.         
* `2-asm-falcon-1` - falcon assembly. 
* `2-asm-falcon-2` - a second round of falcon ??
* `2-asm-falcon-3` - files are empty.            
* `3-unzip` - falcon unzip outputs. Phased the diploid genome.     
  - 'all_h_ctg.fa' haplotigs assembly.      
  - 'all_p_ctg.fa' primary assembly.   
  - 'all_p-h_ctg-combined.fa' diploid assembly combining primary and haplotigs contigs.      
  - `busco` BUSCO results for diploid and primary assemblies.    
The entire `3-unzip` is transfered to lab server for downstream analysis.       
  
* `4-quiver` - variant call analysis.  
