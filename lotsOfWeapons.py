from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup_weapons import Categories, CategoryItem, Base


engine = create_engine('sqlite:///weaponsGuide.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Categories(name="GreatSwords")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Light Slicer", description="A Greatsword light enough to be held in one hand!",
                     picture="GreatSword01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Axes")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Tomahawk", description="Worned out Mohican styled axe. Saw hundreds of battles, is said to be haunted.",
                     picture="Axe01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Bows")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Short bow", description="Small, light and versatile, perfect for spies and thieves.",
                     picture="Bow01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Swords")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Crescent blade", description="A Sword crafted as a fase of the moon.",
                     picture="Sword01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Crossbows")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Piercer", description="A mean Crossbow, can pierce 3 men with one shot.",
                     picture="Crossbow01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Knifes")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Harpy Talon", description="Looks like the feet of a harpy, the handle can be used as a hammer.",
                     picture="Knife01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Maces")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Morning Star", description="Legendary mace made by angels, demon's bane!",
                     picture="Mace01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Shields")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Diamond Wall", description="The first shield given to a soldier joining the King Ozimandias army.",
                     picture="Shield01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Spears")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Spear", description="Common spear.",
                     picture="Spear01.png", categories=category1)

session.add(CatItem1)
session.commit()

category1 = Categories(name="Staffs")

session.add(category1)
session.commit()

CatItem1 = CategoryItem(name="Ancient Sapling Rod", description="Made 10000 year ago, still fresh as in the day it was made.",
                     picture="Staff01.png", categories=category1)

session.add(CatItem1)
session.commit()


print("added menu items!")
