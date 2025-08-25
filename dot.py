import re
pattern = r"a...b"
text = "abd, abb, acb, aab a_b a&b"
matches = (re.findall(pattern, text))
print(matches) 