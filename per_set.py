#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os,commands,shlex


apk_path = "/home/jueimei/AppList.lst"
app = open(apk_path)
save_dic = {}
error_permission = []
PATH = "/home/jueimei/NFS/permission_list"
if os.path.exists(PATH):
    for f in os.listdir(PATH):
    	error_permission.extend([f])
for i in error_permission:
	save_dic[i]=[]
count = 0
black_list_app_count = 0
permission_not_found_count = 0
permission_not_found_list = open("permission_not_found_list.txt", "w")
for i in app:
	count = count + 1
	permission_list = []
	command='./autoSys/android-sdk-linux/build-tools/20.0.0/aapt d permissions  ' + i.strip() 	
	temp = os.popen(command).read()


	if 'permission:' not in temp:
		
		permission_not_found_list.write(i.strip() + "\n") 
		permission_not_found_count = permission_not_found_count + 1	

	else:
		permission_list = temp.split('\n')
		#permission_list = os.popen(command).read().split('\n')
		intersection = set(permission_list)&set(error_permission)
		if intersection:
			label_command = './autoSys/android-sdk-linux/build-tools/20.0.0/aapt d badging  '  + i.strip() +  '| grep application-label:'
			label = os.popen(label_command).read()
			label = label.replace("application-label:"," ")
			label = label.strip()
			label = label.replace("'","")
			label = label + "\t"

			package_command = './autoSys/android-sdk-linux/build-tools/20.0.0/aapt d badging  '  + i.strip() +  '| grep package:\ name='
			package_name = os.popen(package_command).read()
			package = []
			package = package_name.split()
			name = package[1].replace("name=","")
			name = name.replace("'","")
			name = name.strip()+"\t"
			version_name = package[3].replace("versionName=","")
			version_name = version_name.replace("'","")
			version_name = version_name.strip()+"\n"
			for i in intersection:
				if save_dic.has_key(i):
					save_dic[i].append(label)
					save_dic[i].append(name)
					save_dic[i].append(version_name)
					black_list_app_count = black_list_app_count + 1

		

black_list = open("app_permission_black_list.txt", "w")
for i in save_dic:
	black_list.write("["+i+"]"+"\n")
	for ii in save_dic[i]:
		black_list.write(ii)
		# print ii
	black_list.write("\n\n")

print "[Note] Total checked: " + str(count) + " app(s)"
print "[Note] Black list: " + str(black_list_app_count) + " app(s)"
print "[Note] Permissions not found: " + str(permission_not_found_count) + " app(s)"
print "[Note] Regular permission: "+ str(count-black_list_app_count-permission_not_found_count) + " app(s)"
black_list.close()

# if __name__ == "__main__": 
# 	check_permissions(sys.argv[1])