from server_app import db
from database.models import Offer, Category
db.drop_all()
db.create_all()
c = ['общепит', 'магазины', 'услуги', 'мероприятия', 'администрация', 'транспорт', 'образование', 'развлечения', 'спорт']
d = {c.index(name): Category(name) for name in c}
for numb in d:
    db.session.add(d[numb])

db.session.add(Offer('ПМ-ПУ',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ|9:00-15:00|12:50-13:50\nВС',
                     c[6],
                     'Факультет Прикладной Математики - Процессов Управления',
                     {'lat': 29.8305631, 'lng': 59.8821827},
                     'https://apmath.spbu.ru',
                     'пм вуз факультет'))
db.session.add(Offer('К-Руока',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-00:00|\n',
                     c[1],
                     'Финский супермаркет',
                     {'lat': 29.8258102, 'lng': 59.8694873},
                     'http://www.k-ruoka.ru/',
                     'магазин продукты супермаркет финский бухло еда'))
db.session.add(Offer('Говно с дымом',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-00:00|\n',
                     c[1],
                     'Плюхи у Илюхи',
                     {'lat': 29.828242, 'lng': 59.8741827},
                     'http://fbi.com',
                     'бухло кальян содомия современное искусство vape'))
db.session.add(Offer('Банкомат Сбербанк',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-00:00|\n',
                     c[2],
                     'Банкомат',
                     {'lat': 29.827311, 'lng': 59.8737107},
                     'https://sberbank.ru',
                     'банкомат сбербанк безнал снять деньги карта'))

db.session.add(Offer('Герард Миллер',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|10:00-22:00|',
                     c[0],
                     'вкусная шавуха',
                     {'lng': 59.8748755, 'lat': 29.8265393},
                     '',
                     'шаверма шавуха еда пицца поесть кафе столовая паста'))

db.session.add(Offer('Сластёна',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|10:00-22:00|',
                     c[0],
                     'обычная столовая',
                     {'lng': 59.874810, 'lat': 29.830243},
                     '',
                     'столовая кафе покушать еда'))
db.session.add(Offer('Мавзол',
                     'ПН,ВТ,СР,ЧТ,ПТ|10:00-22:00|',
                     c[0],
                     'столовая',
                     {'lng': 59.880414, 'lat': 29.824533},
                     '',
                     'столовая кафе покушать еда'))

db.session.add(Offer('Универсам Андреевский',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-24:00|',
                     c[1],
                     'круглосуточный магазин',
                     {'lng': 59.874869, 'lat': 29.827153},
                     '',
                     'магазин покушать еда товары купить безнал'))
db.session.add(Offer('Универсам Семейный',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|10:00-22:00|',
                     c[1],
                     'магазин',
                     {'lng': 59.873840, 'lat': 29.829202},
                     '',
                     'магазин покушать еда товары купить'))

db.session.add(Offer('Банкомат Сбербанк',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|10:00-22:00|',
                     c[2],
                     'банкомат',
                     {'lng': 59.873840, 'lat': 29.829202},
                     '',
                     'деньги сбербанк сбер банкомат'))
db.session.add(Offer('Банкомат ВТБ 24',
                     'ПН,ВТ,СР,ЧТ,ПТ|10:00-17:00|',
                     c[2],
                     'отделение банка и банкомат',
                     {'lng': 59.879219, 'lat': 29.831249},
                     '',
                     'деньги втб банкомат втб24 банк'))
db.session.add(Offer('Банкомат ВТБ 24',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-24:00|',
                     c[2],
                     'банкомат',
                     {'lng': 59.874810, 'lat': 29.830243},
                     '',
                     'деньги втб банкомат втб24'))


db.session.add(Offer('Прачечная',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|10:00-02:00|',
                     c[2],
                     'Прачечная',
                     {'lng': 59.875613, 'lat': 29.825814},
                     '',
                     'стирка стирать'))
db.session.add(Offer('Waterpunk',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-24:00|',
                     c[2],
                     'Продажа питьевой воды с доставкой до комнаты',
                     {'lng': 59.8748295, 'lat': 29.8266665},
                     '',
                     'вода питьевая'))
db.session.add(Offer('Punkprint',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|00:00-24:00|',
                     c[2],
                     'Печать документов',
                     {'lng': 59.8748295, 'lat': 29.8266665},
                     '',
                     'печать документы фото бумага'))
db.session.add(Offer('Бильярд',
                     'ПН,ВТ,СР,ЧТ,ПТ,СБ,ВС|12:00-20:00|',
                     c[8],
                     'Бильярдная',
                     {'lng': 59.876243, 'lat': 29.827793},
                     '',
                     'бильярд игра'))
db.session.add(Offer('Прокат велосипедов',
                     '',
                     c[2],
                     'Прокат велосипедов летом',
                     {'lng': 59.873368, 'lat': 29.827546},
                     '',
                     'велик велосипед прокат кататься'))


db.session.add(Offer('Администрация общежитий',
                     '',
                     c[4],
                     'Все, что связано с проживанием в ПУНКе.',
                     {'lng': 59.8748295, 'lat': 29.8266665},
                     '',
                     'общага администрация пропуск замена потеря'))
db.session.add(Offer('Касса оплаты',
                     'ПН,ВТ,СР,ЧТ,ПТ|12:00-17:00|',
                     c[4],
                     'Пункт оплаты проживания в общаге',
                     {'lng': 59.882462, 'lat': 29.823127},
                     '',
                     'общага оплата касса'))


db.session.commit()
