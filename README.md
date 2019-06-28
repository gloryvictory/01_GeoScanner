# 01_GeoScanner
`01_GeoScanner` is a recursive file lister (SHP Files, MIF/MID, GDB, etc...).

# Why
There are not any tools for this task.

# License - MIT

Версия документа: 1.0

Год: 2019

Имя проекта – MyGeo (01_GeoScanner - индексатор)

Автор: Замараев Вячеслав (постановка задачи), Поспелов Виталий (Django-разработка)

# Цель проекта
Получить точную и исчерпывающую информацию о существовании и использовании пространственных данных внутри компании. 

# Основная идея
Просканировать всю файловую систему (на Windows машинах - все диски) и создать файл с с набором критериев, затем этот файл анализировать и встраивать функции работы с пространственными данными (загрузка в центральное хранилище или в PostgreSQL+PostGIS)
На этапе анализа будут участвовать слудующие типы данных: 
Пространственные данные (по расширениям):

Вектор: shp, shx, dbf, prj, cbn, xml, MIF, MID, tab, kml, kmz, gps, map

Растр: tif, tiff, jpg, jpeg, geotiff

# Модуль индексатора "01_GeoScanner"
Может быть написан на любом языке программирования: PowerShell, Go, Python, C#
Алгоритм:
1) Получает имя машины (компьютера) 
2) Пробегает по каждому диску в операционной системе и формирует список файлов и его атрибутов (полный путь, размер, дата создания)
3) Формирует CSV файл, имя которого состоит из: ИмяМашины_Диск.csv (например CompZamaraev_c.csv)
4) Все значения могут (но не обязательно) обрамляться в кавычки «”» 

Пример: DESKTOP-NBV0BJF_C.csv, где DESKTOP-NBV0BJF – имя машины, а С – имя диска 
На выходе:   ИмяМашины_Диск.csv
Имена полей: "$compname";"FullName";"Length";"CreationTime";"ModifiedTime";"AccessTime"
Пример файла (DESKTOP-NBV0BJF_C.csv): 
"$compname";"FullName";"Length";"CreationTime";"ModifiedTime";"AccessTime"
"DESKTOP-NBV0BJF";"C:\$compname.csv";"916144";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01"
"DESKTOP-NBV0BJF";"C:\01_GeoScanner\01_GeoScanner.log";"5361";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01"
"DESKTOP-NBV0BJF";"C:\01_GeoScanner\exclusions.txt";"50";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01";"916144";"05.03.2019 19:47:01"

Получается таблица:

|$compname|FullName|Length|CreationTime|ModifiedTime|AccessTime
|---------|--------|------|------------|------------|------------|
|---------|--------|------|------------|------------|------------|

