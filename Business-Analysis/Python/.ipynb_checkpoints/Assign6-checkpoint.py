{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "757b1c98",
   "metadata": {},
   "source": [
    "Python Program to Count the Number of Vowels Present\n",
    "in a String using Sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a363e90b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    " def strcnt(strng):\n",
    "        vow = set('aeiouAEIOU')\n",
    "        cnt = 0\n",
    "        for i in strng:\n",
    "            if i in vow:\n",
    "                cnt = cnt +1\n",
    "        print(cnt)\n",
    "\n",
    "strcnt('nippO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc8303de",
   "metadata": {},
   "outputs": [],
   "source": [
    "strng = input('Enter the String:\\t')\n",
    "vow = 'aeiouAEIOU'\n",
    "lst = [i for i in strng if i in vow]\n",
    "print(len(lst))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef7029ce",
   "metadata": {},
   "source": [
    "Python Program to Check Common Letters in Two Input\n",
    "Strings:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "95032104",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first String:\tabcdefg\n",
      "Enter second String:\tefghijk\n",
      "{'e', 'f', 'g'}\n",
      "{'e', 'f', 'g'}\n"
     ]
    }
   ],
   "source": [
    "str1 = set(input('Enter first String:\\t'))\n",
    "str2 = set(input('Enter second String:\\t'))\n",
    "\n",
    "set3 = str1.intersection(str2)\n",
    "print(set3)\n",
    "\n",
    "set4 = str1 & str2\n",
    "print(set4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bca6752a",
   "metadata": {},
   "source": [
    "Python Program that Displays which Letters are in the\n",
    "First String but not in the Second:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f348681c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first String:\tabcdefghijk\n",
      "Enter second String:\tefghiijklmnop\n",
      "{'c', 'a', 'd', 'b'}\n",
      "{'c', 'a', 'd', 'b'}\n"
     ]
    }
   ],
   "source": [
    "str1 = set(input('Enter first String:\\t'))\n",
    "str2 = set(input('Enter second String:\\t'))\n",
    "\n",
    "set3 = str1.difference(str2)\n",
    "print(set3)\n",
    "\n",
    "set4 = str1 - str2\n",
    "print(set4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ea8020f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__and__',\n",
       " '__class__',\n",
       " '__class_getitem__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__iand__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__ior__',\n",
       " '__isub__',\n",
       " '__iter__',\n",
       " '__ixor__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__or__',\n",
       " '__rand__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__ror__',\n",
       " '__rsub__',\n",
       " '__rxor__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__sub__',\n",
       " '__subclasshook__',\n",
       " '__xor__',\n",
       " 'add',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'difference',\n",
       " 'difference_update',\n",
       " 'discard',\n",
       " 'intersection',\n",
       " 'intersection_update',\n",
       " 'isdisjoint',\n",
       " 'issubset',\n",
       " 'issuperset',\n",
       " 'pop',\n",
       " 'remove',\n",
       " 'symmetric_difference',\n",
       " 'symmetric_difference_update',\n",
       " 'union',\n",
       " 'update']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(set)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d08515bd",
   "metadata": {},
   "source": [
    "Python Program that Displays which Letters are Present\n",
    "in Both the Strings:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1ffe794e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first String:\tabcdefghijk\n",
      "Enter second String:\tefghijklmnop\n",
      "{'e', 'm', 'b', 'h', 'j', 'a', 'g', 'l', 'd', 'k', 'p', 'i', 'o', 'c', 'f', 'n'}\n",
      "['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']\n"
     ]
    }
   ],
   "source": [
    "str1 = set(input('Enter first String:\\t'))\n",
    "str2 = set(input('Enter second String:\\t'))\n",
    "\n",
    "set3 = str1.union(str2)\n",
    "print(set3)\n",
    "\n",
    "\n",
    "set5 = str1 | str2\n",
    "print(sorted(set5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b8a124b",
   "metadata": {},
   "source": [
    "Python Program that Displays which Letters are in the\n",
    "Two Strings but not in Both:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8828ee50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first String:\tabcdefghijk\n",
      "Enter second String:\tefghijklmnop\n",
      "['a', 'b', 'c', 'd', 'l', 'm', 'n', 'o', 'p']\n"
     ]
    }
   ],
   "source": [
    "str1 = set(input('Enter first String:\\t'))\n",
    "str2 = set(input('Enter second String:\\t'))\n",
    "\n",
    "set3 = str1 - str2\n",
    "set4 = str2 - str1\n",
    "set5 = set4 | set3\n",
    "print(sorted(set5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54f60078",
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
