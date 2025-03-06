import testik_2  # type: ignore

def test_stroka():
    if testik_2.back_string("Hi") == "iH":
        print("Test stroka(Hi) is OK ")
    else:
        print("Test stroka(Hi) is Fail")

def test_stroka():
    if testik_2.back_string("Trem") == "merT":
        print("Test stroka(Trem) is OK ")
    else:
        print("Test stroka(Trem) is Fail")

def test_stroka():
    if testik_2.back_string("Praaf") == "faarP":
        print("Test stroka(Praaf) is OK ")
    else:
        print("Test stroka(Praaf) is Fail")

def test_stroka():
    if testik_2.back_string("jili") == "ilij":
        print("Test stroka(jili) is OK ")
    else:
        print("Test stroka(jili) is Fail")

def test_stroka():
    if testik_2.back_string("kat") == "tak":
        print("Test stroka(kat) is OK ")
    else:
        print("Test stroka(kat) is Fail")



def test_polindrome():
    if testik_2.polindrome("Masha") == "ahsaM":
        print("Test polindrome(Masha) is OK")
    else:
        print("Test polindrome(Masha) is Fail")

def test_polindrome():
    if testik_2.polindrome("Reall") == "llaeR":
        print("Test polindrome(Reall) is OK")
    else:
        print("Test polindrome(Reall) is Fail")

def test_polindrome():
    if testik_2.polindrome("fer") == "ref":
        print("Test polindrome(fer) is OK")
    else:
        print("Test polindrome(fer) is Fail")

def test_polindrome():
    if testik_2.polindrome("mn") == "nm":
        print("Test polindrome(mn) is OK")
    else:
        print("Test polindrome(mn) is Fail")

def test_polindrome():
    if testik_2.polindrome("lif") == "fil":
        print("Test polindrome(lif) is OK")
    else:
        print("Test polindrome(lif) is Fail")

def test_voweles():
    if testik_2.vowels("кокос") == 1 :
        print("Test vowels(кокос) is OK")
    else:
        print("Test vowels(кокос) is Fail")

def test_voweles():
    if testik_2.vowels("рука") == 3 :
        print("Test vowels(рука) is OK")
    else:
        print("Test vowels(рука) is Fail")

def test_voweles():
    if testik_2.vowels("терьер") == 3 :
        print("Test vowels(терьер) is OK")
    else:
        print("Test vowels(терьер) is Fail")

def test_voweles():
    if testik_2.vowels("кролик") == 2 :
        print("Test vowels(кролик) is OK")
    else:
        print("Test vowels(кролик) is Fail")

def test_voweles():
    if testik_2.vowels("Шарага") == 2 :
        print("Test vowels(Шарага) is OK")
    else:
        print("Test vowels(Шарага) is Fail")

def test_duplicate():
    if testik_2.remove_duplicates("cold") == "dloc":
        print("Test duplicate(cold) is OK")
    else:
        print("Test duplicate(cold) is Fail")

def test_duplicate():
    if testik_2.remove_duplicates("lish") == "he knows Lish":
        print("Test duplicate(lish) is OK")
    else:
        print("Test duplicate(lish) is Fail")

def test_duplicate():
    if testik_2.remove_duplicates("rtyrtyrty") == "rty":
        print("Test duplicate(rtyrtyrty) is OK")
    else:
        print("Test duplicate(rtyrtyrty) is Fail")

def test_duplicate():
    if testik_2.remove_duplicates("shjhjhg") == "asd":
        print("Test duplicate(shjhjhg) is OK")
    else:
        print("Test duplicate(shjhjhg) is Fail")

def test_duplicate():
    if testik_2.remove_duplicates("kikikiki") == "ui":
        print("Test duplicate(kikikiki) is OK")
    else:
        print("Test duplicate(kikikiki) is Fail")

test_stroka()
test_polindrome()
test_voweles()
test_duplicate()
