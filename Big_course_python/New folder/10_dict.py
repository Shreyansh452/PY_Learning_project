from tkinter import N



# d1 = {'rohan' : 'chor',
#         'pratibha': 'daaku',
#         'sonu':'badmaash',
#         'suresh':{'rice':'beans', 'dhokla': 'chaasni','roti': 'daal'}}
# # print(d1['suresh'])
# d1['ramesh'] = 'chole'
# d1[230] = 'sanju'
# print(d1)
# del d1[230]
# print(d1)

d2 = {
    'Shreyansh' : 'An intelligent boy.',
    'Cheese' : 'Kind of dairy product procure by milk.',
    'Phone' : 'Techincal device use to connect with network of someone.'
}
a = input('Enter the word:  ')
b = a.capitalize()
print(b,'=', d2[b])