#sshigeta_anim398_01_week13_envVarFOR_v1.py

#Dictionary In-Class Assignment
env_var = {}
env_var ['$HIP'] = hou.expandString('$HIP')
env_var ['$JOB'] = hou.expandString('$JOB')
env_var ['$HFS'] = hou.expandString('$HFS')
env_var ['$HDA'] = hou.expandString('$HDA')
env_var ['$HOME'] = hou.expandString('$HOME')

#Asks for prompt of what they would like the letter to search for the variable.
searched_letter = raw_input("Which letter would you like to search for? ")
contains_letter_list = []

for env_keys in env_var: 
	contains_letter = False

	for letter in range( len(env_var[env_keys]) ):
		if searched_letter == env_var[env_keys][letter]:
			contains_letter = True

	if contains_letter: 
		contains_letter_list.append( env_keys )

	print( env_keys + " is mapped to " + env_var[env_keys] )


if (len(contains_letter_list) == 0 ):
    print("No keys contain the letter " + searched_letter )
else: 
    print(str(contains_letter_list) + " contain(s) the letter: " + searched_letter );