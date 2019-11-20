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
# For example, to add your TV show directory, which follows the structure, add the following
# TVS,/path/to/tv/show/library
#
# Various flags can be added to each directory listing
# R - for recursive
# For example, a master photo directory can be declared by
# PHO,/path/to/photos/,R
###
'''
	fil.write(text_to_write)
	fil.close()


#checks if a string is a video file or not, just checks the extension
def check_if_video_file(string_to_check):
	if(string_to_check[-4:] == '.mp4' or string_to_check[-4:] == '.mkv' or string_to_check[-4:] == '.wav' or string_to_check[-4:] == '.m4a' or string_to_check[-4:] == '.avi' or string_to_check[-5:] == '.webm'):
		return True
	else:
		return False

#this function takes in a single video directory as a string and returns the list of video files in it
def get_video_list(video_directory):
	list_of_video_files = []
	subdir_listing = os.listdir(video_directory)
	for current_subdir in subdir_listing:
		try:
			os.listdir(video_directory + '/' + current_subdir)
			continue
		except NotADirectoryError:
			if(check_if_video_file(video_directory + current_subdir)):
				list_of_video_files.append(video_directory + current_subdir)
	return list_of_video_files

#this function returns a list of all the video files in the list of directories supplied to it
def get_video_list_r(video_directories):
	if(type(video_directories) == type(str())):
		list_to_scan = [video_directories]
	elif(type(video_directories) == type(list())):
		list_to_scan = video_directories.copy()
	output_list = []
	for i in list_to_scan:
		subdirs = os.listdir(i)
		for x in subdirs:
			try:
				if(os.listdir(str(i) + '/' + str(x)) != []):
					list_to_scan.append(str(i) + '/' + str(x))
			except NotADirectoryError:
				if(check_if_video_file(str(i) + '/' + str(x))):
					output_list.append(str(i) + '/' + str(x))
	cleaned_list = []
	for d in output_list:
		cleaned_list.append(re.sub('//', '/', d))
	return cleaned_list

#checks if a string is an image file or not, just checks the extension
def check_if_image_file(string_to_check):
	if(string_to_check[-4:] == '.png' or string_to_check[-4:] == '.bmp' or string_to_check[-4:] == '.gif' or string_to_check[-4:] == '.jpg' or string_to_check[-5:] == '.jpeg' or string_to_check[-4:] == '.PNG' or string_to_check[-4:] == '.BMP' or string_to_check[-4:] == '.GIF' or string_to_check[-4:] == '.JPG' or string_to_check[-5:] == '.JPEG'):
		return True
	else:
		return False

#this function returns a list of all the image files in the list of directories supplied to it
def get_photo_list_r(photo_directories):
	if(type(photo_directories) == type(str())):
		list_to_scan = [photo_directories]
	elif(type(photo_directories) == type(list())):
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
	job_list = []
	filename = open('msdr.conf', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			chopped_line = read_string.split(',')
			job_list.append({
				'type' : chopped_line[0],
				'dir' : chopped_line[1],
				'recursive' : True if(chopped_line[2] == 'R') else False
			})
		read_string = filename.readline() #read new line
	filename.close() #finally close the file
	return job_list