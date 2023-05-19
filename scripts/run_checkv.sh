# Runs CheckV

cat ../data/fastA/*fa > ../data/fasta/all.fasta

checkv end_to_end ../data/fasta/all.fasta ../output/checkv-output -d /Users/Liam/opt/miniconda3/envs/checkv-env/checkv-db/checkv-db-v1.5/

