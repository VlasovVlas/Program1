day = int(input(''))
mp = 16637000000
mph = 38241
s = mp + day * 24 * mph
km = s * 1.60934
aemp = 149597870.7 * 0.621371
ae = s / aemp
print(s, "Миль")
print(km, "Километров")
print(ae, 'Астрономических единиц')
ekms = 299792458 / 1000
Smp = s - 16637000000                            #растояние от Земли
Skm = Smp * 1.60934
sec = (Skm / ekms) * 2
hour = sec / 60
print('Задержка связи', hour,'часов')