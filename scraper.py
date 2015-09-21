import urllib.request
import pdb
import re
#f=urllib.request.urlopen("http://www.rw-co.com/en/womens-clothing-sales-tops")
#print (f.read())

"""SUPER OF SCRAPED OBJECT"""
class scrapedObject(object):
	"""Base class of a scraped object, will split further by company below
	"""
	def __init__(self):
		self.urlPrefix = ""
		self.urlList = []
		self.company=""
		self.typeOfItem=""
		self.gender=""
		self.items=[]
		self.urlSuffixList = []

	def getURL(self):
		return self.url

	def populate_URL_list(self):
		for suffix in self.urlSuffixList:
			self.urlList.append(self.urlPrefix + suffix)

	def append_to_suffix_list(self, specific_suffixes):
		for suffix in specific_suffixes:
			self.urlSuffixList.append(suffix)

"""SECTION FOR RW&CO"""

class RWCObject(scrapedObject):
	"""RW&Co object which is a specific type of scrapedObject
	"""
	def __init__(self):
		scrapedObject.__init__(self)
		self.urlPrefix += "http://www.rw-co.com/en/"
		self.company="RW&Co"
	
"""WOMEN"""

class RWCWomenTops(RWCObject):
	"""Women's tops from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="women"
		self.typeOfItem="top"
		self.specific_suffixes = ["womens-tops-blouses-tshirts-tanks-camis", "womens-sweaters"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCWomenBottoms(RWCObject):
	"""Women's bottoms from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="women"
		self.typeOfItem="bottom"
		self.specific_suffixes = ["women-pants", "womens-leggings", "womens-jeans-denim", "womens-skirts"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCWomenJackets(RWCObject):
	"""Women's jackets/coats from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="women"
		self.typeOfItem="jacket"
		self.specific_suffixes = ["womens-blazers-jackets", "womens-coats-winter-jackets"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()


class RWCWomenDresses(RWCObject):
	"""Women's dresses from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="women"
		self.typeOfItem="dress"
		self.specific_suffixes = ["womens-dresses"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCWomenShoesAccessories(RWCObject):
	"""Women's shoes and accessories from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="women"
		self.typeOfItem="shoe-accessory"
		self.specific_suffixes = ["womens-shoes-boots", "womens-accessories"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

"""MEN"""

class RWCMenTops(RWCObject):
	"""Men's tops from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="men"
		self.typeOfItem="top"
		self.specific_suffixes = ["mens-dress-shirts", "mens-casual-shirts", "mens-t-shirts", "mens-sweaters"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCMenBottoms(RWCObject):
	"""Men's bottoms from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="men"
		self.typeOfItem="bottom"
		self.specific_suffixes = ["mens-pants-dress-casual", "mens-jeans-denim"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCMenSuits(RWCObject):
	"""Men's suits from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="men"
		self.typeOfItem="suit"
		self.specific_suffixes = ["mens-suits-regular-short-tall"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

class RWCMenJackets(RWCObject):
	"""Men's suits from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="men"
		self.typeOfItem="jacket"
		self.specific_suffixes = ["mens-jackets-blazers-vests", "mens-coats-winter"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()


class RWCMenShoesAccessories(RWCObject):
	"""Men's shoes & accessories from RW&Co
	"""
	def __init__(self):
		RWCObject.__init__(self)
		self.gender="men"
		self.typeOfItem="shoe-accessory"
		self.specific_suffixes = ["men-shoes-boots", "mens-accessories"]
		self.append_to_suffix_list(self.specific_suffixes)
		self.populate_URL_list()

"""SINGLE ITEM"""

class singleItem(object):
	"""Class for a single item that was scraped
	"""
	def __init__(self):
		self.salePrice=""
		self.originalPrice=""
		self.name=""
		self.imgUrl=""

#Contains a list of all the objects we need to create for RW&Co
AllClasses_RWC = [RWCWomenTops, RWCWomenBottoms, RWCWomenJackets, RWCWomenDresses,
 RWCWomenShoesAccessories, RWCMenTops, RWCMenBottoms, RWCMenSuits, RWCMenJackets, RWCMenShoesAccessories]
newTop = AllClasses_RWC[0]()
pdb.set_trace()

#(class="product-tile"(?s).*?<img src="(.*?)"(?s).*<a class="name-link".*?>((?s).*?)</a>)?