from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()   # start a session to the database
myFirstRestaurant = Restaurant(name="Pizza Palace")  # create a new restaurant entry
session.add(myFirstRestaurant)   # Add the newly created entry
session.commit()  # Commit the changes made so far to the database

print session.query(Restaurant).all()  # Print Restaurant objects

cheezepizza = MenuItem(name="Cheeze pizza",
                       description = "Made with all natural ingredients",
                       course = "Entree",
                       price = "$8.99",
                       restaurant = myFirstRestaurant
                       )
session.add(cheezepizza)
session.commit()

print session.query(MenuItem).all()

##############################################################################
firstResult = session.query(Restaurant).first()
print firstResult.name