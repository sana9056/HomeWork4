from xml.dom import minidom
import urllib.request


def currency_rates():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"  # задаем страницу для API
    webFile = urllib.request.urlopen(url)  # Выводим данные с запроса
    data = webFile.read()

    UrlSplit = url.split("/")[-1]  # чтобы дальше работать с документом переведем в формат xml
    ExtSplit = UrlSplit.split(".")[1]
    FileName = UrlSplit.replace(ExtSplit, "xml")

    with open(FileName, "wb") as localFile:
        localFile.write(data)
    webFile.close()
    # Запускаем парсер
    doc = minidom.parse(FileName)
    currency = doc.getElementsByTagName("Valute")
    # Задаю входные значения
    my_value = 0
    my_name = 0
    my_import_value = input("Введите наименование курса в международом формате типа 'USD':")
    # Прогоняю все значения до необходимого курса
    for rate in currency:
        my_val = rate.getElementsByTagName("CharCode")[0]
        my_val = my_val.firstChild.data
        name = rate.getElementsByTagName("Name")[0]
        name = name.firstChild.data
        value = rate.getElementsByTagName("Value")[0]
        value = value.firstChild.data
        # Если необходимый курс найден, то записываю значения в отдельные переменные и вывожу их
        if my_val == my_import_value:
            my_name = name
            my_value = value
    print(f'Курс {my_name} к Рублю РФ составляет: {my_value}')
    root = doc.getElementsByTagName("ValCurs")[0]
    date = "Текущий курс валют ЦБ РФ представлен на: {date}г. \n".format(date=root.getAttribute('Date'))
    print(date)
