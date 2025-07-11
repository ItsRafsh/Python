


# pertemuan 21
# gunakan markdown

# setiap spasi artinya beda kolom
import pandas as pd

# ------------------- ini merupakan car-sales.csv ------------------- 
data = pd.read_csv('car-sales.csv')
data.loc[9,'colour'] = 'Yellow'
data.tail()
# data.iloc[7]

data.head()

# ngefilter sebuah dataFrame 
data[(data['Doors'] == 4) & (data['Colour'] == 'White')]

data['Price'] = data['Price'].str.replace('$','')
# data['Price'] = data['Price'].str.replace(',','').astype(float)

data.head()

# data['Fuel Consumsiption (1)'] = (data['Odometer (KM)'])

data['Price (Rp)'] = (data['Price'] * 16275)
# data['Price (Rp)'] = 'Rp. ' + (data['Price'] * 16275).astype(str)   kalo mau tampilkan Rp
data.head()

avg = data['Price'].mean()
max = data['Price'].max()
min = data['Price'].min()
median = data['price'].median()
std_dev = data['Price'].std()
print(f'{avg}, {max}, {std_dev:.2f}')

data.drop(columns=['Price (Rp)'], inplace=True)

data.head()
# cara save data nya
# data.to_csv('new-car-sales.csv')



# ------------------- ini merupakan jual-motor.csv ------------------- 

data_motor =pd.read_csv('jual-motor.csv')
data_motor.head()

data_motor['Kapasitas Mesin'] = data_motor['Kapasitas Mesin'].str.replace('cc', '')
data_motor['Harga (Rp)'] = data_motor['Harga (Rp)'].str.replace(',', '') #.astype(float)
# data_motor['Harga (Rp)'] = data_motor['Harga (Rp)'].str.replace('Rp.', '').astype(int) ini ga dipake
data_motor.head()

data_motor['Sisa Umur'] = (10 - (2025 - data_motor['Tahun'])).astype(str) + 'Tahun'
data_motor.head()



