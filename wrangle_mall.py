{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a91f636b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "import env\n",
    "\n",
    "\n",
    "# ignore warnings\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# Wrangling\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Exploring\n",
    "import scipy.stats as stats\n",
    "\n",
    "# Visualizing\n",
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# default pandas decimal number display format\n",
    "pd.options.display.float_format = '{:20,.2f}'.format\n",
    "\n",
    "import acquire\n",
    "#import summarize\n",
    "import prepare"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "3ac09af3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_conn():\n",
    "    db = 'zillow'\n",
    "    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'\n",
    "    return url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "52592c1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define a query for the mall dataset\n",
    "mall_query = '''\n",
    "             SELECT *\n",
    "             FROM customers\n",
    "             '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "9b774640",
   "metadata": {},
   "outputs": [],
   "source": [
    "def acquire_mall():\n",
    "    \"\"\" Acquire mall customer data from mySQL server or cached csv, returns as Pandas DataFrame \"\"\"\n",
    "    \n",
    "    if os.path.exists('mall_customers.csv'):\n",
    "        print(\"Using cached data\")\n",
    "        mall = pd.read_csv('mall_customers.csv')\n",
    "    # Acquire data from database if CSV does not exist\n",
    "    else:\n",
    "        print(\"Acquiring data from server\")\n",
    "        query = \"\"\" SELECT * FROM customers; \"\"\"\n",
    "        mall = pd.read_sql(query, get_connection('mall_customers'))\n",
    "        \n",
    "        mall.to_csv('mall_customers.csv', index=False)\n",
    "        \n",
    "    \n",
    "    return mall"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "78622a39",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'get_db_url' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [35]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#Create the url to access the database\u001b[39;00m\n\u001b[1;32m      2\u001b[0m mall_database \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmall_customers\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m----> 4\u001b[0m mall_url \u001b[38;5;241m=\u001b[39m \u001b[43mget_db_url\u001b[49m(host, username, password, mall_database)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'get_db_url' is not defined"
     ]
    }
   ],
   "source": [
    "#Create the url to access the database\n",
    "mall_database = 'mall_customers'\n",
    "\n",
    "mall_url = get_db_url(host, username, password, mall_database)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e84652cc",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [47]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m mall\u001b[38;5;241m=\u001b[39m\u001b[43macquire_mall\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Input \u001b[0;32mIn [46]\u001b[0m, in \u001b[0;36macquire_mall\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21macquire_mall\u001b[39m():\n\u001b[1;32m      2\u001b[0m     \u001b[38;5;124;03m\"\"\" Acquire mall customer data from mySQL server or cached csv, returns as Pandas DataFrame \"\"\"\u001b[39;00m\n\u001b[0;32m----> 4\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mos\u001b[49m\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mexists(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmall_customers.csv\u001b[39m\u001b[38;5;124m'\u001b[39m):\n\u001b[1;32m      5\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mUsing cached data\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      6\u001b[0m         mall \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmall_customers.csv\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "mall=acquire_mall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed5dd21a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55fcaedb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ecaace6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a3232b63",
   "metadata": {},
   "outputs": [],
   "source": [
    "def one_hot_encode(df):\n",
    "    df['is_female'] = df.gender == 'Female'\n",
    "    df = df.drop(columns='gender')\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "96feebe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def split(df):\n",
    "    train_and_validate, test = train_test_split(df, random_state=123, test_size=.15)\n",
    "    train, validate = train_test_split(train_and_validate, random_state=123, test_size=.2)\n",
    "\n",
    "    print('Train: %d rows, %d cols' % train.shape)\n",
    "    print('Validate: %d rows, %d cols' % validate.shape)\n",
    "    print('Test: %d rows, %d cols' % test.shape)\n",
    "\n",
    "    return train, validate, test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d8e1f0f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scale(train, validate, test):\n",
    "    columns_to_scale = ['age', 'spending_score', 'annual_income']\n",
    "    train_scaled = train.copy()\n",
    "    validate_scaled = validate.copy()\n",
    "    test_scaled = test.copy()\n",
    "\n",
    "    scaler = MinMaxScaler()\n",
    "    scaler.fit(train[columns_to_scale])\n",
    "\n",
    "    train_scaled[columns_to_scale] = scaler.transform(train[columns_to_scale])\n",
    "    validate_scaled[columns_to_scale] = scaler.transform(validate[columns_to_scale])\n",
    "    test_scaled[columns_to_scale] = scaler.transform(test[columns_to_scale])\n",
    "\n",
    "    return train_scaled, validate_scaled, test_scaled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "23855266",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_exploration_data():\n",
    "    df = acquire()\n",
    "    train, validate, test = split(df)\n",
    "    return train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1269b80c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_modeling_data(scale_data=False):\n",
    "    df = acquire()\n",
    "    df = one_hot_encode(df)\n",
    "    train, validate, test = split(df)\n",
    "    if scale_data:\n",
    "        return scale(train, validate, test)\n",
    "    else:\n",
    "        return train, validate, test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75539abc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "600a3d07",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "681cd888",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffc1ec5c",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
