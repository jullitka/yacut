from re import escape
from string import ascii_letters, digits

ALLOWED_SYMBOLS = ascii_letters + digits
REGEX_PATTERN = r'[' + escape(ALLOWED_SYMBOLS) + r']{1,16}$'
MAX_ORIGINAL_SIZE = 128
MAX_SHORT_SIZE = 16
DEFAULT_SHORT_SIZE = 6
NUMBER_OF_ATTEMPTS = 10