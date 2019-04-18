LOGIN_URL = '/account/signin/'
IMAGE_DIR = 'media/images'
FILE_CHUNK_SIZE = 2500000


from time import time
def now_str(mul=1):
	"""
	current time in string format
	"""
	return str(int(time()*(10**mul)))


from uuid import uuid4
from hashlib import md5
def random():
	return str(md5(now_str(2).encode()+uuid4().hex.encode()).hexdigest())
