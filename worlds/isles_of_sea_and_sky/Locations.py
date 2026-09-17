from BaseClasses import Location
import typing

from .Options import IslesOfSeaAndSkyOptions


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class IslesOfSeaAndSkyAdvancement(Location):
    game: str = "Isles Of Sea And Sky"

def get_locations(options: IslesOfSeaAndSkyOptions):
    # Amalgamate locations from all the tables
    locations = advancement_table.copy()
    if options.shuffle_notes: locations.update(note_table);
    if options.circlet_content_enabled: locations.update(mysterious_table);
    if options.shuffle_meteorites: locations.update(meteorite_table);
    if options.circlet_content_enabled & options.shuffle_meteorites: locations.update(
        circlet_meteorite_table);

    # if False & self.options.enable_locksanity: locations.update(locksanity_table);

    if options.enable_snakesanity:
        locations.update(snakesanity_table)
        if options.circlet_content_enabled: locations.update(mysterious_snakesanity_table);
        if options.shuffle_meteorites: locations.update(meteorite_snakesanity_table);
        if options.circlet_content_enabled & options.shuffle_meteorites: locations.update(circlet_meteorite_snakesanity_table)

    # if False & self.options.include_seashells: locations.update(seashell_table);
    # if False & self.options.include_jellyfish: locations.update(jellyfish_table);
    # if False & self.options.secretsanity: locations.update(secrets_table);
    return locations

