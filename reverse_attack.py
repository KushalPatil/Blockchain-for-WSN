with open('blockchain.txt', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('20','10')
print('Attack Reversal Successful......')
with open('blockchain.txt', 'w') as file:
  file.write(filedata)
print('Reverse Successful.....')