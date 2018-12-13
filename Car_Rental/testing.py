# import codecs
# #open it with utf-8 encoding 
# f=codecs.open("myfile.txt","r",encoding='utf-8')
# #read the file to unicode string
# sfile=f.read()

# #check the encoding type
# print(type(sfile)) #it's unicode

# #unicode should be encoded to standard string to display it properly
# print(sfile.encode('utf-8'))
# #check the type of encoded string

# print(type(sfile.encode('utf-8')))


# # https://stackoverflow.com/questions/10376923/reading-non-ascii-characters-from-a-text-file

from ui.Universal_func import address_input_chack
import ui.Universal_func as Universal_f

name = input("Chose: ")
Tester, address = Universal_f.address_input_chack(name)

print(Tester)
print(address)