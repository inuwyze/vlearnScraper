{
 "metadata": {
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
   "version": "3.7.4-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.4 32-bit",
   "metadata": {
    "interpreter": {
     "hash": "378b5933d7440af72b272972b00016984f867e5c35dd4f56f11ce3af81f7077f"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "524\n['Mon (10.45 am to 12.45 pm)']\n['Mon (10.45 am to 12.45 pm)']\n['Mon (10.45 am to 12.45 pm)']\n['Sat (8.45 am to 10.45 am)']\n['Sat (8.45 am to 10.45 am)']\n['Sat (8.45 am to 10.45 am)']\n['Fri (10.45 am to 12.45 pm)']\n['Fri (10.45 am to 12.45 pm)']\n['Fri (10.45 am to 12.45 pm)']\n['Thurs (8.45 am to 10.45 am)']\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "\n",
    "mynewlist=None\n",
    "with open('courseDetails.pkl','rb') as f:\n",
    "    mynewlist = pickle.load(f)\n",
    "\n",
    "# print(mynewlist[0])\n",
    "print(len(mynewlist))\n",
    "for x in mynewlist[445:455]:\n",
    "    print(x[0].split(',',7))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}