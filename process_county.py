
file:str = "census_county_adjacency.txt"

def process_file(fname:str, fout):
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
    with open("output", "w", encoding="utf-8") as fout:
        process_file(file, fout)
              
        
