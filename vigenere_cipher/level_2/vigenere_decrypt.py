# Дешифруємо текст методом Віженера задавши лиш довжину ключа отриману за допомогою методу Фрідмана

import string
from collections import Counter

def decrypt_vigenere(ciphertext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.upper() in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            plain_char = alphabet[(alphabet.index(char.upper()) - shift) % 26]
            plaintext.append(plain_char if char.isupper() else plain_char.lower())
            key_index += 1
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)

def find_key(ciphertext, key_length):
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))  # Залишаємо тільки букви
    alphabet = string.ascii_uppercase
    english_freq = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.0015, 0.0077, 
                    0.04, 0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 0.063, 0.091, 0.028, 0.0098, 
                    0.024, 0.0015, 0.02, 0.00074]
    key = ""
    
    for i in range(key_length):
        subset = ciphertext[i::key_length]
        chi_squares = []
        
        for shift in range(26):
            shifted_freq = Counter(alphabet[(alphabet.index(c) - shift) % 26] for c in subset)
            total = sum(shifted_freq.values())
            chi_square = sum(((shifted_freq[c] / total - english_freq[idx]) ** 2) / english_freq[idx]
                             for idx, c in enumerate(alphabet))
            chi_squares.append(chi_square)
        
        best_shift = chi_squares.index(min(chi_squares))
        key += alphabet[best_shift]
    
    return key

# Тестуємо
ciphertext = """VYC PKHOJT XZ RJV AGXOZFR DM ZGRSIBTAC TWPLIJ.  
RD KSBVAA HPV RLS VCTTEPS RJV YGMWYK IH HPV'J YXF.
HNV CGPRKT GH AS CYO RHL VIYCLZGKE XURQ RLDMVKI MPULGI MG T BKN MPACTZYA AWY ZMEYCUJGDG CL SEPBRKWSA MVOEGH.
AFG YGVASYK, AH AFG CMLXGZ, WOGT MH TPXMWIZSB PQ C DMSX CL RUIVZKFEGTDNP.
TWVQG NFD YWTU UVSW OVYCBBMJ IC ICCLRXYIR KHXUEU RPT VCXIUEA UKKFDNH HVICN AJRPBBBM.
KHXZ GU R DPNZZ. KHDZC YYM UBBJ SEPBRKWSA FSGEICNQ KE ZTTIZZFJS RJZLVL OXV TWL AWCRXOOZVD.
UVP VYCHX HNVRT PQ JFNT. MVKP AGL RJV CAXQZ KO LOMO SCPNHOWUA AFKEEH FSGE OCSW DVYJMM.
ZYEGL GU EM HNQN KHXUE CJ Y BHFGC OG HL KDKDKOR SODR. ZQFIH TFK NEAS UTZRIXB, UI BPKJA NPXMHKE. TWHR KJ YAE.
HNV NXUCVVCCMV-IVNIBPA UGHEWQV OU YCCCGHF WY KHT YYIV MU VORZBPU QGVGCZ VOJ OLU DCTC XG O MCAHZ.
RJV LXGSZVECAF-EVLINFE UIHSGMV MU KCSRNIPAKJK XL HNV RPNC QW APEWHRN CVR UVCXGU NZS DDL HRAT BB G XLPZQ.
VYC BHFGC LXMC QW KPG TUIMH WYTK MU MVK JUQQCEK KPMHKI OU AFG RPIBGZ,
SUI AFG DMGTZOKY DM YTK ADGGOJTH PL VYC EXFLVCI BQG FD PG WSGEGMCEK KTWWAD.
ND HPVZQI WSYZRTZ RQ GPDOS GEYIOGPX. CKXB ZYICNQ VYYI TFK KRJL ACE ZT IFUMES.
UM CIRXLH NRS TAFKTYA LMSGAIOGGJ. YC XHNZCPS QADNPMVE ZN PU YTKGHM WY RN JUNCIBDGOHCE BHLPVPXLA UW SIFJG.
EM PKHOJT XZ CXVP BHFHZD. IOC CIRXLH IRN TENTVQH XJKIYIOGPX.
RWHIMYT PUB NRLVNOMV AGL RQ KFT TFZZSI PLUKPJFSTKS DM YP RPI.
OWIV ACK TKIRJX OXV TD AFG RPIBGZ DAILPKRJH YCX RN PYR.
HIMB MVK GOXUR QW TXXK UW FDYK, VYC IRDK FF PSJ VYC PKHY ZS IOC CIR DY HNV MJZGEZYC.
YFUD TWL NQZLI HT BZEL VD HVCABBM, KHT HAVFP'H VFGWT XZ RJV RNIS.
GCL PYR KJ YI HBIV SJYDCTC PGR YPMQVJ. VYMHX KNF GD ICPVYIA HNV SJYDCTC SH GU RT IOCKI NTKWR.
KHDZC YYM GXOJ KHT ZWOSMA WC YF AI AFGZP EXFOC.
II PQ VYC HISIKAIVP, CEB CHH RZFT, AFCK YGM FKRLAF KKIPDKG.
JZVTYQKKW DY CVZNXVL CSMJM O CFRZ VD CIR HACCJ TWHR VYC LHFQ ZS CLU, EFKEESD, MIIHJ.
YYCC VFOKIRZ BKJYVKSK KHT HPVZQI BG OE ARJMTU UXMV NZMHLJH.
NC RTB LFRVPTG R KPG TUI MPRGPX Y JLSLLL IOGPX YH ECTX AH OC FFCH GCZ RDBPPG ZR.
IAS UELN LVELQT YCX DAZPLI R SHXZKJS IOGPX GH MVGK OCL YFDGGXG OK ICACPJCAR.
ORC AGA GU HSXMS AJEALQU."""

# Вказуємо довжину ключа 12
key_length = 12
print(f"Довжина ключа: {key_length}")

# Знаходимо ключ
key = find_key(ciphertext, key_length)
print(f"Знайдений ключ: {key}")

# Розшифровуємо текст
plaintext = decrypt_vigenere(ciphertext, key)
print(f"Розшифрований текст:\n{plaintext}")
