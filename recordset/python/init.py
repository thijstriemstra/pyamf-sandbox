from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import model, db

def init_data():
    session = model.Session()

    data = [
        ("John","Smith","john"),
        ("Mary","Jones","mary")
    ]

    for d in data:
        cust = model.Customer()

        cust.firstName = d[0]
        cust.lastName = d[1]
        cust.pwd = d[2]

        session.save(cust)

    data = [
        ("Snow","snow.jpg"),
        ("Street","street.jpg"),
        ("Surf","surf.jpg"),
        ("Apparel","apparel.jpg"),
    ]

    for d in data:
        cat = model.Category()

        cat.name = d[0]
        cat.image = d[1]

        session.save(cat)

    data = [
        ("Glide Snowboard","Stiff and responsive board for big-footed riders.",1,"glide.jpg",120,),
        ("Firenze Skiis","Twin tip directional boards with easily adjustable, nonreleasable bindings.",1,"firenze.jpg",250,),
        ("Leaderboard","With its directional shape and long nose, allows for great accuracy on hard snow.",1,"leader.jpg",142,),
        ("EZ Reider Scooter","The EZ offers a smooth ride with twice the amount of ground clearance.",2,"ezrider.jpg",57),
        ("Turbulance Skateboard","Canadian maple provides strength and flexibility, essential to long board life and pop.",2,"turbulance.jpg",65),
        ("Trick Lick Street Bike","Light and foldable for easy commuting.",2,"tricklick.jpg",575),
        ("Robo Board","Ideal beginner board for riders under 150 lbs.",3,"robo.jpg",39),
        ("Finbar","Hard rails and natural rocker make this board very responsive.",3,"finbar.jpg",71),
        ("Doom Rider","This board is very forgiving and fun, and is a great board for all conditions.",3,"doom.jpg",78),
        ("Trick Jacket","2 bottom hem, 1-handed side cinch closure. Internal storm flap with fleece chin.",4,"trickjack.jpg",199),
        ("Big O glasses","Weight reducing frame material that is flexible and durable at all temperatures. ",4,"bigo.jpg",41),
        ("Escape Helmet","Closeable intake ports and fixed exhaust ports give you full temperature control.",4,"escapemet.jpg",29),
        ("Gargoggle","Light-weight high grade polyurethane that is flexible and durable at all temperatures. ",4,"gargoggle.jpg",23),
    ]

    for d in data:
        prod = model.Product()

        prod.name = d[0]
        prod.description = d[1]
        prod.category_id = d[2]
        prod.image = d[3]
        prod.price = d[4]

        session.save(prod)

    order = model.Order()
    order.customer_id = 1

    order2 = model.Order()
    order2.customer_id = 1

    session.save(order)
    session.save(order2)

    data = [
        (1,1,120,1),
        (1,2,250,2),
        (2,1,120,2),
        (2,2,250,1),
        (2,3,142,3)
    ]

    for d in data:
        oi = model.OrderItem()

        oi.order_id = d[0] 
        oi.product_id = d[1] 
        oi.price = d[2] 
        oi.quantity = d[3]

        session.save(oi) 

    session.commit()

def main():
    db.create(db.get_engine())
    init_data()

if __name__ == '__main__':
    main()