advancement_table: dict[str, AdvData] = {
    "Locked A0 - Ancient Rune Stone":               AdvData(112012104, "Locked Key - Turtle"),
    "Stone C0 - Topaz Rune Stone":                  AdvData(101201806, "Stony Cliffs - God Altar"),
    "Water C0 - Sapphire Rune Stone":               AdvData(103201712, "Tidal Reef - God Altar"),
    "Fire C0 - Ruby Rune Stone":                    AdvData(104200107, "Raging Volcano - God Altar"),
    "Wind C2 - Diamond Rune Stone":                 AdvData(105221405, "Frozen Spire"),
    "Serpent A1 - Obsidian Rune Stone":             AdvData(106010410, "Serpent Stacks - Head"),

    "Stone C0 - Topaz Quest Complete":              AdvData(99901201, "Stony Cliffs - God Altar"),
    "Water C0 - Sapphire Quest Complete":           AdvData(99903201, "Tidal Reef - God Altar"),
    "Fire C0 - Ruby Quest Complete":                AdvData(99904201, "Raging Volcano - God Altar"),
    "Wind C2 - Diamond Quest Complete":             AdvData(99905221, "Frozen Spire"),
    "Serpent A1 - Obsidian Quest Complete":         AdvData(106011103, "Serpent Stacks - Head"),

    "Stone Dungeon C1 - Gopher Gloves":             AdvData(102210609, "Stone Dungeon - Gopher Vault"),
    "Water A4 - Frog Flippers":                     AdvData(103041606, "Tidal Reef - South-West"),
    "Fire E0 - Salamander Shirt":                   AdvData(104400804, "Raging Volcano - Phoenix"),
    "Wind A0 - Kite Cloak":                         AdvData(105001805, "Frozen Spire - Post-Rune"),

    "Sanctum A2 - Topaz Shard Hit":                 AdvData(99907021, "Sanctum - Earth Shard"),
    "Sanctum C2 - Sapphire Shard Hit":              AdvData(99907221, "Sanctum - Water Shard"),
    "Sanctum C0 - Ruby Shard Hit":                  AdvData(99907201, "Sanctum - Fire Shard"),
    "Sanctum A0 - Diamond Shard Hit":               AdvData(99907001, "Sanctum - Wind Shard"),

    "Stone E3 - Gold Stone Tablet":                 AdvData(101431110, "Stony Cliffs - Golden Stone"),
    "Stone Dungeon A1 - Blue Stone Tablet":         AdvData(102011309, "Stone Dungeon - West Tunnels"),

    "Fire A0 - Fire Key":                           AdvData(104001504, "Raging Volcano - North-West"),
    "Fire A4 - Fire Key":                           AdvData(104040510, "Raging Volcano - South Coast"),
    "Fire E4 - Fire Key":                           AdvData(104441503, "Raging Volcano - South Coast"),

    #"1 - Egg":         AdvData(991024, "Frozen Spire"), #Broken due to in-game randomness
    #"2 - Egg":         AdvData(991025, "Frozen Spire"), #Broken due to in-game randomness
    #"3 - Egg":         AdvData(991026, "Frozen Spire"), #Broken due to in-game randomness
    #"Wind Key[]":      AdvData(83505440 || 83505040 || 83505400, "Frozen Spire"), #Broken due to in-game randomness

    "Rolling B0 - Big Bell Rung":                   AdvData(99908101, "Rolling Rocks - South-East"),
    "Sunken B1 - Big Bell Rung":                    AdvData(99909111, "Sunken Island - Turtle"),
    "Aggro A1 - Big Bell Rung":                     AdvData(99910011, "Aggro Crag - East"), # Ancient Rune Stone
    "Nunatak A1 - Big Bell Rung":                   AdvData(99911011, "Sea Nunatak - Turtle"),

    "Beast A0 - Phoenix Flute":                     AdvData(116111207, "Beast Ridge - Phoenix"),
    "Shoal A0 - Star Viewing Orb":                  AdvData(114001209, "Eastern Shoal - North-West"),

    # MISC
    "Ancient B2 - Open Ancient Door":               AdvData(100121002, "Sanctum - Turtle"), # Placed in next region for logic
    "Stone Dungeon C2 - Open Topaz Door":           AdvData(102221002, "Stony Cliffs - North-West"),

    "Stone A1 - Tablet Puzzle Clue":                AdvData(101011206, "Stony Cliffs - Phoenix"),
    "Stone A3 - Tablet Puzzle Clue":                AdvData(101030308, "Stony Cliffs - Tablet Slot"),
    "Stone E1 - Tablet Puzzle Clue":                AdvData(101411905, "Stony Cliffs - North-East"),

    "Stone Dungeon A3 - Tablet Puzzle Clue":        AdvData(102031103, "Stone Dungeon - West Tunnels"),
    "Stone Dungeon E1 - Tablet Puzzle Clue":        AdvData(102411706, "Stone Dungeon - Earth Chamber"),
    "Stone Dungeon E3 - Tablet Puzzle Clue":        AdvData(102431410, "Stone Dungeon - South Tunnels"),

    "Beast A1 - Big Bell Stone":                    AdvData(116121206, "Beast Ridge - Bellstone"),
    "Sanctum B1 - Elemental Stone":                 AdvData(107111107, "Sanctum - Peak"),

    #

    "Ancient A1 - Ancient Key":                     AdvData(100011711, "Ancient Isle - Origin"),
    "Ancient A2 - SE - Ancient Key":                AdvData(100020606, "Ancient Isle - Origin"),
    "Ancient A2 - NW - Ancient Key":                AdvData(100020303, "Ancient Isle - Origin"), # Topaz quest
    "Ancient A3 - N - Ancient Key":                 AdvData(100031403, "Ancient Isle - Origin"),
    "Ancient A3 - S - Ancient Key":                 AdvData(100031110, "Ancient Isle - Origin"),
    "Ancient A3 - E - Ancient Key":                 AdvData(100032006, "Ancient Isle - Origin"),
    "Ancient B3 - Ancient Key":                     AdvData(100131706, "Ancient Isle - Origin"),
    "Ancient C1 - Ancient Key":                     AdvData(100211507, "Ancient Isle - Origin"),
    "Ancient C2 - Ancient Key":                     AdvData(100221211, "Ancient Isle - Origin"),
    "Ancient C3 - Ancient Key":                     AdvData(100231806, "Ancient Isle - Origin"),

    "Rolling A0 - Ancient Key":                     AdvData(108000111, "Rolling Rocks - West"),
    "Rolling A1 - Ancient Key":                     AdvData(108011508, "Rolling Rocks - West"),

    "Stone A2 - Ancient Key":                       AdvData(101020909, "Stony Cliffs - Tablet Slot"), # blue & gold tablet
    "Stone B0 - NW1 - Ancient Key":                 AdvData(101100206, "Stony Cliffs - Phoenix"), # 1 ancient key
    "Stone B0 - NW2 - Ancient Key":                 AdvData(101100205, "Stony Cliffs - Phoenix"), # 1 ancient key
    "Stone B0 - NW3 - Ancient Key":                 AdvData(101100204, "Stony Cliffs - Phoenix"), # 1 ancient key
    "Stone B1 - Ancient Key":                       AdvData(101110404, "Stony Cliffs - Phoenix"),
    "Stone B2 - Ancient Key":                       AdvData(101122103, "Stony Cliffs - God Altar"),
    "Stone B4 - Ancient Key":                       AdvData(101141707, "Stony Cliffs - South Star Stone"),
    "Stone C0 - Ancient Key":                       AdvData(101202212, "Stony Cliffs - God Altar"),
    "Stone D3 - Ancient Key":                       AdvData(101330111, "Stony Cliffs - South Coast"),
    "Stone E2 - Ancient Key":                       AdvData(101420103, "Stony Cliffs - God Altar"),  # r rune
    
    "Stone Dungeon B1 - Ancient Key":               AdvData(102111708, "Stone Dungeon - Dirt Chamber"), #gopher gloves
    "Stone Dungeon C1 - Ancient Key":               AdvData(102210411, "Stone Dungeon - Gopher Vault"), #topaz rune, gopher gloves
    "Stone Dungeon D0 - Ancient Key":               AdvData(102301109, "Stone Dungeon - North Tunnels"), #gopher gloves
    "Stone Dungeon D2 - Ancient Key":               AdvData(102320211, "Stone Dungeon - Vault Door"), # t quest
    "Stone Dungeon E2 - Ancient Key":               AdvData(102420803, "Stone Dungeon - Earth Chamber"),

    "Water A0 - E - Ancient Key":                   AdvData(103002110, "Tidal Reef - North-West Low Tide"),
    "Water A0 - S - Ancient Key":                   AdvData(103001712, "Tidal Reef - God Altar"), # frog flippers
    "Water A2 - Ancient Key":                       AdvData(103021007, "Tidal Reef - West Star Stone"), # s quest + (k cloak | 30 star pieces) 
    "Water B3 - Ancient Key":                       AdvData(103132208, "Tidal Reef - God Altar"), # frog flippers
    "Water C0 - Ancient Key":                       AdvData(103200408, "Tidal Reef - God Altar"), # s quest
    "Water C2 - Ancient Key":                       AdvData(103222109, "Tidal Reef - God Altar"),
    "Water C3 - W - Ancient Key":                   AdvData(103230306, "Tidal Reef - God Altar"), # d rune
    "Water C3 - NE1 - Ancient Key":                 AdvData(103231903, "Tidal Reef - Shell Puzzle"), # frog flippers, s quest
    "Water C3 - NE2 - Ancient Key":                 AdvData(103231803, "Tidal Reef - Shell Puzzle"), # frog flippers, s quest
    "Water C3 - NE3 - Ancient Key":                 AdvData(103231703, "Tidal Reef - Shell Puzzle"), # frog flippers, s quest
    "Water C4 - Ancient Key":                       AdvData(103241203, "Tidal Reef - Shell Puzzle"), # shell puzzle, f flippers, s rune?
    "Water D0 - Ancient Key":                       AdvData(103301307, "Tidal Reef - God Altar"), # s rune frog flippers
    "Water D1 - Ancient Key":                       AdvData(103311203, "Tidal Reef - God Altar"), # frog flippers
    "Water D2 - Ancient Key":                       AdvData(103321204, "Tidal Reef - Shell Puzzle"), # s rune, s quest

    "Sunken A0 - Ancient Key":                      AdvData(109001612, "Sunken Island - Turtle"),
    "Sunken B0 - Ancient Key":                      AdvData(109100305, "Sunken Island - Turtle"),
    
    "Fire A1 - SE - Ancient Key":                   AdvData(104011611, "Raging Volcano - God Altar"), # s shirt
    "Fire A1 - SW - Ancient Key":                   AdvData(104011012, "Raging Volcano - God Altar"), # r rune, t rune
    "Fire A1 - NE - Ancient Key":                   AdvData(104012003, "Raging Volcano - Geyser Pass"),
    "Fire A2 - N - Ancient Key":                    AdvData(104022205, "Raging Volcano - God Altar"),
    "Fire A2 - S - Ancient Key":                    AdvData(104022112, "Raging Volcano - God Altar"), # salamander shirt
    "Fire B1 - N1 - Ancient Key":                   AdvData(104110703, "Raging Volcano - Key Triplets"), # r quest
    "Fire B1 - N2 - Ancient Key":                   AdvData(104110803, "Raging Volcano - Key Triplets"), # r quest
    "Fire B1 - N3 - Ancient Key":                   AdvData(104110903, "Raging Volcano - Key Triplets"), # r quest
    "Fire B4 - Ancient Key":                        AdvData(104140607, "Raging Volcano - South Coast"), # r quest
    "Fire C0 - Ancient Key":                        AdvData(104201806, "Raging Volcano - God Altar"), # r quest
    "Fire C1 - NE - Ancient Key":                   AdvData(104212105, "Raging Volcano - God Altar"), # r quest, s shirt
    "Fire C1 - SW - Ancient Key":                   AdvData(104210212, "Raging Volcano - God Altar"), # s shirt
    "Fire C3 - Ancient Key":                        AdvData(104231003, "Raging Volcano - God Altar"), # r quest, r rune
    "Fire D4 - Ancient Key":                        AdvData(104340806, "Raging Volcano - South Coast"), # idol puzzle

    "Aggro B0 - W - Ancient Key":                   AdvData(110100711, "Aggro Crag - East"),
    "Aggro B0 - E - Ancient Key":                   AdvData(110101205, "Aggro Crag - East"),
    
    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Wind A1 - Ancient Key":                        AdvData(105011404, "Frozen Spire - Post-Rune"), # glyph puzzle
    "Wind A3 - Ancient Key":                        AdvData(105031307, "Frozen Spire"), # k cloak
    "Wind B1 - Ancient Key":                        AdvData(105111603, "Frozen Spire - Post-Rune"), # double check req
    "Wind C2 - Ancient Key":                        AdvData(105220705, "Frozen Spire"), # d quest
    "Wind C4 - Ancient Key":                        AdvData(105242109, "Frozen Spire"),
    "Wind D3 - Ancient Key":                        AdvData(105331507, "Frozen Spire"), # k cloak
    "Wind D4 - E - Ancient Key":                    AdvData(105341405, "Frozen Spire - Post-Rune"), # s rune
    "Wind D4 - NW1 - Ancient Key":                  AdvData(105340304, "Frozen Spire"), # d quest
    "Wind D4 - NW2 - Ancient Key":                  AdvData(105340404, "Frozen Spire"), # d quest
    "Wind D4 - NW3 - Ancient Key":                  AdvData(105340504, "Frozen Spire"), # d quest
    "Wind E2 - S - Ancient Key":                    AdvData(105421609, "Frozen Spire"), # d quest
    "Wind E2 - NE - Ancient Key":                   AdvData(105422203, "Frozen Spire"), # d quest
    "Wind E4 - E - Ancient Key":                    AdvData(105440806, "Frozen Spire - Post-Rune"), # d rune
    "Wind E4 - SW - Ancient Key":                   AdvData(105440310, "Frozen Spire - Post-Rune"), # k cloak, d quest

    "Nunatak A1 - Ancient Key":                     AdvData(111011905, "Sea Nunatak - Turtle"), # ancient rune
    "Nunatak B1 - Ancient Key":                     AdvData(111110806, "Sea Nunatak - Turtle"),

    "Tropic A1 - Ancient Key":                      AdvData(113010608, "Star Tropic - Treasure Shore"), # ancient rune

    #77 keys

    "Stone B0 - Topaz":                             AdvData(101101510, "Stony Cliffs - Phoenix"),
    "Stone B1 - Topaz":                             AdvData(101110112, "Stony Cliffs - Phoenix"),
    "Stone B2 - Topaz":                             AdvData(101121212, "Stony Cliffs - South Coast"),
    "Stone C0 - Topaz":                             AdvData(101200506, "Stony Cliffs - God Altar"),
    "Stone C2 - W - Topaz":                         AdvData(101220904, "Stony Cliffs - South Coast"),
    "Stone C2 - E - Topaz":                         AdvData(101221504, "Stony Cliffs - God Altar"),
    "Stone C3 - N - Topaz":                         AdvData(101232107, "Stony Cliffs - God Altar"),
    "Stone C3 - S - Topaz":                         AdvData(101232110, "Stony Cliffs - God Altar"),
    "Stone D2 - Topaz":                             AdvData(101321605, "Stony Cliffs - God Altar"),
    "Stone Dungeon C1 - Topaz":                     AdvData(102211512, "Stone Dungeon - Dirt Chamber"), #Rq: gopher gloves
    "Rolling A0 - Topaz":                           AdvData(108002205, "Rolling Rocks - West"), #Rq: topaz quest, 7 stars
    "Tropic A1 - Topaz":                            AdvData(113011205, "Star Tropic - Treasure Shore"), # all legendaries

    "Water A1 - Sapphire":                          AdvData(103011909, "Tidal Reef - God Altar"), #frog flippers
    "Water B2 - N - Sapphire":                      AdvData(103121703, "Tidal Reef - God Altar"),
    "Water B2 - S - Sapphire":                      AdvData(103120911, "Tidal Reef - God Altar"), # Ancient Key
    "Water C0 - Sapphire":                          AdvData(103202012, "Tidal Reef - God Altar"), # s rune
    "Water C2 - N - Sapphire":                      AdvData(103220803, "Tidal Reef - God Altar"),  # s quest
    "Water C2 - W - Sapphire":                      AdvData(103220306, "Tidal Reef - God Altar"),
    "Water D1 - Sapphire":                          AdvData(103311811, "Tidal Reef - East"),
    "Water D2 - N - Sapphire":                      AdvData(103320503, "Tidal Reef - Shell Puzzle"), #s rune stone
    "Water D2 - W - Sapphire":                      AdvData(103320206, "Tidal Reef - God Altar"),
    "Water D3 - Sapphire":                          AdvData(103331803, "Tidal Reef - Shell Puzzle"), # Ancient Key
    "Sunken B0 - Sapphire":                         AdvData(109101706, "Sunken Island - Turtle"), #sapphire quest, 21 stars
    "Tropic A1 - Sapphire":                         AdvData(113011305, "Star Tropic - Treasure Shore"), # all legendaries

    "Fire A3 - N - Ruby":                           AdvData(104031005, "Raging Volcano - Triple Ruby Pit"),
    "Fire A3 - S - Ruby":                           AdvData(104031211, "Raging Volcano - Triple Ruby Pit"),
    "Fire A3 - NW - Ruby":                          AdvData(104030703, "Raging Volcano - South Coast"), # ancient key
    "Fire B2 - Ruby":                               AdvData(104122109, "Raging Volcano - God Altar"),
    "Fire C0 - Ruby":                               AdvData(104200112, "Raging Volcano - God Altar"), # ruby rune stone
    "Fire C2 - Ruby":                               AdvData(104220504, "Raging Volcano - God Altar"),
    "Fire D0 - Ruby":                               AdvData(104300603, "Raging Volcano - Phoenix"), # salamander shirt
    "Fire D1 - Ruby":                               AdvData(104311210, "Raging Volcano - God Altar"), # ruby rune stone or enter from phoenix (fire elementals)
    "Fire D2 - E - Ruby":                           AdvData(104321804, "Raging Volcano - God Altar"),
    "Fire D2 - W - Ruby":                           AdvData(104321004, "Raging Volcano - God Altar"), # ancient key
    "Aggro B1 - Ruby":                              AdvData(110110511, "Aggro Crag - East"), # ruby quest, 35 stars
    "Tropic A1 - Ruby":                             AdvData(113011304, "Star Tropic - Treasure Shore"), # all legendaries

    "Wind B2 - Diamond":                            AdvData(105120303, "Frozen Spire"),
    "Wind C1 - W - Diamond":                        AdvData(105210910, "Frozen Spire - Post-Rune"), # d rune stone
    "Wind C1 - E - Diamond":                        AdvData(105211110, "Frozen Spire - Post-Rune"), # d rune stone
    "Wind C2 - Diamond":                            AdvData(105220906, "Frozen Spire - Post-Rune"), # diamond rune stone
    "Wind C3 - Diamond":                            AdvData(105230603, "Frozen Spire - Post-Rune"), # diamond quest complete
    "Wind C4 - Diamond":                            AdvData(105241004, "Frozen Spire"),
    "Wind D1 - E - Diamond":                        AdvData(105311612, "Frozen Spire - Post-Rune"), # d rune stone
    "Wind D1 - W - Diamond":                        AdvData(105310210, "Frozen Spire - Post-Rune"), # d rune stone
    "Wind D2 - Diamond":                            AdvData(105321303, "Frozen Spire"),
    "Wind D4 - Diamond":                            AdvData(105340803, "Frozen Spire"),
    "Nunatak B0 - Diamond":                         AdvData(111101003, "Sea Nunatak - Turtle"), # diamond quest complete
    "Tropic A1 - Diamond":                          AdvData(113011204, "Star Tropic - Treasure Shore"), # all legendaries

    "Stone A2 - Obsidian":                          AdvData(101021409, "Stony Cliffs - Tablet Slot"),  # stone tablet blue, tablet gold
    "Stone D1 - Obsidian":                          AdvData(101312204, "Stony Cliffs - God Altar"),
    "Water C4 - Obsidian":                          AdvData(103241803, "Tidal Reef - Shell Puzzle"),  # shell puzzle, f flippers
    "Water D0 - Obsidian":                          AdvData(103301004, "Tidal Reef - God Altar"), 
    "Fire D4 - Obsidian":                           AdvData(104341606, "Raging Volcano - South Coast"),  # idol puzzle
    "Fire E0 - Obsidian":                           AdvData(104401511, "Raging Volcano - Hot Spring"),  # salamander shirt
    "Wind B0 - Obsidian":                           AdvData(105100205, "Frozen Spire - Post-Rune"),
    "Wind A1 - Obsidian":                           AdvData(105010904, "Frozen Spire - Post-Rune"), # Glyph Puzzle
    "Rolling A1 - Obsidian":                        AdvData(108011803, "Rolling Rocks - West"),  # gopher gloves, 7 stars
    "Sunken A0 - Obsidian":                         AdvData(109002010, "Sunken Island - Turtle"),  # frog flippers
    "Aggro B0 - Obsidian":                          AdvData(110100205, "Aggro Crag - North-West"),
    "Nunatak B1 - Obsidian":                        AdvData(111111705, "Sea Nunatak - Turtle"),  # diamond quest
    "Serpent A1 - Obsidian":                        AdvData(106010412, "Serpent Stacks - Head"),  # Obsidian rune stone
    "Lost A1 - Obsidian":                           AdvData(115011106, "Lost Landing - West"),  # Ancient Key

    # All 120 Star Pieces are locations!
    "Ancient A1 - Star Piece":                      AdvData(100011708, "Ancient Isle - West"),
    "Ancient B1 - Star Piece":                      AdvData(100110812, "Ancient Isle - West"),
    "Ancient C0 - Star Piece":                      AdvData(100201308, "Ancient Isle - Origin"),

    "Stone A1 - Star Piece":                        AdvData(101010512, "Stony Cliffs - West Star Stone"), # 5 stars
    "Stone B2 - Star Piece":                        AdvData(101121405, "Stony Cliffs - South Coast"), # t quest
    "Stone B3 - Star Piece":                        AdvData(101130212, "Stony Cliffs - Tablet Slot"), # t quest
    "Stone B4 - Star Piece":                        AdvData(101140303, "Stony Cliffs - South Star Stone"), # g globes t quest
    "Stone C0 - Star Piece":                        AdvData(101200112, "Stony Cliffs - God Altar"), # t quest
    "Stone C1 - Star Piece":                        AdvData(101212011, "Stony Cliffs - God Altar"), # t quest
    "Stone C4 - Star Piece":                        AdvData(101240208, "Stony Cliffs - South Star Stone"), # g gloves t quest
    "Stone D3 - N - Star Piece":                    AdvData(101332203, "Stony Cliffs - Windy Cliff"), # 20 star pieces, t quest, d quest. g gloves
    "Stone D3 - S - Star Piece":                    AdvData(101332007, "Stony Cliffs - Windy Cliff"), # 20 star pieces, t quest, d quest
    "Stone E1 - Star Piece":                        AdvData(101410412, "Stony Cliffs - God Altar"),
    "Stone E4 - Star Piece":                        AdvData(101440203, "Stony Cliffs - South-East"),
    "Stone Dungeon B1 - Star Piece":                AdvData(102110412, "Stone Dungeon - Dirt Chamber"), # g gloves
    "Stone Dungeon C1 - Star Piece":                AdvData(102210506, "Stone Dungeon - Gopher Vault"), # g gloves
    "Stone Dungeon C3 - Star Piece":                AdvData(102230803, "Stone Dungeon - Vault Door"), # t quest
    "Stone Dungeon E1 - Star Piece":                AdvData(102410905, "Stone Dungeon - Earth Chamber"), # t quest
    "Stone Dungeon E2 - Star Piece":                AdvData(102421209, "Stone Dungeon - East Tunnels"), # g gloves, f flippers

    "Stone D1 - Music Puzzle Star Piece 1":         AdvData(99901311, "Stony Cliffs - God Altar"), # t rune, t quest, ancient key
    "Stone D1 - Music Puzzle Star Piece 2":         AdvData(99901312, "Stony Cliffs - God Altar"), # t rune, t quest, ancient key
    "Stone D1 - Music Puzzle Star Piece 3":         AdvData(99901313, "Stony Cliffs - God Altar"), # t rune, t quest, ancient key
    "Stone A2 - Tablet Puzzle Star Piece":          AdvData(99901021, "Stony Cliffs - Tablet Slot"), # blue & gold tablet

    "Water A0 - Star Piece":                        AdvData(103002003, "Tidal Reef - North-West"),
    "Water A2 - N - Star Piece":                    AdvData(103020803, "Tidal Reef - West Star Stone"),
    "Water A2 - S - Star Piece":                    AdvData(103021312, "Tidal Reef - West Star Stone"), # f flippers s quest
    "Water A4 - Star Piece":                        AdvData(103042108, "Tidal Reef - Phoenix"), # f flippers
    "Water B1 - Star Piece":                        AdvData(103110412, "Tidal Reef - God Altar"), # s quest
    "Water B4 - Star Piece":                        AdvData(103142208, "Tidal Reef - Phoenix"),
    "Water C0 - Star Piece":                        AdvData(103201807, "Tidal Reef - God Altar"), # s quest
    "Water C1 - W - Star Piece":                    AdvData(103210204, "Tidal Reef - God Altar"), # Ancient Key x3
    "Water C1 - E - Star Piece":                    AdvData(103211207, "Tidal Reef - God Altar"),
    "Water C2 - Star Piece":                        AdvData(103222207, "Tidal Reef - God Altar"), # s quest
    "Water D2 - Star Piece":                        AdvData(103322012, "Tidal Reef - East"), # f flippers, s shirt
    "Water D3 - Star Piece":                        AdvData(103331910, "Tidal Reef - Shell Puzzle"), # f flippers, ancient key
    "Water E0 - W - Star Piece":                    AdvData(103400109, "Tidal Reef - East"), # f flippers | k cloak 
    "Water E0 - E - Star Piece":                    AdvData(103402005, "Tidal Reef - East"), # s quest & f flippers
    "Water E2 - Star Piece":                        AdvData(103422008, "Tidal Reef - East"), # f flippers
    "Water E3 - NE - Star Piece":                   AdvData(103432204, "Tidal Reef - East"), # s quest, t quest
    "Water E3 - SW - Star Piece":                   AdvData(103430411, "Tidal Reef - East"), # s quest, t quest

    "Water B0 - Music Puzzle Star Piece 1":         AdvData(99903101, "Tidal Reef - God Altar"), # s quest
    "Water B0 - Music Puzzle Star Piece 2":         AdvData(99903102, "Tidal Reef - God Altar"), # s quest
    "Water B0 - Music Puzzle Star Piece 3":         AdvData(99903103, "Tidal Reef - God Altar"), # s quest
    "Water C4 - Shell Puzzle Star Piece":           AdvData(99903241, "Tidal Reef - Shell Puzzle"), # shell puzzle, f flippers

    "Fire B3 - Star Piece":                         AdvData(104132211, "Raging Volcano - Above Volcano"),
    "Fire B4 - Star Piece":                         AdvData(104142005, "Raging Volcano - South Coast"), # r quest
    "Fire C0 - Star Piece":                         AdvData(104202107, "Raging Volcano - God Altar"),
    "Fire C1 - Star Piece":                         AdvData(104210310, "Raging Volcano - God Altar"),
    "Fire C3 - Star Piece":                         AdvData(104231507, "Raging Volcano - Idol Room West"),
    "Fire D1 - N - Star Piece":                     AdvData(104310105, "Raging Volcano - Phoenix"), # r quest
    "Fire D1 - S - Star Piece":                     AdvData(104310109, "Raging Volcano - God Altar"), # ancient key x3
    "Fire D3 - W - Star Piece":                     AdvData(104330507, "Raging Volcano - Below Hot Spring"), # r quest
    "Fire D3 - S - Star Piece":                     AdvData(104331312, "Raging Volcano - Below Hot Spring"), # r quest, s shirt?
    "Fire D4 - Star Piece":                         AdvData(104340404, "Raging Volcano - Below Hot Spring"), # r quest, s shirt?, k cloak
    "Fire E0 - Star Piece":                         AdvData(104401704, "Raging Volcano - Phoenix"), # s shirt
    "Fire E1 - W - Star Piece":                     AdvData(104410106, "Raging Volcano - Phoenix"), # r quest
    "Fire E1 - E - Star Piece":                     AdvData(104411108, "Raging Volcano - Hot Spring"), # s shirt 
    "Fire E3 - W - Star Piece":                     AdvData(104430106, "Raging Volcano - Below Hot Spring"),
    "Fire E3 - S - Star Piece":                     AdvData(104431212, "Raging Volcano - Below Hot Spring"), # r quest, s quest
    "Fire E3 - SE - Star Piece":                    AdvData(104431512, "Raging Volcano - Below Hot Spring"), # r quest, s quest

    "Fire B3 - Music Puzzle Star Piece 1":          AdvData(99904131, "Raging Volcano - Lyre"), # r quest
    "Fire B3 - Music Puzzle Star Piece 2":          AdvData(99904132, "Raging Volcano - Lyre"), # r quest
    "Fire B3 - Music Puzzle Star Piece 3":          AdvData(99904133, "Raging Volcano - Lyre"), # r quest
    "Fire D4 - Idol Puzzle Star Piece":             AdvData(99904341, "Raging Volcano - South Coast"), # idol puzzle

    # locations might be broken due to in-game randomness
    "Wind A0 - Star Piece":                         AdvData(105001106, "Frozen Spire - Post-Rune"), # k cloak
    "Wind A3 - Star Piece":                         AdvData(105031012, "Frozen Spire"), # k cloak
    "Wind B0 - Star Piece":                         AdvData(105101606, "Frozen Spire - Post-Rune"),
    "Wind B1 - Star Piece":                         AdvData(105111309, "Frozen Spire"),
    "Wind B2 - S - Star Piece":                     AdvData(105120212, "Frozen Spire"),
    "Wind B2 - N - Star Piece":                     AdvData(105121703, "Frozen Spire"), # d quest
    "Wind B3 - Star Piece":                         AdvData(105131907, "Frozen Spire"), # d quest
    "Wind C2 - Star Piece":                         AdvData(105220204, "Frozen Spire"), # d quest
    "Wind C3 - NE - Star Piece":                    AdvData(105231703, "Frozen Spire"), # d rune
    "Wind C3 - SW - Star Piece":                    AdvData(105230211, "Frozen Spire"), # d rune
    "Wind D2 - Star Piece":                         AdvData(105320208, "Frozen Spire"), # k cloak
    "Wind D4 - Star Piece":                         AdvData(105341904, "Frozen Spire"),
    "Wind E1 - W - Star Piece":                     AdvData(105410209, "Frozen Spire - Post-Rune"), # k cloak, g gloves
    "Wind E1 - SE - Star Piece":                    AdvData(105410911, "Frozen Spire - Post-Rune"), # d quest, r quest
    "Wind E1 - SW - Star Piece":                    AdvData(105410711, "Frozen Spire - Post-Rune"), # d quest, r quest
    "Wind E2 - Star Piece":                         AdvData(105421004, "Frozen Spire"), # d quest
    "Wind E4 - Star Piece":                         AdvData(105440510, "Frozen Spire - Post-Rune"), # k cloak

    "Wind B4 - Music Puzzle Star Piece 1":          AdvData(99905141, "Frozen Spire - Post-Rune"), # d quest
    "Wind B4 - Music Puzzle Star Piece 2":          AdvData(99905142, "Frozen Spire - Post-Rune"), # d quest
    "Wind B4 - Music Puzzle Star Piece 3":          AdvData(99905143, "Frozen Spire - Post-Rune"), # d quest
    "Wind A1 - Glyph Puzzle Star Piece":            AdvData(99905011, "Frozen Spire - Post-Rune"), # glyph puzzle

    "Rolling A0 - Star Piece":                      AdvData(108000605, "Rolling Rocks - West"), # 7 stars, t quest
    "Rolling B0 - Star Piece":                      AdvData(108101107, "Rolling Rocks - North-East"), # g gloves
    "Rolling B1 - Star Piece":                      AdvData(108111107, "Rolling Rocks - South-East"), # Ancient Key x3
    "Rolling B0 - Big Bell Star Piece":             AdvData(99908102, "Ancient Isle - Origin"), # rolling big bell

    "Sunken A1 - Star Piece":                       AdvData(109011306, "Sunken Island - Turtle"), # ancient rune
    "Sunken B0 - Star Piece":                       AdvData(109101704, "Sunken Island - Turtle"), # 21 stars, s quest
    "Sunken B1 - Big Bell Star Piece":              AdvData(99909112, "Ancient Isle - Origin"), # sunken big bell

    "Aggro A1 - Star Piece":                        AdvData(110010409, "Aggro Crag - South-West"), # ancient key x3
    "Aggro B1 - Star Piece":                        AdvData(110111511, "Aggro Crag - East"), # 35 star, r quest
    "Aggro A1 - Big Bell Star Piece":               AdvData(99910012, "Ancient Isle - Origin"), # aggro big bell

    "Nunatak A0 - Star Piece":                      AdvData(111001310, "Sea Nunatak - Turtle"), # ancient rune
    "Nunatak B0 - Star Piece":                      AdvData(111101903, "Sea Nunatak - Turtle"), # 49 stars, d quest
    "Nunatak A1 - Big Bell Star Piece":             AdvData(99911012, "Ancient Isle - Origin"), # nunatak big bell

    "Lost B1 - Star Piece":                         AdvData(115111209, "Lost Landing - Turtle"),

    "Shoal A0 - Star Piece":                        AdvData(114001711, "Eastern Shoal - North-West"), # f flippers

    "Tropic A0 - Star Piece":                       AdvData(113001911, "Star Tropic - West"),
    "Tropic A1 - Star Piece 1":                     AdvData(113010803, "Star Tropic - Treasure Shore"), # g gloves
    "Tropic A1 - Star Piece 2":                     AdvData(113010905, "Star Tropic - Treasure Shore"), # g gloves, s shirt,
    "Tropic A1 - Star Piece 3":                     AdvData(113011003, "Star Tropic - Treasure Shore"), # g gloves, s shirt, f flippers
    "Tropic A1 - Star Piece 4":                     AdvData(113011105, "Star Tropic - Treasure Shore"), # g gloves, s shirt, f flippers, k cloak
    "Tropic B0 - S - Star Piece":                   AdvData(113100508, "Star Tropic - Star Pocket"),
    "Tropic B0 - N - Star Piece":                   AdvData(113100904, "Star Tropic - West"), # o rune

    "Serpent A1 - W - Star Piece":                  AdvData(106010311, "Serpent Stacks - Head"), # o quest
    "Serpent A1 - N - Star Piece":                  AdvData(106011403, "Serpent Stacks - Head"), # o quest
    "Serpent A2 - Star Piece":                      AdvData(106021904, "Serpent Stacks - Turtle"), # o quest
    "Serpent A3 - Star Piece":                      AdvData(106031705, "Serpent Stacks - Turtle"), # 
    "Serpent A4 - NW - Star Piece":                 AdvData(106040304, "Serpent Stacks - Core"), # o quest, t quest
    "Serpent A4 - N - Star Piece":                  AdvData(106040903, "Serpent Stacks - Core"), # o quest, t quest
    "Serpent A6 - W - Star Piece":                  AdvData(106060204, "Serpent Stacks - Core"), # s quest, o quest
    "Serpent A6 - E - Star Piece":                  AdvData(106062111, "Serpent Stacks - Core"), # s quest, o quest
    "Serpent A7 - E - Star Piece":                  AdvData(106072212, "Serpent Stacks - Tail"), # r quest
    "Serpent A7 - W - Star Piece":                  AdvData(106070212, "Serpent Stacks - Tail"), # r quest
    "Serpent A8 - S - Star Piece":                  AdvData(106082011, "Serpent Stacks - Tail"), # d quest
    "Serpent A8 - N - Star Piece":                  AdvData(106082009, "Serpent Stacks - Tail"), # d quest

    "Locked A0 - Star Piece":                       AdvData(112012012, "Locked Key - Turtle"),

}

