{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2cec759b",
   "metadata": {},
   "source": [
    "#Write a Python program to find the sum of all elements in a list using loop.\n",
    "#Input:- [10,20,30,40]\n",
    "#Output:- 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eaf8814f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,20,30,40\n",
      "[10, 20, 30, 40] <class 'list'>\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "sum = 0\n",
    "for i in lst:\n",
    "    sum = sum + i\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c3cd00f",
   "metadata": {},
   "source": [
    "#Write a Python program to find the multiplication of all elements in a list using loop.\n",
    "#Input:- [10,20,30,40]\n",
    "#Output:- 240000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2635c44c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,20,30,40\n",
      "[10, 20, 30, 40] <class 'list'>\n",
      "240000\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "mul = 1\n",
    "for i in lst:\n",
    "    mul = mul * i\n",
    "print(mul)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31557a46",
   "metadata": {},
   "source": [
    "#Write a Python program to find the largest number from a list using loop.\n",
    "#Input:- [10,100,2321, 1,200,2]\n",
    "#Output:- 2321\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c34b1baf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,100,2321,1,200,2\n",
      "[10, 100, 2321, 1, 200, 2] <class 'list'>\n",
      "2321\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "num = lst[0]\n",
    "for i in range(0,len(lst)):\n",
    "    if  lst[i] >= num:\n",
    "        num = lst[i]\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd40eb66",
   "metadata": {},
   "source": [
    "#Write a Python program to find the smallest number from a list using loop.\n",
    "#Input:- [10,100,2321, 1,200,2]\n",
    "#Output:- 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f6f66080",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,100,2321,1,200,2\n",
      "[10, 100, 2321, 1, 200, 2] <class 'list'>\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "num = lst[0]\n",
    "for i in range(0,len(lst)):\n",
    "    if  lst[i] <= num:\n",
    "        num = lst[i]\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8738b6b",
   "metadata": {},
   "source": [
    "#Write a Python program to count the number of strings having length more than 2 and are palindrome in a list using loop.\n",
    "#Input:- ['ab', 'abc', 'aba', 'xyz', '1991']\n",
    "#Output:- 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a7e679d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List'ab', 'abc', 'aba', 'xyz', '1991'\n",
      "['ab', 'abc', 'aba', 'xyz', '1991'] <class 'list'>\n",
      "aba 3\n",
      "1991 4\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "strg = ''\n",
    "\n",
    "for i in lst:\n",
    "    strg = i\n",
    "    if len(strg)>2:\n",
    "        strf = strg[::-1]\n",
    "        if strg == strf:\n",
    "            print(strg,len(strg))\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66258d89",
   "metadata": {},
   "source": [
    "#Write a Python program to sort a list in ascending order using loop.\n",
    "#Input:- [100,10,1,298,65,483,49876,2,80,9,9213]\n",
    "#Output:- [1,2,9,10,65,80,100,298,483,9213,49876]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8b4fc089",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List100,10,1,298,65,483,49876,2,80,9,9213\n",
      "[100, 10, 1, 298, 65, 483, 49876, 2, 80, 9, 9213] <class 'list'>\n",
      "[1, 2, 9, 10, 65, 80, 100, 298, 483, 9213, 49876]\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "temp = 0\n",
    "num = lst[0]\n",
    "for i in range(0,len(lst)):\n",
    "    for j in range(i+1,len(lst)):\n",
    "        if lst[i]>=lst[j]:\n",
    "            temp = lst[i]\n",
    "            lst[i] = lst[j]\n",
    "            lst[j] = temp\n",
    "    \n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3530f959",
   "metadata": {},
   "source": [
    "#Write a Python program to get a sorted list in increasing order of last element in each tuple in a given list using loop.\n",
    "#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]\n",
    "#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7d9e32af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)\n",
      "[(5, 4), (9, 1), (2, 3), (5, 9), (7, 6), (5, 5)] <class 'list'>\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "\n",
    "temp = 0\n",
    "num = lst[0]\n",
    "for i in range(0,len(lst)):\n",
    "    for j in range(i+1,len(lst)):\n",
    "        if lst[i][1]>=lst[j][1]:\n",
    "            temp = lst[i]\n",
    "            lst[i] = lst[j]\n",
    "            lst[j] = temp\n",
    "    \n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38616b18",
   "metadata": {},
   "source": [
    "#Write a Python program to remove duplicate element from a list using loop.\n",
    "#Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]\n",
    "#Output:- [10,1,11,29,876,768,92]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "85571e88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,1,11,1,29,876,768,10,11,1,92,29,876\n",
      "[10, 1, 11, 1, 29, 876, 768, 10, 11, 1, 92, 29, 876] <class 'list'>\n",
      "[10, 1, 11, 29, 876, 768, 92]\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "for i in lst:\n",
    "    for j in range(len(lst)-1,lst.index(i),-1):\n",
    "        if i == lst[j]:\n",
    "            lst.pop(j)\n",
    "            continue\n",
    "   \n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "bad8347b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,1,11,1,29,876,768,10,11,1,92,29,876\n",
      "[10, 1, 11, 1, 29, 876, 768, 10, 11, 1, 92, 29, 876] <class 'list'>\n",
      "[10, 1, 11, 29, 876, 768, 92]\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "\n",
    "lst = [lst[i] for i in range(0,len(lst)) if i== lst.index(lst[i])]\n",
    "\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7d6a741",
   "metadata": {},
   "source": [
    "#Write a Python program to check a list is empty or not?\n",
    "#Input:- []\n",
    "#Output:- List is empty\n",
    "#Input:- [10,20,30]\n",
    "#Output:- List is not empty"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "70740d17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List[]\n",
      "[] <class 'list'>\n",
      "List is Empty\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "\n",
    "if len(lst)== 0:\n",
    "    print('List is Empty')\n",
    "else:\n",
    "    print('List is not Empty')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9ddc73f",
   "metadata": {},
   "source": [
    "#Write a Python program to copy a list using loop.\n",
    "#inp_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]\n",
    "#out_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "4ec047aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,10.20,10+20j, 'Python', [10,20], (10,20)\n",
      "[10, 10.2, (10+20j), 'Python', [10, 20], (10, 20)] <class 'list'>\n",
      "[10, 10.2, (10+20j), 'Python', [10, 20], (10, 20)]\n"
     ]
    }
   ],
   "source": [
    "lst = list(eval(input('Enter the List')))\n",
    "print(lst, type(lst))\n",
    "\n",
    "lst1 = [i for i in lst if 1==1]\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a84b514",
   "metadata": {},
   "source": [
    "#Write a Python program to find the list of words that are longer than or equal to 4 from a given string.\n",
    "#Input:- 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'\n",
    "#Output:- ['much', 'wood', 'would', 'woodchuck', 'chuck', 'could']\n",
    "#Note:- Duplicate should be avoided."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "29d982f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the ListHow much wood would a woodchuck chuck if a woodchuck could chuck wood\n",
      "['much', 'wood', 'would', 'woodchuck', 'chuck', 'could'] <class 'list'>\n"
     ]
    }
   ],
   "source": [
    "strg = input('Enter the List')\n",
    "lst = strg.split(' ')\n",
    "\n",
    "lst = [lst[i] for i in range(0,len(lst)) if len(lst[i]) >= 4 and i == lst.index(lst[i])]\n",
    "\n",
    "print(lst, type(lst))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdae0d0f",
   "metadata": {},
   "source": [
    "#Write a Python program which takes two list as input and returns True if they have at least 3 common elements.\n",
    "#inp_lst1 = [10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]\n",
    "#inp_lst2 = [(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']\n",
    "#Output:- True\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "0eb26d7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List[10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]\n",
      "[10, 20, 'Python', 10.2, (10+20j), [10, 20, 30], (10, 20, 30)] <class 'list'>\n",
      "Enter the List[(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']\n",
      "[(10, 20, 30), 1, (20+3j), 100.2, (10+20j), [10, 20, 30], 'Python'] <class 'list'>\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "lst1 = list(eval(input('Enter the List')))\n",
    "print(lst1, type(lst1))\n",
    "\n",
    "lst2 = list(eval(input('Enter the List')))\n",
    "print(lst2, type(lst2))\n",
    "\n",
    "num = 0\n",
    "\n",
    "for i in lst1:\n",
    "    for j in lst2:\n",
    "        if i==j:\n",
    "            num = num + 1\n",
    "\n",
    "if num >= 3:\n",
    "    print('True')\n",
    "else:\n",
    "    print('False')\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73f467ff",
   "metadata": {},
   "source": [
    "#Write a Python program to create a 4X4 2D matrix with below elements using loop and list comprehension both.\n",
    "#Output:- [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "88302154",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]\n"
     ]
    }
   ],
   "source": [
    "lst1 = []\n",
    "lst2 = []\n",
    "for i in range(0,4):\n",
    "    lst2 = []\n",
    "    for j in range(0,4):\n",
    "        lst2.append(i*j)\n",
    "    lst1.append(lst2)\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d9c95189",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]\n"
     ]
    }
   ],
   "source": [
    "lst1 = [[i*j for i in range(0,4)] for j in range(0,4)]\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48fb54f7",
   "metadata": {},
   "source": [
    "#Write a Python program to create a 3X4X6 3D matrix wiith below elements using loop\n",
    "#Output:- \n",
    "# [\n",
    "#     [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],\n",
    "#     [[0,0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]],\n",
    "#     [[0,0,0,0,0,0],[2,2,2,2,2,2],[4,4,4,4,4,4],[6,6,6,6,6,6]]\n",
    "# ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6b3ab969",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]], [[0, 0, 0, 0, 0, 0], [2, 2, 2, 2, 2, 2], [4, 4, 4, 4, 4, 4], [6, 6, 6, 6, 6, 6]]]\n"
     ]
    }
   ],
   "source": [
    "lst1 = []\n",
    "lst2 = []\n",
    "lst3 = []\n",
    "for i in range(0,3):\n",
    "    lst2 = []\n",
    "    for j in range(0,4):\n",
    "        lst3 = []\n",
    "        for k in range(0,6):\n",
    "            lst3.append(j*i)\n",
    "        lst2.append(lst3)\n",
    "    lst1.append(lst2)\n",
    "        \n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "68dbd6f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]], [[0, 0, 0, 0, 0, 0], [2, 2, 2, 2, 2, 2], [4, 4, 4, 4, 4, 4], [6, 6, 6, 6, 6, 6]]]\n"
     ]
    }
   ],
   "source": [
    "lst1 = [[[k*j for i in range(0,6)] for j in range(0,4)] for k in range(0,3)]\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ac486f7",
   "metadata": {},
   "source": [
    "#Write a Python program which takes a list of numbers as input and prints a new list after removing even numbers from it.\n",
    "#Input:- [10,21,22,98,87,45,33,1,2,100]\n",
    "#Output:- [21,87,45,33,1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c7a3cd5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,21,22,98,87,45,33,1,2,100\n",
      "[10, 21, 22, 98, 87, 45, 33, 1, 2, 100] <class 'list'>\n",
      "[21, 87, 45, 33, 1]\n"
     ]
    }
   ],
   "source": [
    "lst1 = list(eval(input('Enter the List')))\n",
    "print(lst1, type(lst1))\n",
    "\n",
    "for i in lst1.copy():\n",
    "    if i%2==0:\n",
    "        lst1.remove(i)\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "09b8b54c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the List10,21,22,98,87,45,33,1,2,100\n",
      "[10, 21, 22, 98, 87, 45, 33, 1, 2, 100] <class 'list'>\n",
      "[21, 87, 45, 33, 1]\n"
     ]
    }
   ],
   "source": [
    "lst1 = list(eval(input('Enter the List')))\n",
    "print(lst1, type(lst1))\n",
    "\n",
    "lst1 = [i for i in lst1.copy() if i%2!=0]\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2ed01ae",
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
