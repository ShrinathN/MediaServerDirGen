#!/bin/python

import os
import re

#this function will create the config file when it is run
def create_config_file():
	fil = open('msdr.conf', 'w')
	#the below is the text to write in the newly created config file
	#basic help text is added for understanding of the config file
	text_to_write = '''###
# Welcome to MSDR config file
# Editing this file is very simple
# Lines starting with a '#' are comments and are ignored by the program
#
###DIRECTORIES###
# There are 5 top level directory types
#
# 1 - MUS, music directories, subdirectories must follow the following structure
# Artist->Album->Audio_File
#
# 2 - VID, video directories, will include all subdirectories, and all files
#
# 3 - MOV, movie directories, subdirectories must follow the following structure
# Movie_Name->Video_File
#
# 4 - TVS, TV show directories, subdirectories must follow the followind structure
# TV_Show_Name->Episode_Files
#
# 5 - PHO, Photo directories, will include all subdirectories, and all files
#
# For example, to add a video directory, including subdirectories, add the following
# VID,/path/to/video/directory
# For example, to add a photo directory, including subdirectories, add the following
# PHO,/path/to/photo/directory
# Fir example, to add your TV show directory, which follows the structure, add the following
# TVS,/path/to/tv/show/library
###
'''
	fil.write(text_to_write)
	fil.close()

#checks if a string is an image file or not, just checks the extension
def check_if_image_file(string_to_check):
	if(string_to_check[-4:] == '.png' or string_to_check[-4:] == '.bmp' or string_to_check[-4:] == '.gif' or string_to_check[-4:] == '.jpg' or string_to_check[-5:] == '.jpeg'):
		return True
	else:
		return False

#this function returns a list of all the image files in the list of directories supplied to it
def get_photo_list(photo_directories):
	list_to_scan = photo_directories.copy()
	output_list = []
	for i in list_to_scan:
		subdirs = os.listdir(i)
		for x in subdirs:
			try:
				if(os.listdir(str(i) + '/' + str(x)) != []):
					list_to_scan.append(str(i) + '/' + str(x))
			except NotADirectoryError:
				if(check_if_image_file(str(i) + '/' + str(x))):
					output_list.append(str(i) + '/' + str(x))
	cleaned_list = []
	for d in output_list:
		cleaned_list.append(re.sub('//', '/', d))
	return cleaned_list
			

def get_dir_list_from_config():
	music_dir = [] #MUS
	video_dir = [] #VID
	movie_dir = [] #MOV
	tvsho_dir = [] #TVS
	photo_dir = [] #PHO
	filename = open('msdr.conf', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			if(read_string[0:3] == 'MUS'): #music directory
				music_dir.append(read_string[4:])
			elif(read_string[0:3] == 'VID'): #video directory
				video_dir.append(read_string[4:])
			elif(read_string[0:3] == 'MOV'): #movie directory
				movie_dir.append(read_string[4:])
			elif(read_string[0:3] == 'TVS'): #tv show directory
				tvsho_dir.append(read_string[4:])
			elif(read_string[0:3] == 'PHO'): #photos directory
				photo_dir.append(read_string[4:])
		read_string = filename.readline() #read new line
	filename.close() #finally close the file
	#return all the different directory lists
	return (music_dir, video_dir, movie_dir, tvsho_dir, photo_dir)