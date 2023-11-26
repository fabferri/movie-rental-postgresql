# import the random library
import random
import math
# Initialize the list
firstname = [
'Aaliyah',
'Aaron',
'Abby',
'Abigail',
'Abraham',
'Adam',
'Addison',
'Adrian',
'Adriana',
'Adrianna',
'Aidan',
'Aiden',
'Alan',
'Alana',
'Alejandro',
'Alex',
'Alexa',
'Alexander',
'Alexandra',
'Alexandria',
'Alexia',
'Alexis',
'Alexis',
'Alicia',
'Allison',
'Alondra',
'Alyssa',
'Amanda',
'Amber',
'Amelia',
'Amy',
'Ana',
'Andrea',
'Andres',
'Andrew',
'Angel',
'Angel',
'Angela',
'Angelica',
'Angelina',
'Anna',
'Anthony',
'Antonio',
'Ariana',
'Arianna',
'Ashley',
'Ashlyn',
'Ashton',
'Aubrey',
'Audrey',
'Austin',
'Autumn',
'Ava',
'Avery',
'Ayden',
'Bailey',
'Benjamin',
'Bianca',
'Blake',
'Braden',
'Bradley',
'Brady',
'Brandon',
'Brayden',
'Breanna',
'Brendan',
'Brian',
'Briana',
'Brianna',
'Brittany',
'Brody',
'Brooke',
'Brooklyn',
'Bryan',
'Bryce',
'Bryson',
'Caden',
'Caitlin',
'Caitlyn',
'Caleb',
'Cameron',
'Camila',
'Carlos',
'Caroline',
'Carson',
'Carter',
'Cassandra',
'Cassidy',
'Catherine',
'Cesar',
'Charles',
'Charlotte',
'Chase',
'Chelsea',
'Cheyenne',
'Chloe',
'Christian',
'Christina',
'Christopher',
'Claire',
'Cody',
'Colby',
'Cole',
'Colin',
'Collin',
'Colton',
'Conner',
'Connor',
'Cooper',
'Courtney',
'Cristian',
'Crystal',
'Daisy',
'Dakota',
'Dalton',
'Damian',
'Daniel',
'Daniela',
'Danielle',
'David',
'Delaney',
'Derek',
'Destiny',
'Devin',
'Devon',
'Diana',
'Diego',
'Dominic',
'Donovan',
'Dylan',
'Edgar',
'Eduardo',
'Edward',
'Edwin',
'Eli',
'Elias',
'Elijah',
'Elizabeth',
'Ella',
'Ellie',
'Emily',
'Emma',
'Emmanuel',
'Eric',
'Erica',
'Erick',
'Erik',
'Erin',
'Ethan',
'Eva',
'Evan',
'Evelyn',
'Faith',
'Fernando',
'Francisco',
'Gabriel',
'Gabriela',
'Gabriella',
'Gabrielle',
'Gage',
'Garrett',
'Gavin',
'Genesis',
'George',
'Gianna',
'Giovanni',
'Giselle',
'Grace',
'Gracie',
'Grant',
'Gregory',
'Hailey',
'Haley',
'Hannah',
'Hayden',
'Hector',
'Henry',
'Hope',
'Hunter',
'Ian',
'Isaac',
'Isabel',
'Isabella',
'Isabelle',
'Isaiah',
'Ivan',
'Jack',
'Jackson',
'Jacob',
'Jacqueline',
'Jada',
'Jade',
'Jaden',
'Jake',
'Jalen',
'James',
'Jared',
'Jasmin',
'Jasmine',
'Jason',
'Javier',
'Jayden',
'Jayla',
'Jazmin',
'Jeffrey',
'Jenna',
'Jennifer',
'Jeremiah',
'Jeremy',
'Jesse',
'Jessica',
'Jesus',
'Jillian',
'Jocelyn',
'Joel',
'John',
'Johnathan',
'Jonah',
'Jonathan',
'Jordan',
'Jordan',
'Jordyn',
'Jorge',
'Jose',
'Joseph',
'Joshua',
'Josiah',
'Juan',
'Julia',
'Julian',
'Juliana',
'Justin',
'Kaden',
'Kaitlyn',
'Kaleb',
'Karen',
'Karina',
'Kate',
'Katelyn',
'Katherine',
'Kathryn',
'Katie',
'Kayla',
'Kaylee',
'Kelly',
'Kelsey',
'Kendall',
'Kennedy',
'Kenneth',
'Kevin',
'Kiara',
'Kimberly',
'Kyle',
'Kylee',
'Kylie',
'Landon',
'Laura',
'Lauren',
'Layla',
'Leah',
'Leonardo',
'Leslie',
'Levi',
'Liam',
'Liliana',
'Lillian',
'Lilly',
'Lily',
'Lindsey',
'Logan',
'Lucas',
'Lucy',
'Luis',
'Luke',
'Lydia',
'Mackenzie',
'Madeline',
'Madelyn',
'Madison',
'Makayla',
'Makenzie',
'Malachi',
'Manuel',
'Marco',
'Marcus',
'Margaret',
'Maria',
'Mariah',
'Mario',
'Marissa',
'Mark',
'Martin',
'Mary',
'Mason',
'Matthew',
'Max',
'Maxwell',
'Maya',
'Mckenzie',
'Megan',
'Melanie',
'Melissa',
'Mia',
'Micah',
'Michael',
'Michelle',
'Miguel',
'Mikayla',
'Miranda',
'Molly',
'Morgan',
'Mya',
'Name',
'Name',
'Naomi',
'Natalia',
'Natalie',
'Nathan',
'Nathaniel',
'Nevaeh',
'Nicholas',
'Nicolas',
'Nicole',
'Noah',
'Nolan',
'Oliver',
'Olivia',
'Omar',
'Oscar',
'Owen',
'Paige',
'Parker',
'Patrick',
'Paul',
'Payton',
'Peter',
'Peyton',
'Peyton',
'Preston',
'Rachel',
'Raymond',
'Reagan',
'Rebecca',
'Ricardo',
'Richard',
'Riley',
'Riley',
'Robert',
'Ruby',
'Ryan',
'Rylee',
'Sabrina',
'Sadie',
'Samantha',
'Samuel',
'Sara',
'Sarah',
'Savannah',
'Sean',
'Sebastian',
'Serenity',
'Sergio',
'Seth',
'Shane',
'Shawn',
'Shelby',
'Sierra',
'Skylar',
'Sofia',
'Sophia',
'Sophie',
'Spencer',
'Stephanie',
'Stephen',
'Steven',
'Summer',
'Sydney',
'Tanner',
'Taylor',
'Thomas',
'Tiffany',
'Timothy',
'Travis',
'Trenton',
'Trevor',
'Trinity',
'Tristan',
'Tyler',
'Valeria',
'Valerie',
'Vanessa',
'Veronica',
'Victor',
'Victoria',
'Vincent',
'Wesley',
'William',
'Wyatt',
'Xavier',
'Zachary',
'Zoe',
'Zoey'
]

