# us-county-adjacency

United States County Adjacency Data, Fixed.

## Intro

The US County Adjacency graph is a fun one to explore, but the text file from the US census 
(https://www.census.gov/programs-surveys/geography/library/reference/county-adjacency-file.html)
has some typos
(ss of March 17, 2024).
This repo fixes them and adds a tab-separated (TSV) file.

### The typos

Line 9629, that reads
```
    27165	"Blue Earth County, MN"	27013
```
should be
```
"Watonwan County, MN"	27165	"Blue Earth County, MN"	27013
```

Line 9438, which reads
```
"Todd County, MN"   27111   "Becker County, MN" 27005
```
should be
```
"Otter Tail County, MN"	27111	"Becker County, MN"	27005
```

