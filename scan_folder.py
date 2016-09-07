#!/usr/bin/env python3.4
import os
import time

TIME = 1					# Время обновления
# чот хз почему, но на конце не должно быть / :D
PATH_FOR_LINKS = "/home/boris/links_folder"	# Директория с линками
PATH_FOR_SCAN = "/home/boris/scan_folder"	# Директория для сканирования

def link_founder(PATH_FOR_LINKS):
	"""
	Поиск существующихлинков. Для того чтобы понимать какие линки создавать.
	"""
	CREATED_LINKS = {directory:files for directory, x, files in os.walk(PATH_FOR_LINKS)}
	for directory in CREATED_LINKS.keys():
		for file in CREATED_LINKS[directory]:
			yield file

def scan_folder(PATH_FOR_SCAN):
	"""
	Поиск файлов в директории.
	"""
	FILES_FOUND = {directory:files for directory, x, files in os.walk(PATH_FOR_SCAN)}
	for directory in FILES_FOUND.keys():
		for file in FILES_FOUND[directory]:
			yield file

	
if __name__ == "__main__":	
	links = list(link_founder(PATH_FOR_LINKS))
	files = list(scan_folder(PATH_FOR_SCAN))
	if all([len(files) > 0, len(links) > 0]):
		print("Для текущих файлов линки существуют")
		for i in set(links) & set(files):
			print("path : {DIR}/{FILE} ".format(DIR=PATH_FOR_SCAN,FILE=i))
	
	while True:
		# Главный цикл в котором выполняется скрипт.
		links = list(link_founder(PATH_FOR_LINKS))
		files = list(scan_folder(PATH_FOR_SCAN))
		for i in set(files) - set(links):
			os.link(PATH_FOR_SCAN+'/'+i, PATH_FOR_LINKS+'/'+i.split('/')[-1])
			print("link for {DIR}/{FILE} created".format(DIR=PATH_FOR_LINKS,FILE=i))
		time.sleep(TIME)
