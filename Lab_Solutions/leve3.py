
import binascii


def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


# -------------------------------------------------------------------------
n = 0xCC69BA3A0AE695FE0E48F0D0E67508883009791F701DD85C7BB9B7369AC4DD042A82076B2BF8AD425A9F471A933FCB850F3BAF2C21E4881224597881F6E631E2754FFB2E436F4A7C700E39DD7736C2FA583BC9BFEA7DD5164010CB322CEEF4ABEFB2AA5723EF4734A7F4E0239FD14483567B4C499C6E47D3A37F52D6EAD305A4D3BDF7F050B21A12EFD059C5459F08CF02D55DD2FC1B82F4CC22AD3D8E2050FB28BF00CF1BA9F3CF1BED9754E0E4E347F8A695F92119E08E3C91FB699768AF7985CBFF10734E49790719FBDA25F2D26CCB422AF55C3E26A31199108ABABD3C3FFD54DF22033DF43E8039A24E4D511858F2F794FAB4C5A191B760793B37A7E18F
e = 0x010001
d = 0xCA81DBCA70CE2BBE7B2C6BD6A8D93CD09EB663D66F5E41E0AD7A3935D172427B4419797C051DE197A0EBB6A76F457E3C9DF0C503F5B7CFCE1950C2000F37D227C58CAD0D122589276A63CD93C7ECEA90D524B624790C9C33E4D83E55C10A223ECBC2B6DA89711D9BDEE0CBC4BF29B4B460D2D9AAFB5C8DAFEF83CDEFB8C7C207D9B3EF6BDEB691A15D0F73451E30F3D5E37C46881B6F34BCF2F776667623662A957A5CE80820C9B749A6E27F48D5E184A991136F12AC6F3FCAFCBE3497B29205B9457B839C12C90F92A534037197A972D472984CDE92EED3F40500D3A2A21AA588DC29DC40B283AF51877A86B766A868036EF2385C867800C7D02231EBF2CE11
p = 170436857437540785902894247445629309884819493988198726337160363787266132388801445377172350883259146330710518633323153950488107255453274647690833952071079266615535462115718628529996080297946386916054952930963525522668498855400580516951309863503734146131687670337990358661269686138903141878297721385390421204703
q = 137978932017559751745702136624874154954496829862527332457067512249687998333117572719846957168595861866495967632464915097378576596911015571165340454225721218087595428364080801400548238088288742249145662369868461078198744980520572785232341389134600070345564258064842348774203427257497319140459851255774165194699

# print(n)
# print(e)
# print(d)
m = 52544240263489213319521825334419419391168959946460651046808951093331580864925337576823646249202867381357303129957
print(int2string(m))