#!/bin/bash

#####################################################################################
# Remove duplicate headers from RAW CSV files
# This is hard coded for the TET KW files
# For awk command see:
# https://www.tutorialspoint.com/awk/awk_workflow.htm
#####################################################################################

for i in `ls *.raw.*`
do
  init_col_count=$(head -1 ${i}  | sed 's/[^,]//g' | wc -c)
  awk 'BEGIN{FS=OFS=","} {print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30}' ${i} >> ${i}.out
  new_col_count=$(head -1 ${i}.out  | sed 's/[^,]//g' | wc -c)
  echo "${i} NUM_COL: ${init_col_count} PATCH_COL: ${new_col_count}"
  mv ${i}.out ${i}
done


#####################################################################################
# Rename file names with spurious characters
#
# Uses cut and sed commands to filter out parts of the file names and replacing
# regular expressions
#####################################################################################
for i in `ls`
do
  # prints list of fields separated by the separation character
  prefix=$(echo $i | cut -d . -f 1,2,3)
  echo ${prefix}

  # This only prints one field
  suffix=$(echo $i | cut -d . -f 4)

  midpart=$(echo ${suffix} | cut -d _ -f 1,2)
  lastpart=$(echo ${suffix} | cut -d _ -f 3)
  echo ${lastpart}

  # Replace the regular expression globally (all matches)
  num=$(echo ${lastpart} | sed 's/яАв//g')

  echo "Rename ${i}: ${prefix}.${midpart}-${num}"
  mv ${i} ${prefix}.${midpart}-${num}
done
