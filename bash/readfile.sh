# Read a text file (argument $1) line by line


infile=$1

# Filter out the .txt part of the file name
fbase="${infile%.*}"
> "$fbase".out

# Each line is a ; separated CSV format
while read -r line; do
    # echo "Text read from file $1: $line"
    echo "$line" | awk 'BEGIN{FS=OFS=";"} {print $1, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13}' >> "$fbase".out
done < "$1"
