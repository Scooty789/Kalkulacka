# Univerzální geo kalkulačka verze 1.1
print('Geomterická kalkulačka verze 1.1 by Scooty789')
print('VAROVÁNÍ! Tato verze NEPODPORUJE záporná čísla!')
print('Tvary a funkce se zadávají pomocí čísel!')
aritmetika = '8'
geometrie = '9'
matika = input('Chceš počítat aritmetiku: 8 nebo geometrii?: 9: ')
if matika == '9':
    trojúhelník = '1'
    čtverec = '2'
    obdélník = '3'
    kružnice = '4'
    odpoved = input('Zadej číslo tvaru. Výběr: trojúhelník: 1, čtverec: 2, obdélník: 3, kružnice: 4: ')
    if odpoved == '1':
        operace = input('Co chceš počítat? obvod: 5 nebo obsah: 6? ')
        obvod = '5'
        obsah = '6'
        if operace == '5':
            a = float(input('Zadej stranu trojúhelníku a v cm: '))
            b = float(input('Zadej stranu trojúhelníku b v cm: '))
            c = float(input('Zadej stranu trojúhelníku c v cm: '))
            a_dobre = a > 0
            b_dobre = b > 0
            c_dobre = c > 0
            if (a_dobre, b_dobre, c_dobre):
                print('Obvod trojúhelníku se stranami', a, b, c, 'je', a + b + c, 'cm')
            else:
                print('Zadejte kladnou hodnotu strany.')
        if operace == '6':
            aa = float(input('Zadej stranu trojúhelníku a v cm: '))
            va = float(input('Zadej výšku trojúhleníku va v cm: '))
            aa_dobre = aa > 0
            va_dobre = va > 0
            if (aa_dobre, va_dobre):
                print('Obsah trojúhelníku se stranou a', aa,'cm a výškou va', va, 'cm je', aa * va / 2, 'cm2')
            else:
                print('Zadejte kladnou hodnotu výšky a + strany a')
    elif odpoved == '2': # čtverec
        obvod = '5'
        obsah = '6'
        operace = input('Co chceš počítat? obvod: 5 nebo obsah: 6 ? ')
        if operace == '5':
            ac = float(input('Zadej stranu čtverce a v cm: '))
            ac_dobre = ac > 0
            if ac_dobre:
                print('Obvod čtverce se stranou', ac, 'cm je', ac * 4, 'cm')
            else:
                print('Zadejte kladnou hodnotu strany a')
        if operace == '6':
            ao = float(input('Zadej stranu čtverce a v cm: '))
            ao_dobre = ao > 0
            if ao_dobre:
                print('Obsah čtverce se stranou', ao, 'cm je', ao * ao, 'cm2')
            else:
                    print('Zadejte kladnou hodnotu strany a')
    if odpoved == '3': # obdélník
        obvod = '5'
        obsah = '6'
        operace = input('Co chceš počítat? obvod: 5 nebo obsah: 6? ')
        if  operace == '5':
            aob = float(input('Zadej stranu obdélníku a v cm: '))
            bob = float(input('Zadej stranu obdélníku b v cm: '))
            aob_dobre = aob > 0
            bob_dobre = bob > 0
            if (aob_dobre, bob_dobre):
                print('Obvod obdélníku se stranami', aob, 'cm', bob, 'cm je', 2 * (aob + bob), 'cm')
            else:
                print('Zadejte kladnou hodnotu stran')
        elif operace == '6':
            aobs = float(input('Zadej stranu obdélníku a v cm: '))
            bobs = float(input('Zadej stranu obdélníku b v cm: '))
            aobs_dobre = aobs > 0
            bobs_dobre = bobs > 0
            if (aobs_dobre, bobs_dobre):
                print('Obsah obdélníku se stranami', aobs, 'cm', bobs, 'cm je', aobs * bobs, "cm2")
            else:
                print('Zadejte kladné hodnoty stran a + b')
    if odpoved == '4':
        obvod = '5'
        obsah = '6'
        operace = input('Co chceš počítat? obvod: 5 nebo obsah: 6? ')
        if operace == '5':
            prumer = float(input('Zadejte průměr kružnice v cm: '))
            prumer_dobre = prumer > 0
            if prumer_dobre:
                print('Obvod kružnice s průměrem', prumer, 'cm je', prumer * 3.14, 'cm')
        elif operace == '6':
            polomer = float(input('Zadejte poloměr kružnice v cm: '))
            polomer_dobre = polomer > 0
            if polomer_dobre:
                print('Obsah kružnice s poloměrem', polomer, 'cm je', 3.14 * (polomer * polomer), 'cm2')