lastname = [
'Adams',
'Aitken',
'Alexander',
'Allan',
'Allen',
'Anderson',
'Andrews',
'Armstrong',
'Arnold',
'Atkinson',
'Austin',
'Bailey',
'Baker',
'Ball',
'Barber',
'Barker',
'Barnes',
'Barrett',
'Barton',
'Bates',
'Bell',
'Bennett',
'Berry',
'Bird',
'Bishop',
'Black',
'Blake',
'Booth',
'Bowen',
'Boyle',
'Bradley',
'Brooks',
'Brown ',
'Bruce',
'Buckley',
'Burgess',
'Burke',
'Burns',
'Burton',
'Butler',
'Byrne',
'Cameron',
'Campbell',
'Carr',
'Carter',
'Chambers',
'Chapman',
'Christie',
'Clark',
'Clarke',
'Cole',
'Coleman',
'Collins',
'Cook',
'Cooke',
'Cooper',
'Cox',
'Craig',
'Crawford',
'Cross',
'Cunningham',
'Curtis',
'Davidson',
'Davies ',
'Davis',
'Dawson',
'Day',
'Dean',
'Dickson',
'Dixon',
'Docherty',
'Donaldson',
'Douglas',
'Doyle',
'Duffy',
'Duncan',
'Dunn',
'Edwards',
'Elliott',
'Ellis',
'Evans ',
'Farrell',
'Ferguson',
'Findlay',
'Fisher',
'Fleming',
'Fletcher',
'Forbes',
'Ford',
'Foster',
'Fox',
'Francis',
'Fraser',
'Freeman',
'Frost',
'Gardner',
'George',
'Gibson',
'Gilbert',
'Gill',
'Goddard',
'Goodwin',
'Gordon',
'Graham',
'Grant',
'Gray',
'Green',
'Gregory',
'Griffin',
'Griffiths',
'Hall',
'Hamilton',
'Hammond',
'Harding',
'Hardy',
'Harper',
'Harris',
'Harrison',
'Hart',
'Harvey',
'Hawkins',
'Hayes',
'Henderson',
'Hewitt',
'Higgins',
'Hill',
'Hill',
'Hodgson',
'Holland',
'Holmes',
'Hopkins',
'Howard',
'Hudson',
'Hughes',
'Hunt',
'Hunter',
'Hutchinson',
'Jackson',
'James',
'Jamieson',
'Jenkins',
'Johnson',
'Johnston',
'Johnstone',
'Jones ',
'Jordan',
'Kaur',
'Kelly',
'Kennedy',
'Kerr',
'King',
'Kirk',
'Knight',
'Lambert',
'Lane',
'Lawrence',
'Lee',
'Lewis',
'Lloyd',
'Long',
'Lowe',
'Macdonald',
'Mackay',
'Mackenzie',
'Maclean',
'Macleod',
'Mann',
'Marsh',
'Marshall',
'Martin',
'Martin',
'Mason',
'Matthews',
'May',
'McCarthy',
'McDonald',
'Mcgregor',
'Mcintosh',
'Mcintyre',
'Mckay',
'Mckenzie',
'Mclean',
'Mcmillan',
'Miles',
'Millar',
'Miller',
'Mills',
'Milne',
'Mitchell',
'Moore',
'Morgan',
'Morris',
'Morrison',
'Moss',
'Muir',
'Munro',
'Murphy',
'Murray',
'Nelson',
'Newman',
'Newton',
'Nicholls',
'Nicholson',
"O'Brien",
"O'Connor",
'Oliver',
"O'Neill",
'Osborne',
'Owen',
'Page',
'Palmer',
'Parker',
'Parry',
'Parsons',
'Patel',
'Paterson',
'Payne',
'Pearce',
'Pearson',
'Perry',
'Phillips',
'Porter',
'Potter',
'Powell',
'Price',
'Pritchard',
'Read',
'Reed',
'Rees',
'Reid',
'Reilly',
'Reynolds',
'Richards',
'Richardson',
'Riley',
'Ritchie',
'Roberts',
'Robertson',
'Robinson',
'Robson',
'Rogers',
'Rose',
'Ross',
'Rowe',
'Russell',
'Ryan',
'Sanderson',
'Saunders',
'Scott',
'Sharp',
'Shaw',
'Shepherd',
'Simpson',
'Sinclair',
'Slater',
'Smith ',
'Spencer',
'Stephens',
'Stephenson',
'Stevens',
'Stevenson',
'Stewart',
'Stone',
'Sutherland',
'Sutton',
'Taylor',
'Thomas ',
'Thompson',
'Thomson',
'Turner',
'Walker',
'Wallace',
'Walsh',
'Walters',
'Walton',
'Ward',
'Warren',
'Watkins',
'Watson',
'Watson',
'Watt',
'Watts',
'Webb',
'Webster',
'Wells',
'West',
'Wheeler',
'White',
'White',
'Whitehead',
'Wilkinson',
'Williams ',
'Williamson',
'Willis',
'Wilson',
'Wood',
'Woods',
'Woodward',
'Wright',
'Yates',
'Young'
]


