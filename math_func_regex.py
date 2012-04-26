import re

#regexp = r"[a-z]+\(\d\)"

regexp = r"[a-z]+\(\s*\d*\s*\)"

print re.findall(regexp,"cos(0)") == ["cos(0)"]

print re.findall(regexp,"sqrt( 2222 ) ") == ["sqrt( 2222 )"]

print re.findall(regexp,"cos     (0)") != ["cos     (0)"]

print re.findall(regexp,"sqrt(x)") != ["sqrt(x)"]
