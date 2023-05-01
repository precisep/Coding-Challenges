def hello(word):
    if type(word) == "string":
        print("Please enter a string")
    else:
        greet = print("Hello", word + "!")

    return greet


hello("Precise")
