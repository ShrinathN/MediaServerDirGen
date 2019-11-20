import msdr_filedb

#starting, getting master config from the config file
jobs_to_do = msdr_filedb.get_dir_list_from_config()

#going through all the jobs
for i in jobs_to_do:
	current_dir = i['dir']
	type_of_job = i['type']
	isrecursive = i['recursive']
