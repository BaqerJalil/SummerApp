import csv

data = """
Duckfat - Rating: 4.3
Street & Co. - Rating: 4.3
The Highroller Lobster - Rating: 4.3
Eventide Oyster Company - Rating: 4.3
Wayside Tavern - Rating: 4.8
Central Provisions - Rating: 4.3
Luke's Lobster Portland Pier - Rating: 4.3
The Honey Paw - Rating: 4.3
Scales - Rating: 4.3
Fore Street - Rating: 4.1
Bird & Co - Rating: 4.5
Salt Yard Cafe & Bar - Rating: 4.6
Blyth & Burrows - Rating: 4.5
Via Vecchia - Rating: 4.2
Twelve - Rating: 4.6
Terlingua - Rating: 4.3
Boda - Rating: 4.4
Union Restaurant - Rating: 4.1
Leeward - Rating: 4.5
Isa Bistro - Rating: 4.7
The Independent Ice - Rating: 4.6
DiMillo's On the Water - Rating: 3.8
Little Pig - Rating: 5.0
Empire Chinese Kitchen - Rating: 4.3
Evo - Rating: 4.5
Hot Suppa - Rating: 4.4
Butcher Burger - Rating: 4.6
The Knotted Apron - Rating: 4.6
Paper Tiger - Rating: 4.2
The Great Lost Bear - Rating: 3.9
Sur Lie - Rating: 4.4
Magissa - Rating: 4.3
Crispy Gai - Rating: 4.5
Bite Into Maine - Rating: 4.7
Flatbread Company - Rating: 4.4
Bite Into Maine - Rating: 4.7
Sichuan Kitchen - Rating: 4.3
Wilson County Barbecue - Rating: 4.3
Bread & Friends - Rating: 4.6
Keg and kraken  - Rating: 4.6
Mainely Noods - Rating: 4.3
Lazzari - Rating: 4.0
Bramhall - Rating: 4.3
The King's Head - Rating: 4.0
The Armory Lounge - Rating: 4.3
Mash Tun - Rating: 4.3
Izakaya Minato - Rating: 4.4
Solo Italiano - Rating: 4.2
Pai Men Miyake - Rating: 3.8
Chaval - Rating: 4.3
Maine Oyster Company - Rating: 4.7
Gilbert's Chowder House - Rating: 4.0
Maiz Colombian Street Food - Forest Ave - Rating: 4.6
The Friendly Toast - Portland - Rating: 4.5
Cantina Calafia - Rating: 5.0
Becky's Diner - Rating: 4.1
Bayside American Cafe - Rating: 4.3
Quanto Basta - Rating: 4.4
Kume - Rating: 4.4
The Thirsty Pig - Rating: 3.8
Jing Yan - Rating: 4.4
Room for Improvement - Rating: 4.5
N To Tail - Rating: 4.1
Brickyard Hollow Brewing - Rating: 4.0
Continental - Rating: 4.2
Five of Clubs - Rating: 4.5
Rigby Yard - Rating: 4.2
Miyake - Rating: 4.3
Nom Cafe - Rating: 4.6
SoPo Seafood Market & Raw Bar - Rating: 4.8
Taco Escobarr - Rating: 3.9
Sal De La Tierra - Rating: 4.6
Papi - Rating: 4.4
Ocotillo - Rating: 4.5
Ugly Duckling - Rating: 4.4
CÔNG TỬ BỘT - Rating: 3.9
Ribollita - Rating: 4.0
Flores Restaurant - Rating: 4.3
David's Opus Ten - Rating: 4.4
Roasty's - Rating: 4.3
Thames Landing - Rating: 4.3
Old Port Sea Grill and Raw Bar - Rating: 3.9
Smoked Portland - Rating: 3.9
David's Restaurant - Rating: 4.0
The Porthole Restaurant & Pub - Rating: 3.6
The East Ender - Rating: 4.1
Cargo Pizza Company - Rating: 5.0
Lenora - Rating: 4.2
Franciska Wine Bar - Rating: 5.0
Cuties - Rating: 4.4
Woodford F & B - Rating: 4.0
LB Kitchen - Rating: 4.3
Novel - Rating: 4.5
Tomaso's Canteen - Rating: 4.4
Inkwell - Rating: 4.1
Mi Sen Noodle Bar - Rating: 4.4
Mitr Ping Yang Thai Kitchen - Rating: 4.7
Paella seafood - Rating: 4.8
Clam Bar - Rating: 4.3
Bar Futo - Rating: 4.1
Duckfat Frites Shack - Rating: 4.3
Tuscan Table - Rating: 3.9
Benkay Japanese Restaurant & Sushi Bar - Rating: 4.0
Black Cow - Rating: 3.8
The Front Room - Rating: 3.9
City Farmhouse Kitchen and Bar - Rating: 3.9
Little Tap House - Rating: 4.0
The Sinful Kitchen - Rating: 4.4
Smalls - Rating: 4.2
Benny's - Rating: 5.0
Nonesuch River Brewing - Rating: 4.1
Saltwater Grille - Rating: 3.3
Regards - Rating: 3.9
Banh Appetit - Rating: 4.7
kuno - Rating: 4.7
Bar Publica - Rating: 3.7
Tu Casa Salvadorena Restaurant - Rating: 4.3
Sun Vietnamese Restaurant - Rating: 4.6
The Green Elephant - Rating: 4.5
Roma Cafe - Rating: 4.1
Mesa Grande Taqueria - Rating: 4.2
Genji Ramen - Rating: 5.0
Artemisia Cafe - Rating: 4.4
Tipo - Rating: 4.2
Crunchy Poké - Rating: 4.8
O' Oysters - Rating: 5.0
Andy's Old Port Pub - Rating: 3.8
Za - Rating: 4.2
Ramona's - Rating: 4.5
Quiero Cafe - Rating: 4.7
Low Stakes Lodge - Rating: 4.1
Oun Lido’s - Rating: 4.6
Dutch's - Rating: 4.3
Low Key - Rating: 4.5
CBG Bar & Grill - Rating: 4.0
Porttown Public House & Coffee Bar - Rating: 4.8
Tacos Del Seoul - Rating: 4.9
Il Leone - Rating: 4.7
Marcy's Diner - Rating: 4.3
Dok Mali Thai Kitchen - Rating: 4.1
Portland Lobster Co - Rating: 3.5
The Grill Room - Rating: 3.5
Lil Chippy - Rating: 4.8
Jaffa Mediterranean Grill - Rating: 4.5
Thai Tree - Rating: 4.7
Loco Taco - Rating: 5.0
Calabash - Rating: 4.6
Cheese Louise - Portland - Rating: 4.3
Mr. Tuna - Rating: 4.3
Sicilian Table - Rating: 3.9
Anoche - Rating: 4.1
Portland Hunt & Alpine Club - Rating: 3.9
Other Side Diner - Rating: 4.1
Mandy & Matt’s Cafe - Rating: 4.8
Waypoint Restaurant - Rating: 4.4
Lucky Cheetah - Rating: 4.1
The Well at Jordan's Farm - Rating: 4.1
OTTO - Rating: 4.2
Micucci Grocery - Rating: 4.7
MAMI PORTLAND - Rating: 4.3
Babas - Rating: 4.6
Terra Cotta Pasta - Rating: 4.3
Union Kitchen - Rating: 4.7
Eighteen95 - Rating: 4.5
Noble Pizzeria & Barbecue - Rating: 4.5
Port 65 Kitchen & Bar - Rating: 4.8
Dina’s Cuisine - Rating: 4.5
Fuego - Rating: 4.5
North43Bistro - Rating: 4.1
De Vons - Rating: 5.0
The Corner Room - Rating: 3.6
The Rusty Lantern - Rating: 3.7
Rio Bravo Tacos and Tequila - Rating: 4.3
David's 388 - South Portland - Rating: 4.3
Mr Chickpea - Rating: 4.8
Forage Market - Rating: 3.9
The Local Press - Rating: 4.7
Pattaya Kitchen - Rating: 4.5
Old Port Noodle House - Rating: 4.0
Red Sea Restaurant - Rating: 4.5
Monte's Fine Foods - Rating: 4.4
Docks Seafood - Rating: 3.9
Yosaku - Rating: 3.9
Flores Restaurant - Rating: 4.2
Sebago Brewing Company - Rating: 3.7
Mazzat Restaurant - Rating: 4.7
Camp Pennant - Rating: 3.1
Guerrero Maya Mexican Restaurant - Rating: 4.2
Taco Trio - Rating: 4.2
Bake Maine Pottery Cafe - Rating: 4.7
Tostones Cafe - Rating: 4.9
Kozeta's Restaurant - Rating: 4.6
JP's Bistro - Rating: 4.2
Po' Boys & Pickles - Rating: 4.2
Heritage Soul Food - Rating: 2.0
Harbor Bistro + Terrace - Rating: 3.4
Dok Mali Noodle Bar - Rating: 4.5
Crooked Mile - Rating: 4.4
Jefe Juan's - Rating: 4.7
TIQA - Rating: 3.8
"""

# Split the data by lines, filter out empty lines
lines = [line.strip() for line in data.strip().split('\n') if line.strip()]

with open('restaurants.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Restaurant', 'Rating'])  # CSV header

    for line in lines:
        # Split on " - Rating: "
        if " - Rating: " in line:
            name, rating = line.split(" - Rating: ")
            writer.writerow([name.strip(), rating.strip()])

print("Saved restaurants.csv successfully!")
