#!/bin/bash
#
# Program parameters: $0 $1 $2 ...
# $0 is the command
#
echo "program is $0"

#
# dirname gets the directory
# 'readlink -f' gets the full path of parameter $0 (in this case the command) excluding the
#               command itself

install_dir=$(dirname "$(readlink -f "$0")")
echo "install_dir is $install_dir"

cd $install_dir||exit 1

export CDF_PROJECT="pgs-dev"

#
# basename gets the file name of the parameter $0 (in this case the command) excluding path part
#
baseprod=$(basename "$0")
echo "baseprod is $baseprod"

#
# ${baseprod%_prod} returns the $baseprod variable filtering out the suffix '.sh'
# See https://stackoverflow.com/questions/16623835/remove-a-fixed-prefix-suffix-from-a-string-in-bash
#
baseprod=${baseprod%.sh}
echo "baseprod is $baseprod"

# This determines if the command is for production environment, in which case it is named <command>_prod.sh
base=${baseprod%_prod}
if [[ "$base" != "$baseprod" ]]; then
  export CDF_PROJECT="pgs"
fi
echo "CDF_PROJECT=${CDF_PROJECT}"

# Commented out for this demo
# source ./read_user_settings.sh
# pipenv run python pythonsrc/$base.py $*