# Mysterious Update Items
mysterious_table: dict[str, AdvData] = {
    # Serpent Lock and Circlet
    "Serpent A4 - Serpent Lock Shard":              AdvData(106041904, "Serpent Stacks - Post-Rune"),
    "Serpent A5 - NE - Serpent Lock Shard":         AdvData(106052104, "Serpent Stacks - Serpent Lock"),
    "Serpent A5 - SE - Serpent Lock Shard":         AdvData(106052112, "Serpent Stacks - Serpent Lock"),
    "Serpent A5 - NW - Serpent Lock Shard":         AdvData(106050207, "Serpent Stacks - Serpent Lock"),
    "Serpent A5 - SW - Serpent Lock Shard":         AdvData(106050209, "Serpent Stacks - Serpent Lock"),
    "Serpent A6 - Serpent Lock Shard":              AdvData(106060711, "Serpent Stacks - Core"),
    "Serpent A7 - Serpent Lock Shard":              AdvData(106072006, "Serpent Stacks - Tail"),
    "Serpent A8 - Serpent Lock Shard":              AdvData(106080508, "Serpent Stacks - Tail"),
    "Serpent A5 - Serpent Circlet":                 AdvData(106051108, "Serpent Stacks - Serpent Lock"), # 8 lock shards
    
    # Pyramidion Quest
    "Sunken A1 Serpent Secret - Ancient Key":       AdvData(109011005, "Sunken Island - Turtle"),

    "Fire D3 Serpent Secret - Obsidian":            AdvData(104331811, "Raging Volcano - Below Hot Spring"), # r quest, s shirt
    "Aggro A0 Serpent Secret - Obsidian":           AdvData(110001807, "Aggro Crag - North-West"),
    "Nunatak A1 Serpent Secret - Obsidian":         AdvData(111012008, "Sea Nunatak - Turtle"),
    "Tropic A1 Serpent Secret - Obsidian":          AdvData(113010808, "Star Tropic - Treasure Shore"),

    "Stone D0 Serpent Secret - Pyramidion":         AdvData(101301908, "Stony Cliffs - Giant Wheel"),
    "Stone D1 Serpent Secret - Pyramidion":         AdvData(101310206, "Stony Cliffs - God Altar"),
    "Water A3 Serpent Secret - Pyramidion":         AdvData(103031008, "Tidal Reef - South-West"),
    "Fire E3 Serpent Secret - Pyramidion":          AdvData(104431712, "Raging Volcano - Below Hot Spring"),
    "Wind A1 Serpent Secret - Pyramidion":          AdvData(105011708, "Frozen Spire - Post-Rune"),
    "Wind E3 Serpent Secret - Pyramidion":          AdvData(105432204, "Frozen Spire - Post-Rune"),

    "Rolling A0 Serpent Secret - Pyramidion":       AdvData(108002009, "Rolling Rocks - West"),
    "Rolling B1 Serpent Secret - Pyramidion":       AdvData(108110804, "Rolling Rocks - South-East"),
    "Sunken B0 Serpent Secret - Pyramidion":        AdvData(109101007, "Sunken Island - Turtle"),
    "Aggro B1 Serpent Secret - Pyramidion":         AdvData(110111308, "Aggro Crag - East"),
    "Nunatak B0 Serpent Secret - Pyramidion":       AdvData(111101409, "Sea Nunatak - Turtle"),

    "Serpent A2 Serpent Secret - NW - Pyramidion":  AdvData(106021106, "Serpent Stacks - A2 Pyramidions"),
    "Serpent A2 Serpent Secret - SW - Pyramidion":  AdvData(106021107, "Serpent Stacks - A2 Pyramidions"),
    "Serpent A2 Serpent Secret - NE - Pyramidion":  AdvData(106021206, "Serpent Stacks - A2 Pyramidions"),
    "Serpent A2 Serpent Secret - SE - Pyramidion":  AdvData(106021207, "Serpent Stacks - A2 Pyramidions"),
    "Serpent A5 Serpent Secret - Pyramidion":       AdvData(106050709, "Serpent Stacks - Serpent Lock"),
    "Serpent A9 - Pyramidion":                      AdvData(106091508, "Serpent Stacks - Mysterious Map"), # wind elementals

    "Sanctum A1 Serpent Secret - Pyramidion":       AdvData(107011709, "Sanctum - Turtle"), # a lot of keys to unlock sanctum
    "Sanctum C1 Serpent Secret - Pyramidion":       AdvData(107210609, "Sanctum - Turtle"), # a lot of keys to unlock sanctum

    "Shoal A0 - Pattern Puzzle Pyramidion":         AdvData(114001305, "Eastern Shoal - North-West"), # Visit Stone A3
    "Shoal A1 - Pyramidion":                        AdvData(114012010, "Eastern Shoal - South"), # Yes, this is possible without flippers.
    "Shoal A1 - Pattern Puzzle Pyramidion":         AdvData(114011604, "Eastern Shoal - South"), # Visit Water E2
    "Shoal B0 - Pyramidion":                        AdvData(114101803, "Eastern Shoal - North-East"), 
    "Shoal B0 - Pattern Puzzle Pyramidion":         AdvData(114100708, "Eastern Shoal - North-East"), # hint in wind B0
    "Shoal B1 - Pyramidion":                        AdvData(114110312, "Eastern Shoal - South"), # All elementals, f flippers
    "Shoal B1 - Pattern Puzzle Pyramidion":         AdvData(114110605, "Eastern Shoal - South"), # All elementals, f flippers, hint in Fire B0

    "Lagoon B0 Serpent Secret - Pyramidion":        AdvData(117100709, "Forgotten Lagoon - North"), # Kite Cloak ?
    "Lagoon B1 Serpent Secret - W - Pyramidion":    AdvData(117110907, "Forgotten Lagoon - South"),
    "Lagoon B1 Serpent Secret - C - Pyramidion":    AdvData(117111407, "Forgotten Lagoon - South"),
    "Lagoon B1 Serpent Secret - E - Pyramidion":    AdvData(117111907, "Forgotten Lagoon - South"),
}

