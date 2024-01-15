{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1335f38f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define a function calls addNumber(x, y) that takes in two number and returns the sum of the two numbers.\n",
    "\n",
    "def addNumber(x,y):\n",
    "    return x+y\n",
    "addNumber(5,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5c97f514",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define a function calls subtractNumber(x, y) that takes in two numbers and returns the difference of the two numbers.\n",
    "\n",
    "def subtractNumber(x, y):\n",
    "    if x>y:\n",
    "        return x-y\n",
    "    else:\n",
    "        return y-x\n",
    "subtractNumber(5, 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "27a56239",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function getBiggerNumber(x, y) that takes in two numbers as arguments and returns the bigger number.\n",
    "\n",
    "def getBiggerNumber(x, y):\n",
    "    if x>y:\n",
    "        return x\n",
    "    else:\n",
    "        return y\n",
    "getBiggerNumber(5, 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "044d9432",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0 243 28.274333882308138\n"
     ]
    }
   ],
   "source": [
    "# Python provides many built-in modules with many useful functions. \n",
    "# One such module is the math module. The math module provides many \n",
    "#  useful functions such as sqrt(x), pow(x, y), ceil(x), floor(x) etc. \n",
    "# You will need to do a \"import math\" before you are allowed to use the functions within the math module.\n",
    "\n",
    "import math\n",
    "\n",
    "# Calculate the square root of 16 and stores it in the variable a\n",
    "\n",
    "a = math.sqrt(16)\n",
    "\n",
    "# Calculate 3 to the power of 5 and stores it in the variable b\n",
    "\n",
    "b = pow(3,5)\n",
    "\n",
    "# Calculate area of circle with radius = 3.0 by making use of the math.pi constant and store it in the variable c\n",
    "\n",
    "c = math.pi * pow(3.0,2)\n",
    "\n",
    "print(a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "67c5460f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'82.4'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function to convert temperature from Celsius to Fahrenheit scale.\n",
    "# oC to oF Conversion: Multipy by 9, then divide by 5, then add 32.\n",
    "\n",
    "# Note: Return a string of 2 decimal places.\n",
    "# In - Cel2Fah(28.0)\n",
    "# Out - '82.40'\n",
    "# In - Cel2Fah(0.00)\n",
    "# Out - '32.00'\n",
    "\n",
    "def converTemp(temp):\n",
    "    rt_tmp = (((temp*9)/5)+32)\n",
    "    rt_tmp = str(rt_tmp)\n",
    "    return rt_tmp\n",
    "converTemp(28.0)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9027402b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'21.8'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function to compute the BMI of a person.\n",
    "#     BMI = weight(kg)  /  ( height(m)*height(m) )\n",
    "\n",
    "# Note: Return a string of 1 decimal place.\n",
    "# In - BMI(63, 1.7)\n",
    "# Out - '21.8'\n",
    "# In - BMI(110, 2)\n",
    "# Out - '27.5'\n",
    "\n",
    "def calBmi(wght, hght):\n",
    "    bmi = (wght/(hght*hght))\n",
    "    \n",
    "    return str(round(bmi,2))\n",
    "\n",
    "calBmi(63,1.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "421dcc1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "525"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function percent(value, total) that takes in two numbers as arguments, and returns the percentage value as an integer.\n",
    "# In - percent(46, 90)\n",
    "# Out - 51\n",
    "# In - percent(51, 51)\n",
    "# Out - 100\n",
    "# In - percent(63, 12)\n",
    "# Out - 525\n",
    "\n",
    "def percent(val,ttl):\n",
    "    rt_per = ((val * 100)/ttl)\n",
    "    return round(rt_per)\n",
    "percent(63,12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f104c2d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function to compute the hypotenuse given sides a and b of the triangle.\n",
    "# Hint: You can use math.sqrt(x) to compute the square root of x.\n",
    "# In - hypotenuse(3, 4)\n",
    "# Out - 5\n",
    "# In - hypotenuse(5, 12)\n",
    "# Out - 13\n",
    "\n",
    "import math\n",
    "def pytha_hypotenuse(a,b):\n",
    "    num = math.sqrt(a**2 + b**2)\n",
    "    return round(num)\n",
    "pytha_hypotenuse(3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "055ec4b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function getSumOfLastDigits() that takes in a list of \n",
    "#  positive numbers and returns the sum of all the last digits in the list.\n",
    "# getSumOfLastDigits([2, 3, 4])\n",
    "# 9\n",
    "# getSumOfLastDigits([1, 23, 456])\n",
    "# 10\n",
    "\n",
    "def getSumOfLastDigits(lst):\n",
    "    sum = 0\n",
    "    for i in lst:\n",
    "        sum = sum + int(str(i)[-1])\n",
    "    return round(sum)\n",
    "getSumOfLastDigits([1,23,456])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "69a3b4d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'My name is Lim. I am 20 years old.'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function that uses a default value.\n",
    "# In - introduce('Lim', 20)\n",
    "# Out - 'My name is Lim. I am 20 years old.'\n",
    "# In - introduce('Ahmad')\n",
    "# Out - 'My name is Ahmad. My age is secret.'\n",
    "\n",
    "def introduce(strng = '' ,num = 0):\n",
    "    if num == 0:\n",
    "        return ('My name is {}. My age is secret.'.format(strng))\n",
    "    else:\n",
    "        return ('My name is {}. I am {} years old.'.format(strng,num))\n",
    "\n",
    "\n",
    "    \n",
    "\n",
    "introduce('Lim',20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "5276caf8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function isEquilateral(x, y, z) that accepts the 3 sides of a triangle as arguments. \n",
    "# The program should return True if it is an equilateral triangle.\n",
    "\n",
    "# In - isEquilateral(2, 4, 3)\n",
    "# False - False\n",
    "# In - isEquilateral(3, 3, 3)\n",
    "# Out - True\n",
    "# In - isEquilateral(-3, -3, -3)\n",
    "# Out - False\n",
    "\n",
    "def isEquilateral(a, b, c):\n",
    "    if a>0 and b>0 and c>0:\n",
    "        if a==b==c:\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "        \n",
    "isEquilateral(3, 3, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "67da8de1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-8"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# For a quadratic equation in the form of ax2+bx+c, the discriminant, D is b2-4ac. Write a function to compute the discriminant, D.\n",
    "# In - quadratic(1, 2, 3)\n",
    "# Out - 'The discriminant is -8.'\n",
    "# In - quadratic(1, 3, 2)\n",
    "# Out - 'The discriminant is 1.'\n",
    "# In - quadratic(1, 4, 4)\n",
    "# Out - 'The discriminant is 0.'\n",
    "\n",
    "def quadratic(a, b, c):\n",
    "    return b*2 - 4*a*c\n",
    "\n",
    "quadratic(1, 2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "89423d66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define a function calls addFirstAndLast(x) that takes in a list of numbers and returns the sum of the first and last numbers.\n",
    "# In - addFirstAndLast([])\n",
    "# Out - 0\n",
    "# In - addFirstAndLast([2, 7, 3])\n",
    "# Out - 5\n",
    "# In - addFirstAndLast([10])\n",
    "# Out - 10\n",
    "\n",
    "def addFirstAndLast(lst):\n",
    "    if len(lst) == 0:\n",
    "        return 0\n",
    "    elif len(lst) == 1:\n",
    "        return lst[0]\n",
    "    else:\n",
    "        return round(lst[0] + lst[-1])\n",
    "\n",
    "addFirstAndLast([2,7,3])\n",
    "addFirstAndLast([])\n",
    "addFirstAndLast([10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "81335ce1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# Complete the 'lambda' expression so that it returns True if the argument is an even number, and False otherwise.\n",
    "\n",
    "x = lambda num: True if (num%2 ==0) else False\n",
    "print(x(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "ce9c9b72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "even = lambda x: True if x%2 == 0 else False\n",
    "print(even(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "2a5542ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# In Python, it is possible to pass a function as a argument to another function. \n",
    "# Write a function useFunction(func, num) that takes in a function and a number as arguments. \n",
    "# The useFunction should produce the output shown in the examples given below.\n",
    "\n",
    "def addOne(x):\n",
    "    return x + 1\n",
    "\n",
    "\n",
    "def useFunction(addOne,x):\n",
    "    x = addOne(x)\n",
    "    return x**2\n",
    "# useFunction(addOne, 4)\n",
    "# 25\n",
    "# useFunction(addOne, 9)\n",
    "# 100\n",
    "# useFunction(addOne, 0)\n",
    "# 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "b9ce4d3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Numbers:\t2 3 4\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'4'"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function find_max that accepts three numbers as arguments and returns the largest number among three. \n",
    "# Write another function main, in main() function accept three numbers from user and call find_max.\n",
    "\n",
    "def findMax(a, b, c):\n",
    "    if a >= b and b >= c:\n",
    "        return a\n",
    "    elif b >= a and b >= c:\n",
    "        return b\n",
    "    else:\n",
    "        return c\n",
    "\n",
    "def main():\n",
    "    x,y,z = input('Enter the Numbers:\\t').split()\n",
    "    num = findMax(x,y,z)\n",
    "    return num\n",
    "main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "ab8bd230",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a String:\taeiou\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function, is_vowel that returns the value true if a given character is a vowel, \n",
    "# and otherwise returns false. \n",
    "# Write another function main, in main() function accept a string from user and count number \n",
    "# of vowels in that string.\n",
    "\n",
    "def is_vowel(strn):\n",
    "    vow = 'aeiouAEIOU'\n",
    "    if strn in vow:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "def main():\n",
    "    strng = input('Enter a String:\\t')\n",
    "    count = 0\n",
    "    for i in strng:\n",
    "        if is_vowel(i) == True:\n",
    "            count = count + 1\n",
    "    return(round(count))\n",
    "main()\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1bbe704",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
