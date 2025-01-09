def type(text, t):
    import time
    for char in text:
        print(char, sep="", end="", flush=True)
        time.sleep(t/len(text))

type("Hallo",0.5)