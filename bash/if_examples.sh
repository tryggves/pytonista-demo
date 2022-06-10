#
# Using if statements and testing conditions.
#

# https://linuxize.com/post/how-to-compare-strings-in-bash/
# https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs


VAR1="Linuxize"
VAR2="Linuxize"

echo ""
echo "=== Test 1 ========================================================"
# Single [ is shorthand for the test command
if [ "$VAR1" = "$VAR2" ]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

echo ""
echo "=== Test 2 ========================================================"
read -p "Enter first string: " VAR1
read -p "Enter second string: " VAR2

echo ""
echo "=== Test 3 ========================================================"
# Double [[ is upgraded version of test from ksh.
# This can also test for wildcard matching patterns
if [[ "$VAR1" == "$VAR2" ]]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

echo ""
echo '=== Test 4 ========================================================'
read -p "Enter first string: " VAR1
read -p "Enter second string: " VAR2
[[ "$VAR1" == "$VAR2" ]] && echo "Equal" || echo "Not equal"

echo ""
echo "=== Test 5 ========================================================"
VAR='GNU/Linux is an operating system'
if [[ $VAR == *"Linux"* ]]; then
  echo "It's there."
fi