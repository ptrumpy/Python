mad_lib = ["Oh, the ","outside is ","But the ","is so ","And since we've no place to "]
snow = "Let it snow, let it snow, let it snow."
noun1 = input("Enter a singluar noun - ")
adj = input("Enter an adjective to describe the noun in step 1 - ")
noun2 = input("Enter another noun - ")
adj2 = input("Enter an adjective to describe the noun in the last prompt - ")
verb = input("Enter a verb - ")

print(mad_lib[0] + "\033[1;32;40m" + noun1 +  "\033[0;37;40m " + mad_lib[1] + "\033[1;32;40m" + adj + "\033[0;37;40m .")
print(mad_lib[2] + "\033[1;32;40m" + noun2 +  "\033[0;37;40m " + mad_lib[3] + "\033[1;32;40m" + adj2 + "\033[0;37;40m .")
print(mad_lib[4] + "\033[1;32;40m" + verb + "\033[0;37;40m .")
print(str(snow))
