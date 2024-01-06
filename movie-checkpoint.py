{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "44cec312",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn import svm\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c5d524c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "da = pd.read_csv(\"movies.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "710e801c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9742, 3)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "da.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "870914ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "db = pd.read_csv(\"ratings.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7a791c0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100836, 4)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "92b60760",
   "metadata": {},
   "outputs": [],
   "source": [
    "counts = data['userId'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "494c0a6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.info of         userId  movieId  rating   timestamp\n",
       "0            1        1     4.0   964982703\n",
       "1            1        3     4.0   964981247\n",
       "2            1        6     4.0   964982224\n",
       "3            1       47     5.0   964983815\n",
       "4            1       50     5.0   964982931\n",
       "...        ...      ...     ...         ...\n",
       "100831     610   166534     4.0  1493848402\n",
       "100832     610   168248     5.0  1493850091\n",
       "100833     610   168250     5.0  1494273047\n",
       "100834     610   168252     5.0  1493846352\n",
       "100835     610   170875     3.0  1493846415\n",
       "\n",
       "[100836 rows x 4 columns]>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "babfce2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "610\n"
     ]
    }
   ],
   "source": [
    "num_unique_userid = data['userId'].nunique()\n",
    "print(num_unique_userid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f363b1db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100836.000000</td>\n",
       "      <td>100836.000000</td>\n",
       "      <td>100836.000000</td>\n",
       "      <td>1.008360e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>326.127564</td>\n",
       "      <td>19435.295718</td>\n",
       "      <td>3.501557</td>\n",
       "      <td>1.205946e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>182.618491</td>\n",
       "      <td>35530.987199</td>\n",
       "      <td>1.042529</td>\n",
       "      <td>2.162610e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>8.281246e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>177.000000</td>\n",
       "      <td>1199.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.019124e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>325.000000</td>\n",
       "      <td>2991.000000</td>\n",
       "      <td>3.500000</td>\n",
       "      <td>1.186087e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>477.000000</td>\n",
       "      <td>8122.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.435994e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>610.000000</td>\n",
       "      <td>193609.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>1.537799e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              userId        movieId         rating     timestamp\n",
       "count  100836.000000  100836.000000  100836.000000  1.008360e+05\n",
       "mean      326.127564   19435.295718       3.501557  1.205946e+09\n",
       "std       182.618491   35530.987199       1.042529  2.162610e+08\n",
       "min         1.000000       1.000000       0.500000  8.281246e+08\n",
       "25%       177.000000    1199.000000       3.000000  1.019124e+09\n",
       "50%       325.000000    2991.000000       3.500000  1.186087e+09\n",
       "75%       477.000000    8122.000000       4.000000  1.435994e+09\n",
       "max       610.000000  193609.000000       5.000000  1.537799e+09"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe(include='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "eefa9e73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9742.000000</td>\n",
       "      <td>9742</td>\n",
       "      <td>9742</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>9737</td>\n",
       "      <td>951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Emma (1996)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>1053</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>42200.353623</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>52160.494854</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3248.250000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>7300.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>76232.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>193609.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              movieId        title genres\n",
       "count     9742.000000         9742   9742\n",
       "unique            NaN         9737    951\n",
       "top               NaN  Emma (1996)  Drama\n",
       "freq              NaN            2   1053\n",
       "mean     42200.353623          NaN    NaN\n",
       "std      52160.494854          NaN    NaN\n",
       "min          1.000000          NaN    NaN\n",
       "25%       3248.250000          NaN    NaN\n",
       "50%       7300.000000          NaN    NaN\n",
       "75%      76232.000000          NaN    NaN\n",
       "max     193609.000000          NaN    NaN"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "da.describe(include='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "489398a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The movie with the maximum number of user ratings is Movie ID 356.\n"
     ]
    }
   ],
   "source": [
    "movie_ratings_count = db.groupby('movieId')['rating'].count()\n",
    "max_rated_movie_id = movie_ratings_count.idxmax()\n",
    "print(f\"The movie with the maximum number of user ratings is Movie ID {max_rated_movie_id}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "90ce6347",
   "metadata": {},
   "outputs": [],
   "source": [
    "dc = pd.read_csv(\"tags.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "ae287c9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>tag</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>funny</td>\n",
       "      <td>1445714994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>Highly quotable</td>\n",
       "      <td>1445714996</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>will ferrell</td>\n",
       "      <td>1445714992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>89774</td>\n",
       "      <td>Boxing story</td>\n",
       "      <td>1445715207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>89774</td>\n",
       "      <td>MMA</td>\n",
       "      <td>1445715200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2567</th>\n",
       "      <td>477</td>\n",
       "      <td>2761</td>\n",
       "      <td>animation</td>\n",
       "      <td>1244787872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2568</th>\n",
       "      <td>477</td>\n",
       "      <td>3000</td>\n",
       "      <td>adventure</td>\n",
       "      <td>1241396438</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2569</th>\n",
       "      <td>477</td>\n",
       "      <td>3000</td>\n",
       "      <td>atmospheric</td>\n",
       "      <td>1241396434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2570</th>\n",
       "      <td>477</td>\n",
       "      <td>3000</td>\n",
       "      <td>fantasy world</td>\n",
       "      <td>1241396427</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2571</th>\n",
       "      <td>477</td>\n",
       "      <td>3000</td>\n",
       "      <td>Studio Ghibli</td>\n",
       "      <td>1241396420</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2572 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      userId  movieId              tag   timestamp\n",
       "0          2    60756            funny  1445714994\n",
       "1          2    60756  Highly quotable  1445714996\n",
       "2          2    60756     will ferrell  1445714992\n",
       "3          2    89774     Boxing story  1445715207\n",
       "4          2    89774              MMA  1445715200\n",
       "...      ...      ...              ...         ...\n",
       "2567     477     2761        animation  1244787872\n",
       "2568     477     3000        adventure  1241396438\n",
       "2569     477     3000      atmospheric  1241396434\n",
       "2570     477     3000    fantasy world  1241396427\n",
       "2571     477     3000    Studio Ghibli  1241396420\n",
       "\n",
       "[2572 rows x 4 columns]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dc.head(2572)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "7e9a2b6e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1939</th>\n",
       "      <td>2571</td>\n",
       "      <td>Matrix, The (1999)</td>\n",
       "      <td>Action|Sci-Fi|Thriller</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      movieId               title                  genres\n",
       "1939     2571  Matrix, The (1999)  Action|Sci-Fi|Thriller"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "da[da['title'] == 'Matrix, The (1999)']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "08a231a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average user rating for 'Terminator 2: Judgment Day (1991)' is: nan\n"
     ]
    }
   ],
   "source": [
    "movieId = \"589\"\n",
    "ratings = db[db['movieId'] == movieId]\n",
    "average_rating = ratings['rating'].mean()\n",
    "print(f\"The average user rating for '{title}' is: {average_rating}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "bd50b488",
   "metadata": {},
   "outputs": [],
   "source": [
    "movieId = \"2959\"\n",
    "movie_ratings = db[db['movieId'] == movieId]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "21886f24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2IAAANVCAYAAAAa0E2HAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABOVElEQVR4nO3deXxV5b3o/28gIQwCIsgkMyqiOEJFaClSBBWHOl2xWEewcmhVoNzWGbBW6sRB64BVnOo8FGvVUlDUasUZtA4X/VmEoxIRHEBQCLB+f3iTa0wYdgxPCLzfr1der7PXfvbaz955ytkf19oreVmWZQEAAEAytap7AgAAAFsbIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBmxxbr311sjLyyv9qVu3brRs2TL69esXEyZMiEWLFpV7zLhx4yIvLy+n51mxYkWMGzcunnrqqZweV9FzdejQIQ499NCc9rMhd911V0yaNKnC+/Ly8mLcuHFV+nxV7YknnogePXpEgwYNIi8vLx566KEKxz311FORl5cXDzzwQIX3/+pXv8r5d7sp7b///uXW56677hoXX3xxrFq1qlL7fOutt2LcuHHx/vvvl7vv5JNPjg4dOny/SW9Cn376aRx33HHRvHnzyMvLiyOOOGKTPt/+++8fJ598ckR8897sv//+pfctXLgwzj///OjVq1c0a9YsGjVqFN27d48//elPsWbNmjL7KVl3Ff08//zzZcaua1xeXl7ssssuZcZOmjQpjjrqqOjYsWPk5eWVmd+3jRs3rvT3WvJvHlCz5Ff3BAA2lVtuuSV22WWXKC4ujkWLFsWzzz4bl156aVxxxRVx7733xgEHHFA6dtiwYXHQQQfltP8VK1bE+PHjIyLW+WGpIpV5rsq466674o033oiRI0eWu2/WrFnRpk2bTT6HysqyLI499tjYeeed4+GHH44GDRpEly5dqntaVaZTp05x5513RkTEJ598EjfddFNccMEFsWDBgvjTn/6U8/7eeuutGD9+fOy///7louuCCy6Is846qyqmvUn87ne/i6lTp8bNN98cnTt3ju22267a5vLKK6/E7bffHieeeGJccMEFUVBQEH//+9/jv/7rv+L555+Pm2++udxjLrnkkujXr1+Zbd26dStze9asWeUe98ILL8TIkSPjyCOPLLN98uTJ0aBBg/jJT34Sf/vb36rgVQGbKyEGbLG6desWPXr0KL199NFHx6hRo+JHP/pRHHXUUfHuu+9GixYtIiKiTZs2mzxMVqxYEfXr10/yXBuy3377Vevzb8hHH30Un376aRx55JHRv3//6p5OTrIsi6+//jrq1au3zjH16tUr8zs4+OCDY9ddd43bbrstrr766qhbt26Vzadz585Vtq9N4Y033ojOnTvH8ccfXyX725j3f11++MMfxnvvvRcFBQWl2wYMGBCrVq2Ka6+9NsaPHx9t27Yt85iddtppg/97quj+G264IfLy8mLo0KFltr/11ltRq9Y3Jyx9N+iALYtTE4GtSrt27eLKK6+MZcuWxQ033FC6vaLTBWfOnBn7779/NG3aNOrVqxft2rWLo48+OlasWBHvv/9+bL/99hERMX78+NLTjEpOeSrZ36uvvhrHHHNMNGnSpPQD8fpOg5w6dWrsscceUbdu3ejUqVNcffXVZe4vOQXpu6eglZwmVXKa5P777x+PPvpozJ8/v8xpUCUqOjXxjTfeiJ/+9KfRpEmTqFu3buy1115x2223Vfg8d999d5x33nnRunXraNSoURxwwAExd+7cdb/x3/Lss89G//79o2HDhlG/fv3o3bt3PProo6X3jxs3rjRUf/vb30ZeXl6Vn1p3//33R8+ePaNx48ZRv3796NSpU5x66qllxixdujTGjBkTHTt2jDp16sQOO+wQI0eOjOXLl5cZl5eXF7/61a9i8uTJ0bVr1ygsLCz3vm1Ifn5+7LXXXrFq1ar4/PPPS7e//PLLcdxxx0WHDh2iXr160aFDh/jZz34W8+fPLx1z6623xv/6X/8rIiL69etX+ru+9dZbI6LiUxNL5vznP/85unbtGvXr148999wzHnnkkXJz++tf/xp77LFHFBYWRqdOneKqq66qcA1vzHv6be+//37k5eXF448/Hm+//XbpvEvW8KeffhojRoyIHXbYIerUqROdOnWK8847L1auXFnha/k+73+JJk2alImwEvvuu29ERHzwwQeV2u93LVu2LO6///7o27dv7LjjjmXuK4kwYMvniBiw1Rk0aFDUrl07/vnPf65zzPvvvx+HHHJI9OnTJ26++ebYdttt48MPP4xp06bFqlWrolWrVjFt2rQ46KCDYujQoTFs2LCIiNI4K3HUUUfFcccdF8OHDy/3Af675syZEyNHjoxx48ZFy5Yt484774yzzjorVq1aFWPGjMnpNV533XXxi1/8It57772YOnXqBsfPnTs3evfuHc2bN4+rr746mjZtGnfccUecfPLJ8fHHH8dvfvObMuPPPffc+OEPfxg33XRTLF26NH7729/GYYcdFm+//XbUrl17nc/z9NNPx4ABA2KPPfaIKVOmRGFhYVx33XVx2GGHxd133x2DBw+OYcOGxZ577hlHHXVUnHHGGTFkyJAoLCzM6fWvz6xZs2Lw4MExePDgGDduXNStWzfmz58fM2fOLB2zYsWK6Nu3b3zwwQdx7rnnxh577BFvvvlmXHjhhfHvf/87Hn/88TIh8tBDD8UzzzwTF154YbRs2TKaN2+e87zmzZsX2267bZk19P7770eXLl3iuOOOi+222y4WLlwY119/ffzgBz+It956K5o1axaHHHJIXHLJJXHuuefGtddeG/vss09EbPhI2KOPPhovvfRSXHTRRbHNNtvEZZddFkceeWTMnTs3OnXqFBER06ZNi6OOOip+/OMfx7333hurV6+OK664Ij7++OOc39PvatWqVcyaNStGjBgRX3zxRempmrvuumt8/fXX0a9fv3jvvfdi/Pjxsccee8QzzzwTEyZMiDlz5pQJ94jc3v9vf6ezJFY3ZObMmZGfnx8777xzuft++ctfxnHHHRf169ePXr16xQUXXBA/+tGP1ru/e+65J5YvX17670ZljBs3rvQ/ppx88sml/xEIqEEygC3MLbfckkVE9tJLL61zTIsWLbKuXbuW3h47dmz27X8SH3jggSwisjlz5qxzH5988kkWEdnYsWPL3VeyvwsvvHCd931b+/bts7y8vHLPN2DAgKxRo0bZ8uXLy7y2efPmlRn35JNPZhGRPfnkk6XbDjnkkKx9+/YVzv278z7uuOOywsLCbMGCBWXGHXzwwVn9+vWzzz//vMzzDBo0qMy4++67L4uIbNasWRU+X4n99tsva968ebZs2bLSbatXr866deuWtWnTJlu7dm2WZVk2b968LCKyyy+/fL37+/ac7r///grv/+Uvf1nm/b7iiiuyiCh9TRWZMGFCVqtWrXJrqGRdPPbYY6XbIiJr3Lhx9umnn25wrlmWZX379s122223rLi4OCsuLs4WLlyYXXjhhVlEZJMnT17vY1evXp19+eWXWYMGDbKrrrqqdPv9999f7vdf4qSTTiq3DiIia9GiRbZ06dLSbUVFRVmtWrWyCRMmlG77wQ9+kLVt2zZbuXJl6bZly5ZlTZs2zfk9XZeS9+PbJk+enEVEdt9995XZfumll2YRkU2fPr3Ma8nl/c/VP/7xj6xWrVrZqFGjymx/9dVXs7POOiubOnVq9s9//jO7+eabs65du2a1a9fOpk2btt599uzZM9t2222zr776ar3jdtttt6xv377f9yUAmynHv4GtUpZl671/r732ijp16sQvfvGLuO222+I///lPpZ7n6KOP3uixu+22W+y5555ltg0ZMiSWLl0ar776aqWef2PNnDkz+vfvX+77LyeffHKsWLGi3MUGDj/88DK399hjj4iIMqfMfdfy5cvjhRdeiGOOOSa22Wab0u21a9eOE044IT744IONPr3x+/jBD34QERHHHnts3HffffHhhx+WG/PII49Et27dYq+99orVq1eX/hx44IFlTp8r8ZOf/CSaNGmy0XN48803o6CgIAoKCqJVq1Zx0UUXxTnnnBOnn356mXFffvll/Pa3v40dd9wx8vPzIz8/P7bZZptYvnx5vP3227m/+G/p169fNGzYsPR2ixYtonnz5qW/w+XLl8fLL78cRxxxRNSpU6d03DbbbBOHHXZYmX1tzHuai5kzZ0aDBg3imGOOKbO95KjPE088UWZ7ru//xnr11Vfj2GOPjf322y8mTJhQ5r699947Jk2aFEcccUT06dMnTjnllHjuueeiVatW5Y4gf9ubb74ZL7zwQhx//PFV+l1AoOYRYsBWZ/ny5bFkyZJo3br1Osd07tw5Hn/88WjevHn88pe/jM6dO0fnzp3jqquuyum5WrVqtdFjW7Zsuc5tS5Ysyel5c7VkyZIK51ryHn33+Zs2bVrmdsmpg1999dU6n+Ozzz6LLMtyep6NkZ//zVn23728eInVq1eXjomI+PGPfxwPPfRQrF69Ok488cRo06ZNdOvWLe6+++7SMR9//HG8/vrrpbFU8tOwYcPIsiwWL15c5jly+T1HfLO+XnrppXjxxRfj/vvvjz333DMmTJgQ99xzT5lxQ4YMiWuuuSaGDRsW//jHP+LFF1+Ml156Kbbffvv1vtcb47u/w4hvfo8l+y35fZVc0ObbvrttY97TXCxZsiRatmxZ7ntozZs3j/z8/HLrJNf3f2PMnj07BgwYEDvttFM89thjG3V67LbbbhuHHnpovP766+v8/UyZMiUi4nudlghsGXxHDNjqPProo7FmzZoNXnK+T58+0adPn1izZk28/PLL8cc//jFGjhwZLVq0iOOOO26jniuXv+1TVFS0zm0lH5pL/gv6dy9Y8N0wyFXTpk1j4cKF5bZ/9NFHERHRrFmz77X/iG8uhFCrVq0qf56SKFjXUZgPP/ywXDj89Kc/jZ/+9KexcuXKeP7552PChAkxZMiQ6NChQ+nfkKpXr16FlyuvaJ65/g2nunXrll7R8wc/+EH069cvdttttxg5cmQceuihsc0228QXX3wRjzzySIwdOzbOPvvs0seuXLkyPv3005yerzKaNGkSeXl55b4PFlHxWt3Qe5qLpk2bxgsvvBBZlpV5bxctWhSrV6/+3u//hsyePTsOOOCAaN++fUyfPj0aN2680Y8tOdpe0ZxWrVoVf/7zn6N79+6x1157VdV0gRrKETFgq7JgwYIYM2ZMNG7cuNxpYOtSu3bt6NmzZ1x77bUREaWnCW7MUaBcvPnmm/Haa6+V2XbXXXdFw4YNSy/AUHL1u9dff73MuIcffrjc/r59dGND+vfvHzNnziwNohK333571K9fv0oud9+gQYPo2bNn/OUvfykzr7Vr18Ydd9wRbdq0qfBiCBuy0047Rfv27eP+++8vd8rpJ598Ek8++WSZvxn3bYWFhdG3b9+49NJLI+KbD+AREYceemi899570bRp0+jRo0e5n6q+imPTpk3jD3/4Q3z88cfxxz/+MSK++SCfZVm5IzE33XRTuaN/Vb0WI775ffXo0SMeeuihMn9o+ssvv6zw6orfnktF72ku+vfvH19++WW5P+J9++23l96/qcyZMycOOOCAaNOmTcyYMSOnUx4/++yzeOSRR2Kvvfaq8LTDhx9+OBYvXlzukvXA1skRMWCL9cYbb5R+t2fRokXxzDPPxC233BK1a9eOqVOnlrvC4bdNnjw5Zs6cGYcccki0a9cuvv7669KjIyUf6hs2bBjt27ePv/71r9G/f//YbrvtolmzZpX+kN66des4/PDDY9y4cdGqVau44447YsaMGXHppZdG/fr1I+KboyddunSJMWPGxOrVq6NJkyYxderUePbZZ8vtb/fdd4+//OUvcf3110f37t2jVq1aZf6u2reNHTs2HnnkkejX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AACQmBADAABITIgBAAAkVuNC7LrrrouOHTtG3bp1o3v37vHMM8+sd/zTTz8d3bt3j7p160anTp1i8uTJZe6/8cYbo0+fPtGkSZNo0qRJHHDAAfHiiy9uypcAAABs5WpUiN17770xcuTIOO+882L27NnRp0+fOPjgg2PBggUVjp83b14MGjQo+vTpE7Nnz45zzz03zjzzzHjwwQdLxzz11FPxs5/9LJ588smYNWtWtGvXLgYOHBgffvhhqpcFAABsZWpUiE2cODGGDh0aw4YNi65du8akSZOibdu2cf3111c4fvLkydGuXbuYNGlSdO3aNYYNGxannnpqXHHFFaVj7rzzzhgxYkTstddescsuu8SNN94Ya9eujSeeeCLVywIAALYy+dU9gY21atWqeOWVV+Lss88us33gwIHx3HPPVfiYWbNmxcCBA8tsO/DAA2PKlClRXFwcBQUF5R6zYsWKKC4uju22226dc1m5cmWsXLmy9PbSpUsjIqK4uDiKi4s3+jVtCiXPX93zoOawZsiVNUOurBlyZc2Qq81pzWzsHGpMiC1evDjWrFkTLVq0KLO9RYsWUVRUVOFjioqKKhy/evXqWLx4cbRq1arcY84+++zYYYcd4oADDljnXCZMmBDjx48vt3369OlRv379jXk5m9yMGTOqewrUMNYMubJmyJU1Q66sGXK1OayZFStWbNS4GhNiJfLy8srczrKs3LYNja9oe0TEZZddFnfffXc89dRTUbdu3XXu85xzzonRo0eX3l66dGm0bds2Bg4cGI0aNdqo17GpFBcXx4wZM2LAgAEVHvGD77JmyJU1Q66sGXJlzZCrzWnNlJwttyE1JsSaNWsWtWvXLnf0a9GiReWOepVo2bJlhePz8/OjadOmZbZfccUVcckll8Tjjz8ee+yxx3rnUlhYGIWFheW2FxQUVPsvvsTmNBdqBmuGXFkz5MqaIVfWDLnaHNbMxj5/jblYR506daJ79+7lDjfOmDEjevfuXeFjevXqVW789OnTo0ePHmXeoMsvvzx+97vfxbRp06JHjx5VP3kAAIBvqTEhFhExevTouOmmm+Lmm2+Ot99+O0aNGhULFiyI4cOHR8Q3pwyeeOKJpeOHDx8e8+fPj9GjR8fbb78dN998c0yZMiXGjBlTOuayyy6L888/P26++ebo0KFDFBUVRVFRUXz55ZfJXx8AALB1qDGnJkZEDB48OJYsWRIXXXRRLFy4MLp16xaPPfZYtG/fPiIiFi5cWOZvinXs2DEee+yxGDVqVFx77bXRunXruPrqq+Poo48uHXPdddfFqlWr4phjjinzXGPHjo1x48YleV0AAMDWpUaFWETEiBEjYsSIERXed+utt5bb1rdv33j11VfXub/333+/imYGAACwcWrUqYkAAABbAiEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkVqkQmzdvXlXPAwAAYKtRqRDbcccdo1+/fnHHHXfE119/XdVzAgAA2KJVKsRee+212HvvvePXv/51tGzZMk4//fR48cUXq3puAAAAW6RKhVi3bt1i4sSJ8eGHH8Ytt9wSRUVF8aMf/Sh22223mDhxYnzyySdVPU8AAIAtxve6WEd+fn4ceeSRcd9998Wll14a7733XowZMybatGkTJ554YixcuLCq5gkAALDF+F4h9vLLL8eIESOiVatWMXHixBgzZky89957MXPmzPjwww/jpz/9aVXNEwAAYIuRX5kHTZw4MW655ZaYO3duDBo0KG6//fYYNGhQ1Kr1Tdd17Ngxbrjhhthll12qdLIAAABbgkqF2PXXXx+nnnpqnHLKKdGyZcsKx7Rr1y6mTJnyvSYHAACwJapUiL377rsbHFOnTp046aSTKrN7AACALVqlviN2yy23xP33319u+/333x+33Xbb954UAADAlqxSIfaHP/whmjVrVm578+bN45JLLvnekwIAANiSVSrE5s+fHx07diy3vX379rFgwYLvPSkAAIAtWaVCrHnz5vH666+X2/7aa69F06ZNv/ekAAAAtmSVCrHjjjsuzjzzzHjyySdjzZo1sWbNmpg5c2acddZZcdxxx1X1HAEAALYolbpq4sUXXxzz58+P/v37R37+N7tYu3ZtnHjiib4jBgAAsAGVCrE6derEvffeG7/73e/itddei3r16sXuu+8e7du3r+r5AQAAbHEqFWIldt5559h5552rai4AAABbhUqF2Jo1a+LWW2+NJ554IhYtWhRr164tc//MmTOrZHIAAABbokqF2FlnnRW33nprHHLIIdGtW7fIy8ur6nkBAABssSoVYvfcc0/cd999MWjQoKqeDwAAwBavUpevr1OnTuy4445VPRcAAICtQqVC7Ne//nVcddVVkWVZVc8HAABgi1epUxOfffbZePLJJ+Pvf/977LbbblFQUFDm/r/85S9VMjkAAIAtUaVCbNttt40jjzyyqucCAACwVahUiN1yyy1VPQ8AAICtRqW+IxYRsXr16nj88cfjhhtuiGXLlkVExEcffRRffvlllU0OAABgS1SpI2Lz58+Pgw46KBYsWBArV66MAQMGRMOGDeOyyy6Lr7/+OiZPnlzV8wQAANhiVOqI2FlnnRU9evSIzz77LOrVq1e6/cgjj4wnnniiyiYHAACwJar0VRP/9a9/RZ06dcpsb9++fXz44YdVMjEAAIAtVaWOiK1duzbWrFlTbvsHH3wQDRs2/N6TWp/rrrsuOnbsGHXr1o3u3bvHM888s97xTz/9dHTv3j3q1q0bnTp1qvC0yQcffDB23XXXKCwsjF133TWmTp26qaYPAABQuRAbMGBATJo0qfR2Xl5efPnllzF27NgYNGhQVc2tnHvvvTdGjhwZ5513XsyePTv69OkTBx98cCxYsKDC8fPmzYtBgwZFnz59Yvbs2XHuuefGmWeeGQ8++GDpmFmzZsXgwYPjhBNOiNdeey1OOOGEOPbYY+OFF17YZK8DAADYulUqxP77v/87nn766dh1113j66+/jiFDhkSHDh3iww8/jEsvvbSq51hq4sSJMXTo0Bg2bFh07do1Jk2aFG3bto3rr7++wvGTJ0+Odu3axaRJk6Jr164xbNiwOPXUU+OKK64oHTNp0qQYMGBAnHPOObHLLrvEOeecE/379y8TmgAAAFWpUt8Ra926dcyZMyfuvvvuePXVV2Pt2rUxdOjQOP7448tcvKMqrVq1Kl555ZU4++yzy2wfOHBgPPfccxU+ZtasWTFw4MAy2w488MCYMmVKFBcXR0FBQcyaNStGjRpVbsz6QmzlypWxcuXK0ttLly6NiIji4uIoLi7O5WVVuZLn///+v+KoXbtap0INsWaNNUNurBlyZc2QK2uGXJWsmer+LJ7LHCoVYhER9erVi1NPPTVOPfXUyu4iJ4sXL441a9ZEixYtymxv0aJFFBUVVfiYoqKiCsevXr06Fi9eHK1atVrnmHXtMyJiwoQJMX78+HLbp0+fHvXr19/Yl7RJvfPOjOqeAjWMNUOurBlyZc2QK2uGXM2YUf1rZsWKFRs1rlIhdvvtt6/3/hNPPLEyu90oeXl5ZW5nWVZu24bGf3d7rvs855xzYvTo0aW3ly5dGm3bto2BAwdGo0aNNvwiNqHi4uKYMWNG7LzzgKhdu6Ba50LNsGZNcbzzjjXDxrNmyJU1Q66sGXJVsmYGDBgQBQXVu2ZKzpbbkEqF2FlnnVXmdnFxcaxYsSLq1KkT9evX3yQh1qxZs6hdu3a5I1WLFi0qd0SrRMuWLSscn5+fH02bNl3vmHXtMyKisLAwCgsLy20vKCio9l98iR133HzmwuatuDjinXesGTaeNUOurBlyZc2Qq5I1szl8Ht/Y56/UxTo+++yzMj9ffvllzJ07N370ox/F3XffXZldblCdOnWie/fu5Q43zpgxI3r37l3hY3r16lVu/PTp06NHjx6lb9C6xqxrnwAAAN9XpUKsIjvttFP84Q9/KHe0rCqNHj06brrpprj55pvj7bffjlGjRsWCBQti+PDhEfHNKYPfPho3fPjwmD9/fowePTrefvvtuPnmm2PKlCkxZsyY0jFnnXVWTJ8+PS699NL4P//n/8Sll14ajz/+eIwcOXKTvQ4AAGDrVumLdVSkdu3a8dFHH1XlLssYPHhwLFmyJC666KJYuHBhdOvWLR577LFo3759REQsXLiwzN8U69ixYzz22GMxatSouPbaa6N169Zx9dVXx9FHH106pnfv3nHPPffE+eefHxdccEF07tw57r333ujZs+cmex0AAMDWrVIh9vDDD5e5nWVZLFy4MK655pr44Q9/WCUTW5cRI0bEiBEjKrzv1ltvLbetb9++8eqrr653n8ccc0wcc8wxVTE9AACADapUiB1xxBFlbufl5cX2228fP/nJT+LKK6+sinkBAABssSoVYmvXrq3qeQAAAGw1quxiHQAAAGycSh0R+/YfM96QiRMnVuYpAAAAtliVCrHZs2fHq6++GqtXr44uXbpERMQ777wTtWvXjn322ad0XF5eXtXMEgAAYAtSqRA77LDDomHDhnHbbbdFkyZNIuKbP/J8yimnRJ8+feLXv/51lU4SAABgS1Kp74hdeeWVMWHChNIIi4ho0qRJXHzxxa6aCAAAsAGVCrGlS5fGxx9/XG77okWLYtmyZd97UgAAAFuySoXYkUceGaeccko88MAD8cEHH8QHH3wQDzzwQAwdOjSOOuqoqp4jAADAFqVS3xGbPHlyjBkzJn7+859HcXHxNzvKz4+hQ4fG5ZdfXqUTBAAA2NJUKsTq168f1113XVx++eXx3nvvRZZlseOOO0aDBg2qen4AAABbnO/1B50XLlwYCxcujJ133jkaNGgQWZZV1bwAAAC2WJUKsSVLlkT//v1j5513jkGDBsXChQsjImLYsGEuXQ8AALABlQqxUaNGRUFBQSxYsCDq169fun3w4MExbdq0KpscAADAlqhS3xGbPn16/OMf/4g2bdqU2b7TTjvF/Pnzq2RiAAAAW6pKHRFbvnx5mSNhJRYvXhyFhYXfe1IAAABbskqF2I9//OO4/fbbS2/n5eXF2rVr4/LLL49+/fpV2eQAAAC2RJU6NfHyyy+P/fffP15++eVYtWpV/OY3v4k333wzPv300/jXv/5V1XMEAADYolTqiNiuu+4ar7/+euy7774xYMCAWL58eRx11FExe/bs6Ny5c1XPEQAAYIuS8xGx4uLiGDhwYNxwww0xfvz4TTEnAACALVrOR8QKCgrijTfeiLy8vE0xHwAAgC1epU5NPPHEE2PKlClVPRcAAICtQqUu1rFq1aq46aabYsaMGdGjR49o0KBBmfsnTpxYJZMDAADYEuUUYv/5z3+iQ4cO8cYbb8Q+++wTERHvvPNOmTFOWQQAAFi/nEJsp512ioULF8aTTz4ZERGDBw+Oq6++Olq0aLFJJgcAALAlyuk7YlmWlbn997//PZYvX16lEwIAANjSVepiHSW+G2YAAABsWE4hlpeXV+47YL4TBgAAkJucviOWZVmcfPLJUVhYGBERX3/9dQwfPrzcVRP/8pe/VN0MAQAAtjA5hdhJJ51U5vbPf/7zKp0MAADA1iCnELvllls21TwAAAC2Gt/rYh0AAADkTogBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkJsQAAAASE2IAAACJCTEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMSEGAAAQGJCDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAAAgMSEGAACQmBADAABITIgBAAAkVmNC7LPPPosTTjghGjduHI0bN44TTjghPv/88/U+JsuyGDduXLRu3Trq1asX+++/f7z55pul93/66adxxhlnRJcuXaJ+/frRrl27OPPMM+OLL77YxK8GAADYmtWYEBsyZEjMmTMnpk2bFtOmTYs5c+bECSecsN7HXHbZZTFx4sS45ppr4qWXXoqWLVvGgAEDYtmyZRER8dFHH8VHH30UV1xxRfz73/+OW2+9NaZNmxZDhw5N8ZIAAICtVH51T2BjvP322zFt2rR4/vnno2fPnhERceONN0avXr1i7ty50aVLl3KPybIsJk2aFOedd14cddRRERFx2223RYsWLeKuu+6K008/Pbp16xYPPvhg6WM6d+4cv//97+PnP/95rF69OvLza8TbAwAA1DA1ojRmzZoVjRs3Lo2wiIj99tsvGjduHM8991yFITZv3rwoKiqKgQMHlm4rLCyMvn37xnPPPRenn356hc/1xRdfRKNGjdYbYStXroyVK1eW3l66dGlERBQXF0dxcXHOr68qlTx/dc+DmsOaIVfWDLmyZsiVNUOuNqc1s7FzqBEhVlRUFM2bNy+3vXnz5lFUVLTOx0REtGjRosz2Fi1axPz58yt8zJIlS+J3v/vdOiOtxIQJE2L8+PHltk+fPj3q16+/3semMmPGjOqeAjWMNUOurBlyZc2QK2uGXG0Oa2bFihUbNa5aQ2zcuHEVBs23vfTSSxERkZeXV+6+LMsq3P5t371/XY9ZunRpHHLIIbHrrrvG2LFj17vPc845J0aPHl3msW3bto2BAwdGo0aN1vvYTa24uDhmzJgRAwYMiIKCgmqdCzWDNUOurBlyZc2QK2uGXG1Oa6bkbLkNqdYQ+9WvfhXHHXfcesd06NAhXn/99fj444/L3ffJJ5+UO+JVomXLlhHxzZGxVq1alW5ftGhRuccsW7YsDjrooNhmm21i6tSpG/zlFRYWRmFhYbntBQUF1f6LL7E5zYWawZohV9YMubJmyJU1Q642hzWzsc9frSHWrFmzaNas2QbH9erVK7744ot48cUXY999942IiBdeeCG++OKL6N27d4WP6dixY7Rs2TJmzJgRe++9d0RErFq1Kp5++um49NJLS8ctXbo0DjzwwCgsLIyHH3446tatWwWvDAAAYN1qxOXru3btGgcddFCcdtpp8fzzz8fzzz8fp512Whx66KFlLtSxyy67xNSpUyPim1MSR44cGZdccklMnTo13njjjTj55JOjfv36MWTIkIj45kjYwIEDY/ny5TFl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1lGr1rq/CeaIWBWoVatWtGnTprqnUUajRo2qfRFSs1gz5MqaIVfWDLmyZsjV5rJm1nckrISLdQAAACQmxAAAABITYluYwsLCGDt2bBQWFlb3VKghrBlyZc2QK2uGXFkz5KomrhkX6wAAAEjMETEAAIDEhBgAAEBiQgwAACAxIQYAAJCYEKuBrrvuuujYsWPUrVs3unfvHs8888x6xz/99NPRvXv3qFu3bnTq1CkmT56caKZsLnJZM3/5y19iwIABsf3220ejRo2iV69e8Y9//CPhbNkc5PrvTIl//etfkZ+fH3vttdemnSCbnVzXzMqVK+O8886L9u3bR2FhYXTu3DluvvnmRLNlc5Drmrnzzjtjzz33jPr160erVq3ilFNOiSVLliSaLdXpn//8Zxx22GHRunXryMvLi4ceemiDj6kJn3+FWA1z7733xsiRI+O8886L2bNnR58+feLggw+OBQsWVDh+3rx5MWjQoOjTp0/Mnj07zj333DjzzDPjwQcfTDxzqkuua+af//xnDBgwIB577LF45ZVXol+/fnHYYYfF7NmzE8+c6pLrminxxRdfxIknnhj9+/dPNFM2F5VZM8cee2w88cQTMWXKlJg7d27cfffdscsuuyScNdUp1zXz7LPPxoknnhhDhw6NN998M+6///546aWXYtiwYYlnTnVYvnx57LnnnnHNNdds1Pga8/k3o0bZd999s+HDh5fZtssuu2Rnn312heN/85vfZLvsskuZbaeffnq23377bbI5snnJdc1UZNddd83Gjx9f1VNjM1XZNTN48ODs/PPPz8aOHZvtueeem3CGbG5yXTN///vfs8aNG2dLlixJMT02Q7mumcsvvzzr1KlTmW1XX3111qZNm002RzZPEZFNnTp1vWNqyudfR8RqkFWrVsUrr7wSAwcOLLN94MCB8dxzz1X4mFmzZpUbf+CBB8bLL78cxcXFm2yubB4qs2a+a+3atbFs2bLYbrvtNsUU2cxUds3ccsst8d5778XYsWM39RTZzFRmzTz88MPRo0ePuOyyy2KHHXaInXfeOcaMGRNfffVViilTzSqzZnr37h0ffPBBPPbYY5FlWXz88cfxwAMPxCGHHJJiytQwNeXzb351T4CNt3jx4lizZk20aNGizPYWLVpEUVFRhY8pKiqqcPzq1atj8eLF0apVq002X6pfZdbMd1155ZWxfPnyOPbYYzfFFNnMVGbNvPvuu3H22WfHM888E/n5/t/K1qYya+Y///lPPPvss1G3bt2YOnVqLF68OEaMGBGffvqp74ltBSqzZnr37h133nlnDB48OL7++utYvXp1HH744fHHP/4xxZSpYWrK519HxGqgvLy8MrezLCu3bUPjK9rOlivXNVPi7rvvjnHjxsW9994bzZs331TTYzO0sWtmzZo1MWTIkBg/fnzsvPPOqabHZiiXf2fWrl0beXl5ceedd8a+++4bgwYNiokTJ8att97qqNhWJJc189Zbb8WZZ54ZF154Ybzyyisxbdq0mDdvXgwfPjzFVKmBasLnX//psgZp1qxZ1K5du9x/LVq0aFG56i/RsmXLCsfn5+dH06ZNN9lc2TxUZs2UuPfee2Po0KFx//33xwEHHLApp8lmJNc1s2zZsnj55Zdj9uzZ8atf/SoivvmQnWVZ5Ofnx/Tp0+MnP/lJkrlTPSrz70yrVq1ihx12iMaNG5du69q1a2RZFh988EHstNNOm3TOVK/KrJkJEybED3/4w/jf//t/R0TEHnvsEQ0aNIg+ffrExRdfvNkc4WDzUFM+/zoiVoPUqVMnunfvHjNmzCizfcaMGdG7d+8KH9OrV69y46dPnx49evSIgoKCTTZXNg+VWTMR3xwJO/nkk+Ouu+5y/v1WJtc106hRo/j3v/8dc+bMKf0ZPnx4dOnSJebMmRM9e/ZMNXWqSWX+nfnhD38YH330UXz55Zel2955552oVatWtGnTZpPOl+pXmTWzYsWKqFWr7MfW2rVrR8T/O9IBJWrM599qukgIlXTPPfdkBQUF2ZQpU7K33norGzlyZNagQYPs/fffz7Isy84+++zshBNOKB3/n//8J6tfv342atSo7K233sqmTJmSFRQUZA888EB1vQQSy3XN3HXXXVl+fn527bXXZgsXLiz9+fzzz6vrJZBYrmvmu1w1ceuT65pZtmxZ1qZNm+yYY47J3nzzzezpp5/Odtppp2zYsGHV9RJILNc1c8stt2T5+fnZddddl7333nvZs88+m/Xo0SPbd999q+slkNCyZcuy2bNnZ7Nnz84iIps4cWI2e/bsbP78+VmW1dzPv0KsBrr22muz9u3bZ3Xq1Mn22Wef7Omnny6976STTsr69u1bZvxTTz2V7b333lmdOnWyDh06ZNdff33iGVPdclkzffv2zSKi3M9JJ52UfuJUm1z/nfk2IbZ1ynXNvP3229kBBxyQ1atXL2vTpk02evTobMWKFYlnTXXKdc1cffXV2a677prVq1cva9WqVXb88cdnH3zwQeJZUx2efPLJ9X42qamff/OyzPFcAACAlHxHDAAAIDEhBgAAkJgQAwAASEyIAQAAJCbEAAAAEhNiAAAAiQkxAACAxIQYAABAYkIMAKrQ+++/H3l5eTFnzpzqngoAmzEhBsBW6eSTT468vLzIy8uL/Pz8aNeuXfzXf/1XfPbZZznt44gjjiizrW3btrFw4cLo1q1bFc8YgC2JEANgq3XQQQfFwoUL4/3334+bbrop/va3v8WIESO+1z5r164dLVu2jPz8/CqaJQBbIiEGwFarsLAwWrZsGW3atImBAwfG4MGDY/r06RERsWbNmhg6dGh07Ngx6tWrF126dImrrrqq9LHjxo2L2267Lf7617+WHll76qmnyp2a+NRTT0VeXl488cQT0aNHj6hfv3707t075s6dW2YuF198cTRv3jwaNmwYw4YNi7PPPjv22muvVG8FAIkJMQCIiP/85z8xbdq0KCgoiIiItWvXRps2beK+++6Lt956Ky688MI499xz47777ouIiDFjxsSxxx5belRt4cKF0bt373Xu/7zzzosrr7wyXn755cjPz49TTz219L4777wzfv/738ell14ar7zySrRr1y6uv/76TfuCAahWzpsAYKv1yCOPxDbbbBNr1qyJr7/+OiIiJk6cGBERBQUFMX78+NKxHTt2jOeeey7uu+++OPbYY2ObbbaJevXqxcqVK6Nly5YbfK7f//730bdv34iIOPvss+OQQw6Jr7/+OurWrRt//OMfY+jQoXHKKadERMSFF14Y06dPjy+//LKqXzIAmwlHxADYavXr1y/mzJkTL7zwQpxxxhlx4IEHxhlnnFF6/+TJk6NHjx6x/fbbxzbbbBM33nhjLFiwoFLPtccee5T+361atYqIiEWLFkVExNy5c2PfffctM/67twHYsggxALZaDRo0iB133DH22GOPuPrqq2PlypWlR8Huu+++GDVqVJx66qkxffr0mDNnTpxyyimxatWqSj1XySmPERF5eXkR8c3pj9/dViLLsko9DwA1gxADgP9r7NixccUVV8RHH30UzzzzTPTu3TtGjBgRe++9d+y4447x3nvvlRlfp06dWLNmzfd+3i5dusSLL75YZtvLL7/8vfcLwOZLiAHA/7X//vvHbrvtFpdccknsuOOO8fLLL8c//vGPeOedd+KCCy6Il156qcz4Dh06xOuvvx5z586NxYsXR3FxcaWe94wzzogpU6bEbbfdFu+++25cfPHF8frrr5c7SgbAlkOIAcC3jB49Om688cY44ogj4qijjorBgwdHz549Y8mSJeX+xthpp50WXbp0Kf0e2b/+9a9KPefxxx8f55xzTowZMyb22WefmDdvXpx88slRt27dqnhJAGyG8jInoQPAZmfAgAHRsmXL+POf/1zdUwFgE3D5egCoZitWrIjJkyfHgQceGLVr14677747Hn/88ZgxY0Z1Tw2ATcQRMQCoZl999VUcdthh8eqrr8bKlSujS5cucf7558dRRx1V3VMDYBMRYgAAAIm5WAcAAEBiQgwAACAxIQYAAJCYEAMAAEhMiAEAACQmxAAAABITYgAAAIkJMQAAgMT+fyyvM5SwvbZeAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 10))\n",
    "plt.hist(movie_ratings['rating'], bins=10, edgecolor='blue',alpha=0.7)\n",
    "plt.title(f'Distribution of User Ratings for \"{movieId}\"')\n",
    "plt.xlabel('Rating')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "052573db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct tags for '2571':\n",
      "Empty DataFrame\n",
      "Columns: [userId, tag]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "movieId  = \"2571\"\n",
    "tag = dc[(dc['movieId'] == movieId) & (dc['tag'] == True)]\n",
    "print(f\"Correct tags for '{movieId}':\")\n",
    "print(tag[['userId', 'tag']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "e238a150",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964981247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964983815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964982931</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  movieId  rating  timestamp\n",
       "0       1        1     4.0  964982703\n",
       "1       1        3     4.0  964981247\n",
       "2       1        6     4.0  964982224\n",
       "3       1       47     5.0  964983815\n",
       "4       1       50     5.0  964982931"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "93c02568",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>Comedy|Drama|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movieId                               title  \\\n",
       "0        1                    Toy Story (1995)   \n",
       "1        2                      Jumanji (1995)   \n",
       "2        3             Grumpier Old Men (1995)   \n",
       "3        4            Waiting to Exhale (1995)   \n",
       "4        5  Father of the Bride Part II (1995)   \n",
       "\n",
       "                                        genres  \n",
       "0  Adventure|Animation|Children|Comedy|Fantasy  \n",
       "1                   Adventure|Children|Fantasy  \n",
       "2                               Comedy|Romance  \n",
       "3                         Comedy|Drama|Romance  \n",
       "4                                       Comedy  "
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "da.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "2342ffdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   movieId    title  rating_count  rating_mean\n",
      "0      101  Movie A             2          4.5\n",
      "1      102  Movie B             2          3.5\n",
      "2      103  Movie C             1          2.0\n"
     ]
    }
   ],
   "source": [
    "da = {'movieId': [101, 102, 103, 104],\n",
    "               'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D']}\n",
    "\n",
    "movies = pd.DataFrame(da)\n",
    "\n",
    "\n",
    "merged_df = pd.merge(movies, grouped_ratings, on='movieId', how='inner')\n",
    "\n",
    "print(merged_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "f212f587",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [movieId, title, rating_count, rating_mean]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "\n",
    "filtered_movies = merged_df[merged_df['rating_count'] > 50]\n",
    "\n",
    "\n",
    "print(filtered_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27dbca78",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = pd.read_csv('your_movies_file.csv')\n",
    "ratings = pd.read_csv('your_ratings_file.csv')\n",
    "\n",
    "grouped_ratings = ratings.groupby('movieId').agg({'rating': ['count', 'mean']})\n",
    "grouped_ratings.columns = ['rating_count', 'rating_mean']\n",
    "\n",
    "merged_df = pd.merge(movies, grouped_ratings, on='movieId', how='inner')\n",
    "\n",
    "\n",
    "filtered_movies = merged_df[merged_df['rating_count'] > 50]\n",
    "\n",
    "\n",
    "print(filtered_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "b7fc2e01",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = pd.read_csv('movies.csv')\n",
    "ratings = pd.read_csv('ratings.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "0430808f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      movieId                             title  \\\n",
      "0           1                  Toy Story (1995)   \n",
      "1           2                    Jumanji (1995)   \n",
      "2           3           Grumpier Old Men (1995)   \n",
      "5           6                       Heat (1995)   \n",
      "6           7                    Sabrina (1995)   \n",
      "...       ...                               ...   \n",
      "8287   106782   Wolf of Wall Street, The (2013)   \n",
      "8354   109374  Grand Budapest Hotel, The (2014)   \n",
      "8358   109487               Interstellar (2014)   \n",
      "8457   112852    Guardians of the Galaxy (2014)   \n",
      "8673   122904                   Deadpool (2016)   \n",
      "\n",
      "                                           genres  rating_count  rating_mean  \n",
      "0     Adventure|Animation|Children|Comedy|Fantasy           215     3.920930  \n",
      "1                      Adventure|Children|Fantasy           110     3.431818  \n",
      "2                                  Comedy|Romance            52     3.259615  \n",
      "5                           Action|Crime|Thriller           102     3.946078  \n",
      "6                                  Comedy|Romance            54     3.185185  \n",
      "...                                           ...           ...          ...  \n",
      "8287                           Comedy|Crime|Drama            54     3.916667  \n",
      "8354                                 Comedy|Drama            52     3.778846  \n",
      "8358                                  Sci-Fi|IMAX            73     3.993151  \n",
      "8457                      Action|Adventure|Sci-Fi            59     4.050847  \n",
      "8673               Action|Adventure|Comedy|Sci-Fi            54     3.833333  \n",
      "\n",
      "[436 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "grouped_ratings = ratings.groupby('movieId').agg({'rating': ['count', 'mean']})\n",
    "grouped_ratings.columns = ['rating_count', 'rating_mean']\n",
    "\n",
    "\n",
    "merged_df = pd.merge(movies, grouped_ratings, on='movieId', how='inner')\n",
    "\n",
    "\n",
    "filtered_movies = merged_df[merged_df['rating_count'] > 50]\n",
    "\n",
    "print(filtered_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "3bcdbad6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     movieId                             title  rating_mean\n",
      "277      318  Shawshank Redemption, The (1994)     4.429022\n"
     ]
    }
   ],
   "source": [
    "sorted_movies = filtered_movies.sort_values(by='rating_mean', ascending=False)\n",
    "\n",
    "\n",
    "most_popular_movie = sorted_movies.head(1)\n",
    "\n",
    "\n",
    "print(most_popular_movie[['movieId', 'title', 'rating_mean']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "4221a6d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      movieId                             title  rating_count\n",
      "314       356               Forrest Gump (1994)           329\n",
      "277       318  Shawshank Redemption, The (1994)           317\n",
      "257       296               Pulp Fiction (1994)           307\n",
      "510       593  Silence of the Lambs, The (1991)           279\n",
      "1938     2571                Matrix, The (1999)           278\n"
     ]
    }
   ],
   "source": [
    "top5_popular_movies = filtered_movies.sort_values(by='rating_count', ascending=False).head(5)\n",
    "\n",
    "\n",
    "print(top5_popular_movies[['movieId', 'title', 'rating_count']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "7ffb76bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "movieId                       2571\n",
      "title           Matrix, The (1999)\n",
      "rating_count                   278\n",
      "Name: 1938, dtype: object\n"
     ]
    }
   ],
   "source": [
    "scifi_movies = filtered_movies[filtered_movies['genres'].str.contains('Sci-Fi', case=False)]\n",
    "\n",
    "\n",
    "sorted_scifi_movies = scifi_movies.sort_values(by='rating_count', ascending=False)\n",
    "\n",
    "\n",
    "third_most_popular_scifi_movie = sorted_scifi_movies.iloc[0]\n",
    "\n",
    "print(third_most_popular_scifi_movie[['movieId', 'title', 'rating_count']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0e2fb99",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import numpy as np\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def scrapper(imdbId):\n",
    "    id = str(int(imdbId))\n",
    "    n_zeroes = 7 - len(id)\n",
    "    new_id = \"0\"*n_zeroes + id\n",
    "    URL = f\"https://www.imdb.com/title/tt{new_id}/\"\n",
    "    request_header = {'Content-Type': 'text/html; charset=UTF-8', \n",
    "                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', \n",
    "                      'Accept-Encoding': 'gzip, deflate, br'}\n",
    "    response = requests.FILL_IN_THE_BLANK(URL, headers=request_header)\n",
    "    soup = FILL_IN_THE_BLANK(response.text)\n",
    "    imdb_rating = soup.find('FILL_IN_THE_BLANK', attrs={'FILL_IN_THE_BLANK' : 'FILL_IN_THE_BLANK'})\n",
    "    return imdb_rating.text if imdb_rating else np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "391b6abb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import numpy as np\n",
    "from bs4 import BeautifulSoup\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "6a17bc0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrapper(imdbId):\n",
    "    id = str(int(imdbId))\n",
    "    n_zeroes = 7 - len(id)\n",
    "    new_id = \"0\"*n_zeroes + id\n",
    "    URL = f\"https://www.imdb.com/title/tt{new_id}/\"\n",
    "    request_header = {'Content-Type': 'text/html; charset=UTF-8', \n",
    "                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', \n",
    "                      'Accept-Encoding': 'gzip, deflate, br'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "4bd499c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "imdb = pd.read_csv('links.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "cf4e24e0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'URL' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[109], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m response \u001b[38;5;241m=\u001b[39m requests\u001b[38;5;241m.\u001b[39mget(URL, headers\u001b[38;5;241m=\u001b[39mrequest_header)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'URL' is not defined"
     ]
    }
   ],
   "source": [
    "response = requests.get(URL, headers=request_header)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "b57ce21f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import numpy as np\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "74ef1e11",
   "metadata": {},
   "outputs": [],
   "source": [
    "request_header = {'Content-Type': 'text/html; charset=UTF-8', \n",
    "                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', \n",
    "                      'Accept-Encoding': 'gzip, deflate, br'}\n",
    "response = requests.get(\"https://m.imdb.com/chart/top/\", headers=request_header)\n",
    "soup = BeautifulSoup(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "a8f2f52e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (408435020.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[132], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    return imdb_rating.text if imdb_rating else np.nan\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "imdb_rating = soup.find('td', attrs={'lister-item-header' : 'ipl-rating-widget'})\n",
    "return imdb_rating.text if imdb_rating else np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b10da46c",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
