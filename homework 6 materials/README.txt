OBJECTIVE
*********
Complete the Pose Library.

TASKS/REQUIREMENTS
******************
1) Generate the entries of the Poses menu parameter.  The menu should be populated by poses stored in the HDA sections (see the Extra Files tab in Type Properties).  Sections whose names start with "poselib::" are poses.  Use the section names without the "poselib::" prefix for the menu entry names and labels.

2) Implement the callback script for the Load button parameter.  When clicked, the pose selected in the Poses menu should be loaded into the character node.

The HDA section contents of the selected pose contains a string representation of a Python dictionary with parameter names as the keys and parameter values as the values.

For example,
    "{ 'tx' : 0.25, 'ty' : 0.5, 'tz' : 0.75 }"

Loading a pose means reading the string representation, converting it to a Python dictionary and then setting the parameter values on the character node.

3) Implement the callback script for the Capture button parameter.  When clicked, the names and values of the parameters on the character node should be captured and stored in a Python dictionary.  Only Integer and Float parameters should be captured.  The Python dictionary should be converted to a string representation and stored in an HDA section.  The name of the section must be specified by the value of the Pose Name parameter and prefixed with "poselib::".

If the Pose Name parameter is empty, then the Capture button callback script should display an error message and exit early.

GETTING STARTED
***************
- Open poselib.hip.
- In the Network Editor, RMB-click on the human_animation_rig1 node and choose Type Properties...
- Write Python code in the parameter callback scripts, menu script and the PoseLibrary script section to complete the Pose Library.

HINTS
*****
- Use Python's str() function to convert a Python dictionary into a string representation of the dictionary.
- Use Python's eval() function to convert a string representation of a dictionary to a Python dictionary.

BONUS TASKS
***********
1) Add a Set Keyframes checkbox parameter (below the Load button).  When loading a pose, if the parameter is checked, then keyframes should be set for each parameter that is loaded into the character node.

2) Add an Omit Default Values checkbox parameter (below the Capture button).  When capturing a pose, if the parameter is checked, only capture names and values of parameters that have non-default values.

