
def palidrome(s: str):
    str_len = len(s)
    print("длина слова ", str_len)
    for e in range(0, str_len//2):
        print("сравниваю ", s[e], s[-(e+1)])
        if s[e] != s[-(e+1)]:
            return False
    return True

slovo = input("Введите слово ")
if palidrome(slovo):
    print("Это паллидром")
else:
    print("Это не паллидром")