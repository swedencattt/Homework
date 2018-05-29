from datetime import datetime
from pony.orm import (Database, Required, Optional, Set, PrimaryKey, db_session)

db = Database()


class Product(db.Entity):
	"""Товар"""
	category = Required('Category')
	title = Required(str)
	description = Optional(str)
	unit = Required(str) # единица измерения
	price = Required(float)
	# amount = int # сколько товара в магазине
	# alt_categories = Set('Category')
	history = Set('ProductHistory')
	cart_item = Set('CartItem')
	order_item = Set('OrderItem')

class ProductHistory(db.Entity):
	product = Required('Product')
	created = Optional(datetime, default=datetime.now)
	price = Required(float)


class Category(db.Entity):
	"""Категория товара"""
	parent = Optional('Category')
	title = Required(str)
	products = Set('Product')
	seed = Set('Category')

class Customer(db.Entity):
	"""Покупатель"""
	email = Required(str)
	phone = Required(str)
	name = Required(str)
	addresses = Optional('Address')
	cart = Optional('Cart')
	order = Optional('Order')

class Address(db.Entity):
	"""Адрес"""
	customer = Required('Customer')
	country = Optional(str)
	city = Optional(str)
	street = Optional(str)
	zip_code = Optional(str) # индекс
	house = Optional(int)

class Cart(db.Entity):
	"""Корзина с товарами"""
	customer = Required('Customer') or None
	products = Set('CartItem')

class CartItem(db.Entity):
	"""Элемент корзины"""
	cart = Set('Cart')
	product = Required('Product')
	amount = Required(int) # 1 единица товара

class Order(db.Entity):
	"""Заказ"""
	customer = Required('Customer')
	created = Optional(datetime, default=datetime.now)
	products = Set('OrderItem')
	status = Optional('Status')

class Status(db.Entity):
	"""Статус"""
	name = str
	order = Required('Order')

class OrderItem(db.Entity):
	"""Товар (одна позиция) в заказе"""
	order = Required('Order')
	product = Required('Product')
	amount = Required(int) # 1 единица товара

class Menu:
	"""Меню"""
		

db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


with db_session:
	cat1 = Category(title='car_goods_parts')
	cat2 = Category(title='car_goods_oil')
	cat3 = Category(title='car_goods_chemistry')
	cat4 = Category(title='car_goods_accessories')
	prod1 = Product(category=cat1, title='break_pads', unit='thing', price='999')
	prod2 = Product(category=cat1, title='tire', unit='thing', price='2500')
	prod3 = Product(category=cat1, title='clutch', unit='thing', price='3200')
	prod4 = Product(category=cat2, title='engine_oil', unit='liter', price='650')
	prod5 = Product(category=cat2, title='gear_oil', unit='liter', price='500')
	prod6 = Product(category=cat3, title='antifreeze', unit='liter', price='450')
	prod7 = Product(category=cat3, title='fuel_additive', unit='liter', price='999')
	prod8 = Product(category=cat4, title='car_mat', unit='thing', price='390')
	prod9 = Product(category=cat4, title='car_flavor', unit='thing', price='130')
	
