Script: TransformingEvents.py

Args: 
1. input_file - file with recorded events

Description: 
For every user we are interested in matrix of size 26x26 for every pair of english letters.
Every cell of matrix is list of numbers - delays in ms between certain pair of letters.
So the meaning of this script is to transform all recorded events to mentioned matrix of list.

File input format:
Described here https://docs.google.com/document/d/12RPjglSk9KB7SSOt1MXfXJn7EtUb_VgHOOKZa-Zvd3Y/edit

File output format:

Output file should be called "{GUID}-{input_file}".

For every pair of english letters (order matters) should exists a single line. Line format:
AB : number1 number2 ... numberN
where A and B are letters (A and B can be equal), number1 number2 ... numberN - delays in milliseconds.

--------------------------------------------------------------------------------------------------------------- 