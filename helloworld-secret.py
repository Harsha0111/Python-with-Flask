import os

try:
    helloworld = os.environ["helloworld"]
except KeyError:
    helloworld = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

print (helloworld)