{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c84bb76a",
   "metadata": {},
   "source": [
    "Q. W. A P. which takes one number from 0 to 9 from the user and prints\n",
    "it in the word. And if the word is not from 0 to 9 then\n",
    "it should print that number is outside of the range and program should\n",
    "exit.\n",
    "For exapmple:-\n",
    "input = 1\n",
    "output = one"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6657aabf",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = int(input('Enter the Number between 0-9:'))\n",
    "if num == 0:\n",
    "    print('Zero')\n",
    "elif num == 1:\n",
    "    print('One')\n",
    "elif num == 2:\n",
    "    print('Two')\n",
    "elif num == 3:\n",
    "    print('Three')\n",
    "elif num == 4:\n",
    "    print('Four')\n",
    "elif num == 5:\n",
    "    print('Five')\n",
    "elif num == 6:\n",
    "    print('Six')\n",
    "elif num == 7:\n",
    "    print('Seven')\n",
    "elif num == 8:\n",
    "    print('Eight')\n",
    "elif num == 9:\n",
    "    print('Nine')\n",
    "else:\n",
    "    print('Invalid')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a43b676",
   "metadata": {},
   "source": [
    "Q. W A P to check whether a year entered by user is an leap year or not?\n",
    "Check with below input:-\n",
    "leap year:- 2012, 1968, 2004, 1200, 1600,2400\n",
    "Non-lear year:- 1971, 2006, 1700,1800,1900"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "b6452c6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Year:1800\n",
      "Not a Leap Year\n"
     ]
    }
   ],
   "source": [
    "year = int(input('Enter Year:'))\n",
    "\n",
    "if (year%100 == 0) and (year%400 == 0):\n",
    "    print('Leap Year')\n",
    "elif (year%4 == 0) and (year%100 != 0):\n",
    "    print('Leap Year')\n",
    "else:\n",
    "    print('Not a Leap Year')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04ab7a46",
   "metadata": {},
   "source": [
    "Q. W A P which takes one number from the user and checks whether it is\n",
    "an even or odd number?, If it even then prints number is\n",
    "even number else prints that number is odd number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f90f974d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a Number:0\n",
      "Even\n"
     ]
    }
   ],
   "source": [
    "num = int(input('Enter a Number:'))\n",
    "\n",
    "if (num % 2 == 0):\n",
    "    print('Even')\n",
    "elif (num % 2 == 1):\n",
    "    print('Odd')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c58c054",
   "metadata": {},
   "source": [
    "Q. W A P which takes two numbers from the user and prints below output:-\n",
    "1. num1 is greater than num2 if num1 is greater than num2\n",
    "2. num1 is smaller than num2 if num1 is smaller than num2\n",
    "3. num1 is equal to num2 if num1 and num2 are equal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "cfe1623a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter First Number:5\n",
      "Enter Second Number:3\n",
      "5 is greater than 3\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input('Enter First Number:'))\n",
    "num2 = int(input('Enter Second Number:'))\n",
    "\n",
    "print('{} is greater than {}'.format(num1,num2)) if num1>num2 else print('{} is equal to {}'.format(num1,num2)) if num1 == num2 else print('{} is smaller than {}'.format(num1,num2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01352329",
   "metadata": {},
   "source": [
    "Q. Write a Python program to find the length of the my_str using loop:-\n",
    "Input:- 'Write a Python program to find the length of the my_str'\n",
    "Output:- 55"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a4c72478",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "my_str = 'Write a Python program to find the length of the my_str'\n",
    "\n",
    "num = 0\n",
    "\n",
    "for i in my_str:\n",
    "    num = num + 1\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f029b435",
   "metadata": {},
   "source": [
    "Q. Write a Python program to find the total number of times letter 'p'\n",
    "is appeared in the below string using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.\\n'\n",
    "Output:- 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d5e26321",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "my_str = 'peter piper picked a peck of pickled peppers.\\n'\n",
    "\n",
    "num = 0\n",
    "\n",
    "for i in range(0,len(my_str)):\n",
    "    if my_str[i] == 'p':\n",
    "        num = num+1\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db88d349",
   "metadata": {},
   "source": [
    "Q. Write a python program to find below output using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.'\n",
    "Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled',\n",
    "'peppers']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "bb85f313",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']\n"
     ]
    }
   ],
   "source": [
    "my_str = 'peter piper picked a peck of pickled peppers.'\n",
    "lst = []\n",
    "str=''\n",
    "for i in range(0,len(my_str)):\n",
    "    if my_str[i] != ' ':\n",
    "        str = str + my_str[i]\n",
    "    else:\n",
    "        lst.append(str)\n",
    "        str = ''\n",
    "        continue\n",
    "lst.append(str)\n",
    "print(lst)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85b7355d",
   "metadata": {},
   "source": [
    "Q. Write a python program to find below output using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.'\n",
    "Output:- 'peppers pickled of peck a picked piper peter'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "87514fd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "peppers. pickled of peck a picked piper peter\n"
     ]
    }
   ],
   "source": [
    "my_str = 'peter piper picked a peck of pickled peppers.'\n",
    "lst = []\n",
    "str=''\n",
    "for i in range(0,len(my_str)):\n",
    "    if my_str[i] != ' ':\n",
    "        str = str + my_str[i]\n",
    "    else:\n",
    "        lst.append(str)\n",
    "        str = ''\n",
    "        continue\n",
    "lst.append(str)\n",
    "print(' '.join(lst[len(lst)::-1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5dc50237",
   "metadata": {},
   "source": [
    "Q. Write a python program to find below output using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.'\n",
    "Output:- '.sreppep delkcip fo kcep a dekcip repip retep'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "cac913c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ".sreppep delkcip fo kcep a dekcip repip retep\n"
     ]
    }
   ],
   "source": [
    "my_str =  'peter piper picked a peck of pickled peppers.'\n",
    "new_str = ''\n",
    "for i in range(-1,-len(my_str)-1,-1):\n",
    "    new_str = new_str + my_str[i]\n",
    "print(new_str)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ea55b79",
   "metadata": {},
   "source": [
    "Q. Write a python program to find below output using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.'\n",
    "Output:- 'retep repip dekcip a kcep fo delkcip sreppep'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "03555b34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "retep repip dekcip a kcep fo delkcip .sreppep\n"
     ]
    }
   ],
   "source": [
    "my_str =  'peter piper picked a peck of pickled peppers.'\n",
    "new_str = ''\n",
    "for i in range(-1,-len(my_str)-1,-1):\n",
    "    new_str = new_str + my_str[i]\n",
    "    \n",
    "lst = []\n",
    "str=''\n",
    "for i in range(0,len(new_str)):\n",
    "    if new_str[i] != ' ':\n",
    "        str = str + new_str[i]\n",
    "    else:\n",
    "        lst.append(str)\n",
    "        str = ''\n",
    "        continue\n",
    "lst.append(str)\n",
    "print(' '.join(lst[len(lst)::-1]))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5d627f7",
   "metadata": {},
   "source": [
    "Q. Write a python program to find below output using loop:-\n",
    "Input:- 'peter piper picked a peck of pickled peppers.'\n",
    "Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "d37d4460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Peter Piper Picked A Peck Of Pickled Peppers.\n"
     ]
    }
   ],
   "source": [
    "my_str = 'peter piper picked a peck of pickled peppers.'\n",
    "lst = []\n",
    "str=''\n",
    "for i in range(0,len(my_str)):\n",
    "    if my_str[i] != ' ':\n",
    "        str = str + my_str[i]\n",
    "    else:\n",
    "        lst.append(str)\n",
    "        str = ''\n",
    "        continue\n",
    "lst.append(str)\n",
    "new_lst=[]\n",
    "for j in range(0,len(lst)):\n",
    "    new_lst.append(lst[j].capitalize())\n",
    "\n",
    "print(' '.join(new_lst[::]))    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f300e7f",
   "metadata": {},
   "source": [
    "Q. Write a python program to implement index method using loop. If\n",
    "sub_str is found in my_str then it will print the index\n",
    "of first occurrence of first character of matching string in my_str:-\n",
    "Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',\n",
    "sub_str = 'Pickl'\n",
    "Output:- 29"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "55f7f8a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n"
     ]
    }
   ],
   "source": [
    "my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'\n",
    "sub_str = 'Pickl'\n",
    "str = ''\n",
    "for i in range(0,len(my_str)):\n",
    "    for j in range(0,len(sub_str)):\n",
    "        str =str + my_str[i+j]\n",
    "    if sub_str == str:\n",
    "        print(i)\n",
    "        break\n",
    "    else:\n",
    "        str =''\n",
    "        continue\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "836ba9e3",
   "metadata": {},
   "source": [
    "Q. Write a python program to implement replace method using loop. If\n",
    "sub_str is found in my_str then it will replace the first\n",
    "occurrence of sub_str with new_str else it will will print sub_str not\n",
    "found:-\n",
    "Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',\n",
    "sub_str = 'Peck', new_str = 'Pack'\n",
    "Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "d579b131",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Peter Piper Picked A Pack Of Pickled Peppers.\n"
     ]
    }
   ],
   "source": [
    "my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'\n",
    "sub_str = 'Peck'\n",
    "new_str = 'Pack'\n",
    "str = ''\n",
    "for i in range(0,len(my_str)):\n",
    "    for j in range(0,len(sub_str)):\n",
    "        str =str + my_str[i+j]\n",
    "    if sub_str == str:\n",
    "        ind = i\n",
    "        break\n",
    "    else:\n",
    "        str =''\n",
    "        continue\n",
    "str = ''\n",
    "for a in range(0,ind):\n",
    "    str = str + my_str[a]\n",
    "for b, c in zip(range(ind,ind+len(new_str)), range(0,len(new_str))):\n",
    "                str = str + new_str[c]\n",
    "for d in range(ind+len(new_str),len(my_str)):\n",
    "    str = str + my_str[d]\n",
    "print(str)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "528ea6b8",
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
