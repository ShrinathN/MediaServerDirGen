#!/bin/python

def get_music_dir_list():
	music_list = []
	filename = open('music_dir_list', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			music_list.append(read_string)
		read_string = filename.readline()
	filename.close()
	return music_list
	
def get_movie_dir_list():
	movie_list = []
	filename = open('movie_dir_list', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			movie_list.append(read_string)
		read_string = filename.readline()
	filename.close()
	return movie_list

def get_tv_dir_list():
	tv_list = []
	filename = open('tv_dir_list.txt', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			tv_list.append(str(read_string))
		read_string = filename.readline()			
	return tv_list

def get_images_dir_list():
	images_list = []
	filename = open('images_dir_list', 'r') #opening file
	read_string = filename.readline() #reading the first line
	while(read_string != ''): #looping all lines
		if(read_string[0] != '#'): #not a comment
			images_list.append(read_string)
		read_string = filename.readline()			
	return images_list