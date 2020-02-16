# Extract phone no and email from a long text or a document
# Nepali phone number types identified here: 01-4545454 9861353535 +977-9861353535 (977)9861353535 (977) 9825478965 (977)-9825478965

#import regex library
import re

#Regex regular expression format for phone numbers
phoneregex = re.compile(r'''(
    (\d{10})|
    (\+\d{3}-\d{10})|
    (\(\d{3}\)(-*)(\s*)\d{10})|
    (\d{2}-\d{7})
)''', re.VERBOSE)

#Regex regular expression format for email addresses
emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)


# Replace with the text document you want to scan for phone numbers and email address from.
text = "Hello prasannadhungel4@gmail.com 9861337234 sdfhkjhs +977-9861337234 jksdhfhsj sdfgsdj hello23@yahoo.com (977) 9825478965 01-4565987 (977)9825478965"


matches  = []
for groups in phoneregex.findall(text):
    matches.append(groups[0])

for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) >0:
    print('\n'.join(matches))


