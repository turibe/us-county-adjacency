# us-county-adjacency

United States County Adjacency Data, with corrections.

## Intro

The US County Adjacency Graph is fun to explore, but the text file from the US census 
(https://www.census.gov/programs-surveys/geography/library/reference/county-adjacency-file.html)
has some typos (as of March 17, 2024).
This repo fixes them and adds a [tab-separated (TSV) file](https://github.com/turibe/us-county-adjacency/blob/main/county_adjacency.tsv).

### The typos

Line 9629, which reads
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

We also fix some inconsistent Spanish accent encodings (see [differences.diff](https://github.com/turibe/us-county-adjacency/blob/small_updates/differences.diff)).

### The tab-separated (TSV) file

The TSV file `county_adjacency.tsv` is the result of running the Python 3 script `process_county.py`,
with `census_county_adjacency_fixed.txt` as its input.

### Encodings

The original file uses `"ISO-8859-1"` . The TSV file uses `UTF-8`.

### Acknowledgements

The Census file was similarly processed here, but includes the typos:
https://data.world/markmarkoh/us-county-adjacency