print('-----------------------------')
print('-----------------------------')
customerAddress = []
customerAddress.append(["Aldermanbury Square",'EC2V 7HR','London','UK'])
customerAddress.append(["Aldermans Walk",'EC2M 3UJ','London','UK'])
customerAddress.append(["Aldgate",'EC3N 1RE','London','UK'])
customerAddress.append(["Aldgate High Street",'EC3N 1AB','London','UK'])
customerAddress.append(["Allhallows Lane",'EC4R 3UL','London','UK'])
customerAddress.append(["Amen Corner",'EC4M 7DA','London','UK'])
customerAddress.append(["Amen Court",'EC4M 7BU','London','UK'])
customerAddress.append(["America Square",'EC3N 2LR','London','UK'])
customerAddress.append(["Leadenhall Street",'EC3V 4AG','London','UK'])
customerAddress.append(["Angel Court",'EC2R 7HB','London','UK'])
customerAddress.append(["Angel Lane",'EC4R 3AB','London','UK'])
customerAddress.append(["Apothocary Street",'EC4V 6LX','London','UK'])
customerAddress.append(["Arthur Street",'EC4R 9AB','London','UK'])
customerAddress.append(["Austin Friars",'EC2N 2HA','London','UK'])
customerAddress.append(["Ave Maria Lane",'EC4M 7AQ','London','UK'])
customerAddress.append(["Barbican",'EC2Y 8AT','London','UK'])
customerAddress.append(["Barbican, Brandon Mews",'EC2Y 8BE','London','UK'])
customerAddress.append(["Barbican, Lambert Jones Mews",'EC2Y 8DP','London','UK'])
customerAddress.append(["Barbican, Lauderdale Place",'EC2Y 8EN','London','UK'])
customerAddress.append(["Barbican, Shaftesbury Place",'EC2Y 8AA','London','UK'])
customerAddress.append(["Barbican, Speed Highwalk",'EC2Y 8DX','London','UK'])
customerAddress.append(["Barbican, St. Giles Churchyard",'EC2Y 8DA','London','UK'])
customerAddress.append(["Barbican, St. Giles Terrace",'EC2Y 8DU','London','UK'])
customerAddress.append(["Barbican, The Postern",'EC2Y 8BJ','London','UK'])
customerAddress.append(["Barbican, Wallside",'EC2Y 8BH','London','UK'])
customerAddress.append(["Bartholomew Lane",'EC2N 2AX','London','UK'])
customerAddress.append(["Basinghall Avenue",'EC2V 5DD','London','UK'])
customerAddress.append(["Basinghall Street",'EC2V 5AY','London','UK'])
customerAddress.append(["Bassishaw Highwalk",'EC2V 5DS','London','UK'])
customerAddress.append(["Bastion Highwalk",'EC2Y 5AP','London','UK'])
customerAddress.append(["Beech Street",'EC2Y 8AD','London','UK'])
customerAddress.append(["Bell Inn Yard",'EC3V 0BL','London','UK'])
customerAddress.append(["Bell Wharf Lane",'EC4R 3TB','London','UK'])
customerAddress.append(["Bengal Court",'EC3V 9DD','London','UK'])
customerAddress.append(["Bennet's Hill",'EC4V 4ER','London','UK'])
customerAddress.append(["Bevis Marks",'EC3A 7BA','London','UK'])
customerAddress.append(["Billiter Street",'EC3M 2RY','London','UK'])
customerAddress.append(["Birchin Lane",'EC3V 9BW','London','UK'])
customerAddress.append(["Bishopsgate",'EC2M 3AB','London','UK'])
customerAddress.append(["Bishopsgate Arcade",'EC2M 3YD','London','UK'])
customerAddress.append(["Bishopsgate Churchyard",'EC2M 3TJ','London','UK'])
customerAddress.append(["Black Friars Lane",'EC4V 6EB','London','UK'])
customerAddress.append(["Blake Morgan, New Street Square",'EC4A 3DJ','London','UK'])
customerAddress.append(["Blomfield Street",'EC2M 7AJ','London','UK'])
customerAddress.append(["Bolt Court",'EC4A 3DQ','London','UK'])
customerAddress.append(["Booth Lane",'EC4V 4AP','London','UK'])
customerAddress.append(["Botolph Alley",'EC3R 8DR','London','UK'])
customerAddress.append(["Botolph Lane",'EC3R 8DE','London','UK'])
customerAddress.append(["Bouverie Street",'EC4Y 8AX','London','UK'])
customerAddress.append(["Bow Churchyard",'EC4M 9DQ','London','UK'])
customerAddress.append(["Bow Lane",'EC4M 9AL','London','UK'])
customerAddress.append(["Brabant Court",'EC3M 8AD','London','UK'])
customerAddress.append(["Bread Street",'EC4M 9AJ','London','UK'])
customerAddress.append(["Bream's Buildings",'EC4A 1DT','London','UK'])
customerAddress.append(["Bride Court",'EC4Y 8DU','London','UK'])
customerAddress.append(["Bride Lane",'EC4Y 8DT','London','UK'])
customerAddress.append(["Bridewell Place",'EC4V 6AP','London','UK'])
customerAddress.append(["Bridgewater Square",'EC2Y 8AG','London','UK'])
customerAddress.append(["Broad Street Place",'EC2M 7JH','London','UK'])
customerAddress.append(["Broadgate",'EC2M 2QS','London','UK'])
customerAddress.append(["Broken Wharf",'EC4V 3DT','London','UK'])
customerAddress.append(["Bullhorn International, Bishopgate",'EC2M 3AJ','London','UK'])
customerAddress.append(["Bulls Head Passage",'EC3V 1LU','London','UK'])
customerAddress.append(["Burgon Street",'EC4V 5DR','London','UK'])
customerAddress.append(["Bury Street",'EC3A 5AG','London','UK'])
customerAddress.append(["Bush Lane",'EC4R 0AN','London','UK'])
customerAddress.append(["Byward Street",'EC3R 5AS','London','UK'])
customerAddress.append(["Camomile Street",'EC3A 7LL','London','UK'])
customerAddress.append(["Cannon Street",'EC4M 5SB','London','UK'])
customerAddress.append(["Carey Lane",'EC2V 8AE','London','UK'])
customerAddress.append(["Carlisle Avenue",'EC3N 2ES','London','UK'])
customerAddress.append(["Carmelite Street",'EC4Y 0BS','London','UK'])
customerAddress.append(["Carter Court",'EC4V 5EN','London','UK'])
customerAddress.append(["Carter Lane",'EC4V 5AB','London','UK'])
customerAddress.append(["Castle Baynard Street",'EC4V 4EA','London','UK'])
customerAddress.append(["Castle Court",'EC3V 9AE','London','UK'])
customerAddress.append(["Caterina , Silk Street",'EC2Y 8AL','London','UK'])
customerAddress.append(["Cavendish Court",'EC3A 7GA','London','UK'])
customerAddress.append(["Cheapside",'EC2V 6AA','London','UK'])
customerAddress.append(["Cheapside Passage",'EC2V 6AF','London','UK'])
customerAddress.append(["Church Entry",'EC4V 5EU','London','UK'])
customerAddress.append(["Queen Victoria Street",'EC4N 4XY','London','UK'])
customerAddress.append(["Clement's Lane",'EC4N 7AE','London','UK'])
customerAddress.append(["Clifford's Inn Passage",'EC4A 1BL','London','UK'])
customerAddress.append(["Cloak Lane",'EC4R 2RU','London','UK'])
customerAddress.append(["Coleman Street",'EC2R 5AL','London','UK'])
customerAddress.append(["College Hill",'EC4R 2RA','London','UK'])
customerAddress.append(["College Street",'EC4R 2RH','London','UK'])
customerAddress.append(["Compter Passage",'EC2V 7AL','London','UK'])
customerAddress.append(["Cooper's Row",'EC3N 2BQ','London','UK'])
customerAddress.append(["Coppa Club, Three Quays Walk",'EC3R 6AH','London','UK'])
customerAddress.append(["Copthall Avenue",'EC2R 7BH','London','UK'])
customerAddress.append(["Cornhill",'EC3V 3LA','London','UK'])
customerAddress.append(["Cousin Lane",'EC4R 3TE','London','UK'])
customerAddress.append(["Crane Court",'EC4A 2EJ','London','UK'])
customerAddress.append(["Creechurch Lane",'EC3A 5AY','London','UK'])
customerAddress.append(["Creed Lane",'EC4V 5BR','London','UK'])
customerAddress.append(["Crescent",'EC3N 2LY','London','UK'])
customerAddress.append(["Crosswall",'EC3N 2JY','London','UK'])
customerAddress.append(["Crown Court",'EC2V 6JP','London','UK'])
customerAddress.append(["Crutched Friars",'EC3N 2AB','London','UK'])
customerAddress.append(["Crutched Friars, Railway Arches",'EC3N 2AU','London','UK'])
customerAddress.append(["Cullum Street",'EC3M 7JJ','London','UK'])
customerAddress.append(["Cursitor Street",'EC4A 1LL','London','UK'])
customerAddress.append(["Deans Court",'EC4V 5AA','London','UK'])
customerAddress.append(["Devonshire Row",'EC2M 4RH','London','UK'])
customerAddress.append(["Devonshire Square",'EC2M 4AB','London','UK'])
customerAddress.append(["Distaff Lane",'EC4M 8AQ','London','UK'])
customerAddress.append(["Liverpool Street",'EC2M 7AR','London','UK'])
customerAddress.append(["Dominion Street",'EC2M 2EF','London','UK'])
customerAddress.append(["Dorset Rise",'EC4Y 8EN','London','UK'])
customerAddress.append(["Dowgate Hill",'EC4R 2SU','London','UK'])
customerAddress.append(["Dukes Place",'EC3A 7LP','London','UK'])
customerAddress.append(["East Harding Street",'EC4A 3AS','London','UK'])
customerAddress.append(["Eastcheap",'EC3M 1AA','London','UK'])
customerAddress.append(["Eldon Street",'EC2M 7LA','London','UK'])
customerAddress.append(["Exchange Arcade",'EC2M 3WA','London','UK'])
customerAddress.append(["Falcon Court",'EC4Y 1BW','London','UK'])
customerAddress.append(["Fann Street",'EC2Y 8DY','London','UK'])
customerAddress.append(["Farringdon Street",'EC4A 4AB','London','UK'])
customerAddress.append(["Fenchurch Avenue",'EC3M 5AD','London','UK'])
customerAddress.append(["Fenchurch Place",'EC3M 4AJ','London','UK'])
customerAddress.append(["Fenchurch Street",'EC3M 3BD','London','UK'])
customerAddress.append(["Fenchurch Street, Fenchurch Buildings",'EC3M 5HN','London','UK'])
customerAddress.append(["Fetter Lane",'EC4A 1AA','London','UK'])
customerAddress.append(["Finch Lane",'EC3V 3NA','London','UK'])
customerAddress.append(["Finsbury Avenue",'EC2M 2PA','London','UK'])
customerAddress.append(["Finsbury Circus",'EC2M 7AQ','London','UK'])
customerAddress.append(["Finsbury Street",'EC2Y 9AU','London','UK'])
customerAddress.append(["Fish Street Hill",'EC3R 6AJ','London','UK'])
customerAddress.append(["Fishmongers Hall Wharf",'EC4R 3AE','London','UK'])
customerAddress.append(["Fleet Place",'EC4M 7RA','London','UK'])
customerAddress.append(["Fleet Street",'EC4A 2AB','London','UK'])
customerAddress.append(["Fore Street",'EC2Y 5DB','London','UK'])
customerAddress.append(["Fore Street Avenue",'EC2Y 9DT','London','UK'])
customerAddress.append(["Foster Lane",'EC2V 6HD','London','UK'])
customerAddress.append(["Frederick's Place",'EC2R 8AB','London','UK'])
customerAddress.append(["Friar Street",'EC4V 5DT','London','UK'])
customerAddress.append(["Friday Street",'EC4M 9BT','London','UK'])
customerAddress.append(["Frobisher Crescent",'EC2Y 8HD','London','UK'])
customerAddress.append(["Furnival Street",'EC4A 1AB','London','UK'])
customerAddress.append(["Garlick Hill",'EC4V 2AB','London','UK'])
customerAddress.append(["George Yard",'EC3V 9DF','London','UK'])
customerAddress.append(["Godliman Street",'EC4V 5AJ','London','UK'])
customerAddress.append(["Goring Street",'EC3A 8BG','London','UK'])
customerAddress.append(["Gough Square",'EC4A 3DE','London','UK'])
customerAddress.append(["Gracechurch Street",'EC3V 0AA','London','UK'])
customerAddress.append(["Great New Street",'EC4A 3BN','London','UK'])
customerAddress.append(["Great St. Helen's",'EC3A 6AP','London','UK'])
customerAddress.append(["Great St. Thomas Apostle",'EC4V 2BB','London','UK'])
customerAddress.append(["Great Swan Alley",'EC2R 7NH','London','UK'])
customerAddress.append(["Great Tower Street",'EC3R 5AA','London','UK'])
customerAddress.append(["Great Winchester Street",'EC2N 2JA','London','UK'])
customerAddress.append(["Gresham Street",'EC2V 7AA','London','UK'])
customerAddress.append(["Greystoke Place",'EC4A 1GP','London','UK'])
customerAddress.append(["Groveland Court",'EC4M 9EH','London','UK'])
customerAddress.append(["Guildhall Buildings",'EC2V 5AR','London','UK'])
customerAddress.append(["Guildhall Yard",'EC2V 5AA','London','UK'])
customerAddress.append(["Gutter Lane",'EC2V 6BR','London','UK'])
customerAddress.append(["Harp Lane",'EC3R 6DP','London','UK'])
customerAddress.append(["Hart Street",'EC3R 7NB','London','UK'])
customerAddress.append(["Haydon Street",'EC3N 1DB','London','UK'])
customerAddress.append(["Heneage Lane",'EC3A 5DQ','London','UK'])
customerAddress.append(["High Timber Street",'EC4V 3HT','London','UK'])
customerAddress.append(["Hind Court",'EC4A 3DL','London','UK'])
customerAddress.append(["Honey Lane",'EC2V 8BT','London','UK'])
customerAddress.append(["Houndsditch",'EC3A 7BD','London','UK'])
customerAddress.append(["Idol Lane",'EC3R 5DD','London','UK'])
customerAddress.append(["India Street",'EC3N 2HS','London','UK'])
customerAddress.append(["Inner Temple Lane",'EC4Y 1AF','London','UK'])
customerAddress.append(["Ireland Yard",'EC4V 5EH','London','UK'])
customerAddress.append(["Ironmonger Lane",'EC2V 8EP','London','UK'])
customerAddress.append(["Jewry Street",'EC3N 2ER','London','UK'])
customerAddress.append(["John Carpenter Street",'EC4Y 0AN','London','UK'])
customerAddress.append(["Johnsons Court",'EC4A 3EA','London','UK'])
customerAddress.append(["King Street",'EC2V 8AU','London','UK'])
customerAddress.append(["King William Street",'EC4N 7AA','London','UK'])
customerAddress.append(["Kings Arms Yard",'EC2R 7AF','London','UK'])
customerAddress.append(["Knightrider Court",'EC4V 5AR','London','UK'])
customerAddress.append(["Knightrider Street",'EC4V 5BH','London','UK'])
customerAddress.append(["Lambeth Hill",'EC4V 4AG','London','UK'])
customerAddress.append(["Laurence Pountney Hill",'EC4R 0BE','London','UK'])
customerAddress.append(["Laurence Pountney Lane",'EC4R 0EE','London','UK'])
customerAddress.append(["Lawrence Lane",'EC2V 8DP','London','UK'])
customerAddress.append(["Leadenhall Market",'EC3V 1LR','London','UK'])
customerAddress.append(["Leadenhall Place",'EC3M 7DX','London','UK'])
customerAddress.append(["Leadenhall Street",'EC3A 1AA','London','UK'])
customerAddress.append(["Lime Street",'EC3M 7AA','London','UK'])
customerAddress.append(["Limeburner Lane",'EC4M 7AX','London','UK'])
customerAddress.append(["Little New Street",'EC4A 3JR','London','UK'])
customerAddress.append(["Little Trinity Lane",'EC4V 2AN','London','UK'])
customerAddress.append(["Liverpool Street",'EC2M 7NH','London','UK'])
customerAddress.append(["Liverpool Street, The Arcade",'EC2M 7PN','London','UK'])
customerAddress.append(["Lloyd's Avenue",'EC3N 3AA','London','UK'])
customerAddress.append(["Lombard Court",'EC3V 9BJ','London','UK'])
customerAddress.append(["Lombard Lane",'EC4Y 8AD','London','UK'])
customerAddress.append(["Lombard Street",'EC3V 9AA','London','UK'])
customerAddress.append(["London Street",'EC3R 7JP','London','UK'])
customerAddress.append(["London Wall",'EC2M 5ND','London','UK'])
customerAddress.append(["London Wall Buildings",'EC2M 5NS','London','UK'])
customerAddress.append(["Lothbury",'EC2R 7AP','London','UK'])
customerAddress.append(["Lovat Lane",'EC3R 8AE','London','UK'])
customerAddress.append(["Love Lane",'EC2V 7JN','London','UK'])
customerAddress.append(["Lower New Change Passage",'EC4M 9AH','London','UK'])
customerAddress.append(["Lower Thames Street",'EC3R 6AF','London','UK'])
customerAddress.append(["Ludgate Broadway",'EC4V 6DU','London','UK'])
customerAddress.append(["Ludgate Circus",'EC4M 7LD','London','UK'])
customerAddress.append(["Ludgate Hill",'EC4M 7AA','London','UK'])
customerAddress.append(["Ludgate Square",'EC4M 7AS','London','UK'])
customerAddress.append(["Mansion House Place",'EC4N 8BJ','London','UK'])
customerAddress.append(["Mark Lane",'EC3R 7LU','London','UK'])
customerAddress.append(["Martin Lane",'EC4R 0DJ','London','UK'])
customerAddress.append(["Mason's Avenue",'EC2V 5BT','London','UK'])
customerAddress.append(["Milton Street",'EC2Y 9BH','London','UK'])
customerAddress.append(["Mincing Lane",'EC3R 7AE','London','UK'])
customerAddress.append(["Minories",'EC3N 1BJ','London','UK'])
customerAddress.append(["Minster Court",'EC3R 7AA','London','UK'])
customerAddress.append(["Minster Pavement",'EC3R 7PP','London','UK'])
customerAddress.append(["Mitre Street",'EC3A 5BU','London','UK'])
customerAddress.append(["Monkwell Square",'EC2Y 5BL','London','UK'])
customerAddress.append(["Monument Street",'EC3R 8AH','London','UK'])
customerAddress.append(["Moor Lane",'EC2Y 9AP','London','UK'])
customerAddress.append(["Moorfields",'EC2Y 9AA','London','UK'])
customerAddress.append(["Moorfields Highwalk",'EC2Y 9DP','London','UK'])
customerAddress.append(["Moorgate",'EC2M 6AB','London','UK'])
customerAddress.append(["Moorgate Place",'EC2R 6EA','London','UK'])
customerAddress.append(["Nevill Lane",'EC4A 3AP','London','UK'])
customerAddress.append(["New Bridge Street",'EC4V 6AA','London','UK'])
customerAddress.append(["New Broad Street",'EC2M 1JD','London','UK'])
customerAddress.append(["New Change",'EC4M 9AF','London','UK'])
customerAddress.append(["New Change Passage",'EC4M 9AG','London','UK'])
customerAddress.append(["New Fetter Lane",'EC4A 1AG','London','UK'])
customerAddress.append(["New London Street",'EC3R 7NA','London','UK'])
customerAddress.append(["New Street",'EC2M 4TP','London','UK'])
customerAddress.append(["New Street Square",'EC4A 3AT','London','UK'])
customerAddress.append(["Nicholas Lane",'EC4N 7BN','London','UK'])
customerAddress.append(["Noble Street",'EC2V 7JX','London','UK'])
customerAddress.append(["Aldermanbury Square",'EC2V 7AZ','London','UK'])
customerAddress.append(["Northumberland Alley",'EC3N 2EJ','London','UK'])
customerAddress.append(["Oat Lane",'EC2V 7DE','London','UK'])
customerAddress.append(["Octagon Arcade",'EC2M 2AB','London','UK'])
customerAddress.append(["Old Bailey",'EC4M 7AN','London','UK'])
customerAddress.append(["Old Billingsgate Walk",'EC3R 6DX','London','UK'])
customerAddress.append(["Old Broad Street",'EC2M 1JB','London','UK'])
customerAddress.append(["Old Change Court",'EC4M 8EN','London','UK'])
customerAddress.append(["Old Jewry",'EC2R 8DD','London','UK'])
customerAddress.append(["Old Mitre Court",'EC4Y 7BP','London','UK'])
customerAddress.append(["Paternoster Row",'EC4M 7EJ','London','UK'])
customerAddress.append(["Paternoster Square",'EC4M 7DX','London','UK'])
customerAddress.append(["Paul's Walk",'EC4V 3QH','London','UK'])
customerAddress.append(["Pemberton Row",'EC4A 3BA','London','UK'])
customerAddress.append(["Wood Street",'EC2V 7AW','London','UK'])
customerAddress.append(["Pepys Street",'EC3N 2NR','London','UK'])
customerAddress.append(["Philpot Lane",'EC3M 8AA','London','UK'])
customerAddress.append(["Pilgrim Street",'EC4V 6DR','London','UK'])
customerAddress.append(["Pilgrim Street, Priory Court",'EC4V 6DE','London','UK'])
customerAddress.append(["Playhouse Yard",'EC4V 5EX','London','UK'])
customerAddress.append(["Pleydell Street",'EC4Y 8DB','London','UK'])
customerAddress.append(["Plough Place",'EC4A 1DE','London','UK'])
customerAddress.append(["Plumtree Court",'EC4A 4AJ','London','UK'])
customerAddress.append(["Poppins Court",'EC4A 4AX','London','UK'])
customerAddress.append(["Poultry",'EC2R 8AJ','London','UK'])
customerAddress.append(["Princes Street",'EC2R 8AQ','London','UK'])
customerAddress.append(["Printer Street",'EC4A 3BH','London','UK'])
customerAddress.append(["Printers Inn Court",'EC4A 1LR','London','UK'])
customerAddress.append(["Pudding Lane",'EC3R 8AB','London','UK'])
customerAddress.append(["Puddle Dock",'EC4V 3DS','London','UK'])
customerAddress.append(["Queen Street",'EC4N 1SA','London','UK'])
customerAddress.append(["Queen Street Place",'EC4R 1BE','London','UK'])
customerAddress.append(["Queen Victoria Street",'EC4N 4SA','London','UK'])
customerAddress.append(["Queenhithe",'EC4V 3DX','London','UK'])
customerAddress.append(["Queens Head Passage",'EC4M 7DZ','London','UK'])
customerAddress.append(["Finsbury Circus",'EC2M 7AZ','London','UK'])
customerAddress.append(["Red Lion Court",'EC4A 3EB','London','UK'])
customerAddress.append(["Rolls Passage",'EC4A 1HL','London','UK'])
customerAddress.append(["Rood Lane",'EC3M 8AP','London','UK'])
customerAddress.append(["Ropemaker Street",'EC2Y 9AR','London','UK'])
customerAddress.append(["Rose Street",'EC4M 7DQ','London','UK'])
customerAddress.append(["Royal Exchange Avenue",'EC3V 3LT','London','UK'])
customerAddress.append(["Royal Exchange Buildings",'EC3V 3LF','London','UK'])
customerAddress.append(["Royal Exchange, The Courtyard",'EC3V 3LQ','London','UK'])
customerAddress.append(["Royal Mint Court",'EC3N 4HJ','London','UK'])
customerAddress.append(["Russia Row",'EC2V 8BL','London','UK'])
customerAddress.append(["Queen Victoria Street",'EC4V 4BE','London','UK'])
customerAddress.append(["Blake Tower, Fann Street",'EC2Y 8AF','London','UK'])
customerAddress.append(["Salisbury Court",'EC4Y 8AA','London','UK'])
customerAddress.append(["Salisbury Square",'EC4Y 8AE','London','UK'])
customerAddress.append(["Salters Hall Court",'EC4N 8AH','London','UK'])
customerAddress.append(["Savage Gardens",'EC3N 2AR','London','UK'])
customerAddress.append(["Seething Lane",'EC3N 4AH','London','UK'])
customerAddress.append(["Serjeant's Inn",'EC4Y 1AG','London','UK'])
customerAddress.append(["Ship Tavern Passage",'EC3V 1LY','London','UK'])
customerAddress.append(["Shoe Lane",'EC4A 3BE','London','UK'])
customerAddress.append(["Skewered, Mark Lane",'EC3R 7AF','London','UK'])
customerAddress.append(["Sky Garden Walk",'EC3M 8AF','London','UK'])
customerAddress.append(["South Place",'EC2M 2AF','London','UK'])
customerAddress.append(["St. Andrew Street",'EC4A 3AE','London','UK'])
customerAddress.append(["St. Andrew's Hill",'EC4V 5BY','London','UK'])
customerAddress.append(["St. Botolph Street",'EC3A 7AL','London','UK'])
customerAddress.append(["St. Bride Street",'EC4A 4AD','London','UK'])
customerAddress.append(["St. Bride's Avenue",'EC4Y 8AU','London','UK'])
customerAddress.append(["St. Brides Passage",'EC4Y 8EJ','London','UK'])
customerAddress.append(["St. Clare Street",'EC3N 1LQ','London','UK'])
customerAddress.append(["St. Dunstan's Hill",'EC3R 8AD','London','UK'])
customerAddress.append(["St. Georges Lane",'EC3R 8DJ','London','UK'])
customerAddress.append(["St. Helen's Place",'EC3A 6AB','London','UK'])
customerAddress.append(["St. James's Passage",'EC3A 5DH','London','UK'])
customerAddress.append(["St. Mary At Hill",'EC3R 8DU','London','UK'])
customerAddress.append(["St. Mary Axe",'EC3A 8AA','London','UK'])
customerAddress.append(["St. Michael's Alley",'EC3V 9DS','London','UK'])
customerAddress.append(["St. Olave's Court",'EC2V 8EX','London','UK'])
customerAddress.append(["St. Paul's Churchyard",'EC4M 8AB','London','UK'])
customerAddress.append(["St. Swithin's Lane",'EC4N 8AD','London','UK'])
customerAddress.append(["Stew Lane",'EC4V 3PT','London','UK'])
customerAddress.append(["Suffolk Lane",'EC4R 0AT','London','UK'])
customerAddress.append(["Sun Street",'EC2M 2PL','London','UK'])
customerAddress.append(["Swan Lane",'EC4R 3TN','London','UK'])
customerAddress.append(["Swingers, Brown's Buildings",'EC3A 8AL','London','UK'])
customerAddress.append(["Talbot Court",'EC3V 0BP','London','UK'])
customerAddress.append(["Telegraph Street",'EC2R 7AR','London','UK'])
customerAddress.append(["Temple",'EC4Y 7AA','London','UK'])
customerAddress.append(["Temple Avenue",'EC4Y 0DA','London','UK'])
customerAddress.append(["Temple, Brick Court",'EC4Y 9AD','London','UK'])
customerAddress.append(["Temple, Crown Office Row",'EC4Y 7AT','London','UK'])
customerAddress.append(["Temple, Essex Court",'EC4Y 9AH','London','UK'])
customerAddress.append(["Temple, Garden Court",'EC4Y 9BJ','London','UK'])
customerAddress.append(["Temple, Harcourt Buildings",'EC4Y 9DA','London','UK'])
customerAddress.append(["Temple, Hare Court",'EC4Y 7BE','London','UK'])
customerAddress.append(["Temple, King's Bench Walk",'EC4Y 7DB','London','UK'])
customerAddress.append(["Temple, Middle Temple Lane",'EC4Y 9AA','London','UK'])
customerAddress.append(["Temple, New Court",'EC4Y 9BE','London','UK'])
customerAddress.append(["Temple, Paper Buildings",'EC4Y 7EP','London','UK'])
customerAddress.append(["Temple, Plowden Buildings",'EC4Y 9BU','London','UK'])
customerAddress.append(["Temple, Pump Court",'EC4Y 7AB','London','UK'])
customerAddress.append(["Temple, Queen Elizabeth Buildings",'EC4Y 9BS','London','UK'])
customerAddress.append(["Temple, Temple Gardens",'EC4Y 9AU','London','UK'])
customerAddress.append(["The City Centre, Basinghall Street",'EC2V 5AG','London','UK'])
customerAddress.append(["The Monument Building, Monument Street",'EC3R 8AF','London','UK'])
customerAddress.append(["Threadneedle Street",'EC2R 8AR','London','UK'])
customerAddress.append(["Threadneedle Walk",'EC2R 8HG','London','UK'])
customerAddress.append(["Throgmorton Avenue",'EC2N 2BY','London','UK'])
customerAddress.append(["Throgmorton Street",'EC2N 2AD','London','UK'])
customerAddress.append(["Tokenhouse Yard",'EC2R 7AS','London','UK'])
customerAddress.append(["Took's Court",'EC4A 1LB','London','UK'])
customerAddress.append(["Tower Hill",'EC3N 4AB','London','UK'])
customerAddress.append(["Tower Hill Terrace",'EC3N 4EE','London','UK'])
customerAddress.append(["Tower Pier",'EC3N 4DT','London','UK'])
customerAddress.append(["Tower Place",'EC3R 5BT','London','UK'])
customerAddress.append(["Tower Place East",'EC3R 5BS','London','UK'])
customerAddress.append(["Trig Lane",'EC4V 3QQ','London','UK'])
customerAddress.append(["Trinity Square",'EC3N 4AA','London','UK'])
customerAddress.append(["Trump Street",'EC2V 8AF','London','UK'])
customerAddress.append(["Tudor Street",'EC4Y 0AA','London','UK'])
customerAddress.append(["Undershaft",'EC3A 8EE','London','UK'])
customerAddress.append(["Upper Cheapside Passage",'EC2V 6AG','London','UK'])
customerAddress.append(["Upper Thames Street",'EC4R 3TA','London','UK'])
customerAddress.append(["Victoria Avenue",'EC2M 4NS','London','UK'])
customerAddress.append(["Victoria Embankment",'EC4Y 0DS','London','UK'])
customerAddress.append(["Vine Street",'EC3N 2DB','London','UK'])
customerAddress.append(["Walbrook",'EC4N 8AF','London','UK'])
customerAddress.append(["Wardrobe Place",'EC4V 5AF','London','UK'])
customerAddress.append(["Warwick Lane",'EC4M 7BP','London','UK'])
customerAddress.append(["Watling Street",'EC4M 9BB','London','UK'])
customerAddress.append(["Well Court",'EC4M 9DN','London','UK'])
customerAddress.append(["White Hart Street",'EC4M 7DW','London','UK'])
customerAddress.append(["White Lion Court",'EC3V 3NP','London','UK'])
customerAddress.append(["White Lyon Court",'EC2Y 8EA','London','UK'])
customerAddress.append(["Whitecross Place",'EC2M 2PB','London','UK'])
customerAddress.append(["Whitefriars Street",'EC4Y 8BH','London','UK'])
customerAddress.append(["Whittington Avenue",'EC3V 1LE','London','UK'])
customerAddress.append(["Wilson Street",'EC2M 2SJ','London','UK'])
customerAddress.append(["Wine Office Court",'EC4A 3BY','London','UK'])
customerAddress.append(["Wood Street",'EC2V 6DL','London','UK'])
customerAddress.append(["Wormwood Street",'EC2M 1RP','London','UK'])