meteorite_table: dict[str, AdvData] = {

    "Stone C2 - Earth Warp Pattern":                AdvData(99901221, "Stony Cliffs - God Altar"),
    "Water B4 - Water Warp Pattern":                AdvData(99903141, "Tidal Reef - Phoenix"),
    "Fire C3 - Fire Warp Pattern":                  AdvData(99904231, "Raging Volcano - God Altar"),
    "Wind B3 - Wind Warp Pattern":                  AdvData(99905131, "Frozen Spire"),
    "Warp ?? - Tropic Warp Pattern":                AdvData(99920001, "Warp Hub"),
    "Lost B1 - Lost Warp Pattern":                  AdvData(99915111, "Lost Landing - Staircase"),
    "Ancient Cavern B1 - Ancient Warp Pattern":     AdvData(99918111, "Ancient Cavern - South"),
    "Lost A0 - Compass Warp Pattern":               AdvData(99915001, "Lost Landing - Compass"),

    "Tropic B1 - Meteorite":                        AdvData(113110805, "Star Tropic - Meteorite"),
    "Lost A0 - Meteorite":                          AdvData(115001704, "Lost Landing - Compass"),
    "Ancient A0 - Meteorite":                       AdvData(100000805, "Ancient Cavern - North"),
    "Totem B0 - Meteorite":                         AdvData(119101606, "Totem"),

    # In the future, could include milestones as locations. e.g. each of the steam achievements, plus extras.
}

circlet_meteorite_table: dict[str, AdvData] = {
    # This one is only enabled if pyramidions are also enabled since it requires serpent circlet 
    "Lagoon A0 - Meteorite":                        AdvData(117000905, "Forgotten Lagoon - Meteorite")
}

note_table: dict[str, AdvData] = {
    # 24 checks
    "Stone B0 - Music Note":                        AdvData(101102012, "Stony Cliffs - Phoenix"), # ancient key
    "Stone B2 - Music Note":                        AdvData(101121209, "Stony Cliffs - South Coast"), # topaz quest
    "Stone B3 - Music Note":                        AdvData(101131011, "Stony Cliffs - South Coast"), # topaz rune
    "Stone C1 - Music Note":                        AdvData(101211704, "Stony Cliffs - God Altar"), #
    "Stone D1 - Music Note":                        AdvData(101310510, "Stony Cliffs - God Altar"), # topaz quest
    "Stone D4 - Music Note":                        AdvData(101341907, "Stony Cliffs - South Coast"), # topaz rune

    "Water A2 - Music Note":                        AdvData(103021807, "Tidal Reef - God Altar"), # s rune | f flippers
    "Water B0 - Music Note":                        AdvData(103100208, "Tidal Reef - North-West Low Tide"),
    "Water C1 - Music Note":                        AdvData(103210611, "Tidal Reef - God Altar"),
    "Water D1 - Music Note":                        AdvData(103312203, "Tidal Reef - East"), # s rune
    "Water E0 - Music Note":                        AdvData(103401810, "Tidal Reef - East"), # s rune
    "Water E2 - Music Note":                        AdvData(103421811, "Tidal Reef - East"), # s rune

    "Fire A2 - Music Note":                         AdvData(104021110, "Raging Volcano - God Altar"),
    "Fire B0 - Music Note":                         AdvData(104101210, "Raging Volcano - Key Triplets"),
    "Fire B2 - Music Note":                         AdvData(104121512, "Raging Volcano - Lyre"),
    "Fire C3 - Music Note":                         AdvData(104231511, "Raging Volcano - Idol Room West"),
    "Fire D3 - Music Note":                         AdvData(104332209, "Raging Volcano - Below Hot Spring"),
    "Fire E1 - Music Note":                         AdvData(104412009, "Raging Volcano - Hot Spring"),

    "Wind A0 - Music Note":                         AdvData(105002010, "Frozen Spire - Post-Rune"),
    "Wind A2 - Music Note":                         AdvData(105021908, "Frozen Spire"),
    "Wind B1 - Music Note":                         AdvData(105110910, "Frozen Spire"),
    "Wind C3 - Music Note":                         AdvData(105230208, "Frozen Spire"), # itemless from C3 albatross
    "Wind D3 - Music Note":                         AdvData(105330512, "Frozen Spire - Post-Rune"), # d quest
    "Wind E3 - Music Note":                         AdvData(105430307, "Frozen Spire - Post-Rune"),  # d rune
}

