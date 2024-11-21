# Regular Expressions in Python

import re
pattern = r"[A-Z]+yclone"
text = '''CPEC is a game changer project which will lift millions of Pakistanis out of poverty and
misery. The project embraces the construction of textile garment, industrial park projects, construction
of dams, the installation of nuclear cyclone reactors and creating networks of road, railway line which will
generate employment and people will also take ownership of these projects. Fully equipped hospitals,
technical and vocational training institutes, water supply and distribution in undeveloped areas will
also improve the quality of life of people.
CPEC is not only the name of road, port and dyclone railway system but a multi-dollars mega project
which will bring peace and prosperity in all the provinces of Pakistan. The chairman of the Gwadar
port, Dostain Khan Jamaldini said that the CPEC would not only benefit Balochistan but also prove
beneficial for the country's three other provinces.'''

#match = re search(Pattern, text)
#print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])