# Very good for printing comments during running program or debug.
def announce(f):
    def wrapper():
        print("Abount to run the function...")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("Hello, world!")

hello()