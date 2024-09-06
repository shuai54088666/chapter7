import os
def run(**args):
    print("[*] In dirlister moule.")
    files = os.listdir(".")
    
    return str(files)
