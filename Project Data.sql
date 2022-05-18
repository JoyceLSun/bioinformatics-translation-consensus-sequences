---start codon at [1009] of cdna seq

---top 10% (minus pe scores of 0 and 1)
select B.geneid, B.probability, A.lengthorf, A.orfsequence, C.cdnasequence --A.* 
from dbo.tableTranscriptsWithOrfs A, dbo.tblProteinExpressions B, dbo.tableTranscripts C
where A.id = B.id 
and B.geneid = C.geneid
and B.probability > 0.9
order by probability desc

select B.geneid, C.cdnasequence --A.* 
from dbo.tblProteinExpressions B, dbo.tableTranscripts C
where B.geneid = C.geneid
---and pe != 0 and pe != 1 ---might not need to get rid of 1, but seemed repetitive for no reason
and B.probability > 0.9
order by probability desc

---middle 10% protein expression
select B.geneid, B.probability, A.lengthorf, A.orfsequence, C.cdnasequence --A.* 
from dbo.tableTranscriptsWithOrfs A, dbo.tblProteinExpressions B, dbo.tableTranscripts C
where A.id = B.id 
and B.geneid = C.geneid
and B.probability > 0.45 and B.probability< 0.55
order by probability desc

select B.geneid, C.cdnasequence 
from dbo.tblProteinExpressions B, dbo.tableTranscripts C
where B.geneid = C.geneid
and B.probability > 0.45 and B.probability< 0.55
order by probability desc

---bottom 10% protein expression
select B.geneid, B.probability, A.lengthorf, A.orfsequence, C.cdnasequence --A.* 
from dbo.tableTranscriptsWithOrfs A, dbo.tblProteinExpressions B, dbo.tableTranscripts C
where A.id = B.id 
and B.geneid = C.geneid
and probability != 0 
and B.probability < 0.1
order by probability asc

select B.geneid, C.cdnasequence --A.* 
from dbo.tblProteinExpressions B, dbo.tableTranscripts C
where B.geneid = C.geneid
and probability != 0 
and B.probability < 0.1
order by probability desc



