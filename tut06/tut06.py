import os , shutil
import re

def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	series_names = ['','Breaking Bad','Game of Thrones','Lucifer']
	folder_names = ['','./wrong_srt/Breaking Bad/','./wrong_srt/Game of Thrones/','./wrong_srt/Lucifer/']

	if(0<webseries_num<4):
		series_req = series_names[webseries_num]
		folder_req = folder_names[webseries_num]
		if not os.path.exists('./corrected_srt/'):
			os.mkdir('./corrected_srt/')
		if not os.path.exists('./corrected_srt/'+series_req):
			os.mkdir('./corrected_srt/'+series_req)
		else: 
			print("Already Done")
			return
	else: 
		print('Enter valid input!')
		return
	
	# z = 0
	for file_name in os.listdir(folder_req):
		native = folder_req + file_name
		final_destination = './corrected_srt/' + series_req + '/'

		if(webseries_num==1):
			x = re.search("s\d\de\d\d",file_name).start()
			season = int(file_name[x+1:x+3])
			episode = int(file_name[x+4:x+6])
			epiname = ''
			E = 'Episode ' + '0'*(episode_padding - len(str(episode))) + str(episode)
		
		if(webseries_num==2 or webseries_num==3):
			x = re.search("\dx\d\d",file_name).start()
			season = int(file_name[x])
			episode = int(file_name[x+2:x+4])
			y = re.search("[.]",file_name).start()
			epiname = file_name[x+7:y]
			E = 'Episode ' + '0'*(episode_padding - len(str(episode))) + str(episode) + ' - '
 
		N = series_req + ' - '
		S = 'Season ' + '0'*(season_padding - len(str(season))) + str(season) + ' '
		# E = 'Episode ' + '0'*(episode_padding - len(str(episode))) + str(episode) + ' - '
		P =  epiname

		if(file_name[-4:]=='.mp4'): ex = '.mp4'; 
		else: ex = '.srt'; 
		# z += 1
		final_name = final_destination + N + S + E + P + ex
		# final_destination = 'corrected.srt/' + series_req + '/' + final_name
		# final_destination = './corrected_srt/' + series_req
		shutil.copy(native , final_destination)
		os.rename(final_destination + file_name , final_name)
		# native = folder_req + final_name
		# shutil.copy(final_name , final_destination)

	sol = os.listdir(final_destination)
	for x in sol:
		print(x)
	return

regex_renamer()