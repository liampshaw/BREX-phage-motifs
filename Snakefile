#Run scripts/countThreeMotifs.py
# Run scripts/plotData.Rmd
# Other scripts - probably don't need to run

rule all:
	input:
		"output/Main-figure.pdf",
		"output/checkv-output/quality_summary.tsv"

rule count_motifs:
	output:
		"output/motif_counts.csv",
		"output/phage_lengths.csv"
	run:
		"python scripts/countThreeMotifs.py"


rule make_R_plot:
	input:
		"scripts/plotData.R"
	output:
		"output/Main-figure.pdf"
	run:
		"Rscript scripts/plotData.R"

rule run_check_v:
	input:
		"scripts/run_checkv.sh"
	output:
		"output/checkv-output/quality_summary.tsv"
	run:
		shell("cd scripts")
		shell("./run_checkv.sh")

