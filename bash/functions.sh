#!/bin/bash

#
# Function examples
#

# Global variable
g_num=10
g_str="Hello global"

func_1()
{
  echo "In func_1"
  echo "Exit func_1"
}


func_2()
{
  echo "In func_2"
  # Define a local variable only in function scope
  local f_var1="Hello func_2"
  local f_var2=3
  local f_var3=4

  # Here is an arithmetic expression on two local variables. Notice that we can omit the $/${} on the variables
  # in the expression.
  local f_sum=$(( f_var2+f_var3 ))
  echo "f_var1=$f_var1"
  echo "f_sum=$f_sum"

  # Reference global variable
  echo "g_str=$g_str"
  f_sum=$(( g_num+f_var2 ))
  echo "f_sum=$f_sum"
  echo "Exit func_2"

}

# Function taking parameters
func_3()
{
  local f_par1=$1
  echo "In func_3"
  echo "f_par1=$f_par1"
  echo "Exit func_3"
}

echo "f_var1=$f_var1"     # Echoes empty string
echo "g_num=$g_num"       # Echoes value of g_num

func_1
func_2
func_3 100                # Call with number
func_3 "Hello func3"      # Call with string