print(customerAddress)
print(len(customerAddress))


def rnd_list(mylist):
  #define new empty list
  new_list=[]
  while mylist:
    # Use the random.choice() function to randomly select an element from the list
    rnd_element = random.choice(mylist)
    mylist.remove(rnd_element)
    new_list.append(rnd_element)
  return new_list

newlist_firstname= rnd_list(firstname)
newlist_lastname= rnd_list(lastname)
newlist_customerAddress= rnd_list(customerAddress)


fullList = [[]]
i=0
numRecord=1500
for i in range(max( len(newlist_firstname),len(newlist_lastname),numRecord ) ):
  if i == len(newlist_firstname):
    # reorganize the order of the list items
    random.shuffle(newlist_firstname) 
  if i == len(newlist_lastname):
    random.shuffle(newlist_lastname)
  if i == len(newlist_lastname):
     random.shuffle(newlist_lastname)
  fullList.append([newlist_firstname[i % len(newlist_firstname)],
                   newlist_lastname[i % len(newlist_lastname)], 
                   newlist_customerAddress[i % len(newlist_customerAddress)][0], 
                   newlist_customerAddress[i % len(newlist_customerAddress)][1],
                   newlist_customerAddress[i % len(newlist_customerAddress)][2],
                   newlist_customerAddress[i % len(newlist_customerAddress)][3]
                   ])
