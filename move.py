infsp = int(input("Inf SP "))
cavsp = int(input("Cav SP "))
elesp = int(input("Ele SP "))
cavspadj = 2 * cavsp
sp = infsp + cavsp + elesp
adjsp = infsp + cavspadj + elesp

approv = int(input("AP province total")) #road #devast 
apmoun = 6 * int(input("# mountains"))
apmars = 3 * int(input("# marshes"))
aprivemi = int(input("# minor river crossings"))
aprivemo = 2 * int(input("# moderate river crossings"))
aprivema = 3 * int(input("# major river crossings"))

accap = approv + apmoun + apmars + aprivemi + aprivemo + aprivema

alp = 0

if 1 <= adjsp <= 10:
    if 1 <= accap <= 16:
        alp = 0
    if 17 <= accap <= 42:
        if sp == 1:
            alp = 0
        else:
            alp = 1
    if 43 <= accap:
        alp = 2
if 11 <= adjsp <= 25:
    if 1 <= accap <= 6:
        alp = 0
    if 7 <= accap <= 21:
        alp = 1
    if 22 <= accap <= 27:
        alp = 2
    if 28 <= accap <= 34:
        alp = 3
    if 35 <= accap <= 42:
        alp = 4
    if 43 <= accap:
        alp = 5
