import re

#regexp = r"\w+(?:-\w+)+"

#regexp = r"\w+|w+(?:\w+)+"

regexp = r"[a-z]+-?[a-z]+"

print re.findall(regexp,"well-liked") == ["well-liked"]

print re.findall(regexp,"html") == ["html"]

print re.findall(regexp,"a-b-c") != ["a-b-c"]

print re.findall(regexp,"a--b") != ["a--b"]
