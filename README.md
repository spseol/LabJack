# LabJack

Toto je stručný návod k používání základních příkazů pro JabJack U3-HV...

I.  Naimportujeme knihovny
>>> import u3
>>> d=u3.U3()
Po případě nastavit všechny hodnoty na původní příkazem.
>>> d.config()


II. Základní příkazy
Nejjednodužší spůzob je pomocí zapisovnání registrů. Vystačí nám dvě funkce.
>>>d.writeRegister(...)
>>>d.readRegister(...)

Registry jsou čísla přiřazená k příkazům, které LabJack provede.
Př.:  Pro kontakt AIN0(Analog Input) je registr 0, chceme-li přečíst napětí tak
>>>d.readRegister(0)
Při použití read nám navrátí buď hodnotu kterou změří, nebo hodnotu která je na daném registru nastavena. U read zadáváme pouze číslo registru.

U funkce write píšeme první číslo registru a za něj hodnotu.
>>>d.writeRegister(5000,5)
Nastání DAC0 na 5V.


