from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from band_database_setup import Band, Base, AlbumItem, User

engine = create_engine('sqlite:///bandalbumswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Metal Hunger", email="hungry@metal.com",
             picture='http://thekatynews.com/wp-content/uploads/2016/08/HSO-ROLLING-STONES.jpg')
session.add(User1)
session.commit()

# Menu for UrbanBurger
band1 = Band(user_id=1, name="Urban Burger Band")

session.add(band1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.50", era="Peak", band=band1)

session.add(albumItem2)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="French Fries", description="with garlic and parmesan",
                     price="$2.99", era="Roots", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", era="Swan-Song", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", era="Peak", band=band1)

session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", era="Reformation", band=band1)

session.add(albumItem5)
session.commit()

albumItem6 = AlbumItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", era="Reformation", band=band1)

session.add(albumItem6)
session.commit()

albumItem7 = AlbumItem(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese", price="$3.49", era="Peak", band=band1)

session.add(albumItem7)
session.commit()

albumItem8 = AlbumItem(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", era="Peak", band=band1)

session.add(albumItem8)
session.commit()


# Menu for Super Stir Fry
band2 = Band(user_id=1, name="Super Stir Fry Band")

session.add(band2)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", era="Peak", band=band2)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", era="Peak", band=band2)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", era="Peak", band=band2)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", era="Peak", band=band2)

session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", era="Peak", band=band2)

session.add(albumItem5)
session.commit()

albumItem6 = AlbumItem(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", era="Peak", band=band2)

session.add(albumItem6)
session.commit()


# Menu for Panda Garden
band1 = Band(user_id=1, name="Panda Garden Band")

session.add(band1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", era="Peak", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", era="Roots", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     price="$9.95", era="Peak", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", era="Peak", band=band1)

session.add(albumItem4)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", era="Peak", band=band1)

session.add(albumItem2)
session.commit()


# Menu for Thyme for that
band1 = Band(user_id=1, name="Thyme for That Vegetarian Cuisine Band")

session.add(band1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", era="Swan-Song", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$4.50", era="Swan-Song", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", era="Roots", band=band1)

session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", era="Peak", band=band1)

session.add(albumItem5)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", era="Peak", band=band1)

session.add(albumItem2)
session.commit()


# Menu for Tony's Bistro
band1 = Band(user_id=1, name="Tony\'s Bistro Band")

session.add(band1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", era="Peak", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", era="Peak", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", era="Swan-Song", band=band1)

session.add(albumItem4)
session.commit()

albumItem5 = AlbumItem(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", era="Peak", band=band1)

session.add(albumItem5)
session.commit()


# Menu for Andala's
band1 = Band(user_id=1, name="Andala\'s Band")

session.add(band1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", era="Peak", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", era="Roots", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", era="Roots", band=band1)

session.add(albumItem4)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", era="Peak", band=band1)

session.add(albumItem2)
session.commit()


# Menu for Auntie Ann's
band1 = Band(user_id=1, name="Auntie Ann\'s Diner' Band")

session.add(band1)
session.commit()

albumItem9 = AlbumItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", era="Peak", band=band1)

session.add(albumItem9)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", era="Swan-Song", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem3 = AlbumItem(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", era="Roots", band=band1)

session.add(albumItem3)
session.commit()

albumItem4 = AlbumItem(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", era="Peak", band=band1)

session.add(albumItem4)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", era="Peak", band=band1)

session.add(albumItem2)
session.commit()

albumItem10 = AlbumItem(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", era="Swan-Song", band=band1)

session.add(albumItem10)
session.commit()


# Menu for Cocina Y Amor
band1 = Band(user_id=1, name="Cocina Y Amor Band")

session.add(band1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", era="Peak", band=band1)

session.add(albumItem1)
session.commit()

albumItem2 = AlbumItem(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", era="Peak", band=band1)

session.add(albumItem2)
session.commit()


band1 = Band(user_id=1, name="State Bird Provisions Band")
session.add(band1)
session.commit()

albumItem1 = AlbumItem(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", era="Roots", band=band1)

session.add(albumItem1)
session.commit

albumItem1 = AlbumItem(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95", era="Swan-Song", band=band1)

session.add(albumItem1)
session.commit()


albumItem1 = AlbumItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$4.25", era="Swan-Song", band=band1)

session.add(albumItem1)
session.commit()


print "added album items!"

