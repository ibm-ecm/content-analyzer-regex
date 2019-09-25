# Samples-RegEx-Patterns

Regular Expressions are used to find out a sequence of characters that define a search pattern. This repository contains artifacts to extract the valid email, url, US phone number, currency, UK postal code, US zipcode and date formats from the given input text file.


The python script `Regex.py` contains the regular expression validations which when applied to the given input file will extract the valid patterns.

**Usage**
Run the python script by passing in the command line input arguments as below:
_Regex.py input_file_name [arguments]_

Regex.py - Name of the python script file

input_file_name - the sample text file to extract the matching patterns

[arguments] - specify one or more of the following arguments
`-e` extracts all the valid email occurrences <br>
`-u` extracts all the valid url occurrences <br>
`-c` extracts all the currency value (USD, EUR, CAN) occurrences <br>
`-p` extracts all the US phone number occurrences <br>
`-k` extracts all the UK postal code occurrences <br>
`-d` extracts all the date occurrences <br>


## Valid formats supported
#### Email 
Regular Expression: 
```[a-zA-Z0-9][a-zA-Z0-9!#$%&\'*+/=.?^_`{|}~-]*@(?:[a-zA-Z](?:[a-zA-Z0-9-]*)?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z])?```

The format of email addresses is local-part@domain.
The local-part could be in the following formats:
1. Uppercase and lowercase letters A to Z and a to z
2. Valid digits 0 to 9
3. Printable characters !#$%&'*+-/=?^_`{|}~

The domain could be in the following formats:
1.	Uppercase and lowercase letters A to Z and a to z
2.	Valid digits 0 to 9, provided that top-level domain names are not all-numeric
3.	Hyphen - provided that it is not the first or last character

Ref: https://en.wikipedia.org/wiki/Email_address 


#### Url
Regular Expression: ```http[s]?://(?:[a-zA-Z0-9$-_@.&+!*\(\),]|(?:%[0-9a-zA-Z]))+(?=\s)```

A typical URL example could be http://www.example.com/index.html, which indicates a protocol (http), a hostname (www.example.com), and a file name (index.html)
Ref: https://www.ibm.com/support/knowledgecenter/en/SSGMCP_5.5.0/administering/cpsm/eyuadc0079.html


#### US Phone Numbers
Regular Expression: ```[+]?[1\s-]*[\(-]?[0-9]{3}[-\)]?[\s-]?[0-9]{3}[\s-]?[0-9]{4}(?=\s)```

The regular expression recognises only US phone number formats, few example patterns are below for reference:  
- (###) ###-####
- +(#)(###) ###-####
- (#)(###) ###-####


#### Currency
Regular Expression: ```(?:\$|can\$|C\$|€|USD|CAD|EUR|ATS|BEF|DEM|EEK|ESP|FIM|FRF|GRD|IEP|ITL|LUF|NLG|PTE|can)[\s\S]?\d{1,3}(?:,\d{3})*(?:\.\d{1,3})?(?=\s)```

The regular expression recognizes only US Dollar - USD, Euro - EUR and Canadian Dollar - CAD currency formats. 
Considered the following currency symbols 
- $ symbol in USD currency format.
- can$, CAD,can and C$ in Canadian currency formats.
- Euro currency formats -  EUR, ATS, BEF, DEM, EEK, ESP, FIM, FRF, GRD, IEP, ITL, LUF, NLG, PTE.


#### UK Postal Code
Regular Expression: ```[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}```

Ref: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom 


#### US Zipcode
Regular Expression: ```\s?[0-9]{5}[-][0-9]{4}$```
The regular expression recognises only the 5-digit US zip code. The above regular expression supports the following pattern as valid one. 
- xxxxx-xxxx


#### Date

The regular expression recognises the following date formats.

dd/mm/yyyy
Regular Expression: ```\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:0?[1-9]|1[0-2])(?:/)(?:\d{4})```

mm/dd/yyyy
Regular Expression: ```\s?(?:0?[1-9]|1[0-2])(?:/)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:\d{4})```

1st mon/month yyyy
Regular Expression: ```\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:nd|rd|th|st)?(?:[\s|,|]?\s?)(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)\s\d{4}'date_regex3 = '\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:nd|rd|th|st)?(?:[\s|,|]?\s?)(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)\s\d{4}```

mon/month, 1, yyyy
Regular Expression: ```\s?(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)(?:[\s|,]?\s?)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:[\s|,]?\s?)\s\d{4}```

