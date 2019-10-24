with open('blockchain.txt', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('10','20')
print('Searching for ledger..........')
print('Finding Mining value in Ledger')
with open('blockchain.txt','r') as fi:
  filel=fi.read() 
print('Ledger Altered by changing Data/Mining value......')
with open('blockchain.txt', 'w') as file:
  file.write(filedata)
print('Write Successful.....')