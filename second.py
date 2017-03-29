import re
def parse(text):
	return re.sub(r'([.,!?])',r' \1 ',text).split()
