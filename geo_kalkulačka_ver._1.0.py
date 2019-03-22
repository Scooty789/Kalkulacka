# Univerzální geo kalkulačka verze 1.0
print('Geomterická kalkulačka verze 1.0 by Scooty789')
print('VAROVÁNÍ! Tato verze NEPODPORUJE záporná čísla!')
print('Tvary a funkce se zadávají pomocí čísel!')
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
    elif operace == '6':
                        aa = float(input('Zadej stranu trojúhelníku a v cm: '))
                        va = float(input('Zadej výšku trojúhleníku va v cm: '))
                        aa_dobre = aa > 0
                        va_dobre = va > 0
                        if (aa_dobre, va_dobre):
                            print('Obsah trojúhelníku se stranou a', aa,'cm a výškou va', va, 'cm je', aa * va / 2, 'cm2')
                        else:
                                print('Zadejte kladnou hodnotu výšky a + strany a')
    else: print('Jiné funkce kalkulačka zatím nepodporuje')
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
    elif operace == '6':
                ao = float(input('Zadej stranu čtverce a v cm: '))
                ao_dobre = ao > 0
                if ao_dobre:
                    print('Obsah čtverce se stranou', ao, 'cm je', ao * ao, 'cm2')
                else:
                        print('Zadejte kladnou hodnotu strany a')
    else: print('Jiné funkce kalkulačka zatím nepodporuje')
elif odpoved == '3': # obdélník
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
    else: print('Jiné funkce kalkulačka zatím nepodporuje')
elif odpoved == '4':
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
print('Děkujeme za použítí kalkulačky. Pokud chcete počítat znovu, ukončete a spusťte program znovu.')
input('Zmáčkněte ENTER pro ukončení kalkulačky')
