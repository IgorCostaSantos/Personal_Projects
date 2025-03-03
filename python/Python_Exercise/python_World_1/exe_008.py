m = int(input('uma distancia em métros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f"""
a médida de {m} corresponde á
\033[1;36;40m{km}km\033[m
\033[1;36;40m{hm}hm\033[m
\033[1;36;40m{dam}dam\033[m
\033[1;36;40m{dm}dm\033[m
\033[1;36;40m{cm}cm\033[m
\033[1;36;40m{mm}mm\033[m""")
