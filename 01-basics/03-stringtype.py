# single line string
s = "  You are awesome  "
print(s)

# multi line string
s1 = """You are
the creator
of your destiny"""
print(s1)

# index string
print(s[0])

# repetition of string
print(s*2)

# length of string
print(len(s))
print(len(s1))

# slicing a string
# does not include element at ending index
print(s[0:5])
print(s[0:]) # 0 to the end
print(s[:8]) # beginning to 8th element
print(s[-3:-1]) # from the end
print(s[0:9:2]) # steps 
print(s[15::-1]) # reverse string
print(s[::-1]) # reverse string

# strip spaces
print(s.strip()) # all
print(s.lstrip()) # left side
print(s.rstrip()) # right side

# find a substring
# substring, starting index, ending index
# if not found, returns -1
print(s.find("awe", 0, len(s)))

# prints occurrence of a substring
print(s.count('a'))

# replace a substring
print(s.replace("awesome", "super"))

# change upper or lower case
print(s.upper())
print(s.lower())
print(s.title())