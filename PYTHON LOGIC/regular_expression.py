import re

txt = ("Hi, my name is PA)(*&^%$#@RVA R. SHARMA. I am 18 years old. I am studying in the college of LDRP INSTITUTE OF TECHNOLOGY AND REASERCH. I live in gandhinagar sector-4/c, plot no.-1313/2. My father's name is RAKESHKUMAR J. SHARMA")

x = re.findall("parva\Z", txt)
print(x)
if x:
    print("yes, there is one match found")
else:
    print("no match found")
