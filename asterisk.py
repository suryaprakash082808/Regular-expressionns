import re
text= "He said: h ho hoooo!"
pattern = r"ho*"
matches = re.findall(pattern, text)
print(matches)  