{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0a7539e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize a dictionary \"emp_info\" with below details\n",
    "# In - emp_info['Tom']\n",
    "# Out - {'email':'tom_latham019@gmail.com', 'Phone': +1987654321, 'City': 'California'}\n",
    "\n",
    "# In - emp_info['Kathy']\n",
    "# Out - {'email':'kathy_abram897@gmail.com', 'Phone': +1887654321, 'City': 'New York'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dcb9a7d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Name:\tTom\n",
      "Enter the Key:\temail\n",
      "Enter the Value:\ttom_latham019@gmail.com\n",
      "Enter the Key:\tPhone\n",
      "Enter the Value:\t+1987654321\n",
      "Enter the Key:\tCity\n",
      "Enter the Value:\tCalifornia\n",
      "Enter the Name:\tKathy\n",
      "Enter the Key:\temail\n",
      "Enter the Value:\tkathy_abram897@gmail.com\n",
      "Enter the Key:\tPhone\n",
      "Enter the Value:\t+1887654321\n",
      "Enter the Key:\tCity\n",
      "Enter the Value:\tNew York\n",
      "{'Tom': {'email': 'tom_latham019@gmail.com', 'Phone': '+1987654321', 'City': 'California'}, 'Kathy': {'email': 'kathy_abram897@gmail.com', 'Phone': '+1887654321', 'City': 'New York'}}\n"
     ]
    }
   ],
   "source": [
    "emp_info = {}\n",
    "\n",
    "for i in range(2):\n",
    "    emp_name = input('Enter the Name:\\t')\n",
    "    info = {}\n",
    "    for j in range(3):\n",
    "        info1 = input('Enter the Key:\\t')\n",
    "        info2 = input('Enter the Value:\\t')\n",
    "        \n",
    "        info[info1] = info2\n",
    "    emp_info[emp_name] = info\n",
    "print(emp_info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cadc8237",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a dictionary out of below inputs\n",
    "# lst1 = ['emp1', 'emp2', 'emp3']\n",
    "# emp_key = ['e_name', 'e_id', 'e_sal']\n",
    "# emp1_val = ['John', 'SG101', '$10,000']\n",
    "# emp2_val = ['Smith', 'SG102', '$9,000']\n",
    "# emp3_val = ['Peter', 'SG103', '$9,500']\n",
    "\n",
    "# Expected Output:- {'emp1':{'e_name':'John', 'e_id':'SG101', 'e_sal':$10,000}, \n",
    "#                    'emp2':{'e_name':'Smith', 'e_id':'SG102', 'e_sal':$9,000}, \n",
    "#                    'emp3':{'e_name':'Peter', 'e_id':'SG103', 'e_sal':$9,500}}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "717ae0d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'emp1': {'e_name': 'John', 'e_id': 'SG101', 'e_sal': '$10,000'}, 'emp2': {'e_name': 'Smith', 'e_id': 'SG102', 'e_sal': '$9,000'}, 'emp3': {'e_name': 'Peter', 'e_id': 'SG103', 'e_sal': '$9,500'}}\n"
     ]
    }
   ],
   "source": [
    "emp1_val = ['John', 'SG101', '$10,000']\n",
    "emp2_val = ['Smith', 'SG102', '$9,000']\n",
    "emp3_val = ['Peter', 'SG103', '$9,500']\n",
    "emp_key = ['e_name', 'e_id', 'e_sal']\n",
    "lst1 = ['emp1', 'emp2', 'emp3']\n",
    "lst={}\n",
    "\n",
    "for i,k in zip([emp1_val,emp2_val,emp3_val],lst1):\n",
    "    in_d = {}\n",
    "    for j in range(len(i)):\n",
    "        in_d[emp_key[j]] = i[j]\n",
    "    lst[k] = in_d\n",
    "print(lst)\n",
    "    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5e6d6987",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "80\n"
     ]
    }
   ],
   "source": [
    "# Acess the value of key 'history'\n",
    "\n",
    "sampleDict = { \n",
    "   \"class\":{ \n",
    "      \"student\":{ \n",
    "         \"name\":\"Mike\",\n",
    "         \"marks\":{ \n",
    "            \"physics\":70,\n",
    "            \"history\":80\n",
    "         }\n",
    "      }\n",
    "   }\n",
    "}\n",
    "\n",
    "\n",
    "print(sampleDict['class']['student']['marks']['history'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "256703f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize dictionary with default values. Inputs are:-\n",
    "# employees = ['Kelly', 'Emma', 'John']\n",
    "# defaults = {\"designation\": 'Application Developer', \"salary\": 8000}\n",
    "\n",
    "#Expected output:- {'Kelly': {'designation': 'Application Developer', 'salary': 8000}, \n",
    "#                   'Emma': {'designation': 'Application Developer', 'salary': 8000}, \n",
    "#                   'John': {'designation': 'Application Developer', 'salary': 8000}}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d062b6fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Kelly': {'designation': 'Application Developer', 'salary': 8000}, 'Emma': {'designation': 'Application Developer', 'salary': 8000}, 'John': {'designation': 'Application Developer', 'salary': 8000}}\n"
     ]
    }
   ],
   "source": [
    "employees = ['Kelly', 'Emma', 'John']\n",
    "defaults = {\"designation\": 'Application Developer', \"salary\": 8000}\n",
    "lst = {}\n",
    "\n",
    "for i in employees:\n",
    "    lst[i] = defaults\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e016cc11",
   "metadata": {},
   "outputs": [],
   "source": [
    "# In gene expression, mRNA is transcribed from a DNA template. \n",
    "# The 4 nucleotide bases of A, T, C, G corresponds to the U, A, G, C bases of the mRNA. \n",
    "# Write a function that returns the mRNA transcript given the sequence of a DNA strand.\n",
    "\n",
    "# Use a dictionary to provide the mapping of DNA to RNA bases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "76202fb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "UACUAACUGUAACUCCUAGGUA\n"
     ]
    }
   ],
   "source": [
    "def dna2rna(dna_seq):\n",
    "    rna_seq = ''\n",
    "    mapp = {'A':'U','T':'A','C':'G','G':'C'}\n",
    "    for i in dna_seq:\n",
    "        rna_seq = rna_seq + mapp.get(i)\n",
    "    return rna_seq\n",
    "    \n",
    "print(dna2rna('ATGATTGACATTGAGGATCCAT'))\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1b7df48d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write a function which takes a word as input and returns a dictionary with\n",
    "# letters as key and no of time letters are repeated as value.\n",
    "# In - count_letter('google.com')\n",
    "# Out - {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2eea66b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'m': 1, 'c': 1, 'l': 1, 'g': 2, 'o': 3, 'e': 1, '.': 1}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def dicto(strng):\n",
    "    set1 = set(strng)\n",
    "    dicte = {}\n",
    "    for i in set1:\n",
    "        dicte[i] = strng.count(i)\n",
    "    return dicte\n",
    "dicto('google.com')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "bc594d66",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A DNA strand consisting of the 4 nucleotide bases is usually represented with a string of letters: A,T, C, G. \n",
    "# Write a function that computes the base composition of a given DNA sequence.\n",
    "\n",
    "# In - baseComposition(\"CTATCGGCACCCTTTCAGCA\")\n",
    "# Out - {'A': 4, 'C': 8, 'T': 5,  'G': 3 }\n",
    "    \n",
    "# In - baseComposition(\"AGT\")\n",
    "# Out - {'A': 1, 'C': 0, 'T': 1,  'G': 1 }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "32a5f39c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A': 4, 'T': 5, 'C': 8, 'G': 3}\n",
      "{'A': 1, 'T': 1, 'C': 0, 'G': 1}\n"
     ]
    }
   ],
   "source": [
    "def baseComposition(strng):\n",
    "    nucleotide = ['A','T','C','G']\n",
    "    dicto = {}\n",
    "    for i in nucleotide:\n",
    "        dicto[i] = strng.count(i)\n",
    "    return dicto\n",
    "print(baseComposition('CTATCGGCACCCTTTCAGCA'))\n",
    "print(baseComposition('AGT'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ed87ed98",
   "metadata": {},
   "outputs": [],
   "source": [
    "# [MCQ] Suppose \"d\" is an empty dictionary, which statement does not assign \"d\" with {\"Name\":\"Tom\"}? \n",
    "# 1. d = {\"Name\": \"Tom\" }\n",
    "# 2. d[\"Name\"] = \"Tom\"\n",
    "# 3. d.update({\"Name\": \"Tom\" })\n",
    "# 4. d.setdefault(\"Name\", \"Tom\")\n",
    "# 5. None of the above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "41f06785",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Tom'}\n"
     ]
    }
   ],
   "source": [
    "#1,2,3,4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "09337428",
   "metadata": {},
   "outputs": [],
   "source": [
    "# [MCQ] d = {\"a\":1, \"b\":2}. Which of the statements returns [1,2]? \n",
    "# 1. d.keys()\n",
    "# 2. d.values()\n",
    "# 3. d.items()\n",
    "# 4. d.popitem()\n",
    "# 5. None of the above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "73441c83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('b', 2)\n"
     ]
    }
   ],
   "source": [
    "#2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e5489b84",
   "metadata": {},
   "outputs": [],
   "source": [
    "# [MCQ] Which of the following declarations is not valid for 'dict' type?\n",
    "# 1. d = {\"Name\": \"Tom\" }\n",
    "# 2. d = { (1,3,4): 4.5 }\n",
    "# 3. d = { [\"First\", \"Last\"]: (1,3) }\n",
    "# 4. d = { 1: 0.4 }\n",
    "# 5. None of the above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2a6656aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1,2,3,4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "18289f10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write a function reverseLookup(dictionary, value) that takes in a dictionary \n",
    "# and a value as arguments and returns a sorted list of all keys that contains the value. \n",
    "# The function will return an empty list if no match is found.\n",
    "\n",
    "# In - reverseLookup({'a':1, 'b':2, 'c':2}, 1)\n",
    "# Out - ['a']\n",
    "# In - reverseLookup({'a':1, 'b':2, 'c':2}, 2)\n",
    "# Out - ['b', 'c']\n",
    "# In - reverseLookup({'a':1, 'b':2, 'c':2}, 3)\n",
    "# Out - []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "9086a394",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c']\n"
     ]
    }
   ],
   "source": [
    "def reverseLookup(dicto, val):\n",
    "    key_lst = list(dicto.keys())\n",
    "    val_lst = list(dicto.values())\n",
    "    idx = 0\n",
    "    out_lst = []\n",
    "    for i in range(idx,len(val_lst)):\n",
    "        if val_lst[i] == val:\n",
    "            out_lst.append(key_lst[i])\n",
    "            idx = i+1\n",
    "            continue\n",
    "    out_lst.sort()\n",
    "    return out_lst\n",
    "     \n",
    "print(reverseLookup({'a':3, 'b':3, 'c':3}, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "dec2585a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write a function invertDictionary(d) that takes in a dictionary as\n",
    "# argument and return a dictionary that inverts the keys and the values of the original dictionary.\n",
    "# In - invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})\n",
    "# Out - {1: ['a'], 2: ['b', 'd'], 3: ['c']}\n",
    "# In - invertDictionary({'a':3, 'b':3, 'c':3})\n",
    "# Out - {3: ['a', 'c', 'b']}\n",
    "# In - invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})\n",
    "# Out - {1: ['b', 'd'], 2: ['a', 'c']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "a4021657",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: ['b', 'd'], 2: ['a', 'c']}\n"
     ]
    }
   ],
   "source": [
    "def invertDictionary(d):\n",
    "    val_lst = set(d.values())\n",
    "    dicto = {}\n",
    "    for i in val_lst:\n",
    "        dicto[i] = reverseLookup(d,i)\n",
    "    return dicto\n",
    "print(invertDictionary({'a':2, 'b':1, 'c':2, 'd':1}))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "f5470e70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write a function that converts a sparse vector into a dictionary as described above.\n",
    "# In - convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])\n",
    "# Out - {0: 1, 3: 2, 7: 3, 12: 4}\n",
    "# In - convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])\n",
    "# Out - {0: 1, 2: 1, 4: 2, 6: 1, 9: 1}\n",
    "# In - convertVector([0, 0, 0, 0, 0])\n",
    "# Out - {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "66500c96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: 1, 2: 1, 4: 2, 6: 1, 9: 1}\n"
     ]
    }
   ],
   "source": [
    "def convertVector(lst):\n",
    "    idx = 0\n",
    "    dicto = {}\n",
    "    for i in range(idx,len(lst)):\n",
    "        if lst[i] != 0:\n",
    "            dicto[i] = lst[i]\n",
    "            idx = i+1\n",
    "            continue\n",
    "    return dicto\n",
    "print(convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0]))            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "4c8bc6a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write a function that converts a dictionary back to its sparse vector representation.\n",
    "# In - convertDictionary({0: 1, 3: 2, 7: 3, 12: 4})\n",
    "# Out - [1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]\n",
    "# In - convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})\n",
    "# Out - [1, 0, 1, 0, 2, 0, 1, 0, 0, 1]\n",
    "# In - convertDictionary({})\n",
    "# Out - []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "06181bfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 0, 1, 0, 2, 0, 1, 0, 0, 1]"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def convertDictionary(d):\n",
    "    key_lst = list(d.keys())\n",
    "    val_lst = list(d.values())\n",
    "    lst = []\n",
    "    idx = 0\n",
    "    try:\n",
    "        lent = key_lst[-1]\n",
    "    except IndexError:\n",
    "        pass\n",
    "    for i in range(len(key_lst)):\n",
    "        for j in range(len(lst),lent+1):\n",
    "            if key_lst[i] == j:\n",
    "                lst.append(val_lst[i])\n",
    "                break\n",
    "            else:\n",
    "                lst.append(0)\n",
    "    return lst\n",
    "convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "c3321c25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__class__',\n",
       " '__class_getitem__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__delitem__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__ior__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__or__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__reversed__',\n",
       " '__ror__',\n",
       " '__setattr__',\n",
       " '__setitem__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'fromkeys',\n",
       " 'get',\n",
       " 'items',\n",
       " 'keys',\n",
       " 'pop',\n",
       " 'popitem',\n",
       " 'setdefault',\n",
       " 'update',\n",
       " 'values']"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Given a Python dictionary, Change Brad’s salary to 8500\n",
    "# sampleDict = {\n",
    "#      'emp1': {'name': 'Jhon', 'salary': 7500},\n",
    "#      'emp2': {'name': 'Emma', 'salary': 8000},\n",
    "#      'emp3': {'name': 'Brad', 'salary': 6500}\n",
    "# }\n",
    "\n",
    "# Expected Output\n",
    "# sampleDict = {\n",
    "#      'emp1': {'name': 'Jhon', 'salary': 7500},\n",
    "#      'emp2': {'name': 'Emma', 'salary': 8000},\n",
    "#      'emp3': {'name': 'Brad', 'salary': 8500}\n",
    "# }\n",
    "dir(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "34bcdca6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method_descriptor:\n",
      "\n",
      "pop(...)\n",
      "    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\n",
      "    \n",
      "    If the key is not found, return the default if given; otherwise,\n",
      "    raise a KeyError.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(dict.pop)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a21654eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "sampleDict = {\n",
    "      'emp1': {'name': 'Jhon', 'salary': 7500},\n",
    "      'emp2': {'name': 'Emma', 'salary': 8000},\n",
    "      'emp3': {'name': 'Brad', 'salary': 6500}\n",
    " }\n",
    "\n",
    "sampleDict.update()"
   ]
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