seashell_table: dict[str, AdvData] = {

#     # 24 checks
#     "Water B2 - Shell":                             AdvData(109001, "Tidal Reef"),
#     "Water C0 - Shell":                             AdvData(110034, "Tidal Reef"),
#     "Water B0 - Shell":                             AdvData(113779, "Tidal Reef"),
#     "Water B1 - Shell":                             AdvData(109727, "Tidal Reef"),
#     "Water C1 - Shell":                             AdvData(109466, "Tidal Reef"),
#     "Water C2 - Shell":                             AdvData(108836, "Tidal Reef"),
#     "Water D2 - Shell":                             AdvData(109127, "Tidal Reef Post-Rune"), # s rune
#     "Water A1 - Shell":                             AdvData(111286, "Tidal Reef"), # s rune
#     "Water A0 - Shell":                             AdvData(111579, "Tidal Reef Post-Rune"), # s rune
#     "Water A3 - Shell":                             AdvData(114803, "Tidal Reef"), # s rune
#     "Water B3 - Shell":                             AdvData(110854, "Tidal Reef S"), # s rune
#     "Water B4 - Shell":                             AdvData(126146, "Tidal Reef S"), # s rune
#     "Water C4 - Shell":                             AdvData(126171, "Tidal Reef S"),
#     "Water C3 - Shell":                             AdvData(108596, "Tidal Reef Post-Rune"), # s rune
#     "Water D4 - Shell":                             AdvData(129544, "Tidal Reef Post-Rune"), # s rune
#     "Water E4 - Shell":                             AdvData(125935, "Tidal Reef Post-Rune"), # s rune
#     "Water E2 - Shell":                             AdvData(113315, "Tidal Reef Post-Rune"), # s rune
#     "Water E1 - Shell":                             AdvData(113547, "Tidal Reef Post-Rune"), # s rune
#     "Water E0 - Shell":                             AdvData(110713, "Tidal Reef Post-Rune"), # s rune
#     "Water D3 - Shell":                             AdvData(113163, "Tidal Reef Post-Rune"), # s rune
#     "Water A4 - Shell":                             AdvData(126066, "Tidal Reef S"),  # f flippers
#     "Water D1 - Shell":                             AdvData(109899, "Tidal Reef"),  # f flippers
#     "Water D0 - Shell":                             AdvData(110330, "Tidal Reef Post-Rune"),  # f flippers
#     "Water A2 - Shell":                             AdvData(112462, "Tidal Reef Post-Rune"),  # f flippers

}

# 10 checks
jellyfish_table: dict[str, AdvData] = {
    # "Topaz Sea - Jellyfish":                        AdvData(199005022, "Topaz Sea"),
    # "Diamond Sea - Jellyfish":                      AdvData(199004821, "Eastern Sea"),
    # "Obsidian Sea - Jellyfish":                     AdvData(199001727, "Obsidian Sea"),
    # "Sapphire Sea - Jellyfish":                     AdvData(199003403, "Sapphire Sea"),
    # "Ruby Sea - W - Jellyfish":                     AdvData(199004232, "Ruby Sea"),
    # "Ruby Sea - E - Jellyfish":                     AdvData(199006132, "Ruby Sea"),
    # "Beast Sea - W - Jellyfish":                    AdvData(199005311, "Beast Sea"),
    # "Beast Sea - E - Jellyfish":                    AdvData(199006512, "Beast Sea"),
    # "Lost Sea - Jellyfish":                         AdvData(199003331, "Lost Sea"),
    # "Northeast Sea - Jellyfish":                    AdvData(199006107, "Forgotten Sea"),
}

# 24 checks
secrets_table: dict[str, AdvData] = {

    # "Ancient A1 - Discover Secret":                 AdvData(101044, "Ancient Isle"),

    # "Stone E1 - Discover Secret":                   AdvData(107724, "Stony Cliffs"),
    # "Stone D4 - Discover Secret":                   AdvData(106792, "Stony Cliffs Post-Rune"),

    # "Rolling A0 - Discover Secret":                 AdvData(103790, "Rolling Rocks"),

    # "Nunatak B0 - E - Discover Secret":             AdvData(123457, "Sea Nunatak - Turtle"),
    # "Nunatak B0 - SE - Discover Secret":            AdvData(123426, "Sea Nunatak - Turtle"),
    # "Nunatak B0 - CW - Discover Secret":            AdvData(123461, "Sea Nunatak - Turtle"),
    # "Nunatak B0 - W - Discover Secret":             AdvData(123447, "Sea Nunatak - Turtle"),

    # "Shoal A0 - W - Discover Secret":               AdvData(104364, "Eastern Shoal - North-West"),
    # "Shoal A0 - E - Discover Secret":               AdvData(104321, "Eastern Shoal - North-West"),
    # "Shoal A0 - SE - Discover Secret":              AdvData(104322, "Eastern Shoal - North-West"),

    # "Aggro B1 - Discover Secret":                   AdvData(122712, "Aggro Crag"),
    # "Aggro A0 - W - Discover Secret":               AdvData(122517, "Aggro Crag"),
    # "Aggro A0 - E - Discover Secret":               AdvData(122488, "Aggro Crag"),

    # "Sunken A0 - Discover Secret":                  AdvData(122982, "Sunken Island - Turtle"),

    # "Tropic A0 - Discover Secret":                  AdvData(103122, "Star Tropic"),

    # "Lost B1 - CS - Discover Secret":               AdvData(128953, "Lost Landing"),
    # "Lost B1 - W - Discover Secret":                AdvData(128951, "Lost Landing"),

    # "Fire C4 - Discover Secret":                    AdvData(118109, "Raging Volcano Post-Rune"),
    # "Fire C2 - Discover Secret":                    AdvData(115494, "Raging Volcano"),
    # "Fire E1 - Discover Secret":                    AdvData(118553, "Raging Volcano Post-Rune"),

    # "Wind A0 - Discover Secret":                    AdvData(120206, "Frozen Spire"),
    # "Wind A1 - Discover Secret":                    AdvData(120347, "Frozen Spire"),
    # "Wind D1 - Discover Secret":                    AdvData(121434, "Frozen Spire - Post-Rune"),

}

