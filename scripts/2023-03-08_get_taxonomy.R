library(rentrez) # for fetching taxonomy

accessions = read.csv("accessions.txt", header=F)$V1
# Checks out
# Fetch taxonomy for every virus
accessions.df = data.frame(accession=accessions, taxonomy="")
for (i in 1:nrow(accessions.df)){
  xml.record = entrez_fetch(db="nuccore", id=accessions.df$accession[i],rettype = "xml", parsed=TRUE) 
  xml.list = XML::xmlToList(xml.record)
  taxonomy = xml.list$GBSeq$GBSeq_taxonomy
  accessions.df$taxonomy[i] = taxonomy
  print(i)
}
write.csv(accessions.df, file="autographiviridae_with_taxonomy.csv", row.names = F)