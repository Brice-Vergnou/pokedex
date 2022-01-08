##### RAN ONLY ONCE TO GET ALL POKEMON NAMES AND SELECT THEM ######
def get_names():
       pokemon_names = requests.get("https://cdn.pikalytics.com/images/datasets/pokemon_v3.js?v=1")
       pokemon_names = pokemon_names.text[25:-4].replace("//", "").replace("\'","").split(",")
       pokemon_names = list(map(lambda x: x[5:], pokemon_names))
       tmp = pokemon_names
       with open("data_dex.py", "w") as f:
           f.write(str(pokemon_names))

dex = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard',
       'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill',
       'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Rattata-Alola', 'Raticate',
       'Raticate-Alola', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu',
       'Raichu-Alola', 'Sandshrew', 'Sandshrew-Alola', 'Sandslash',
       'Sandslash-Alola', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Clefairy',
       'Clefable', 'Vulpix', 'Vulpix-Alola', 'Ninetales', 'Ninetales-Alola', 'Jigglypuff', 'Wigglytuff', 'Zubat',
       'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Diglett-Alola',
       'Dugtrio', 'Dugtrio-Alola', 'Meowth', 'Meowth-Alola', 'Meowth-Galar', 'Persian', 'Persian-Alola',
       'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra',
       'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout',
       'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Geodude-Alola', 'Graveler', 'Graveler-Alola',
       'Golem', 'Golem-Alola', 'Ponyta', 'Ponyta-Galar', 'Rapidash', 'Rapidash-Galar', 'Slowpoke', 'Slowpoke-Galar',
       'Slowbro', 'Slowbro-Galar', 'Magnemite', 'Magneton', 'Farfetchd', 'Farfetchd-Galar', 'Doduo',
       'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Grimer-Alola', 'Muk', 'Muk-Alola', 'Shellder', 'Cloyster', 'Gastly',
       'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler',
       'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Exeggutor-Alola', 'Cubone', 'Marowak',
       'Marowak-Alola', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing',
       'Weezing-Galar', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra',
       'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Mr. Mime-Galar', 'Scyther', 'Jynx', 'Electabuzz',
       'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras',
       'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte',
       'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno',
       'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew',
       'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr',
       'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou',
       'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep',
       'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip',
       'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon',
       'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce',
       'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle',
       'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine',
       'Corsola', 'Corsola-Galar', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom',
       'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop',
       'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar',
       'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile',
       'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert',
       'Poochyena', 'Mightyena', 'Zigzagoon', 'Zigzagoon-Galar', 'Linoone', 'Linoone-Galar', 'Wurmple', 'Silcoon',
       'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow',
       'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain',
       'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred',
       'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye',
       'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham',
       'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin',
       'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt',
       'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu',
       'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish',
       'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform',
       'Kecleon', 'Shuppet', 'Banette', 'Duskull',
       'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal',
       'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence',
       'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias',
       'Latios', 'Kyogre', 'Groudon', 'Rayquaza',
       'Jirachi', 'Deoxys', 'Deoxys-Attack', 'Deoxys-Defense', 'Deoxys-Speed', 'Turtwig', 'Grotle',
       'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia',
       'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade',
       'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam',
       'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim',
       'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius',
       'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly',
       'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax',
       'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak',
       'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone',
       'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon',
       'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom',
       'Rotom-Heat', 'Rotom-Wash', 'Rotom-Frost', 'Rotom-Fan', 'Rotom-Mow', 'Uxie', 'Mesprit', 'Azelf', 'Dialga',
       'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai',
       'Shaymin', 'Arceus', 'Arceus-Bug', 'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric',
       'Arceus-Fairy', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying', 'Arceus-Ghost', 'Arceus-Grass',
       'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic', 'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water',
       'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott',
       'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear',
       'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle',
       'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino',
       'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk',
       'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil',
       'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka',
       'Darumaka-Galar', 'Darmanitan', 'Darmanitan-Galar', 'Maractus',
       'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Yamask-Galar', 'Cofagrigus', 'Tirtouga',
       'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino',
       'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna',
       'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus',
       'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink',
       'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent',
       'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk',
       'Stunfisk-Galar', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant',
       'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta',
       'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Tornadus-Therian', 'Thundurus',
       'Thundurus-Therian', 'Reshiram', 'Zekrom', 'Landorus', 'Landorus-Therian', 'Kyurem', 'Kyurem-Black',
       'Kyurem-White', 'Keldeo', 'Meloetta', 'Genesect', 'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen',
       'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling',
       'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo',
       'Pyroar', 'Flabebe', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro',
       'Furfrou', 'Espurr', 'Meowstic', 'Meowstic-F', 'Honedge', 'Doublade', 'Aegislash',
       'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp',
       'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus',
       'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant',
       'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal',
       'Zygarde', 'Diancie', 'Volcanion',
       'Rowlet', 'Dartrix', 'Decidueye', 'Litten', 'Torracat', 'Incineroar', 'Popplio', 'Brionne', 'Primarina',
       'Pikipek', 'Trumbeak', 'Toucannon', 'Yungoos', 'Gumshoos', 'Grubbin', 'Charjabug', 'Vikavolt',
       'Crabrawler', 'Crabominable',
       'Cutiefly', 'Ribombee', 'Rockruff', 'Lycanroc', 'Lycanroc-Midnight',
       'Lycanroc-Dusk', 'Wishiwashi', 'Mareanie', 'Toxapex', 'Mudbray', 'Mudsdale', 'Dewpider',
       'Araquanid', 'Fomantis', 'Lurantis', 'Morelull', 'Shiinotic', 'Salandit',
       'Salazzle', 'Stufful', 'Bewear', 'Bounsweet', 'Steenee', 'Tsareena', 'Comfey', 'Oranguru',
       'Passimian', 'Wimpod', 'Golisopod', 'Sandygast', 'Palossand', 'Pyukumuku', 'Type: Null', 'Silvally',
       'Silvally-Bug', 'Silvally-Dark', 'Silvally-Dragon', 'Silvally-Electric', 'Silvally-Fairy', 'Silvally-Fighting',
       'Silvally-Fire', 'Silvally-Flying', 'Silvally-Ghost', 'Silvally-Grass', 'Silvally-Ground', 'Silvally-Ice',
       'Silvally-Poison', 'Silvally-Psychic', 'Silvally-Rock', 'Silvally-Steel', 'Silvally-Water', 'Minior',
       'Komala', 'Turtonator', 'Togedemaru', 'Mimikyu',
       'Bruxish', 'Drampa', 'Dhelmise', 'Jangmo-o', 'Hakamo-o', 'Kommo-o',
       'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala',
       'Nihilego', 'Buzzwole', 'Pheromosa', 'Xurkitree', 'Celesteela', 'Kartana', 'Guzzlord', 'Necrozma',
       'Necrozma-Dusk-Mane', 'Necrozma-Dawn-Wings', 'Magearna', 'Magearna-Original', 'Marshadow',
       'Poipole', 'Naganadel', 'Stakataka', 'Blacephalon', 'Zeraora', 'Meltan', 'Melmetal', 'Grookey',
       'Thwackey', 'Rillaboom', 'Scorbunny', 'Raboot', 'Cinderace', 'Sobble', 'Drizzile', 'Inteleon', 'Skwovet',
       'Greedent', 'Rookidee', 'Corvisquire', 'Corviknight', 'Blipbug', 'Dottler', 'Orbeetle',
       'Nickit', 'Thievul', 'Gossifleur', 'Eldegoss', 'Wooloo', 'Dubwool', 'Chewtle', 'Drednaw',
       'Yamper', 'Boltund', 'Rolycoly', 'Carkol', 'Coalossal', 'Applin', 'Flapple',
       'Appletun', 'Silicobra', 'Sandaconda', 'Cramorant',
       'Arrokuda', 'Barraskewda', 'Toxel', 'Toxtricity',
       'Sizzlipede', 'Centiskorch', 'Clobbopus', 'Grapploct', 'Sinistea',
       'Polteageist', 'Hatenna', 'Hattrem', 'Hatterene', 'Impidimp', 'Morgrem', 'Grimmsnarl',
       'Obstagoon', 'Perrserker', 'Cursola', "Sirfetch'd", 'Mr. Rime', 'Runerigus', 'Milcery',
       'Alcremie', 'Falinks', 'Pincurchin', 'Snom', 'Frosmoth', 'Stonjourner', 'Eiscue', 'Indeedee',
       'Indeedee-F', 'Morpeko', 'Cufant', 'Copperajah',
       'Dracozolt', 'Arctozolt', 'Dracovish', 'Arctovish', 'Duraludon', 'Dreepy', 'Drakloak',
       'Dragapult', 'Zacian', 'Zacian-Crowned', 'Zamazenta', 'Zamazenta-Crowned', 'Eternatus', 'Urshifu',
       'Urshifu-Rapid-Strike',
       'Glastrier', 'Spectrier', 'Zapdos-Galar', 'Articuno-Galar', 'Moltres-Galar', 'Regieleki',
       'Regidrago', 'Slowking-Galar', 'Calyrex-Shadow', 'Calyrex-Ice']

