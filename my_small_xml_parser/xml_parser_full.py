from lxml import etree as et

# Выбираем файл и получаем дерево
tree = et.parse('mebel.xml')
root = tree.getroot()
# Создаем файл для записи инфрмации и записываем корневой тег
file_output = open('TEST___0001.txt', 'w')
file_output.writelines('##############\n')
file_output.writelines(root.tag + '\n')
file_output.writelines('===============\n')

# Обрабатываем первый уровень дерева
for item in root:
    if item.tag == '{urn:1C.ru:commerceml_2}Каталог':
        new = item

# Обрабатываем второй путь дерева
for item in new:
    if item.tag == '{urn:1C.ru:commerceml_2}Товары':
        child = item

# После нахождения уровня "Товар" ищем в нем необходимую информацию
# И записываем полученный результат в файл
for item in child:
    for alfa in item:
        if alfa.tag == '{urn:1C.ru:commerceml_2}Наименование':
            file_output.writelines('\n')
            file_output.writelines('\n')
            stroka = str('name:\t' + str(alfa.text) + str(alfa.attrib) + '\n')
            file_output.writelines(stroka)
        if alfa.tag == '{urn:1C.ru:commerceml_2}Картинка':
            stroka = str('path:\t' + str(alfa.text) + str(alfa.attrib) + '\n')
            file_output.writelines(stroka)

file_output.close()
