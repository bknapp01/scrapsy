a = "1$"

while True:
    try:
        a.replace("$", "")
        a = 0
    except:
        pass
print(a)