if matika == '8':
    sčítaní = '10'
    odčítání = '11'
    násobení = '12'
    dělení = '13'
    umocnňování: '14'
    odmocňování: '15'
    arit_operace = input('Zadej aritmetickou fuknci: Sčítání: 10, Odčítání: 11, Násobení: 12, Dělení: 13, Umocňování: 14, Odmocňování: 15: ')
    if arit_operace == '10':
        cislo1 = float(input('Zadej 1. číslo, které chcete sečíst: '))
        cislo1_dobre = cislo1 > 0
        cislo2 = float(input('Zadej 2. čislo, které chcete sečíst: '))
        cislo2_dobre = cislo2 > 0
        if (cislo1_dobre, cislo2_dobre):
            print('Součet', cislo1, 'a', cislo2, 'je', cislo1 + cislo2)
        else: print('Zadejte kladná čísla.')
    if arit_operace == '11':
        cislo3 = float(input('Zadej 1. čislo, které chcete odečíst: '))
        cislo4 = float(input('Zadej 2. čislo, které chcete odečíst: '))
        cislo3_dobre = cislo3 > 0
        cislo4_dobre = cislo4 > 0
        if (cislo3_dobre, cislo4_dobre):
            print('Rozdíl čísel', cislo3, 'a', cislo4, 'je', cislo3 - cislo4)
        else: print('Zadejte kladná čísla.')
    if arit_operace == '12':
        cislo5 = float(input('Zadej 1. číslo, které chcete násobit: '))
        cislo6 = float(input('Zadej 2. číslo, které chcete násobit: '))
        cislo5_dobre = cislo5 > 0
        cislo6_dobre = cislo6 > 0
        if (cislo6_dobre, cislo5_dobre):
            print('Součin čísel', cislo5, 'a', cislo6, 'je', cislo5 * cislo6)
    if arit_operace == '13':
        cislo7 = float(input('Zadej 1. číslo, které chcete dělit: '))
        cislo8 = float(input('Zadej 2. číslo, které chcete dělit: '))
        cislo7_dobre = cislo7 > 0
        cislo8_dobre = cislo8 > 0
        if (cislo7_dobre, cislo8_dobre):
            print('Podíl čísel', cislo7, 'a', cislo8, 'je', cislo7 / cislo8)
    if arit_operace == '14':
        cislo9 =  float(input('Zadej 1. číslo, které chcete umocňovat: '))
        cislo10 = float(input('Zadej 2. číslo, které chcete umocňovat: '))
        cislo9_dobre = cislo9 > 0
        cislo10_dobre = cislo10 > 0
        if (cislo9_dobre, cislo10_dobre):
            print('Výsledek umocnění', cislo9, 'a', cislo10, 'je', cislo9 ** cislo10)
    if arit_operace == '15':
        from math import sqrt
        cislo11 = float(input('Zadej 1. číslo, které chcete odmocňovat: '))
        cislo11_dobre = cislo11 > 0
        if cislo11_dobre:
            print('Odmocnina', cislo11, 'je', sqrt(cislo11))
print('Děkujeme za použítí kalkulačky. Pokud chcete počítat znovu, ukončete a spusťte program znovu.')
input('Zmáčkněte ENTER pro ukončení kalkulačky')
