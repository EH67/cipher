def atbash(str):
    for i in str.upper().strip():
        if i in ',\'\".?/!@#$%^&*()-+=\n     ':
            print(i, end="")
        else:
            print(chr(155 - ord(i)), end="")


