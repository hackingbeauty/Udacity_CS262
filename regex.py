import re

regexp = r"[a-z]{2}|[0-9]+"

print re.findall(regexp,"ab") == ["ab"]
print re.findall(regexp,"1") == ["1"]
print re.findall(regexp,"123") == ["123"]
print re.findall(regexp,"a") != ["a"]
print re.findall(regexp,"abc") != ["abc"]
print re.findall(regexp,"abc123") != ["abc123"]
