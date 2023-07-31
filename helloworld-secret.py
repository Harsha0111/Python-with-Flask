import os

try:
    helloworld = os.environ["HELLO_WORLD"]
    hi = os.environ["HI"]
except KeyError:
    helloworld = "SECRET_MSG not available in secrets!"
    hi = "Hi not available!"
    # or raise an error if it's not available so that the workflow fails

print (helloworld , hi )