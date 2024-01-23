{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8d59a0a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rat\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which gives output as:- 'cat' in str.\n",
    "import re\n",
    "str = 'cat mat bat rat'\n",
    "\n",
    "print(re.match(r'[r][a-z]{2}',str).group())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e017038d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rat\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which gives output as:- 'rat' in str.\n",
    "import re\n",
    "str = 'cat mat bat rat'\n",
    "\n",
    "print(re.search(r'r[a-z]{2}',str).group())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "679326e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mat', 'man']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which gives output as:- ['mat', 'man'] in str.\n",
    "import re\n",
    "str = 'cat mat bat rat man'\n",
    "\n",
    "print(re.findall(r'ma[a-z]',str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "3c95c9e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', 's', 'Programming', 'is', 'very', 'easy', 'to', 'learn']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which gives output as:- \n",
    "#['Python', 's', 'Programming', 'is', 'very', 'easy', 'to', 'learn'] in str.\n",
    "import re\n",
    "str = \"Python's Programming: is very easy to learn\"\n",
    "\n",
    "print(re.findall(r'[Pa-z]+',str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "34200841",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python Programming: is very easy to learn\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which gives output as:- Python Programming: is very easy to learn in str.\n",
    "import re\n",
    "str = \"Python's Programming: is very easy to learn\"\n",
    "\n",
    "lst = re.findall(r'[^\\'a-z][A-Za-z:]+',str)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "2e64d15c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peter', 'per', 'picked', 'peck', 'pickled', 'peppers']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words starting with p.\n",
    "#Output:- ['peter', 'per', 'picked', 'peck', 'pickled', 'peppers']\n",
    "import re\n",
    "str = \"peter giper picked a peck of pickled peppers\"\n",
    "\n",
    "lst = re.findall(r'p[A-Za-z:]+',str)\n",
    "print(lst)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "ca9e0046",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peter', 'picked', 'peck', 'pickled', 'peppers']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words starting with p except 'per' which is not a separate word.\n",
    "#Output:- ['peter', 'picked', 'peck', 'pickled', 'peppers']\n",
    "import re\n",
    "str = \"peter giper picked a peck of pickled peppers\"\n",
    "\n",
    "lst = re.findall(r'\\bp[A-Za-z:]+',str)\n",
    "print(lst)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "169f3212",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['8th', '11th']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words starting with a digit.\n",
    "#Output:- ['8th', '11th']\n",
    "import re\n",
    "str = 'The election in delhi will be held on 8th and result for the same will be declared on 11th'\n",
    "\n",
    "lst = re.findall(r'\\d[0-9A-Za-z:]+',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "7a73050c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peter', 'giper']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words having 5 characters.\n",
    "#Output:- ['peter', 'giper']\n",
    "import re\n",
    "str = \"peter giper picked a peck of pickled peppers\"\n",
    "\n",
    "lst = re.findall(r'\\b[a-z]{5}\\b',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "336925e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Retrieving', 'words', 'having', 'least', 'characters']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words having at least 4 characters.\n",
    "#Output:- ['Retrieving',  'words', 'having', 'least', 'characters']\n",
    "import re\n",
    "str = \"Retrieving all words having at least 4 characters\"\n",
    "\n",
    "lst = re.findall(r'\\b[A-Za-z0-9]{4,50}',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "d8ff42ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['all', 'words', 'least']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves all words having at characters between 3 to 5 words.\n",
    "#Output:- ['all', 'words', 'least']\n",
    "import re\n",
    "str = \"Retrieving all words having at least 4 characters\"\n",
    "\n",
    "lst = re.findall(r'\\b[A-Za-z0-9]{3,5}\\b',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "483ce4eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['8', '11']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves only digits from the string.\n",
    "#Output:- ['8', '11']\n",
    "import re\n",
    "str = 'The election in delhi will be held on 8 and result for the same will be declared on 11'\n",
    "\n",
    "lst = re.findall(r'[0-9]{1,50}',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "44af29ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1234567890']\n"
     ]
    }
   ],
   "source": [
    "#Write the regular expression and use proper method which Retrieves a phone number from the given string.\n",
    "#Output:- 1234567890\n",
    "import re\n",
    "str = \"Learnbay : 1234567890\"\n",
    "\n",
    "lst = re.findall(r'[0-9]{1,10}',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "613311e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Learnbay', ' : ']\n"
     ]
    }
   ],
   "source": [
    "##Write the regular expression and use proper method which Etracts name from the string but not number.\n",
    "#Output:- Learnbay : \n",
    "import re\n",
    "str = \"Learnbay : 1234567890\"\n",
    "\n",
    "lst = re.findall(r'[^0-9]{1,10}',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "e4a522a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['anil', 'akhil', 'anant', 'ankur']\n"
     ]
    }
   ],
   "source": [
    "##Write the regular expression and use proper method which Retrieves name starting with 'an' or 'ak'.\n",
    "#Output:- ['anil', 'akhil', 'anant', 'ankur']\n",
    "import re\n",
    "str = 'anil akhil anant abhi arun arati arundhati abhijit ankur'\n",
    "\n",
    "lst = re.findall(r'\\ba[nk][a-z]+\\b',str)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a953c869",
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
