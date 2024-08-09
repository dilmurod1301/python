def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija
print(kopaytma(5,9))


talaba = {
    'ism':'ism',
    'familiya':'familiya'
}
def Talabalar(ism,familiya,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qay.funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba = Talabalar("Hasan", "Fayzulayev", fakultet='Ximiya', kurs=4)
talaba1 = Talabalar("Husan", "Karimov", fakultet='Matematika', kurs=1)
print(talaba)
print(talaba1)


