## -*- coding: utf-8 -*-
import json
from lxml import etree as ET
import os
import random
import datetime

from src.texts import Text
from src.img import Img
from src.address import Address
from src.characteristics import Characteristics
from src.prices import Price
from src.titles import Title
from src.color import Color
from src.doors_material import DoorsMaterial

# нужную из кампаний переместите на последнюю позицию
# т.е. в таком варианте генерация будет для stolishnici
# скрипт будет брать заголовки, тексты и фото из соответсвующего каталога
company = 'kitchen'
# -----------------------------------------------------


#------------- кол-во объявлений -----------------------------------
AD_COUNT_M = 1  #кол-во объявлений  по москве
AD_COUNT_MO = 1  #кол-во объявлений по мос. обл.
# -------------------------------------------------------------------

ARTICUL_PART = 'may-' # префикс артикула
AD_START_ID = 100000 # стартовое значение числовой части артикула

#  общие настройки генерации для данной кампании (номер тлф., фио менеджера и т.д.)
COMMON_JSON_FILE = f'company/{company}/common_data.json'
# файл результирующиего xml-фида
RESULT_FEED_NAME = f'company/{company}/feeds/{datetime.datetime.now().strftime("%Y-%m-%d").replace("-", "_")}.xml'

# постоянная часть ссылки на фото (используется только если вы будут размещать фото на своем хостинге)
# если фото будете хранить на imgbb.com То данную настройку можно не трогать (она в скрипте не будет использована)
BASE_IMG_URL = '' #f'https://biopoten-store.ru/avito/{company}/img/'

# данный флаг определяет место хранения фото
# True  - изображения берем из готового файла со списком url
# False - изображения берем из локальных каталогов и после генерации грузим на свой хостинг,
# так же в этом случае будет использован параметр BASE_IMG_URL (см. выше)
IMG_URLS_FLAG = True

def load_json_data(file):
    try:
        if os.path.isfile(file) is False:
            print(f'Файл {file} не обнаружен.')
            return []
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print('load_json exception:', e)
        return []