# Est. 101 extra checks here.
locksanity_table: dict[str, AdvData] = {
    # "Ancient B3 - Lock":                            AdvData(100221, "Ancient Isle"),
    # "Ancient B2 - Lock":                            AdvData(101289, "Ancient Isle"),
    # "Ancient A3 - Lock":                            AdvData(100548, "Ancient Isle"),
    # "Ancient C2 - 3x Lock":                         AdvData(100436, "Ancient Isle"),
    # "Ancient A1 - 3x Lock":                         AdvData(101049, "Ancient Isle"), # access o sea

    # "Stone C2 - Lock":                              AdvData(107588, "Stony Cliffs"),
    # "Stone E1 - 3x Lock":                           AdvData(107761, "Stony Cliffs"),
    # "Stone B1 - Lock":                              AdvData(107044, "Stony Cliffs NW"), # t rune

    # "Water B2 - Lock":                              AdvData(108972, "Tidal Reef"),
    # "Water C1 - 3x Lock":                           AdvData(109439, "Tidal Reef"),
    # "Water D3 - Lock":                              AdvData(113120, "Tidal Reef Post-Rune"), # s rune

    # "Fire E0 - 3x Lock (Fire)":                     AdvData(118309, "Raging Volcano NE"),
    # "Fire A3 - Lock":                               AdvData(116779, "Raging Volcano Post-Rune"),
    # "Fire D2 - Lock":                               AdvData(115819, "Raging Volcano"),
    # "Fire D2 - 3x Lock":                            AdvData(115799, "Raging Volcano"),

    # "Wind C3 - Lock":                               AdvData(120637, "Frozen Spire - Post-Rune"),
    # "Wind D3 - 3x Lock":                            AdvData(120553, "Frozen Spire"),
    # "Wind D1 - Lock":                               AdvData(121455, "Frozen Spire - Post-Rune"),
    # "Wind A0 - Lock (Wind)":                        AdvData(120220, "Frozen Spire"),

    # "Sanctum B2 - W - 3x Lock":                     AdvData(123943, "Sanctum - Turtle"),
    # "Sanctum B2 - E - 3x Lock":                     AdvData(123942, "Sanctum - Turtle"),
    # "Sanctum A1 - 3x Lock":                         AdvData(124157, "Sanctum - Turtle"),
    # "Sanctum C1 - 3x Lock":                         AdvData(124282, "Sanctum - Turtle"),

    # "Rolling B1 - 3x Lock":                         AdvData(104767, "Rolling Rocks - Post-Rune"),

    # "Sunken A1 - 3x Lock":                          AdvData(123081, "Sunken Island - Turtle"),

    # "Aggro A1 - 3x Lock":                           AdvData(122917, "Aggro Crag"),

    # "Nunatak A0 - 3x Lock":                         AdvData(123383, "Sea Nunatak - Turtle"),

    # "Locked A0 - 6x Lock":                          AdvData(104286, "Locked Key - Turtle"),

    # "Lost A1 - Lock":                               AdvData(127286, "Lost Landing"),

    # "Ancient C1 - Star Lock 1":                     AdvData(100984, "Ancient Isle"),

    # "Overworld - Star Lock 3":                      AdvData(108488, "Topaz Sea"),
    # "Overworld - Star Lock 15":                     AdvData(108494, "Topaz Sea"),
    # "Overworld - Star Lock 30":                     AdvData(108499, "Eastern Sea"),
    # "Overworld - Star Lock 45":                     AdvData(108516, "Obsidian Sea"),

    # "Stone A1 - Star Lock 5":                       AdvData(107545, "Stony Cliffs NW"),
    # "Stone C4 - Star Lock 15":                      AdvData(107259, "Stony Cliffs Post-Rune"),
    # "Stone E3 - Star Lock 20":                      AdvData(106823, "Stony Cliffs Post-Rune"),
    # "Stone Dungeon A1 - Star Lock 20":              AdvData(101941, "Stony Cliffs Post-Rune"),

    # "Water A2 - Star Lock 30":                      AdvData(112443, "Tidal Reef Post-Rune"),

    # "Rolling A0 - Star Lock 7":                     AdvData(103800, "Rolling Rocks"),
    # "Sunken B0 - Star Lock 21":                     AdvData(123144, "Sunken Island - Turtle"),
    # "Lost B0 - Star Lock 30":                       AdvData(100181, "Lost Landing"),
    # "Aggro B0 - Star Lock 35":                      AdvData(122670, "Aggro Crag"),
    # "Nunatak B0 - Star Lock 49":                    AdvData(123481, "Sea Nunatak - Turtle"),

    # "Ancient B1 - Ancient Rune Lock":               AdvData(100251, "Ancient Isle"),

    # "Stone C0 - Topaz Rune Lock":                   AdvData(108053, "Stony Cliffs Post-Rune"), #post-rune is inclusive of rune lock checks
    # "Stone C1 - Topaz Rune Lock":                   AdvData(107476, "Stony Cliffs Post-Rune"),
    # "Stone E1 - Topaz Rune Lock":                   AdvData(107758, "Stony Cliffs Post-Rune"),
    # "Stone E2 - Topaz Rune Lock":                   AdvData(107666, "Stony Cliffs Post-Rune"),
    # "Stone E3 - Topaz Rune Lock":                   AdvData(106822, "Stony Cliffs Post-Rune"),
    # "Stone C4 - Topaz Rune Lock":                   AdvData(107252, "Stony Cliffs Post-Rune"),

    # "Water C0 - Sapphire Rune Lock":                AdvData(110023, "Tidal Reef Post-Rune"),
    # "Water B2 - Sapphire Rune Lock":                AdvData(108971, "Tidal Reef Post-Rune"),
    # "Water A0 - Sapphire Rune Lock":                AdvData(111572, "Tidal Reef Post-Rune"),
    # "Water A3 - Sapphire Rune Lock":                AdvData(114802, "Tidal Reef Post-Rune"),
    # "Water D2 - N - Sapphire Rune Lock":            AdvData(109109, "Tidal Reef Post-Rune"),
    # "Water D2 - S - Sapphire Rune Lock":            AdvData(109106, "Tidal Reef Post-Rune"),
    # "Water D0 - Sapphire Rune Lock":                AdvData(110316, "Tidal Reef Post-Rune"),
    # "Water C3 - E - Sapphire Rune Lock":            AdvData(108592, "Tidal Reef Post-Rune"),
    # "Water C3 - W - Sapphire Rune Lock":            AdvData(108593, "Tidal Reef Post-Rune"),
    # "Water B3 - Sapphire Rune Lock":                AdvData(110851, "Tidal Reef Post-Rune"),

    # "Fire A1 - S - Ruby Rune Lock":                 AdvData(116434, "Raging Volcano Post-Rune"),
    # "Fire A1 - E - Ruby Rune Lock":                 AdvData(116436, "Raging Volcano Post-Rune"),
    # "Fire A2 - Ruby Rune Lock":                     AdvData(115237, "Raging Volcano Post-Rune"),
    # "Fire A3 - Ruby Rune Lock":                     AdvData(116778, "Raging Volcano Post-Rune"),
    # "Fire B2 - N - Ruby Rune Lock":                 AdvData(115374, "Raging Volcano Post-Rune"),
    # "Fire B2 - S - Ruby Rune Lock":                 AdvData(115375, "Raging Volcano Post-Rune"),
    # "Fire C0 - Ruby Rune Lock":                     AdvData(116200, "Raging Volcano Post-Rune"),
    # "Fire C1 - Ruby Rune Lock":                     AdvData(115702, "Raging Volcano Post-Rune"),
    # "Fire C3 - S - Ruby Rune Lock":                 AdvData(116304, "Raging Volcano Post-Rune"),
    # "Fire C3 - W - Ruby Rune Lock":                 AdvData(116302, "Raging Volcano Post-Rune"),
    # "Fire D1 - Ruby Rune Lock":                     AdvData(116005, "Raging Volcano Post-Rune"),
    # "Fire E0 - Ruby Rune Lock":                     AdvData(118316, "Raging Volcano Post-Rune"),

    # "Wind C3 - Diamond Rune Lock":                  AdvData(120636, "Frozen Spire - Post-Rune"),
    # "Wind D4 - Diamond Rune Lock":                  AdvData(122402, "Frozen Spire - Post-Rune"),
    # "Wind E3 - Diamond Rune Lock":                  AdvData(121758, "Frozen Spire - Post-Rune"),
    # "Wind E2 - W - Diamond Rune Lock":              AdvData(121659, "Frozen Spire - Post-Rune"),
    # "Wind E2 - E - Diamond Rune Lock":              AdvData(121666, "Frozen Spire - Post-Rune"),
    # "Wind E0 - Diamond Rune Lock":                  AdvData(120494, "Frozen Spire - Post-Rune"),
    # "Wind D1 - Diamond Rune Lock":                  AdvData(121454, "Frozen Spire - Post-Rune"),
    # "Wind C2 - Diamond Rune Lock":                  AdvData(121372, "Frozen Spire - Post-Rune"),
    # "Wind C1 - Diamond Rune Lock":                  AdvData(121260, "Frozen Spire - Post-Rune"),
    # "Wind B1 - Diamond Rune Lock":                  AdvData(120915, "Frozen Spire - Post-Rune"),
    # "Wind B3 - Diamond Rune Lock":                  AdvData(121098, "Frozen Spire - Post-Rune"),
    # "Wind A2 - Diamond Rune Lock":                  AdvData(120736, "Frozen Spire - Post-Rune"),

    # "Serpent A2 - Elemental Rune Lock":             AdvData(104819, "Serpent Stacks"),
    # "Serpent A1 - N - Obsidian Rune Lock":          AdvData(125703, "Serpent Stacks - Post-Rune"),
    # "Serpent A1 - W - Obsidian Rune Lock":          AdvData(125701, "Serpent Stacks - Post-Rune"),
    # "Serpent A1 - E - Obsidian Rune Lock":          AdvData(125689, "Serpent Stacks - Post-Rune"),
    # "Serpent A3 - Obsidian Rune Lock":              AdvData(103366, "Serpent Stacks - Post-Rune"),

    # "Rolling A1 - Ancient Rune Lock":               AdvData(104495, "Rolling Rocks - Post-Rune"),
    # "Rolling B0 - Ancient Rune Lock":               AdvData(104912, "Rolling Rocks - Post-Rune"),

    # "Sunken A0 - Ancient Rune Lock":                AdvData(123006, "Sunken Island - Turtle"),
    # "Sunken B1 - Ancient Rune Lock":                AdvData(123252, "Sunken Island - Turtle"),

    # "Aggro B1 - Ancient Rune Lock":                 AdvData(122860, "Aggro Crag"),
    # "Aggro A1 - Ancient Rune Lock":                 AdvData(122919, "Aggro Crag"),

    # "Nunatak B0 - Ancient Rune Lock":               AdvData(123480, "Sea Nunatak - Turtle"),

    # "Locked A0 - Ancient Rune Lock":                AdvData(104284, "Locked Key - Turtle"),

    # "Tropic A1 - Ancient Rune Lock":                AdvData(104457, "Star Tropic"),
    # "Tropic B0 - Ancient Rune Lock":                AdvData(104247, "Star Tropic"),
    # "Tropic B0 - Obsidian Rune Lock":               AdvData(104246, "Star Tropic"),

    # "Shoal A0 - Ancient Rune Lock":                 AdvData(104388, "Eastern Shoal - North-West"),
    # 
}