##### RUN ONLY ONCE AS WELL, TURN LIST INTO DICT WITH EACH CATEGORY #####
import urllib.request

urls = ["https://www.pikalytics.com/api/p/2021-12/gen8ou-1825/",
        "https://www.pikalytics.com/api/p/2021-12/ss-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8monotype-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8nationaldexag-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8ubers-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8uu-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8ru-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8nu-1760/",
        "https://www.pikalytics.com/api/p/2021-12/gen8pu-1760/"]
categories = ["OverUsed", "VGC", "Monotype", "All", "Ubers", "UnderUsed", "RarelyUsed", "NeverUsed", "PU"]

def list_to_dict():
       pok_cat = {}
       for j, mon in enumerate(dex):
           pok_cat[mon] = []
           for i, url in enumerate(urls):
               print(f"Pokemon {j} {mon} : {categories[i]}     -    {url + mon.lower().replace(' ', '%20')}")
               try:
                   urllib.request.urlopen(url + mon.lower().replace(' ', '%20'), timeout=1)
                   pok_cat[mon].append(categories[i])
               except:
                   print("Doesn't exist")
       with open("data.json", "w") as f:
           f.write(str(pok_cat))

##### ALSO RUN ONCE, REMOVE POKEMONS WITH NO DATA #####
import json

def clean_dict():
       with open("data.json", "r") as f:
           dex = json.load(f)

       tmp = dex
       for mon in list(tmp):
           if dex[mon] == []:
               del dex[mon]

       with open('data_cleaned.json', 'w') as outfile:  # Dont overwrite the previous file in case it doesnt work as intended
           json.dump(dex, outfile)
