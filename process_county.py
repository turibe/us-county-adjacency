"""Convert the US Census county adjacency file into a tab-separated (TSV) file."""

import os
import sys
from typing import TextIO

def process_file(fname:str, fout:TextIO):
    """Process the US census file and produce a DB-friendly TSV file."""
    lines:int = 0
    sourcename = ""
    sourcezip = ""
    with open(fname, "r", encoding="ISO-8859-1") as f:
        fout.write('"county_name"\t"county_zip"\t"adjacent_county_name"\t"adjacent_county_zip"\n')
        while True:
            if not f.readable():
                break
            line = f.readline()
            parts = line.split("\t")
            if len(parts) <= 1:
                break
            lines += 1
            # print(f"line {lines}, parts: {len(parts)}")
            if lines > 2000000:
                break
            if not parts[0] == '':
                sourcename = parts[0]
                sourcezip = parts[1]
            targetname = parts[2]
            targetzip = parts[3]
            fout.write(f"{sourcename}\t{sourcezip}\t{targetname}\t{targetzip}")
            fout.flush()
    print(f"Read {lines} lines")

if __name__ == "__main__":
    input_file:str = "census_county_adjacency_fixed.txt"
    OUTPUT_FILE = "county_adjacency_fixed.tsv"
    if os.path.isfile(OUTPUT_FILE):
        print(f"Error: Output file {OUTPUT_FILE} exists, exiting\n")
        sys.exit(1)
    print(f"Writing to {OUTPUT_FILE}")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as foutput:
        process_file(input_file, foutput)