snakesanity_table: dict[str, AdvData] = { # TODO: Overworld ID
    "Overworld - Sapphire Sea - Damsnake":          AdvData(199112016, "Sapphire Sea"),
    "Overworld - Lost Sea - Damsnake":              AdvData(199112227, "Lost Sea"),
    "Overworld - Beast Sea - Damsnake":             AdvData(199114914, "Beast Sea"),
    "Overworld - Forgotten Sea - Damsnake":         AdvData(199115007, "Forgotten Sea"),

    "Ancient A1 - Snakeblock":                      AdvData(100011210, "Ancient Isle - West"),
    "Ancient A3 - Snakeblock":                      AdvData(100031004, "Ancient Isle - Origin"),
    "Ancient B2 - W - Snakeblock":                  AdvData(100120208, "Ancient Isle - Origin"),
    "Ancient B2 - E - Snakeblock":                  AdvData(100122109, "Ancient Isle - Origin"),
    "Ancient B3 - Snakeblock":                      AdvData(100131205, "Ancient Isle - Origin"),
    "Ancient C2 - W - Snakeblock":                  AdvData(100221011, "Ancient Isle - Origin"),
    "Ancient C2 - S - Snakeblock":                  AdvData(100221411, "Ancient Isle - Origin"),
    "Ancient C2 - E - Snakeblock":                  AdvData(100221808, "Ancient Isle - Origin"),
    "Ancient C3 - Snakeblock":                      AdvData(100230504, "Ancient Isle - Origin"),

    "Stone A0 - Snakeblock":                        AdvData(101001612, "Stony Cliffs - Phoenix"),
    "Stone A2 - N - Snakeblock":                    AdvData(101022203, "Stony Cliffs - Phoenix"),
    "Stone A2 - S - Snakeblock":                    AdvData(101022204, "Stony Cliffs - Tablet Slot"),
    "Stone A3 - Snakeblock":                        AdvData(101032012, "Stony Cliffs - Tablet Slot"),
    "Stone A4 - W - Snakeblock":                    AdvData(101040503, "Stony Cliffs - Tablet Slot"),
    "Stone A4 - E - Snakeblock":                    AdvData(101042209, "Stony Cliffs - South Star Stone"), #g gloves
    "Stone B0 - Snakeblock":                        AdvData(101101607, "Stony Cliffs - Phoenix"), # Ancient Key
    "Stone B1 - W - Snakeblock":                    AdvData(101111504, "Stony Cliffs - Phoenix"), # Ancient Key
    "Stone B1 - E - Snakeblock":                    AdvData(101112206, "Stony Cliffs - Phoenix"), # Entrance from Stone Dungeon
    "Stone B2 - W - Snakeblock":                    AdvData(101121012, "Stony Cliffs - South Coast"),
    "Stone B2 - E - Snakeblock":                    AdvData(101121412, "Stony Cliffs - South Coast"),
    "Stone B3 - S - Snakeblock":                    AdvData(101130312, "Stony Cliffs - Tablet Slot"),
    "Stone B3 - N - Snakeblock":                    AdvData(101130403, "Stony Cliffs - South Coast"),
    "Stone B4 - Snakeblock":                        AdvData(101141110, "Stony Cliffs - South Star Stone"), # Earth Elementals
    "Stone C1 - Snakeblock":                        AdvData(101211108, "Stony Cliffs - God Altar"), # Earth Elementals
    "Stone C2 - Snakeblock":                        AdvData(101220811, "Stony Cliffs - South Coast"),
    "Stone C4 - Snakeblock":                        AdvData(101240504, "Stony Cliffs - Windy Cliff"), # Earth | Wind Elementals
    "Stone D1 - Snakeblock":                        AdvData(101310909, "Stony Cliffs - God Altar"), # Earth Elementals
    "Stone D2 - Snakeblock":                        AdvData(101320409, "Stony Cliffs - God Altar"),
    "Stone D3 - W - Snakeblock":                    AdvData(101331111, "Stony Cliffs - Windy Cliff"), # Earth | Wind Elementals
    "Stone D3 - N - Snakeblock":                    AdvData(101331506, "Stony Cliffs - Windy Cliff"), # Earth & Wind Elementals
    "Stone D3 - S - Snakeblock":                    AdvData(101331512, "Stony Cliffs - Windy Cliff"),
    "Stone D4 - Snakeblock":                        AdvData(101340504, "Stony Cliffs - Windy Cliff"), # Earth | Wind Elementals
    "Stone E0 - Snakeblock":                        AdvData(101400407, "Stony Cliffs - North-East"),
    "Stone E1 - W - Snakeblock":                    AdvData(101410909, "Stony Cliffs - God Altar"),
    "Stone E1 - E - Snakeblock":                    AdvData(101411107, "Stony Cliffs - God Altar"), # Entrance from Caverns
    "Stone E4 - Snakeblock":                        AdvData(101440210, "Stony Cliffs - South Coast"),
    "Stone Dungeon B1 - Snakeblock":                AdvData(102111111, "Stone Dungeon - West Tunnels"),
    "Stone Dungeon B2 - W - Snakeblock":            AdvData(102120308, "Stone Dungeon - West Tunnels"),
    "Stone Dungeon B2 - N - Snakeblock":            AdvData(102121107, "Stone Dungeon - West Tunnels"),
    "Stone Dungeon B2 - E - Snakeblock":            AdvData(102121509, "Stone Dungeon - Vault Door"),
    "Stone Dungeon C1 - Snakeblock":                AdvData(102211307, "Stone Dungeon - Gopher Vault"), # Gopher Gloves
    "Stone Dungeon C3 - Snakeblock":                AdvData(102231206, "Stone Dungeon - Vault Door"),
    "Stone Dungeon C4 - Snakeblock":                AdvData(102241306, "Stone Dungeon - South Tunnels"), # Earth Elementals
    "Stone Dungeon D1 - W - Snakeblock":            AdvData(102311011, "Stone Dungeon - Vault Door"),
    "Stone Dungeon D1 - N - Snakeblock":            AdvData(102311606, "Stone Dungeon - Below Xylophone"),
    "Stone Dungeon D1 - S - Snakeblock":            AdvData(102311607, "Stone Dungeon - Vault Door"),
    "Stone Dungeon D1 - E - Snakeblock":            AdvData(102312108, "Stone Dungeon - Vault Door"), # Entrance from Xylophone Room
    "Stone Dungeon D2 - W - Snakeblock":            AdvData(102320710, "Stone Dungeon - Vault Door"),
    "Stone Dungeon D2 - CW - Snakeblock":           AdvData(102321208, "Stone Dungeon - Vault Door"),
    "Stone Dungeon D2 - CE - Snakeblock":           AdvData(102321508, "Stone Dungeon - Vault Door"),
    "Stone Dungeon D2 - E - Snakeblock":            AdvData(102322007, "Stone Dungeon - Vault Door"),
    "Stone Dungeon E1 - Snakeblock":                AdvData(102411106, "Stone Dungeon - Earth Chamber"), # East Cavern Entrance
    "Stone Dungeon E2 - Snakeblock":                AdvData(102420607, "Stone Dungeon - Earth Chamber"),

    "Water A0 - W - Snakeblock":                    AdvData(103001408, "Tidal Reef - North-West"),
    "Water A0 - S - Snakeblock":                    AdvData(103001609, "Tidal Reef - God Altar"), # f flippers
    "Water A2 - Snakeblock":                        AdvData(103021406, "Tidal Reef - West Star Stone"),
    "Water A3 - Snakeblock":                        AdvData(103031004, "Tidal Reef - West Star Stone"),
    "Water B0 - W -Snakeblock":                     AdvData(103100107, "Tidal Reef - North-West"),
    "Water B0 - C - Snakeblock":                    AdvData(103100809, "Tidal Reef - God Altar"), # Water Elementals
    "Water B0 - E - Snakeblock":                    AdvData(103101508, "Tidal Reef - God Altar"), # Water Elementals
    "Water B1 - C - Snakeblock":                    AdvData(103111309, "Tidal Reef - God Altar"), # Water B1 Star Piece
    "Water B1 - E - Snakeblock":                    AdvData(103111712, "Tidal Reef - God Altar"), # Water Elementals or Kite Cloak
    "Water B2 - C - Snakeblock":                    AdvData(103121608, "Tidal Reef - God Altar"),
    "Water B2 - N - Snakeblock":                    AdvData(103121905, "Tidal Reef - God Altar"),
    "Water B3 - Snakeblock":                        AdvData(103131003, "Tidal Reef - God Altar"),
    "Water B4 - Snakeblock":                        AdvData(103141906, "Tidal Reef - Phoenix"),
    "Water C1 - W - Snakeblock":                    AdvData(103210210, "Tidal Reef - God Altar"),
    "Water C1 - CW - Snakeblock":                   AdvData(103210808, "Tidal Reef - God Altar"),
    "Water C1 - CE - Snakeblock":                   AdvData(103211508, "Tidal Reef - God Altar"),
    "Water C1 - E - Snakeblock":                    AdvData(103211909, "Tidal Reef - God Altar"),
    "Water C2 - W - Snakeblock":                    AdvData(103220108, "Tidal Reef - God Altar"),
    "Water C2 - C - Snakeblock":                    AdvData(103221407, "Tidal Reef - God Altar"),
    "Water C2 - E - Snakeblock":                    AdvData(103221608, "Tidal Reef - God Altar"),
    "Water C2 - SE - Snakeblock":                   AdvData(103221711, "Tidal Reef - God Altar"),
    "Water D0 - W - Snakeblock":                    AdvData(103300705, "Tidal Reef - God Altar"),
    "Water D0 - E - Snakeblock":                    AdvData(103301507, "Tidal Reef - God Altar"), # God Altar to East Entrance
    "Water D1 - Snakeblock":                        AdvData(103310612, "Tidal Reef - East"),
    "Water D2 - W - Snakeblock":                    AdvData(103320107, "Tidal Reef - God Altar"),
    "Water D2 - S - Snakeblock":                    AdvData(103321310, "Tidal Reef - Shell Puzzle"), # Frog Flippers or Water Elementals
    "Water D2 - E - Snakeblock":                    AdvData(103322104, "Tidal Reef - Shell Puzzle"), # Frog Flippers or Water Elementals
    "Water D3 - Snakeblock":                        AdvData(103331409, "Tidal Reef - Shell Puzzle"), # Water Elementals
    "Water E1 - W - Snakeblock":                    AdvData(103410905, "Tidal Reef - East"), # Frog Flippers
    "Water E1 - E - Snakeblock":                    AdvData(103412006, "Tidal Reef - East"), # Frog Flippers
    "Water E2 - W - Snakeblock":                    AdvData(103420408, "Tidal Reef - East"),
    "Water E2 - SW - Snakeblock":                   AdvData(103420611, "Tidal Reef - East"),
    "Water E2 - NE - Snakeblock":                   AdvData(103421505, "Tidal Reef - East"),
    "Water E2 - SE - Snakeblock":                   AdvData(103421610, "Tidal Reef - East"),
    "Water E2 - E - Snakeblock":                    AdvData(103421908, "Tidal Reef - East"), # Water E2 Star Piece
    "Water E3 - W - Snakeblock":                    AdvData(103430210, "Tidal Reef - East"),
    "Water E3 - C - Snakeblock":                    AdvData(103430910, "Tidal Reef - East"), # Earth & Water Elementals

    "Fire A0 - W - Snakeblock":                     AdvData(104001109, "Raging Volcano - North-West"),
    "Fire A0 - E - Snakeblock":                     AdvData(104001707, "Raging Volcano - North-West"),
    "Fire A1 - N - Snakeblock":                     AdvData(104011805, "Raging Volcano - North-West"),
    "Fire A1 - E - Snakeblock":                     AdvData(104012007, "Raging Volcano - Geyser Pass"),
    "Fire A3 - W - Snakeblock":                     AdvData(104031007, "Raging Volcano - Triple Ruby Pit"),
    "Fire A3 - S - Snakeblock":                     AdvData(104031611, "Raging Volcano - South Coast"),
    "Fire A3 - SE - Snakeblock":                    AdvData(104032111, "Raging Volcano - Lyre"),
    "Fire A3 - NE - Snakeblock":                    AdvData(104032206, "Raging Volcano - Lyre"),
    "Fire A4 - Snakeblock":                         AdvData(104041904, "Raging Volcano - South Coast"),
    "Fire B0 - Snakeblock":                         AdvData(104100208, "Raging Volcano - North-West Pass"),
    "Fire B1 - Snakeblock":                         AdvData(104111910, "Raging Volcano - God Altar"), # Salamander Shirt
    "Fire B2 - W - Snakeblock":                     AdvData(104120608, "Raging Volcano - God Altar"),
    "Fire B2 - S - Snakeblock":                     AdvData(104120711, "Raging Volcano - Lyre"),
    "Fire B2 - CW - Snakeblock":                    AdvData(104120809, "Raging Volcano - God Altar"),
    "Fire B2 - CE - Snakeblock":                    AdvData(104121208, "Raging Volcano - God Altar"),
    "Fire B2 - E - Snakeblock":                     AdvData(104121908, "Raging Volcano - God Altar"),
    "Fire B3 - W - Snakeblock":                     AdvData(104130109, "Raging Volcano - Lyre"), # Fire Elementals
    "Fire B3 - NW - Snakeblock":                    AdvData(104130405, "Raging Volcano - Lyre"), # Fire Elementals
    "Fire B3 - E - Snakeblock":                     AdvData(104131508, "Raging Volcano - Lyre"), # Fire Elementals
    "Fire B3 - SE - Snakeblock":                    AdvData(104132209, "Raging Volcano - Above Volcano"),
    "Fire B4 - W - Snakeblock":                     AdvData(104140708, "Raging Volcano - South Coast"), # Fire Elementals
    "Fire B4 - E - Snakeblock":                     AdvData(104141908, "Raging Volcano - South Coast"), # Fire Elementals
    "Fire C1 - Snakeblock":                         AdvData(104212007, "Raging Volcano - God Altar"),
    "Fire C2 - N - Snakeblock":                     AdvData(104221105, "Raging Volcano - God Altar"),
    "Fire C2 - NE - Snakeblock":                    AdvData(104221805, "Raging Volcano - God Altar"),
    "Fire C2 - E - Snakeblock":                     AdvData(104222110, "Raging Volcano - God Altar"),
    "Fire C3 - W - Snakeblock":                     AdvData(104230206, "Raging Volcano - Lyre"),
    "Fire C3 - N - Snakeblock":                     AdvData(104230803, "Raging Volcano - God Altar"), # Fire Elementals
    "Fire C4 - S - Snakeblock":                     AdvData(104241408, "Raging Volcano - Above Volcano"),
    "Fire C4 - N - Snakeblock":                     AdvData(104241703, "Raging Volcano - Above Volcano"),
    "Fire D1 - W - Snakeblock":                     AdvData(104310708, "Raging Volcano - God Altar"),
    "Fire D1 - SW - Snakeblock":                    AdvData(104310711, "Raging Volcano - God Altar"), # Ancient Key x3
    "Fire D1 - C - Snakeblock":                     AdvData(104311511, "Raging Volcano - God Altar"), # Ruby Rune
    "Fire D1 - NE - Snakeblock":                    AdvData(104311906, "Raging Volcano - God Altar"), # Entrance from Phoenix or Fire Elementals
    "Fire D1 - SE - Snakeblock":                    AdvData(104312112, "Raging Volcano - Hot Spring"), # Salamander Shirt
    "Fire D2 - W - Snakeblock":                     AdvData(104320707, "Raging Volcano - God Altar"),
    "Fire D2 - C - Snakeblock":                     AdvData(104321511, "Raging Volcano - God Altar"),
    "Fire D2 - NE - Snakeblock":                    AdvData(104322006, "Raging Volcano - God Altar"),
    "Fire D2 - SE - Snakeblock":                    AdvData(104322012, "Raging Volcano - Below Hot Spring"),
    "Fire D3 - W - Snakeblock":                     AdvData(104330107, "Raging Volcano - Idol Room West"), # Salamander Shirt
    "Fire D3 - SW - Snakeblock":                    AdvData(104330310, "Raging Volcano - Below Hot Spring"), # Fire Elementals
    "Fire D3 - E - Snakeblock":                     AdvData(104331904, "Raging Volcano - Below Hot Spring"), # Fire Elementals
    "Fire D4 - W - Snakeblock":                     AdvData(104340508, "Raging Volcano - Idol Room West"),
    "Fire D4 - E - Snakeblock":                     AdvData(104342008, "Raging Volcano - Below Hot Spring"),
    "Fire E3 - W - Snakeblock":                     AdvData(104430508, "Raging Volcano - Below Hot Spring"), # Fire and Water Elementals
    "Fire E3 - CW - Snakeblock":                    AdvData(104430608, "Raging Volcano - Below Hot Spring"), # Fire and Water Elementals
    "Fire E3 - S - Snakeblock":                     AdvData(104431112, "Raging Volcano - Below Hot Spring"), # Fire and Water Elementals
    "Fire E4 - W - Snakeblock":                     AdvData(104440208, "Raging Volcano - Below Hot Spring"),
    "Fire E4 - N - Snakeblock":                     AdvData(104441103, "Raging Volcano - Below Hot Spring"),
    "Fire E4 - NE - Snakeblock":                    AdvData(104441203, "Raging Volcano - South Coast"),

    "Wind A2 - SW - Snakeblock":                    AdvData(105021312, "Frozen Spire"),
    "Wind A2 - SE - Snakeblock":                    AdvData(105021612, "Frozen Spire"), # Wind Elementals
    "Wind A3 - Snakeblock":                         AdvData(105030711, "Frozen Spire"),
    "Wind B0 - W - Snakeblock":                     AdvData(105101111, "Frozen Spire - Post-Rune"),
    "Wind B0 - E - Snakeblock":                     AdvData(105101610, "Frozen Spire - Post-Rune"),
    "Wind B1 - Snakeblock":                         AdvData(105111911, "Frozen Spire"), # Wind Elementals
    "Wind B2 - SW - Snakeblock":                    AdvData(105120412, "Frozen Spire"), # Wind Elementals
    "Wind B2 - E - Snakeblock":                     AdvData(105121608, "Frozen Spire"),
    "Wind B3 - SW - Snakeblock":                    AdvData(105130611, "Frozen Spire"),
    "Wind B3 - NE - Snakeblock":                    AdvData(105131605, "Frozen Spire"), # Kite Cloak
    "Wind B3 - CE - Snakeblock":                    AdvData(105131606, "Frozen Spire"), # Kite Cloak
    "Wind B4 - Snakeblock":                         AdvData(105140905, "Frozen Spire - Post-Rune"), # Wind Elementals
    "Wind C0 - Snakeblock":                         AdvData(105200206, "Frozen Spire - Post-Rune"),
    "Wind C1 - Snakeblock":                         AdvData(105210604, "Frozen Spire - Post-Rune"),
    "Wind C2 - Snakeblock":                         AdvData(105220706, "Frozen Spire"), # Collect Ancient Key C2
    "Wind C4 - N - Snakeblock":                     AdvData(105240804, "Frozen Spire"),
    "Wind C4 - C - Snakeblock":                     AdvData(105241108, "Frozen Spire"),
    "Wind C4 - E - Snakeblock":                     AdvData(105241908, "Frozen Spire"),
    "Wind D2 - SW - Snakeblock":                    AdvData(105320509, "Frozen Spire"),
    "Wind D2 - SE - Snakeblock":                    AdvData(105322012, "Frozen Spire"),
    "Wind D4 - Snakeblock":                         AdvData(105341909, "Frozen Spire"), # Ancient Key x3
    "Wind E1 - W - Snakeblock":                     AdvData(105410709, "Frozen Spire - Post-Rune"), # Fire Elementals
    "Wind E1 - C - Snakeblock":                     AdvData(105412010, "Frozen Spire - Post-Rune"), # Fire Elementals
    "Wind E1 - E - Snakeblock":                     AdvData(105412110, "Frozen Spire - Post-Rune"),
    "Wind E3 - Snakeblock":                         AdvData(105430406, "Frozen Spire - Post-Rune"), # Wind Elementals
    "Wind E4 - Snakeblock":                         AdvData(105440904, "Frozen Spire - Post-Rune"), # Wind Elementals

    # "Serpent A0 - Snakeblock":                      AdvData(106001009, "Serpent Stacks - ???"), # Beavis' Snakeblock
    "Serpent A1 - W - Snakeblock":                  AdvData(106010612, "Serpent Stacks - Head"),
    "Serpent A1 - C - Snakeblock":                  AdvData(106011108, "Serpent Stacks - Head"), # Obsidian Rune Stone
    "Serpent A1 - CE - Snakeblock":                 AdvData(106011410, "Serpent Stacks - Head"), # Obsidian Rune Stone
    "Serpent A1 - E - Snakeblock":                  AdvData(106011911, "Serpent Stacks - Head"), # Shadow Elementals
    "Serpent A6 - NW - Snakeblock":                 AdvData(106060906, "Serpent Stacks - Core"), # Kite Cloak or Shadow + Water Elementals
    "Serpent A6 - SW - Snakeblock":                 AdvData(106060907, "Serpent Stacks - Core"), # Kite Cloak or Shadow + Water Elementals
    "Serpent A6 - C - Snakeblock":                  AdvData(106061108, "Serpent Stacks - Core"),
    "Serpent A6 - E - Snakeblock":                  AdvData(106061609, "Serpent Stacks - Core"), # Kite Cloak or Shadow + Water Elementals
    "Serpent A8 - E - Snakeblock":                  AdvData(106082108, "Serpent Stacks - Tail"),

    "Sanctum A0 - W - Snakeblock":                  AdvData(107000109, "Sanctum - Wind Shard"),
    "Sanctum A0 - CW - Snakeblock":                 AdvData(107000909, "Sanctum - Wind Shard"),
    "Sanctum A0 - CE - Snakeblock":                 AdvData(107001110, "Sanctum - Wind Shard"),
    "Sanctum A0 - E - Snakeblock":                  AdvData(107002012, "Sanctum - Wind Shard"),
    "Sanctum A1 - Snakeblock":                      AdvData(107011907, "Sanctum - Turtle"),
    "Sanctum A2 - W - Snakeblock":                  AdvData(107020507, "Sanctum - Earth Shard"),
    "Sanctum A2 - C - Snakeblock":                  AdvData(107020808, "Sanctum - Earth Shard"),
    "Sanctum A2 - S - Snakeblock":                  AdvData(107021112, "Sanctum - Earth Shard"),
    "Sanctum C0 - W - Snakeblock":                  AdvData(107200612, "Sanctum - Fire Shard"),
    "Sanctum C0 - CSW - Snakeblock":                AdvData(107200909, "Sanctum - Fire Shard"),
    "Sanctum C0 - CN - Snakeblock":                 AdvData(107201007, "Sanctum - Fire Shard"),
    "Sanctum C0 - CNW - Snakeblock":                AdvData(107201406, "Sanctum - Fire Shard"),
    "Sanctum C0 - E - Snakeblock":                  AdvData(107201711, "Sanctum - Fire Shard"),
    "Sanctum C1 - Snakeblock":                      AdvData(107210407, "Sanctum - Turtle"),
    "Sanctum C2 - W - Snakeblock":                  AdvData(107220906, "Sanctum - Water Shard"),
    "Sanctum C2 - E - Snakeblock":                  AdvData(107221608, "Sanctum - Water Shard"),

    "Rolling B0 - Snakeblock":                      AdvData(108101611, "Rolling Rocks - North-East"), # Ancient Rune Stone

    "Aggro B0 - W - Snakeblock":                    AdvData(110100609, "Aggro Crag - North-West"),
    "Aggro B0 - S - Snakeblock":                    AdvData(110100710, "Aggro Crag - East"),
    "Aggro B1 - W - Snakeblock":                    AdvData(110110110, "Aggro Crag - South-West"), # Ancient Rune Stone
    "Aggro B1 - E - Snakeblock":                    AdvData(110111906, "Aggro Crag - East"), # 35 Star Pieces

    "Nunatak A1 - Snakeblock":                      AdvData(111011807, "Sea Nunatak - Turtle"), # Share Logic with A1 Ancient Key

    "Locked A0 - W - Snakeblock":                   AdvData(112011010, "Locked Key - Turtle"), # Ancient Key x6
    "Locked A0 - E - Snakeblock":                   AdvData(112011309, "Locked Key - Turtle"), # Ancient Key x6

    "Tropic A0 - W - Snakeblock":                   AdvData(113001410, "Star Tropic - West"),
    "Tropic A0 - C - Snakeblock":                   AdvData(113001710, "Star Tropic - West"),
    "Tropic A0 - E - Snakeblock":                   AdvData(113002011, "Star Tropic - West"),
    "Tropic B0 - N - Snakeblock":                   AdvData(113100306, "Star Tropic - West"),
    "Tropic B0 - S - Snakeblock":                   AdvData(113100410, "Star Tropic - West"),

    "Shoal A0 - Snakeblock":                        AdvData(114001307, "Eastern Shoal - North-West"), # Kite Cloak

    "Lost B1 - Snakeblock":                         AdvData(115111306, "Lost Landing - Staircase"),
}

