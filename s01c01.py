# Set 1 - Challenge 1

# Convert hex to base64

# The following hex sequence:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce the following base64 sequence:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

hexseq = raw_input("input your hex sequence -> ")
base64seq = hexseq.decode("hex").encode("base64")

print ("your base64 sequence -> %s") % base64seq
