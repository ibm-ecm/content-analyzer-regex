# Samples-RegEx-Patterns

Regular Expressions are used to find out a sequence of characters that define a search pattern. This repository contains artifacts to extract the valid email, url, US phone number, currency, UK postal code, US zipcode and date formats from the given input text file.

The python script `Regex.py` contains the regular expression validations which when applied to the given input file will extract the valid patterns.

## Usage <br>
Run the python script by passing in the command line input arguments as below: <br><br>
Regex.py _input_file_name_ _[arguments]_ <br>
where _Regex.py_ is the name of the python script file (provided) <br>
_input_file_name_ - the input text file from where the text matching the patterns has to be extracted from <br>
_[arguments]_ - specify one or more of the following arguments <br>
`-e` extracts all the valid email occurrences <br>
`-u` extracts all the valid url occurrences <br>
`-c` extracts all the currency value (USD, EUR, CAN) occurrences <br>
`-p` extracts all the US phone number occurrences <br>
`-k` extracts all the UK postal code occurrences <br>
`-d` extracts all the date occurrences <br>


## Supported formats

Here are the various formats supported for different types.
### Email 
_Regular Expression:_ <br>
```[a-zA-Z0-9][a-zA-Z0-9!#$%&\'*+/=.?^_`{|}~-]*@(?:[a-zA-Z](?:[a-zA-Z0-9-]*)?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z])?```

The email addresses are generally in the form _local-part@domain_.

The local-part of the email address may use any of these ASCII characters:
1. Uppercase and lowercase letters `A` to `Z` and `a` to `z`
2. Digits `0` to `9`
3. Printable characters ```!#$%&'*+-/=?^_`{|}~```

The domain could be in the following formats:
1.	Uppercase and lowercase letters `A` to `Z` and `a` to `z`
2.	Digits `0` to `9`, provided that top-level domain names are not all-numeric
3.	Hyphen `-` provided that it is not the first or last character

Ref: https://en.wikipedia.org/wiki/Email_address


### URL
Regular Expression: <br>
```http[s]?://(?:[a-zA-Z0-9$-_@.&+!*\(\),]|(?:%[0-9a-zA-Z]))+(?=\s)```

A typical URL could have the form `http://www.example.com/index.html`, which indicates a protocol (`http`), a hostname (`www.example.com`), and a file name (`index.html`). The regular expression is intended to match URL that starts with either `http` or `https`. <br>
Ref: https://en.wikipedia.org/wiki/URL


### US Phone Numbers
Regular Expression: <br>
```[+]?[1\s-]*[\(-]?[0-9]{3}[-\)]?[\s-]?[0-9]{3}[\s-]?[0-9]{4}(?=\s)```

The regular expression recognises the US phone number formats in the below patterns:  
- (###) ###-####
- +(#)(###) ###-####
- (#)(###) ###-####

Ref: https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers#North_America
<br>

### Currency
Regular Expression: <br>
```(?:\$|can\$|C\$|€|USD|CAD|EUR|ATS|BEF|DEM|EEK|ESP|FIM|FRF|GRD|IEP|ITL|LUF|NLG|PTE|can)[\s\S]?\d{1,3}(?:,\d{3})*(?:\.\d{1,3})?(?=\s)```

The regular expression validates only US Dollar (USD), Euro (EUR) and Canadian Dollar (CAD) currency formats as below: 
Considered the following currency symbols 
- US currency format starting with `$` symbol.
- Canadian currency formats starting with `can$`, `CAD`, `can`, `C$` symbols.
- Euro currency formats starting with `EUR`, `ATS`, `BEF`, `DEM`, `EEK`, `ESP`, `FIM`, `FRF`, `GRD`, `IEP`, `ITL`, `LUF`, `NLG`, `PTE`, `€` symbols.


### UK Postal Code
Regular Expression: <br>
```[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}```

UK Postal code format is as follows, where A signifies a letter and 9 a digit:

| Format | Coverage | Example |
|--------|----------|---------|
|AA9A 9AA|	WC postcode area; EC1–EC4, NW1W, SE1P, SW1	|EC1A 1BB|
|A9A 9AA|	E1W, N1C, N1P	|W1A 0AX|
|A9 9AA|	B, E, G, L, M, N, S, W	|M1 1AE|
|A99 9AA|	B, E, G, L, M, N, S, W	|B33 8TH|
|AA9 9AA|	All other postcodes|	CR2 6XH|
|AA99 9AA|	All other postcodes|DN55 1PT|

Ref: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom 


### US Zipcode
Regular Expression: <br>
```\s?[0-9]{5}[-][0-9]{4}$``` <br>

The regular expression matches US Zipcode that includes nine digits in the format  `ddddd-dddd`
Ref: https://en.wikipedia.org/wiki/List_of_postal_codes

### Date

The regular expression validates the dates that appear in the following formats

Regular Expressions: <br>
dd/mm/yyyy - ```\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:0?[1-9]|1[0-2])(?:/)(?:\d{4})```

mm/dd/yyyy - ```\s?(?:0?[1-9]|1[0-2])(?:/)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:/)(?:\d{4})```

1st mon/month yyyy - ```\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:nd|rd|th|st)?(?:[\s|,|]?\s?)(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)\s\d{4}'date_regex3 = '\s?(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:nd|rd|th|st)?(?:[\s|,|]?\s?)(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)\s\d{4}```

mon/month, 1, yyyy - ```\s?(?:[Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)(?:[\s|,]?\s?)(?:0?[1-9]|[1,2][0-9]|3[0-1])(?:[\s|,]?\s?)\s\d{4}```