mysterious_snakesanity_table: dict[str, AdvData] = {
    # Serpent Lock
    "Serpent A5 - NW - Snakeblock": AdvData(106050804, "Serpent Stacks - Serpent Lock"),
    "Serpent A5 - NE - Snakeblock": AdvData(106051504, "Serpent Stacks - Serpent Lock"), # Shadow Elementals
    "Serpent A5 - E - Snakeblock": AdvData(106052007, "Serpent Stacks - Serpent Lock"),
    
    # Pyramidion Quests
    "Water A3 Serpent Secret - W - Snakeblock":         AdvData(103030409, "Tidal Reef - South-West"), # Serpent Circlet
    "Water A3 Serpent Secret - CW - Snakeblock":        AdvData(103030708, "Tidal Reef - South-West"), # Serpent Circlet
    "Water A3 Serpent Secret - C - Snakeblock":         AdvData(103030309, "Tidal Reef - South-West"), # Serpent Circlet
    "Water A3 Serpent Secret - E - Snakeblock":         AdvData(103031308, "Tidal Reef - South-West"), # Serpent Circlet
    
    "Serpent A8 - SE - Snakeblock":                     AdvData(106082211, "Serpent Stacks - Mysterious Map"),
    "Serpent A9 - Snakeblock":                          AdvData(106091804, "Serpent Stacks - Mysterious Map"),

    "Shoal A1 - NW - Snakeblock":                       AdvData(114011003, "Eastern Shoal - South"),  # Kite Cloak
    "Shoal A1 - SW - Snakeblock":                       AdvData(114011010, "Eastern Shoal - South"),  # Kite Cloak
    "Shoal A1 - N - Snakeblock":                        AdvData(114011104, "Eastern Shoal - South"),  # Kite Cloak
    "Shoal A1 - S - Snakeblock":                        AdvData(114011110, "Eastern Shoal - South"),  # Kite Cloak
    "Shoal B0 - Snakeblock":                            AdvData(114100908, "Eastern Shoal - North-East"),
    "Shoal B1 - W - Snakeblock":                        AdvData(114110405, "Eastern Shoal - South"), # Frog Flippers, Earth Elementals
    "Shoal B1 - NW - Snakeblock":                       AdvData(114110603, "Eastern Shoal - South"), # Frog Flippers, Earth, Water and Fire Elementals
    "Shoal B1 - S - Snakeblock":                        AdvData(114111111, "Eastern Shoal - South"), # Frog Flippers, Earth and Water Elementals
    "Shoal B1 - NE - Snakeblock":                       AdvData(114111804, "Eastern Shoal - North-East"),
}

# Warps in Logic adds additional routes in logic that could expect you to travel through some of these snake blocks.
# Since warps in logic is a logic rule, it won't add these snakeblocks as checks.
# These snakeblocks are only checks if meteorite randomization is enabled
meteorite_snakesanity_table: dict[str, AdvData] = {
    "Ancient Cavern A1 - Snakeblock":                   AdvData(118011408, "Ancient Cavern - North"),
}

circlet_meteorite_snakesanity_table: dict[str, AdvData] = {
    "Lagoon A0 - Snakeblock":                           AdvData(117001409, "Forgotten Lagoon - Meteorite"),
}


exclusion_table = {



}

events_table = {
}
