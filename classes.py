import math
from enum import Enum

file = open("tavolsagok.txt", "w+")


def beolvas():
    file2 = open("beadando.txt", 'r+', encoding='utf8')
    varos = []
    for i in file2:
        adat = []
        i = i.strip().split("   ")
        for x in range(len(i)):
            if x == 3 or x == 4:
                adat.append(float(i[x]))
            elif x == 5:
                if "/" in i[x]:
                    i[x] = i[x].split("/")
                    ido = (int(i[x][0]), int(i[x][1]))
                else:
                    ido = int(i[x])
                adat.append(ido)
            elif x == 6:
                adat.append(int(i[x]))
            else:
                adat.append(str(i[x]))
        varos.append(adat)
    return varos


class vehicle(Enum):
    start = "Kezdőváros"
    car = "Autó"
    plane = "Repülőgép"
    car_or_plane = "Autó vagy repülőgép"


def rad_convert(deg) -> float:
    return deg / 180 * math.pi


class Varos:
    def __init__(self, nev: str, lat: float, lon: float, travel_time: int, transport: int):
        self.nev = nev
        self.lat = lat
        self.lon = lon
        self.travel_time = travel_time
        self.transport = transport

    def tavolsag(self) -> float:
        r = 6367
        lat1 = rad_convert(Pécs.lat)
        lon1 = rad_convert(Pécs.lon)
        lat2 = rad_convert(self.lat)
        lon2 = rad_convert(self.lon)
        dist = round(2 * r * math.asin(math.sqrt(
            (math.sin((lat2 - lat1) / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) * (math.sin((lon2 - lon1) / 2)) ** 2)),
                     6)
        return dist

    def mile_convert(self) -> float:
        return self.tavolsag() * 0.62137119

    def ido_calc(self):
        if self.transport == "Autó":
            time = self.travel_time
            days = time // 60 // 24
            hours = time // 60 % 24
            minutes = time % 60
            print("Utazási idő: %d:%d:%d" % (days, hours, minutes))
            return [days, hours, minutes]
        else:
            print("Kiindulási hely, nincs utazási idő")
            return 0

    def file_write_tavolsag_km(self):
        print("Távolság:\n\t%f km" % self.tavolsag())
        file.write("\n\tPécs - %s: \n\t%f km" % (self.nev, self.tavolsag()))

    def file_write_tavolsag_mi(self):
        print("Távolság:\n\t%f mérföld" % self.mile_convert())
        file.write("\n\tPécs - %s:\n\t%f mérföld" % (self.nev, self.mile_convert()))

    def file_write_time(self):
        ido = self.ido_calc()
        print(self.nev)
        file.write(self.nev)
        if self.nev == "Pécs":
            file.write("\n")
            return 0
        file.write("\n\t\tUtazási idő: %d:%d:%d\n\t" % (ido[0], ido[1], ido[2]))


class Europai_varos(Varos):
    def __init__(self, nev: str, country: str, lat: float, lon: float, travel_time: int, transport: int):
        super().__init__(nev, lat, lon, travel_time, transport)
        self.country = country

    def melyik_orszag(self):
        print(self.country)
        return self.country

    def ido_calc(self):
        if self.transport == "Autó":
            time = self.travel_time
            days = time // 60 // 24
            hours = time // 60 % 24
            minutes = time % 60
            print("Utazási idő: %d:%d:%d" % (days, hours, minutes))
            return [days, hours, minutes]
        else:
            time_plane = self.travel_time[0]
            time_car = self.travel_time[1]
            plane_days = time_plane // 60 // 24
            plane_hours = time_plane // 60 % 24
            plane_minutes = time_plane % 60
            car_days = time_car // 60 // 24
            car_hours = time_car // 60 % 24
            car_minutes = time_car % 60
            return [plane_days, plane_hours, plane_minutes, car_days, car_hours, car_minutes]

    def file_write_time(self):
        ido = self.ido_calc()
        file.write("%s\n\t"%self.nev)
        print(self.nev)
        file.write("Ország: %s" % self.melyik_orszag())

        if self.nev=="Bécs":
            print("Utazási idő: %d:%d:%d" % (ido[0], ido[1], ido[2]))
            file.write("\n\tUtazási idő: %d:%d:%d" % (ido[0], ido[1], ido[2]))
        else:
            print("Utazási idő: %d:%d:%d repülővel, %d:%d:%d autóval" % (ido[0], ido[1], ido[2], ido[3], ido[4], ido[5]))
            file.write("\n\t\tUtazási idő repülőgéppel: %d:%d:%d" % (ido[0], ido[1], ido[2]))
            file.write("\n\t\tUtazási idő autóval: %d:%d:%d" % (ido[3], ido[4], ido[5]))


class Masik_kontinens_varos(Europai_varos):
    def __init__(self, nev: str, country: str, continent: str, lat: float, lon: float,
                 travel_time: int, transport: int):
        super().__init__(nev, country, lat, lon, travel_time, transport)
        self.continent = continent

    def melyik_kontinens(self):
        print(self.continent)
        return self.continent

    def ido_calc(self):
        time = self.travel_time + Budapest.travel_time
        days = time // 60 // 24
        hours = time // 60 % 24
        minutes = time % 60
        return [days, hours, minutes]

    def file_write_time(self):
        ido = self.ido_calc()
        print(self.nev)
        file.write(self.nev)
        file.write("\n\tOrszág: %s \n\tKontinens: %s" % (self.melyik_orszag(), self.melyik_kontinens()))
        print("Utazási idő: %d:%d:%d" % (ido[0], ido[1], ido[2]))
        file.write("\n\t\tUtazási idő: %d:%d:%d" % (ido[0], ido[1], ido[2]))


def feltolt():
    for i in beolvas():
        if i[0] == "Pécs":
            globals()[i[0]] = Varos(i[0], i[3], i[4], i[5], vehicle.start.value)
        elif i[0] == "Budapest":
            globals()[i[0]] = Varos(i[0], i[3], i[4], i[5], vehicle.car.value)
        elif i[0] == "Bécs":
            globals()[i[0]] = Europai_varos(i[0], i[1], i[3], i[4], i[5], vehicle.car.value)
        elif i[2] == "-":
            globals()[i[0]] = Europai_varos(i[0], i[1], i[3], i[4], i[5], vehicle.car_or_plane.value)
        else:
            globals()[i[0]] = Masik_kontinens_varos(i[0], i[1], i[2], i[3], i[4], i[5], vehicle.plane.value)


def beker():
    mertek = input("Kérek egy mértékegységet (km/mi): ")
    if mertek in ["km", "mi"]:
        varos = input("Kérek egy városnevet: ")
        if mertek == "mi":
            try:
                globals()[varos].file_write_time()
                globals()[varos].file_write_tavolsag_mi()
            except(KeyError):
                print("Nincs ilyen város a listában")
                beker()
        if mertek == "km":
            try:
                globals()[varos].file_write_time()
                globals()[varos].file_write_tavolsag_km()
            except(KeyError):
                print("Nincs ilyen város a listában")
                beker()
    else:
        print("Csak kilométert és mérföldet fogadok el")
        beker()


if __name__ == '__main__':
    feltolt()
    beker()
    file.close()
