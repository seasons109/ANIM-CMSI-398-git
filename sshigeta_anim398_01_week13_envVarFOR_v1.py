#sshigeta_anim398_01_week13_envVarFOR_v1.py

#Dictionary In-Class Assignment
env_var = {}
env_var ['$HIP'] = 'the home directory' #hou.expandString('$HIP')
env_var ['$JOB'] = 'the project directory' #hou.expandString('$JOB')
env_var ['$HFS'] = 'HFS file path' #hou.expandString('$HFS')
env_var ['$HDA'] = 'HDA file path'
env_var ['$HOME'] = 'HOME file path'

#Asks for prompt of what they would like the letter to search for the variable.
searched_letter = 'r'

for env_keys in env_var: 
	
	for letter in range( len(env_var[env_keys]) ):
		if searched_letter == env_var[env_keys][letter]:
			print("It worked! " + env_var[env_keys] )

		print("letter: " + str(letter) + "   " +  env_var[env_keys][letter])

