# sprawdz, czy nawias ma swoja pare, jesli ma swroc True, jesli nie False
def para_nawiasow(tekst: str) -> bool:
    # TODO
    otwierajace = tekst.count("(")
    zamykajace = tekst.count(")")
    if(otwierajace == zamykajace):
         return True
    else:
        return False