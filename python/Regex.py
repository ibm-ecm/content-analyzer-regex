'''
Disclaimer of warranties.
This code is sample code created by IBM Corporation. IBM grants you a
non-exclusive copyright license to use this sample code example. This
sample code is not part of any standard IBM product and is provided to you
solely for the purpose of assisting you in the development of your
applications. This example has not been thoroughly tested under all
conditions. IBM, therefore cannot guarantee nor may you imply reliability,
serviceability, or function of these programs. The code is provided "as is",
without warranty of any kind. IBM shall not be liable for any damages
arising out of your or any other parties use of the sample code, even if IBM
has been advised of the possibility of such damages. if you do not agree with
these terms, do not use the sample code.
Copyright IBM corp. 2019 all rights reserved.
To run, see README.md
'''

import re  # importing re module to deal with regular expressions
import sys  # gives access to System-specific parameters and functions

# defining command line input arguments to be entered by the user

f = open(sys.argv[1], 'r')  # opening the input file in read mode

# defining list variables to store the results
curr_res = []
mail_res = []
phno_res = []
ukpostcode_res = []
url_res = []
uszip_res = []
date_res = []

# defining flag variables

mail_flag = False
curr_flag = False
phno_flag = False
url_flag = False
ukpostcode_flag = False
uszip_flag = False
date_flag = False

# email regular expresssion
mail_regex = '[a-zA-Z0-9][a-zA-Z0-9!#$%&\'*+/=.?^_`{|}~-]*@(?:[a-zA-Z](?:[a-zA-Z0-9-]*)?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z])?'

# currency regular expresssion
curr_regex = '(?:\$|can\$|C\$|€|USD|CAD|EUR|ATS|BEF|DEM|EEK|ESP|FIM|FRF|GRD|IEP|ITL|LUF|NLG|PTE|can)[\s\S]?\d{1,3}(?:,\d{3})*(?:\.\d{1,3})?(?=\s)'

# UK Postal Code regular expresssion
ukpostcode_regex = '[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}'

# US phone number regular expresssion
phno_regex = '[+]?[1\s-]*[\(-]?[0-9]{3}[-\)]?[\s-]?[0-9]{3}[\s-]?[0-9]{4}(?=\s)'

# url regular expresssion
url_regex = 'http[s]?://(?:[a-zA-Z0-9$-_@.&+!*\(\),]|(?:%[0-9a-zA-Z]))+(?=\s)'

# US Zip code regular expression
uszip_regex = '\s?[0-9]{5}(?:-[0-9]{4})?$'

# Date format: dd/mm/yyyy regular expression
date_regex1 = '\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:0?[1-9]|1[0-2])(?:/)(?:\d{4})'

# Date format: mm/dd/yyyy regular expression
date_regex2 ='\s?(?:0?[1-9]|1[0-2])(?:/)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:\d{4})'

# Date format: 1st, mon/month yyyy regular expression
date_regex3 = '\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:nd|rd|th|st)?(?:[\s|,|]?\s?)(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)\s\d{4}'

# Date format: mon/month, 1, yyyy regular expression
date_regex4 = '\s?(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)(?:[\s|,]?\s?)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:[\s|,]?\s?)\s\d{4}'


choice = ['-e', '-u', '-p', '-c', '-k', '-z', '-d']
count = len(sys.argv)

for i in range(2, count):

	if (sys.argv[i]) not in choice:
		print("\nUsage: <prog.py> <input file> [optional arguments]\n\nFrist Argument\t", sys.argv[0], "python script name with .py extension to be entered\n\nSecond Argument", sys.argv[1], "\ttext input file with .txt extension to be entered as 2nd argument \n\n[optional arguments]\n-e\t--this option displays all the valid Email occurrences from the input file\n-u\t--this option displays all the valid Url occurrences from the input file\n-c\t--this option displays only EURO,Canada and US Currency format occurrences from the input file\n-p\t--this option displays only valid US Phone number occurrences from the input file\n-k\t--this option displays only valid UK Postal code occurrences from the input file\n-z\t--this option displays only valid US ZIP code occurrences from the input file\n-d\t--this option displays the following date format occurrences from the input file\n\t  dd/mm/yyyy, mm/dd/yyyy, 1st mon/month yyyy, mon/month, 1, yyyy")
		sys.exit()

	elif sys.argv[i] == '-e':
		mail_flag = True

	elif sys.argv[i] == '-c':
		curr_flag = True

	elif sys.argv[i] == '-u':
		url_flag = True

	elif sys.argv[i] == '-p':
		phno_flag = True

	elif sys.argv[i] == '-k':
		ukpostcode_flag = True

	elif sys.argv[i] == '-z':
		uszip_flag = True

	elif sys.argv[i] == '-d':
		date_flag = True

for line in f.readlines():
	if curr_flag is True:
		curr = re.findall(curr_regex, line)
		if len(curr) > 0:
			curr_res.extend(curr)

	if mail_flag is True:
		mail = re.findall(mail_regex, line)
		if len(mail) > 0:
			mail_res.extend(mail)

	if phno_flag is True:
		ph = re.findall(phno_regex, line)
		if len(ph) > 0:
			phno_res.extend(ph)

	if ukpostcode_flag is True:
		ukpostcode = re.findall(ukpostcode_regex, line)
		if len(ukpostcode) > 0:
			ukpostcode_res.extend(ukpostcode)

	if url_flag is True:
		url = re.findall(url_regex, line)
		if len(url) > 0:
			url_res.extend(url)

	if uszip_flag is True:
		uszip = re.findall(uszip_regex, line)
		if len(uszip) > 0:
			uszip_res.extend(uszip)

	if date_flag is True:
		date1 = re.findall(date_regex1, line)
		date2 = re.findall(date_regex2, line)
		date3 = re.findall(date_regex3, line)
		date4 = re.findall(date_regex4, line)
		if len(date1) > 0:
			date_res.extend(date1)
		if len(date2) > 0:
			date_res.extend(date2)
		if len(date3) > 0:
			date_res.extend(date3)
		if len(date4) > 0:
			date_res.extend(date4)

# printing the results
for i in range(2, count):

	if '-e' in sys.argv[i]:
		print("\nValid Email occurrences in the input file are:\n", mail_res)

	if '-c' in sys.argv[i]:
		print("\nRecognized currency (USD/CAD/EURO) occurrences in the input file are:\n", curr_res)

	if '-p' in sys.argv[i]:
		print("\nValid US Phone number occurrences in the input file are:\n",  phno_res)

	if '-u' in sys.argv[i]:
		print("\nValid URL occurrences in the input file are:\n", url_res)

	if '-k' in sys.argv[i]:
		print("\nValid UK Postal code occurrences in the input file are:\n", ukpostcode_res)

	if '-z' in sys.argv[i]:
		print("\n Valid US ZIP code occurrences in the input file are:\n", uszip_res)

	if '-d' in sys.argv[i]:
		print("\n Recognized date formats (dd/mm/yyyy, mm/dd/yyyy, 1st,mon/month yyyy, mon/month 1, yyyy) in the input file are:\n", date_res)