def create_avito_feed(common_ad_list, common_data):
    '''
    основная функция генерации xml
    :param ad_list:
    :param common_data:
    :return:
    '''
    root = ET.Element('Ads', formatVersion="3", target="avito.ru")
    etree = ET.ElementTree(root)
    color = Color()
    doors_material = DoorsMaterial()

    for index, ad in enumerate(common_ad_list):
        Id = ET.Element('Id')
        AdStatus = ET.Element('AdStatus')
        AllowEmail = ET.Element('AllowEmail')
        AdType = ET.Element('AdType')
        ManagerName = ET.Element('ManagerName')
        ContactPhone = ET.Element('ContactPhone')
        Address = ET.Element('Address')
        Category = ET.Element('Category')
        GoodsType = ET.Element('GoodsType')
        GoodsSubType = ET.Element('GoodsSubType')
        ComponentsType = ET.Element('ComponentsType')
        Condition = ET.Element('Condition')
        Availability = ET.Element('Availability')

        DoorsMaterial_ = ET.Element('DoorsMaterial')
        Color_ = ET.Element('Color')
        KitchenShape = ET.Element('KitchenShape')
        Width = ET.Element('Width')
        Height = ET.Element('Height')
        DepthByWorktop = ET.Element('DepthByWorktop')
        DepthByCorner = ET.Element('DepthByCorner')
        WorktopIncluded = ET.Element('WorktopIncluded')
        TabletopMaterial = ET.Element('TabletopMaterial')
        FurnitureAdditions = ET.Element('FurnitureAdditions')
        PriceType = ET.Element('PriceType')

        Title = ET.Element('Title')
        Price = ET.Element('Price')
        Description = ET.Element('Description')
        Image1 = ET.Element('Image')
        Image2 = ET.Element('Image')
        Image3 = ET.Element('Image')
        Image4 = ET.Element('Image')
        Image5 = ET.Element('Image')
        Image6 = ET.Element('Image')
        Image7 = ET.Element('Image')
        Image8 = ET.Element('Image')
        Image9 = ET.Element('Image')
        Image10 = ET.Element('Image')


        Id.text = ad['Id']
        AdStatus.text = common_data['AdStatus']
        AllowEmail.text = common_data['AllowEmail']
        AdType.text = common_data['AdType']
        ManagerName.text = common_data['ManagerName']
        ContactPhone.text = common_data['ContactPhone']
        Address.text = ad['Address']
        Category.text = common_data['Category']
        GoodsType.text = common_data['GoodsType']
        GoodsSubType.text = common_data['GoodsSubType']
        ComponentsType.text = 'Столешницы'


        Condition.text = common_data['Condition']
        Availability.text = 'Под заказ'
        Title.text = ad['name']
        Price.text = ad['Price']

        Color_.text = color.get_random()
        DoorsMaterial_.text = doors_material.get_random()
        KitchenShape.text = random.choice(['Прямая', 'Угловая', 'Другая'])
        Width.text = '200'
        Height.text = '220'
        DepthByWorktop.text = '60'
        DepthByCorner.text = '150'
        WorktopIncluded.text = 'Есть'
        TabletopMaterial.text = random.choice([
            'ДСП', 'ЛДСП', 'МДФ', 'Дерево', 'Пластик'
            ])

        FurnitureOption1 = ET.Element('Option')
        FurnitureOption2 = ET.Element('Option')
        FurnitureOption3 = ET.Element('Option')
        FurnitureOption4 = ET.Element('Option')
        FurnitureOption5 = ET.Element('Option')
        FurnitureOption6 = ET.Element('Option')

        FurnitureOption1.set('Option', 'Шкаф под мойку')
        FurnitureOption2.set('Option', 'Шкаф под духовку')
        FurnitureOption3.set('Option', 'Шкаф с ящиками')
        FurnitureOption4.set('Option', 'Пенал')
        FurnitureOption5.set('Option', 'Навесные шкафы')
        FurnitureOption6.set('Option', 'Навесной шкаф под вытяжку')

        FurnitureAdditions = ET.Element('FurnitureAdditions')
        FurnitureAdditions.append(FurnitureOption1)
        FurnitureAdditions.append(FurnitureOption2)
        FurnitureAdditions.append(FurnitureOption3)
        FurnitureAdditions.append(FurnitureOption4)
        FurnitureAdditions.append(FurnitureOption5)
        FurnitureAdditions.append(FurnitureOption6)

        PriceType.text = 'за погонный метр'

        Image1.set('url', ad['Image1'].strip())
        Image2.set('url', ad['Image2'].strip())
        Image3.set('url', ad['Image3'].strip())
        Image4.set('url', ad['Image4'].strip())
        Image5.set('url', ad['Image5'].strip())
        Image6.set('url', ad['Image6'].strip())
        Image7.set('url', ad['Image7'].strip())
        Image8.set('url', ad['Image8'].strip())
        Image9.set('url', ad['Image9'].strip())
        Image10.set('url', ad['Image10'].strip())

        Images = ET.Element('Images')
        Images.append(Image1)
        Images.append(Image2)
        Images.append(Image3)
        Images.append(Image4)
        Images.append(Image5)
        Images.append(Image6)
        Images.append(Image7)
        Images.append(Image8)
        Images.append(Image9)
        Images.append(Image10)

        ad_description = ad['description'] + f"{ad['Articul']}\n"
        # ad_description = update_article(ad_description, ad['Articul'])
        Description.text = ET.CDATA(ad_description)

        offer = ET.Element('Ad')
        offer.append(Id)
        offer.append(AdStatus)
        offer.append(AllowEmail)
        offer.append(AdType)
        offer.append(ManagerName)
        offer.append(ContactPhone)
        offer.append(Address)
        offer.append(Category)
        offer.append(GoodsType)
        offer.append(GoodsSubType)
        offer.append(Condition)
        offer.append(Availability)
        offer.append(Title)
        offer.append(Price)
        offer.append(Description)
        offer.append(Images)
        offer.append(Color_)

        offer.append(DoorsMaterial_)
        offer.append(KitchenShape)
        offer.append(Width)
        offer.append(Height)
        offer.append(DepthByWorktop)
        offer.append(DepthByCorner)
        offer.append(WorktopIncluded)
        offer.append(TabletopMaterial)
        offer.append(FurnitureAdditions)
        offer.append(PriceType)

        root.append(offer)

    myfile = open(RESULT_FEED_NAME, "wb")
    etree.write(myfile, encoding='utf-8', xml_declaration=True, pretty_print=True)



