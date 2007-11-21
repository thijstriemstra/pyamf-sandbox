create table Customer
(
	customerId   		varchar(25) not null primary key,
	firstName    		varchar(20) not null,
	lastName     		varchar(20) not null,
	pwd   		varchar(15) not null
);

commit;

insert into Customer (
		customerId,
		firstName,
		lastName,
		pwd )
	VALUES (?,?,?,?);

{
"john","John","Smith","john"
"mary","Mary","Jones","mary"
};

commit;

create table Category
(
	categoryId   		int not null primary key,
	name	   	varchar(20) not null,
	image 		varchar(50)	
);

commit;

insert into Category (
		categoryId,
		name,
		image )
	VALUES (?,?,?);

{
1,"Snow","snow.jpg"
2,"Street","street.jpg"
3,"Surf","surf.jpg"
4,"Apparel","apparel.jpg"
};

commit;

create table Product
(
	productId    		int not null primary key,
	name  		varchar(30) not null,
	description   		varchar(255),
	categoryId   		int not null foreign key references Category(categoryId),
	image 		varchar(50),
	price    		double not null
);

commit;

insert into Product(
	productId, 
	name, 
	description, 
	categoryId, 
	image, 
	price ) 
      VALUES(?,?,?,?,?,?);

{

1,"Glide Snowboard","Stiff and responsive board for big-footed riders.",1,"glide.jpg",120
2,"Firenze Skiis","Twin tip directional boards with easily adjustable, nonreleasable bindings.",1,"firenze.jpg",250
3,"Leaderboard","With its directional shape and long nose, allows for great accuracy on hard snow.",1,"leader.jpg",142
4,"EZ Reider Scooter","The EZ offers a smooth ride with twice the amount of ground clearance.",2,"ezrider.jpg",57
5,"Turbulance Skateboard","Canadian maple provides strength and flexibility, essential to long board life and pop.",2,"turbulance.jpg",65
6,"Trick Lick Street Bike","Light and foldable for easy commuting.",2,"tricklick.jpg",575
7,"Robo Board","Ideal beginner board for riders under 150 lbs.",3,"robo.jpg",39
8,"Finbar","Hard rails and natural rocker make this board very responsive.",3,"finbar.jpg",71
9,"Doom Rider","This board is very forgiving and fun, and is a great board for all conditions.",3,"doom.jpg",78
10,"Trick Jacket","2 bottom hem, 1-handed side cinch closure. Internal storm flap with fleece chin.",4,"trickjack.jpg",199
11,"Big O glasses","Weight reducing frame material that is flexible and durable at all temperatures. ",4,"bigo.jpg",41
12,"Escape Helmet","Closeable intake ports and fixed exhaust ports give you full temperature control.",4,"escapemet.jpg",29
13,"Gargoggle","Light-weight high grade polyurethane that is flexible and durable at all temperatures. ",4,"gargoggle.jpg",23
};

commit;

create table Order
(
	orderId   		int not null primary key,
	customerId		varchar(25) not null foreign key references Customer(customerId),
	status		varchar(10) default 'Pending',
	orderDate		date default CURRENT_DATE
);

commit;

insert into Order (
	orderId,
	customerId)
	VALUES (?,?);
{
1,"john"
2,"john"
};

commit;

create table OrderItem
(
	itemId   		int not null primary key,	
	orderId   		int not null foreign key references Order(orderId) on delete cascade,
	productId		int not null foreign key references Product(productId),
	price		double not null,
	qty		int not null
);

commit;

insert into OrderItem (
		itemId,
		orderId,
		productId,
		price,
		qty )
	VALUES (?,?,?,?,?);

{
1,1,1,120,1
2,1,2,250,2
3,2,1,120,2
4,2,2,250,1
5,2,3,142,3
};

commit;

create table Sequence
(
	sequenceId   		varchar(25) not null primary key,
	lastKey		int
);

commit;

insert into Sequence (
		sequenceId,
		lastKey)
	VALUES (?,?);

{
"Order",2
"OrderItem",5
};

commit;
