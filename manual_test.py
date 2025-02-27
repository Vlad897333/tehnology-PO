import Test_2

def test_stroka():
    if Test_2.back_string("Hello") == "olleH":
        print("Test stroka(Hello) is OK ")
    else:
        print("Test stroka(Hello) is Fail")

def test_stroka():
    if Test_2.back_string("Trem") == "merT":
        print("Test stroka(Trem) is OK ")
    else:
        print("Test stroka(Trem) is Fail")

def test_stroka():
    if Test_2.back_string("Praaf") == "faarP":
        print("Test stroka(Praaf) is OK ")
    else:
        print("Test stroka(Praaf) is Fail")

def test_stroka():
    if Test_2.back_string("jili") == "ilij":
        print("Test stroka(jili) is OK ")
    else:
        print("Test stroka(jili) is Fail")

def test_stroka():
    if Test_2.back_string("kat") == "tak":
        print("Test stroka(kat) is OK ")
    else:
        print("Test stroka(kat) is Fail")



def test_polindrome():
    if Test_2.polindrome("Masha") == "ahsaM":
        print("Test polindrome(Masha) is OK")
    else:
        print("Test polindrome(Masha) is Fail")

def test_polindrome():
    if Test_2.polindrome("Reall") == "llaeR":
        print("Test polindrome(Reall) is OK")
    else:
        print("Test polindrome(Reall) is Fail")

def test_polindrome():
    if Test_2.polindrome("feer") == "reef":
        print("Test polindrome(feer) is OK")
    else:
        print("Test polindrome(feer) is Fail")

def test_polindrome():
    if Test_2.polindrome("man") == "nam":
        print("Test polindrome(man) is OK")
    else:
        print("Test polindrome(man) is Fail")

def test_polindrome():
    if Test_2.polindrome("life") == "efil":
        print("Test polindrome(life) is OK")
    else:
        print("Test polindrome(life) is Fail")

def test_voweles():
    if Test_2.vowels("кокос") == 1 :
        print("Test vowels(кокос) is OK")
    else:
        print("Test vowels(кокос) is Fail")

def test_voweles():
    if Test_2.vowels("рукав") == 3 :
        print("Test vowels(рукав) is OK")
    else:
        print("Test vowels(рукав) is Fail")

def test_voweles():
    if Test_2.vowels("терьер") == 3 :
        print("Test vowels(терьер) is OK")
    else:
        print("Test vowels(терьер) is Fail")

def test_voweles():
    if Test_2.vowels("кролик") == 2 :
        print("Test vowels(кролик) is OK")
    else:
        print("Test vowels(кролик) is Fail")

def test_voweles():
    if Test_2.vowels("Шарага") == 2 :
        print("Test vowels(Шарага) is OK")
    else:
        print("Test vowels(Шарага) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("cold") == "dloc":
        print("Test duplicate(cold) is OK")
    else:
        print("Test duplicate(cold) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("lish") == "he knows Lish":
        print("Test duplicate(lish) is OK")
    else:
        print("Test duplicate(lish) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("rtyrtyrty") == "rty":
        print("Test duplicate(rtyrtyrty) is OK")
    else:
        print("Test duplicate(rtyrtyrty) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("shjhjhg") == "asd":
        print("Test duplicate(shjhjhg) is OK")
    else:
        print("Test duplicate(shjhjhg) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("kikikiki") == "ui":
        print("Test duplicate(kikikiki) is OK")
    else:
        print("Test duplicate(kikikiki) is Fail")

test_stroka()
test_polindrome()
test_voweles()
test_duplicate()
