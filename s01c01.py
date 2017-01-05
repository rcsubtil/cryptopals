# Set 1 - Challenge 1

# Convert hex to base64

print "\nthe sequence: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hexseq = raw_input("input your hex sequence -> ")

print "\nshould produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
base64seq = hexseq.decode("hex").encode("base64")

print ("your base64 sequence -> %s") % base64seq
