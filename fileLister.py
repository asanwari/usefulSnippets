# This code recursivly lists all files and sub-directories in a given directory
# and stores it in a json file. Currently, import os

# input: python fileLister.py <parent_dir>
# output format: {"files": ["f1",f2"], "child_dir_1_name": {"files": [],"second_level_dir":{...}}, "child_dir_2_name": {"files": []}}



import sys
import json
import itertools
def main():
	path = sys.argv[1]
	directory_contents = {}
	directory_contents = list_files(path, directory_contents)
	print(directory_contents.keys())
	print(directory_contents['files'])
	with open('filePaths.json', 'w+') as outfile:
		json.dump(directory_contents, outfile)

def list_files(path, dir_obj):
	dirs = os.walk(path)
	d = next(itertools.islice(dirs, 0, None))
	# first, append all files that this folder contains
	# if it contains no files, an empty array will be appended
	dir_obj['files'] = d[2]

	# recursive case
	if len(d[1]) >0:
		for path in d[1]:
			# new object for path
			dir_obj[path] = {}
			# new path
			new_path = d[0]+ '\\'+ path
			print(f'going into {new_path}'.format(new_path = new_path) )
			# recursive call for the new path
			dir_obj[path] = list_files(new_path, dir_obj[path])
	
	return dir_obj



if __name__ == '__main__':
	main()