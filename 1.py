
#!/usr/bin/python3

import json

# buka file JSON
file_json = open('biodata.json')

# load file JSON
data = json.loads(file_json.read())

# Input Nama sesuai dijson
a = input("Masukkan Nama Lengkap :  ")

# return data
if a == data['nama']:
    print("Name : %s" % data['nama'])
    print("Age : %i" % data['Age'])
    print("Addreas : %s" % data['addreas'])
    print("hobby : ")
    for hob in data['hobby']:
         print("\t%s \t: %s" % (hob, data['hobby'][hob]))
    print("Status : %s" % data['is_married'])
    print("School : ")
    for sch in data['list_school']:
        print(sch)
    print("skill : ")
    for skill in data['skill']:
        print("\t%s \t: %s" % (skill, data['skill'][skill]))
    print("Tertarik dengan koding : %s" % data['interest_in_coding'])
else:
    print("Maaf data tidak ditemukan")
