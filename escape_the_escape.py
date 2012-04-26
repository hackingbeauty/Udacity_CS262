import re

regexp = r'"(?:[^\\]| "'

print re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']

print re.findall(regexp,'"\\"') != ['"\\"']