def write_stat(common_ad_list_count):
    with open(f'log.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + '*'*25)
        f.write(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d')}] Компания: '{company}':")
        f.write(f"\nвсего объявлений: {common_ad_list_count}")
        f.write(f"\nкухонные гарнитуры (Москва): {AD_COUNT_M}")
        f.write(f"\nкухонные гарнитуры (Мос.обл.): {AD_COUNT_MO}")

        print(f"Компания: '{company}':")
        print("всего объявлений:", common_ad_list_count)
        print("кухонные гарнитуры (Москва):", AD_COUNT_M)
        print("кухонные гарнитуры (Мос.обл.):", AD_COUNT_MO)


def union_lists(list1: list, list2: list) -> list:
    """
    Объединение списков с равномерным распределением элементов внутри них.
    Предусмотрен вариант, когда один из списков пустой.

    :param list1: Первый список.
    :param list2: Второй список.
    :return: Объединенный список.
    """
    res_list = []

    if not list1:
        return list2[:]  # Возвращаем копию list2, чтобы не менять исходный список
    if not list2:
        return list1[:]  # Возвращаем копию list1, чтобы не менять исходный список

    big_list = []
    small_list = []

    if len(list1) > len(list2):
        big_list = list1
        small_list = list2
        proportion = len(list1) // len(list2)  # Целочисленное деление
    else:
        big_list = list2
        small_list = list1
        proportion = len(list2) // len(list1)  # Целочисленное деление

    big_list_elements_counter = 0
    small_list_index = 0

    for item in big_list:
        res_list.append(item)
        big_list_elements_counter += 1
        if small_list_index < len(small_list) and big_list_elements_counter == proportion:
            res_list.append(small_list[small_list_index])
            small_list_index += 1
            big_list_elements_counter = 0

    # Добавляем оставшиеся элементы из small_list, если они есть
    while small_list_index < len(small_list):
         res_list.append(small_list[small_list_index])
         small_list_index += 1

    return res_list


def clean_txt_file(input_file, output_file):
    """
    Читает текстовый файл, удаляет HTML-сущности
 из каждой строки
    и сохраняет очищенный текст в новый файл.

    Args:
        input_file (str): Путь к входному текстовому файлу.
        output_file (str): Путь к выходному текстовому файлу.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                cleaned_line = line.replace('', '')
                outfile.write(cleaned_line)

        print(f"Файл '{input_file}' успешно очищен и сохранен в '{output_file}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    common_data = load_json_data(COMMON_JSON_FILE)  # общие параметры
    text = Text(company_name=company, products=['kitchen'])
    img = Img(company_name=company, products=['kitchen'], img_count=10)
    address = Address(company_name=company)
    characteristics = Characteristics('colors.txt')
    price = Price()
    title = Title()
    characteristics = Characteristics('colors.txt')

    common_MO_ad_list = []  # общий список объявлений по области
    common_Moskow_ad_list = []  # общий список объявлений по Москве

    for index in range(AD_COUNT_MO):
        common_MO_ad_list.append(
            {
                'product': 'kitchen',
                'name': title.get_kitchen_title(),
                'Address': address.get_MO_address()
                }
        )

    for index in range(AD_COUNT_M):
        common_Moskow_ad_list.append(
            {
                'product': 'kitchen',
                'name': title.get_kitchen_title(),
                'Address': address.get_moskow_address()
                }
        )


# -----------------------------------------------------------------------------------------------------------------

    moskow_ad_list = []
    add_index = 1
    for ad in common_Moskow_ad_list:
        product = ad['product']
        ad['Price'] = str(price.get_price(product))
        ad['Articul'] = '\nАртикул:' + ARTICUL_PART + str(index + AD_START_ID)
        ad['Id'] = str(index + AD_START_ID)
        ad['Image1'] = BASE_IMG_URL + img.get_url(product, 1)
        ad['Image2'] = BASE_IMG_URL + img.get_url(product, 2)
        ad['Image3'] = BASE_IMG_URL + img.get_url(product, 3)
        ad['Image4'] = BASE_IMG_URL + img.get_url(product, 4)
        ad['Image5'] = BASE_IMG_URL + img.get_url(product, 5)
        ad['Image6'] = BASE_IMG_URL + img.get_url(product, 6)
        ad['Image7'] = BASE_IMG_URL + img.get_url(product, 7)
        ad['Image8'] = BASE_IMG_URL + img.get_url(product, 8)
        ad['Image9'] = BASE_IMG_URL + img.get_url(product, 9)
        ad['Image10'] = BASE_IMG_URL + img.get_url(product, 10)
        ad['description'] = text.get_text(product).replace('{HEADER}', ad['name'])
        ad['Id'] = str(add_index + AD_START_ID)
        add_index += 1
        moskow_ad_list.append(ad.copy())

    MO_ad_list = []

    for ad in common_MO_ad_list:
        product = ad['product']
        ad['Price'] = str(price.get_price(product))
        ad['Articul'] = '\nАртикул:' + ARTICUL_PART + str(index + AD_START_ID)
        ad['Id'] = str(index + AD_START_ID)
        ad['Image1'] = BASE_IMG_URL + img.get_url(product, 1)
        ad['Image2'] = BASE_IMG_URL + img.get_url(product, 2)
        ad['Image3'] = BASE_IMG_URL + img.get_url(product, 3)
        ad['Image4'] = BASE_IMG_URL + img.get_url(product, 4)
        ad['Image5'] = BASE_IMG_URL + img.get_url(product, 5)
        ad['Image6'] = BASE_IMG_URL + img.get_url(product, 6)
        ad['Image7'] = BASE_IMG_URL + img.get_url(product, 7)
        ad['Image8'] = BASE_IMG_URL + img.get_url(product, 8)
        ad['Image9'] = BASE_IMG_URL + img.get_url(product, 9)
        ad['Image10'] = BASE_IMG_URL + img.get_url(product, 10)
        ad['description'] = text.get_text(product).replace('{HEADER}', ad['name'])
        ad['Id'] = str(add_index + AD_START_ID)
        add_index += 1
        MO_ad_list.append(ad.copy())

    # перемешиваем
    random.shuffle(moskow_ad_list)
    random.shuffle(MO_ad_list)

    #----- делаем равномерное распределение объявлений
    common_ad_list = union_lists(moskow_ad_list, MO_ad_list)


    # генерируем feed
    create_avito_feed(common_ad_list, common_data)
    write_stat(len(common_ad_list))
