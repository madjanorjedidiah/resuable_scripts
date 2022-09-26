import os
import geopandas
import urllib.request
import pandas as pd
import glob
import csv
import random


#  get all files in a directory
def fetch_files(path, extension=None):
	filenames = os.listdir(path)
	if extension == None:
		return [print(filename) for filename in filenames]
	else:
		return [print(filename) for filename in filenames if filename.endswith(extension)]
# fetch_files('/home/jed', '.swp')


# convert data to json
def write_to_json(file):
	if os.path.exists(file):
		incoming_data = open(file, 'r').read()
		new_file = open("data.json","w")
		new_file.write(incoming_data)
		return True
	else:
		print("this is not a valid data")
		return False
# write_to_json("/home/jed/Desktop/Orders")


# convert shapefiles to geojson
def write_shp_to_geojson(shapefile):
	if os.path.exists(file):
		shp_file = geopandas.read_file(shapefile)
		return shp_file.to_file('myshpfile.geojson', driver='GeoJSON')
	else:
		print("this shapefile is not a valid or does not exist")
		return False
# write_shp_to_geojson('/home/jed/Desktop/trials/ernest/Regional Boundary_2019/Regional_Boundary_2019.shp')


# load data from api as json
def load_data_from_api(link):
	response = urllib.request.urlopen(link)
	data = response.read().decode('utf-8')
	file = open("data.json","w")
	return file.write(data)
# load_data_from_api('https://geoservicess.herokuapp.com/api/regions')


# combine a list of csvs as one
def combine_csvs(files_path, output_location, output_name):
	# joining files with concat and read_csv
	df = pd.concat(map(pd.read_csv, files_path), ignore_index=True)
	return df.to_csv(output_location+ '/' +output_name, index=False)


# get current year
def get_current_year():
    now = datetime.now()
    return now.year


# convert string to float
def string_to_float(a):
    if a == '':
        return 0
    else:
        return float(a)


# write to csv
def write_to_csv(path, filename, data):
	# open the file in the write mode
	with open(path + filename, 'w') as f:
	    # create the csv writer
	    writer = csv.writer(f)
	    # write a row to the csv file
	    writer.writerow(row)
	return 'done'


#  ensuring that numbers are integers
def format_num(value):
    return f"{'{:,}'.format(int(value))}"


#  formating money value
def format_ghc(value):
    return f"GH¢{'{:,}'.format(float(value))}"


#  calculate the maximum amount in a list of amounts
def max_amt(rev_list):
    return format_ghc(max(rev_list))


#  calculate the minimum amount in a list of amounts
def min_amt(rev_list):
    return format_ghc(min(rev_list))

# calculate the average amount in a list of amounts
def avg_amt(rev_list):
    return format_ghc(round((max(rev_list)-min(rev_list))/len(rev_list), 2))


#  calculate the total amount in a list of amounts
def tot_amt(rev_list):
    return format_ghc(round(sum(rev_list), 2))


#  merge separate colums or lists as one
def merge_list(lists):
	return list(zip(*lists))
#merge_list([['a','b'], [1,2]])


#  create a random list of ages
def rand_age(num, age_range):
	return [random.randint(*age_range) for a in range(0, num)]
# rand_age(10, (20, 50))


# create a random list of names
def rand_names(num, name):
	return [name + str(a) for a in range(0, num)]
# rand_names(5, 'jed')


aa = ['aa', 'aa', 'bb', 'bb', 'cc', 'cc']
def revome_duplicates(list):
	dictt = {}
	return [dictt[a]for a in list]