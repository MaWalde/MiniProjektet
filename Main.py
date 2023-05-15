import subprocess
try:
    import nltk
except ImportError:
    subprocess.check_call(["pip", "install", "nltk"])
    import nltk

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True, raise_on_error=True)
