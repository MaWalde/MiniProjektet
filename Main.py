import subprocess
try:
    import nltk
except ImportError:
    subprocess.check_call(["pip", "install", "nltk"])
    import nltk