print(fullList)


inputFile = "users.sql"
# Opening the given file in write mode
with open(inputFile, 'w') as filedata:
   filedata.write('\c movies\n')
   filedata.write('DROP TABLE IF EXISTS customer CASCADE;\n')
   filedata.write('CREATE TABLE IF NOT EXISTS customer\n')
   filedata.write('(customer_id  INT PRIMARY KEY NOT NULL GENERATED BY DEFAULT AS IDENTITY (START WITH 1 INCREMENT BY 1),\n')
   filedata.write('firstname     varchar(40),\n')
   filedata.write('lastname      varchar(40),\n')
   filedata.write('address       varchar(50),\n')
   filedata.write('zip           varchar(10),\n')
   filedata.write('city          varchar(10),\n')
   filedata.write('country       varchar(10)\n')
   filedata.write(');\n')
   filedata.write('INSERT INTO customer(firstname,lastname,address,zip,city,country)\n')
   filedata.write('VALUES\n')
   # Traverse in each element of the input list 
   for i in range(1,len(fullList),1):
    str0=str(fullList[i][0]).replace("'", "''")
    str1=str(fullList[i][1]).replace("'", "''")
    str2=str(fullList[i][2]).replace("'", "''")
    str3=str(fullList[i][3]).replace("'", "''")
    str4=str(fullList[i][4]).replace("'", "''")
    str5=str(fullList[i][5]).replace("'", "''")

    # Writing each element of the list into the file
    # Here “%s\n” % syntax is used to move to the next line after adding an item to the file.
    if i !=  (len(fullList)-1):
      filedata.write('(\'{0}\', \'{1}\', \'{2}\', \'{3}\' ,\'{4}\', \'{5}\'),\n'.format(str0,str1,str2,str3, str4, str5) )
    elif i ==  (len(fullList)-1):
      filedata.write('(\'{0}\', \'{1}\', \'{2}\', \'{3}\' ,\'{4}\', \'{5}\');\n'.format(str0,str1,str2,str3, str4, str5) )
# Closing the input file
filedata.close()

print('-----------------------')
for row in fullList:
    for element in row:
        print(element, end=" ")
    # CR/LF
    print()
