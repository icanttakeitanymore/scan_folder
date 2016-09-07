#!/usr/bin/env python3
import os
import time

TIME = 1 				    # Время обновления
PATH_FOR_LINKS = "/home/boris/links_folder" # Папка для линков
PATH_FOR_SCAN = "/home/boris/scac_folder"   # Сканируемая папка

def link_founder(PATH_FOR_LINKS):
	"""
	Поиск существующихлинков. Для того чтобы понимать какие линки создавать.
	"""
	CREATED_LINKS = {directory:files for directory,x, files in os.path(PATH_FOR_LINKS)}
	for directory in CREATED_LINKS.keys():
		for file in CREATED_LINKS[directory]
			yield "{DIR}/{FILE}".format(DIR=directory,FILE=file)

def scan_folder(PATH_FOR_SCAN):
	"""
	Поиск файлов в директории.
	"""
	FILES_FOUND = {directory:files for directory,x, files in os.path(PATH_FOR_SCAN)}
	for directory in FILES_FOUND.keys():
		for file in FILES_FOUND[directory]
			yield "{DIR}/{FILE}".format(DIR=directory,FILE=file)

	
if __name__ == "__main__":
	print("Для текущих файлов линки существуют")
	links = list(link_founder)
	files = list(scac_folder)
	for i in set(links) & set(files):
		print("path : ", i)
	
	while True:
		# Главный цикл в котором выполняется скрипт.
		links = list(link_founder)
		files = list(scac_folder)
		for i in set(files) - set(links):
			os.link(i, PATH_FOR_LINKS+i.split("/")[-1])
		time.sleep(TIME)
