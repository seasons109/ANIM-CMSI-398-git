#sshigeta_anim398_01_week13_envVarFOR_v1.py

#Dictionary In-Class Assignment
env_var = {}
env_var ['$HIP'] = 'the home directory' #hou.expandString('$HIP')
env_var ['$JOB'] = 'the project directory' #hou.expandString('$JOB')
env_var ['$HFS'] = 'HFS file path' #hou.expandString('$HFS')
env_var ['$HDA'] = 'HDA file path'
env_var ['$HOME'] = 'HOME file path'

#Asks for prompt of what they would like the letter to search for the variable.
searched_letter = 'i'
contains_letter_list = []

for env_keys in env_var: 
	contains_letter = False

	for letter in range( len(env_var[env_keys]) ):
		if searched_letter == env_var[env_keys][letter]:
			contains_letter = True

		#print("letter: " + str(letter) + "   " +  env_var[env_keys][letter])
	if contains_letter: 
		contains_letter_list.append( env_keys )
	print( env_keys + " is mapped to " + env_var[env_keys] )

if (len(contains_letter_list) == 0 ):
    print("No keys contain the letter " + searched_letter )
else: 
    print(str(contains_letter_list) + " contain(s) the letter: " + searched_letter );