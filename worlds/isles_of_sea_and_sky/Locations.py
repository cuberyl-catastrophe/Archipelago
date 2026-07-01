from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class IslesOfSeaAndSkyAdvancement(Location):
    game: str = "Isles Of Sea And Sky"

advancement_table = {
    "Locked A0 - Ancient Rune Stone":               AdvData(112012104, "Locked"),
    "Stone C0 - Topaz Rune Stone":                  AdvData(101201806, "Stony Cliffs"),
    "Water C0 - Sapphire Rune Stone":               AdvData(103201712, "Tidal Reef"),
    "Fire C0 - Ruby Rune Stone":                    AdvData(104200107, "Raging Volcano"),
    "Wind C2 - Diamond Rune Stone":                 AdvData(105221405, "Frozen Spire"),
    "Serpent A1 - Obsidian Rune Stone":             AdvData(106010410, "Serpent Stacks"),

    "Stone C0 - Topaz Quest Complete":              AdvData(99901201, "Stony Cliffs"),
    "Water C0 - Sapphire Quest Complete":           AdvData(99903201, "Tidal Reef"),
    "Fire C0 - Ruby Quest Complete":                AdvData(99904201, "Raging Volcano"),
    "Wind C2 - Diamond Quest Complete":             AdvData(99905221, "Frozen Spire"),
    "Serpent A1 - Obsidian Quest Complete":         AdvData(99908011, "Serpent Stacks Post-Rune"),

    "Stone Dungeon C1 - Gopher Gloves":             AdvData(102210609, "Stony Cliffs NW"),
    "Water A4 - Frog Flippers":                     AdvData(103041606, "Tidal Reef Post-Rune"),
    "Fire E0 - Salamander Shirt":                   AdvData(104400804, "Raging Volcano NE"),
    "Wind A0 - Kite Cloak":                         AdvData(105001805, "Frozen Spire Post-Rune"),

    "Sanctum A2 - Topaz Shard Hit":                 AdvData(99907021, "Sanctum"),
    "Sanctum C2 - Sapphire Shard Hit":              AdvData(99907221, "Sanctum"),
    "Sanctum C0 - Ruby Shard Hit":                  AdvData(99907201, "Sanctum"),
    "Sanctum A0 - Diamond Shard Hit":               AdvData(99907001, "Sanctum"),

    "Stone E3 - Gold Stone Tablet":                 AdvData(101431110, "Stony Cliffs Post-Rune"),
    "Stone Dungeon A1 - Blue Stone Tablet":         AdvData(102011309, "Stony Cliffs Post-Rune"),

    "Fire A0 - Fire Key":                           AdvData(104001504, "Raging Volcano Post-Rune"),
    "Fire A4 - Fire Key":                           AdvData(104040510, "Raging Volcano Post-Rune"),
    "Fire E4 - Fire Key":                           AdvData(104441503, "Raging Volcano Post-Rune"),

    #"1 - Egg":         AdvData(991024, "Frozen Spire"), #Broken due to in-game randomness
    #"2 - Egg":         AdvData(991025, "Frozen Spire"), #Broken due to in-game randomness
    #"3 - Egg":         AdvData(991026, "Frozen Spire"), #Broken due to in-game randomness
    #"Wind Key[]":      AdvData(83505440 || 83505040 || 83505400, "Frozen Spire"), #Broken due to in-game randomness

    "Rolling B0 - Big Bell Rung":                   AdvData(99908101, "Rolling Rocks Post-Rune"),
    "Sunken B1 - Big Bell Rung":                    AdvData(99909111, "Sunken Island"),
    "Aggro A1 - Big Bell Rung":                     AdvData(99910011, "Aggro Crag"),
    "Nunatak A1 - Big Bell Rung":                   AdvData(99911011, "Sea Nunatak"),

    "Beast A0 - Phoenix Flute":                     AdvData(116111207, "Beast Bridge"),
    "Shoal A0 - Star Viewing Orb":                  AdvData(114001209, "Shoal"),

    # MISC
    "Ancient B2 - Open Ancient Door":               AdvData(100121002, "Sanctum"), # Placed in next region for logic
    "Stone Dungeon C2 - Open Topaz Door":           AdvData(102221002, "Stony Cliffs Post-Rune"),

    "Stone A1 - Tablet Puzzle Clue":                AdvData(101011206, "Stony Cliffs NW"),
    "Stone A3 - Tablet Puzzle Clue":                AdvData(101030308, "Stony Cliffs Post-Rune"),
    "Stone E1 - Tablet Puzzle Clue":                AdvData(101411905, "Stony Cliffs NW"),

    "Stone Dungeon A3 - Tablet Puzzle Clue":        AdvData(102031103, "Stony Cliffs Post-Rune"),
    "Stone Dungeon E1 - Tablet Puzzle Clue":        AdvData(102411706, "Stony Cliffs"),
    "Stone Dungeon E3 - Tablet Puzzle Clue":        AdvData(102431410, "Stony Cliffs Post-Rune"),

    "Beast A1 - Big Bell Stone":                    AdvData(116121206, "Beast Bridge"),
    "Sanctum B1 - Elemental Stone":                 AdvData(107111107, "Sanctum Peak"),

    #

    "Ancient A1 - Ancient Key":                     AdvData(100011711, "Ancient Isle"),
    "Ancient A2 - SE - Ancient Key":                AdvData(100020606, "Ancient Isle"),
    "Ancient A2 - NW - Ancient Key":                AdvData(100020303, "Ancient Isle"), # Topaz quest
    "Ancient A3 - N - Ancient Key":                 AdvData(100031403, "Ancient Isle"),
    "Ancient A3 - S - Ancient Key":                 AdvData(100031110, "Ancient Isle"),
    "Ancient A3 - E - Ancient Key":                 AdvData(100032006, "Ancient Isle"),
    "Ancient B3 - Ancient Key":                     AdvData(100131706, "Ancient Isle"),
    "Ancient C1 - Ancient Key":                     AdvData(100211507, "Ancient Isle"),
    "Ancient C2 - Ancient Key":                     AdvData(100221211, "Ancient Isle"),
    "Ancient C3 - Ancient Key":                     AdvData(100231806, "Ancient Isle"),

    "Rolling A0 - Ancient Key":                     AdvData(108000111, "Rolling Rocks"),  # 7 stars
    "Rolling A1 - Ancient Key":                     AdvData(108011508, "Rolling Rocks"),

    "Stone A2 - Ancient Key":                       AdvData(101020909, "Stony Cliffs Post-Rune"), # blue & gold tablet
    "Stone B0 - NW1 - Ancient Key":                 AdvData(101100206, "Stony Cliffs NW"), # topaz quest
    "Stone B0 - NW2 - Ancient Key":                 AdvData(101100205, "Stony Cliffs NW"), # topaz quest
    "Stone B0 - NW3 - Ancient Key":                 AdvData(101100204, "Stony Cliffs NW"), # topaz quest
    "Stone B1 - Ancient Key":                       AdvData(101110404, "Stony Cliffs NW"), #
    "Stone B2 - Ancient Key":                       AdvData(101122103, "Stony Cliffs"),
    "Stone B4 - Ancient Key":                       AdvData(101141707, "Stony Cliffs Post-Rune"), #topaz quest, topaz rune
    "Stone C0 - Ancient Key":                       AdvData(101202212, "Stony Cliffs"), #topaz quest
    "Stone D3 - Ancient Key":                       AdvData(101330111, "Stony Cliffs Post-Rune"),  # topaz rune
    "Stone E2 - Ancient Key":                       AdvData(101420103, "Stony Cliffs Post-Rune"),  # r rune
    
    "Stone Dungeon B1 - Ancient Key":               AdvData(102111708, "Stony Cliffs NW"), #gopher gloves
    "Stone Dungeon C1 - Ancient Key":               AdvData(102210411, "Stony Cliffs NW"), #topaz rune, gopher gloves
    "Stone Dungeon D0 - Ancient Key":               AdvData(102301109, "Stony Cliffs NW"), #gopher gloves
    "Stone Dungeon D2 - Ancient Key":               AdvData(102320211, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon E2 - Ancient Key":               AdvData(102420803, "Stony Cliffs Post-Rune"),

    "Water A0 - E - Ancient Key":                   AdvData(103002110, "Tidal Reef Post-Rune"), # s rune
    "Water A0 - S - Ancient Key":                   AdvData(103001712, "Tidal Reef Post-Rune"), # frog flippers
    "Water A2 - Ancient Key":                       AdvData(103021007, "Tidal Reef Post-Rune"), # frog flippers, s quest
    "Water B3 - Ancient Key":                       AdvData(103132208, "Tidal Reef"), # frog flippers
    "Water C0 - Ancient Key":                       AdvData(103200408, "Tidal Reef"), # s quest
    "Water C2 - Ancient Key":                       AdvData(103222109, "Tidal Reef"),
    "Water C3 - W - Ancient Key":                   AdvData(103230306, "Tidal Reef Post-Rune"), # d rune
    "Water C3 - NE1 - Ancient Key":                 AdvData(103231903, "Tidal Reef Post-Rune"), # frog flippers
    "Water C3 - NE2 - Ancient Key":                 AdvData(103231803, "Tidal Reef Post-Rune"), # frog flippers
    "Water C3 - NE3 - Ancient Key":                 AdvData(103231703, "Tidal Reef Post-Rune"), # frog flippers
    "Water D0 - Ancient Key":                       AdvData(103301307, "Tidal Reef Post-Rune"), # frog flippers
    "Water D1 - Ancient Key":                       AdvData(103311203, "Tidal Reef"), # frog flippers
    "Water D2 - Ancient Key":                       AdvData(103321204, "Tidal Reef Post-Rune"), # frog flippers
    "Water C4 - Ancient Key":                       AdvData(103241203, "Tidal Reef Post-Rune"), # shell puzzle, f flippers

    "Sunken A0 - Ancient Key":                      AdvData(109001612, "Sunken Island"),
    "Sunken B0 - Ancient Key":                      AdvData(109100305, "Sunken Island"),
    
    "Fire A1 - SE - Ancient Key":                   AdvData(104011611, "Raging Volcano"), # s shirt
    "Fire A1 - SW - Ancient Key":                   AdvData(104011012, "Raging Volcano Post-Rune"), # t rune
    "Fire A1 - NE - Ancient Key":                   AdvData(104012003, "Raging Volcano Post-Rune"),
    "Fire A2 - N - Ancient Key":                    AdvData(104022205, "Raging Volcano"),
    "Fire A2 - S - Ancient Key":                    AdvData(104022112, "Raging Volcano"), # salamander shirt
    "Fire B1 - N1 - Ancient Key":                   AdvData(104110703, "Raging Volcano Post-Rune"), # r quest
    "Fire B1 - N2 - Ancient Key":                   AdvData(104110803, "Raging Volcano Post-Rune"), # r quest
    "Fire B1 - N3 - Ancient Key":                   AdvData(104110903, "Raging Volcano Post-Rune"), # r quest
    "Fire B4 - Ancient Key":                        AdvData(104140607, "Raging Volcano Post-Rune"), # r quest
    "Fire C0 - Ancient Key":                        AdvData(104201806, "Raging Volcano"), # r quest
    "Fire C1 - NE - Ancient Key":                   AdvData(104212105, "Raging Volcano Post-Rune"), # s shirt
    "Fire C1 - SW - Ancient Key":                   AdvData(104210212, "Raging Volcano"), # s shirt
    "Fire C3 - Ancient Key":                        AdvData(104231003, "Raging Volcano Post-Rune"), # r quest
    "Fire D4 - Ancient Key":                        AdvData(104340806, "Raging Volcano Post-Rune"), # idol puzzle

    "Aggro B0 - W - Ancient Key":                   AdvData(110100711, "Aggro Crag"),
    "Aggro B0 - E - Ancient Key":                   AdvData(110101205, "Aggro Crag"),
    
    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Wind A1 - Ancient Key":                        AdvData(105011404, "Frozen Spire Post-Rune"), # glyph puzzle
    "Wind A3 - Ancient Key":                        AdvData(105031307, "Frozen Spire Post-Rune"), # k cloak
    "Wind B1 - Ancient Key":                        AdvData(105111603, "Frozen Spire Post-Rune"), # double check req
    "Wind C2 - Ancient Key":                        AdvData(105220705, "Frozen Spire"), # d quest
    "Wind C4 - Ancient Key":                        AdvData(105242109, "Frozen Spire"),
    "Wind D3 - Ancient Key":                        AdvData(105331507, "Frozen Spire Post-Rune"), # k cloak
    "Wind D4 - E - Ancient Key":                    AdvData(105341405, "Frozen Spire Post-Rune"), # s rune
    "Wind D4 - NW1 - Ancient Key":                  AdvData(105340304, "Frozen Spire"), # d quest
    "Wind D4 - NW2 - Ancient Key":                  AdvData(105340404, "Frozen Spire"), # d quest
    "Wind D4 - NW3 - Ancient Key":                  AdvData(105340504, "Frozen Spire"), # d quest
    "Wind E2 - S - Ancient Key":                    AdvData(105421609, "Frozen Spire"), # d quest
    "Wind E2 - NE - Ancient Key":                   AdvData(105422203, "Frozen Spire Post-Rune"), # d quest
    "Wind E4 - E - Ancient Key":                    AdvData(105440806, "Frozen Spire Post-Rune"), # d rune
    "Wind E4 - SW - Ancient Key":                   AdvData(105440310, "Frozen Spire Post-Rune"), # k cloak, d quest

    "Nunatak A1 - Ancient Key":                     AdvData(111011905, "Sea Nunatak"), # ancient rune
    "Nunatak B1 - Ancient Key":                     AdvData(111110806, "Sea Nunatak"),

    "Tropic A1 - Ancient Key":                      AdvData(113010608, "Star Tropic"), # ancient rune

    #77 keys

    "Stone B0 - Topaz":                             AdvData(101101510, "Stony Cliffs NW"),
    "Stone B1 - Topaz":                             AdvData(101110112, "Stony Cliffs NW"),
    "Stone B2 - Topaz":                             AdvData(101121212, "Stony Cliffs Post-Rune"), #Rq: topaz quest
    "Stone C0 - Topaz":                             AdvData(101200506, "Stony Cliffs Post-Rune"),
    "Stone C2 - W - Topaz":                         AdvData(101220904, "Stony Cliffs Post-Rune"),
    "Stone C2 - E - Topaz":                         AdvData(101221504, "Stony Cliffs"),
    "Stone C3 - N - Topaz":                         AdvData(101232107, "Stony Cliffs"),
    "Stone C3 - S - Topaz":                         AdvData(101232110, "Stony Cliffs"),
    "Stone D2 - Topaz":                             AdvData(101321605, "Stony Cliffs"),
    "Stone Dungeon C1 - Topaz":                     AdvData(102211512, "Stony Cliffs NW"), #Rq: gopher gloves
    "Rolling A0 - Topaz":                           AdvData(108002205, "Rolling Rocks"), #Rq: topaz quest, 7 stars
    "Tropic A1 - Topaz":                            AdvData(113011205, "Star Tropic"), #Rq: ancient rune stone, all legendaries

    "Water A1 - Sapphire":                          AdvData(103011909, "Tidal Reef"), #frog flippers
    "Water B2 - S - Sapphire":                      AdvData(103120911, "Tidal Reef"),
    "Water B2 - N - Sapphire":                      AdvData(103121703, "Tidal Reef"),
    "Water C0 - Sapphire":                          AdvData(103202012, "Tidal Reef Post-Rune"), #sapphire rune stone #
    "Water C2 - N - Sapphire":                      AdvData(103220803, "Tidal Reef"),  # sapphire quest
    "Water C2 - W - Sapphire":                      AdvData(103220306, "Tidal Reef"),
    "Water D1 - Sapphire":                          AdvData(103311811, "Tidal Reef Post-Rune"), #s rune stone
    "Water D2 - N - Sapphire":                      AdvData(103320503, "Tidal Reef Post-Rune"),
    "Water D2 - W - Sapphire":                      AdvData(103320206, "Tidal Reef Post-Rune"), #s rune stone
    "Water D3 - Sapphire":                          AdvData(103331803, "Tidal Reef Post-Rune"), #s rune stone
    "Sunken B0 - Sapphire":                         AdvData(109101706, "Sunken Island"), #sapphire quest, 21 stars
    "Tropic A1 - Sapphire":                         AdvData(113011305, "Star Tropic"), # ancient rune stone, all legendaries

    "Fire A3 - N - Ruby":                           AdvData(104031005, "Raging Volcano Post-Rune"),
    "Fire A3 - S - Ruby":                           AdvData(104031211, "Raging Volcano Post-Rune"), #r rune stone
    "Fire A3 - NW - Ruby":                          AdvData(104030703, "Raging Volcano Post-Rune"), # r rune stone
    "Fire B2 - Ruby":                               AdvData(104122109, "Raging Volcano"),
    "Fire C0 - Ruby":                               AdvData(104200112, "Raging Volcano Post-Rune"), # ruby rune stone
    "Fire C2 - Ruby":                               AdvData(104220504, "Raging Volcano"),
    "Fire D0 - Ruby":                               AdvData(104300603, "Raging Volcano NE"),
    "Fire D1 - Ruby":                               AdvData(104311210, "Raging Volcano Post-Rune"), # ruby rune stone
    "Fire D2 - E - Ruby":                           AdvData(104321804, "Raging Volcano"),
    "Fire D2 - W - Ruby":                           AdvData(104321004, "Raging Volcano"),
    "Aggro B1 - Ruby":                              AdvData(110110511, "Aggro Crag"), # ruby quest, 35 stars
    "Tropic A1 - Ruby":                             AdvData(113011304, "Star Tropic"), # ancient rune stone, all legendaries

    "Wind B2 - Diamond":                            AdvData(105120303, "Frozen Spire"),
    "Wind C1 - W - Diamond":                        AdvData(105210910, "Frozen Spire Post-Rune"), # d rune stone
    "Wind C1 - E - Diamond":                        AdvData(105211110, "Frozen Spire Post-Rune"), # d rune stone
    "Wind C2 - Diamond":                            AdvData(105220906, "Frozen Spire Post-Rune"), # diamond rune stone
    "Wind C3 - Diamond":                            AdvData(105230603, "Frozen Spire Post-Rune"), # diamond quest complete
    "Wind C4 - Diamond":                            AdvData(105241004, "Frozen Spire"),
    "Wind D1 - E - Diamond":                        AdvData(105311612, "Frozen Spire Post-Rune"), # d rune stone
    "Wind D1 - W - Diamond":                        AdvData(105310210, "Frozen Spire Post-Rune"), # d rune stone
    "Wind D2 - Diamond":                            AdvData(105321303, "Frozen Spire"),
    "Wind D4 - Diamond":                            AdvData(105340803, "Frozen Spire Post-Rune"),
    "Nunatak B0 - Diamond":                         AdvData(111101003, "Sea Nunatak"), # diamond quest complete
    "Tropic A1 - Diamond":                          AdvData(113011204, "Star Tropic"), # ancient rune stone, all legendaries

    "Stone A2 - Obsidian":                          AdvData(101021409, "Stony Cliffs Post-Rune"),  # stone tablet blue, tablet golda
    "Stone D1 - Obsidian":                          AdvData(101312204, "Stony Cliffs"),
    "Water C4 - Obsidian":                          AdvData(103241803, "Tidal Reef Post-Rune"),  # shell puzzle, f flippers
    "Water D0 - Obsidian":                          AdvData(103301004, "Tidal Reef Post-Rune"),  # frog flippers
    "Fire D4 - Obsidian":                           AdvData(104341606, "Raging Volcano Post-Rune"),  # idol puzzle
    "Fire E0 - Obsidian":                           AdvData(104401511, "Raging Volcano Post-Rune"),  # salamander shirt
    "Wind B0 - Obsidian":                           AdvData(105100205, "Frozen Spire"),
    "Wind A1 - Obsidian":                           AdvData(105010904, "Frozen Spire Post-Rune"), # Glyph Puzzle
    "Rolling A1 - Obsidian":                        AdvData(108011803, "Rolling Rocks"),  # gopher gloves, 7 stars
    "Sunken A0 - Obsidian":                         AdvData(109002010, "Sunken Island"),  # frog flippers
    "Aggro B0 - Obsidian":                          AdvData(110100205, "Aggro Crag"),  # salamander shirt
    "Nunatak B1 - Obsidian":                        AdvData(111111705, "Sea Nunatak"),  # diamond quest
    "Serpent A1 - Obsidian":                        AdvData(106010412, "Serpent Stacks Post-Rune"),  # rune stones: t,s,r,d,o, o quest(?)
    "Lost A1 - Obsidian":                           AdvData(115011106, "Lost Landing"),  # phoenix flute (or secret find?)

    # All 120 Star Pieces are locations!
    "Ancient A1 - Star Piece":                      AdvData(100011708, "Ancient Isle"),
    "Ancient B1 - Star Piece":                      AdvData(100110812, "Ancient Isle"),
    "Ancient C0 - Star Piece":                      AdvData(100201308, "Ancient Isle"),

    "Stone A1 - Star Piece":                        AdvData(101010512, "Stony Cliffs NW"), # 5 stars
    "Stone B2 - Star Piece":                        AdvData(101121405, "Stony Cliffs Post-Rune"), # t quest
    "Stone B3 - Star Piece":                        AdvData(101130212, "Stony Cliffs Post-Rune"), # t quest
    "Stone B4 - Star Piece":                        AdvData(101140303, "Stony Cliffs Post-Rune"), # g globes t quest
    "Stone C0 - Star Piece":                        AdvData(101200112, "Stony Cliffs"), # t quest
    "Stone C1 - Star Piece":                        AdvData(101212011, "Stony Cliffs"), # t quest
    "Stone C4 - Star Piece":                        AdvData(101240208, "Stony Cliffs Post-Rune"), # g gloves t quest
    "Stone D3 - N - Star Piece":                    AdvData(101332203, "Stony Cliffs Post-Rune"), # 20 star pieces, t quest, d quest. g gloves
    "Stone D3 - S - Star Piece":                    AdvData(101332007, "Stony Cliffs Post-Rune"), # 20 star pieces, t quest, d quest
    "Stone E1 - Star Piece":                        AdvData(101410412, "Stony Cliffs"),
    "Stone E4 - Star Piece":                        AdvData(101440203, "Stony Cliffs Post-Rune"),
    "Stone Dungeon B1 - Star Piece":                AdvData(102110412, "Stony Cliffs NW"), # g gloves
    "Stone Dungeon C1 - Star Piece":                AdvData(102210506, "Stony Cliffs NW"), # g gloves
    "Stone Dungeon C3 - Star Piece":                AdvData(102230803, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon E1 - Star Piece":                AdvData(102410905, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon E2 - Star Piece":                AdvData(102421209, "Stony Cliffs Post-Rune"), # g gloves, f flippers

    "Stone D1 - Music Puzzle Star Piece 1":         AdvData(99901311, "Stony Cliffs"), # t rune, t quest, ancient key
    "Stone D1 - Music Puzzle Star Piece 2":         AdvData(99901312, "Stony Cliffs"), # t rune, t quest, ancient key
    "Stone D1 - Music Puzzle Star Piece 3":         AdvData(99901313, "Stony Cliffs"), # t rune, t quest, ancient key
    "Stone A2 - Tablet Puzzle Star Piece":          AdvData(99901021, "Stony Cliffs Post-Rune"), # blue & gold tablet

    "Water A0 - Star Piece":                        AdvData(103002003, "Tidal Reef Post-Rune"), # s rune
    "Water A2 - S - Star Piece":                    AdvData(103021312, "Tidal Reef Post-Rune"), # f flippers
    "Water A2 - N - Star Piece":                    AdvData(103020803, "Tidal Reef Post-Rune"), # f flippers s quest || k cloak
    "Water A4 - Star Piece":                        AdvData(103042108, "Tidal Reef S"), # f flippers
    "Water B1 - Star Piece":                        AdvData(103110412, "Tidal Reef"), # f flippers
    "Water B4 - Star Piece":                        AdvData(103142208, "Tidal Reef S"),
    "Water C0 - Star Piece":                        AdvData(103201807, "Tidal Reef"), # s quest
    "Water C1 - W - Star Piece":                    AdvData(103210204, "Tidal Reef"),
    "Water C1 - E - Star Piece":                    AdvData(103211207, "Tidal Reef"),
    "Water C2 - Star Piece":                        AdvData(103222207, "Tidal Reef"), # s quest
    "Water D2 - Star Piece":                        AdvData(103322012, "Tidal Reef Post-Rune"), # f flippers, s shirt
    "Water D3 - Star Piece":                        AdvData(103331910, "Tidal Reef Post-Rune"), # f flippers | Double check
    "Water E0 - W - Star Piece":                    AdvData(103400109, "Tidal Reef Post-Rune"), # f flippers
    "Water E0 - E - Star Piece":                    AdvData(103402005, "Tidal Reef Post-Rune"), # s quest | double check
    "Water E2 - Star Piece":                        AdvData(103422008, "Tidal Reef Post-Rune"), # f flippers
    "Water E3 - NE - Star Piece":                   AdvData(103432204, "Tidal Reef Post-Rune"), # s quest, t quest
    "Water E3 - SW - Star Piece":                   AdvData(103430411, "Tidal Reef Post-Rune"), # s quest, t quest

    "Water B0 - Music Puzzle Star Piece 1":         AdvData(99903101, "Tidal Reef Post-Rune"), # s quest
    "Water B0 - Music Puzzle Star Piece 2":         AdvData(99903102, "Tidal Reef Post-Rune"), # s quest
    "Water B0 - Music Puzzle Star Piece 3":         AdvData(99903103, "Tidal Reef Post-Rune"), # s quest
    "Water C4 - Shell Puzzle Star Piece":           AdvData(99903241, "Tidal Reef Post-Rune"), # shell puzzle, f flippers

    "Fire B3 - Star Piece":                         AdvData(104132211, "Raging Volcano Post-Rune"),
    "Fire B4 - Star Piece":                         AdvData(104142005, "Raging Volcano Post-Rune"), # r quest
    "Fire C0 - Star Piece":                         AdvData(104202107, "Raging Volcano"),
    "Fire C1 - Star Piece":                         AdvData(104210310, "Raging Volcano"),
    "Fire C3 - Star Piece":                         AdvData(104231507, "Raging Volcano Post-Rune"),
    "Fire D1 - S - Star Piece":                     AdvData(104310109, "Raging Volcano"), # r quest
    "Fire D1 - N - Star Piece":                     AdvData(104310105, "Raging Volcano Post-Rune"), # r rune
    "Fire D3 - S - Star Piece":                     AdvData(104331312, "Raging Volcano Post-Rune"), # r quest | double check
    "Fire D3 - W - Star Piece":                     AdvData(104330507, "Raging Volcano Post-Rune"), # r quest | double
    "Fire D4 - Star Piece":                         AdvData(104340404, "Raging Volcano Post-Rune"), # r quest, s shirt, k cloak
    "Fire E0 - Star Piece":                         AdvData(104401704, "Raging Volcano NE"), # s shirt
    "Fire E1 - E - Star Piece":                     AdvData(104411108, "Raging Volcano Post-Rune"), # r quest shirt
    "Fire E1 - W - Star Piece":                     AdvData(104410106, "Raging Volcano Post-Rune"), # s shirt
    "Fire E3 - S - Star Piece":                     AdvData(104431212, "Raging Volcano Post-Rune"), # r quest, s quest
    "Fire E3 - SE - Star Piece":                    AdvData(104431512, "Raging Volcano Post-Rune"), # r quest, s quest
    "Fire E3 - W - Star Piece":                     AdvData(104430106, "Raging Volcano Post-Rune"),

    "Fire B3 - Music Puzzle Star Piece 1":          AdvData(99904131, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - Music Puzzle Star Piece 2":          AdvData(99904132, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - Music Puzzle Star Piece 3":          AdvData(99904133, "Raging Volcano Post-Rune"), # r quest
    "Fire D4 - Idol Puzzle Star Piece":             AdvData(99904341, "Raging Volcano Post-Rune"), # idol puzzle

    # locations might be broken due to in-game randomness
    "Wind A0 - Star Piece":                         AdvData(105001106, "Frozen Spire Post-Rune"), # k cloak
    "Wind A3 - Star Piece":                         AdvData(105031012, "Frozen Spire"), # k cloak
    "Wind B0 - Star Piece":                         AdvData(105101606, "Frozen Spire Post-Rune"),
    "Wind B1 - Star Piece":                         AdvData(105111309, "Frozen Spire"),
    "Wind B2 - S - Star Piece":                     AdvData(105120212, "Frozen Spire Post-Rune"),
    "Wind B2 - N - Star Piece":                     AdvData(105121703, "Frozen Spire Post-Rune"), # d quest
    "Wind B3 - Star Piece":                         AdvData(105131907, "Frozen Spire Post-Rune"), # d quest
    "Wind C2 - Star Piece":                         AdvData(105220204, "Frozen Spire"), # d quest
    "Wind C3 - NE - Star Piece":                    AdvData(105231703, "Frozen Spire"), # d rune
    "Wind C3 - SW - Star Piece":                    AdvData(105230211, "Frozen Spire"), # d rune
    "Wind D2 - Star Piece":                         AdvData(105320208, "Frozen Spire Post-Rune"), # k cloak
    "Wind D4 - Star Piece":                         AdvData(105341904, "Frozen Spire"),
    "Wind E1 - W - Star Piece":                     AdvData(105410209, "Frozen Spire Post-Rune"), # k cloak, g gloves
    "Wind E1 - SE - Star Piece":                    AdvData(105410911, "Frozen Spire Post-Rune"), # d quest, r quest
    "Wind E1 - SW - Star Piece":                    AdvData(105410711, "Frozen Spire Post-Rune"), # d quest, r quest
    "Wind E2 - Star Piece":                         AdvData(105421004, "Frozen Spire"), # d quest
    "Wind E4 - Star Piece":                         AdvData(105440510, "Frozen Spire Post-Rune"), # k cloak

    "Wind B4 - Music Puzzle Star Piece 1":          AdvData(99905141, "Frozen Spire Post-Rune"), # d quest
    "Wind B4 - Music Puzzle Star Piece 2":          AdvData(99905142, "Frozen Spire Post-Rune"), # d quest
    "Wind B4 - Music Puzzle Star Piece 3":          AdvData(99905143, "Frozen Spire Post-Rune"), # d quest
    "Wind A1 - Glyph Puzzle Star Piece":            AdvData(99905011, "Frozen Spire Post-Rune"), # glyph puzzle

    "Rolling A0 - Star Piece":                      AdvData(108000605, "Rolling Rocks"), # 7 stars, t quest
    "Rolling B0 - Star Piece":                      AdvData(108101107, "Rolling Rocks Post-Rune"), # g gloves
    "Rolling B1 - Star Piece":                      AdvData(108111107, "Rolling Rocks Post-Rune"), #
    "Rolling B0 - Big Bell Star Piece":             AdvData(99908102, "Ancient Isle"), # rolling big bell

    "Sunken A1 - Star Piece":                       AdvData(109011306, "Sunken Island"), # ancient rune
    "Sunken B0 - Star Piece":                       AdvData(109101704, "Sunken Island"), # 21 stars, s quest
    "Sunken B1 - Big Bell Star Piece":              AdvData(99909112, "Ancient Isle"), # sunken big bell

    "Aggro A1 - Star Piece":                        AdvData(110010409, "Aggro Crag"), # ancient rune
    "Aggro B1 - Star Piece":                        AdvData(110111511, "Aggro Crag"), # 35 star, r quest
    "Aggro A1 - Big Bell Star Piece":               AdvData(99910012, "Ancient Isle"), # aggro big bell

    "Nunatak A0 - Star Piece":                      AdvData(111001310, "Sea Nunatak"), # ancient rune
    "Nunatak B0 - Star Piece":                      AdvData(111101903, "Sea Nunatak"), # 49 stars, d quest
    "Nunatak A1 - Big Bell Star Piece":             AdvData(99911012, "Ancient Isle"), # nunatak big bell

    "Lost B1 - Star Piece":                         AdvData(115111209, "Lost Landing"),

    "Shoal A0 - Star Piece":                        AdvData(114001711, "Shoal"), # f flippers

    "Tropic A0 - Star Piece":                       AdvData(113001911, "Star Tropic"), #
    "Tropic A1 - 4 - Star Piece":                   AdvData(113011105, "Star Tropic"), # g gloves, s shirt, f flippers, k cloak
    "Tropic A1 - 1 - Star Piece":                   AdvData(113010803, "Star Tropic"), # g gloves
    "Tropic A1 - 2 - Star Piece":                   AdvData(113010905, "Star Tropic"), # g gloves, s shirt,
    "Tropic A1 - 3 - Star Piece":                   AdvData(113011003, "Star Tropic"), # g gloves, s shirt, f flippers
    "Tropic B0 - S - Star Piece":                   AdvData(113100508, "Star Tropic"), # a rune
    "Tropic B0 - N - Star Piece":                   AdvData(113100904, "Star Tropic"), # o rune, s shirt

    "Serpent A1 - W - Star Piece":                  AdvData(106010311, "Serpent Stacks Post-Rune"), # k cloak, o quest
    "Serpent A1 - N - Star Piece":                  AdvData(106011403, "Serpent Stacks Post-Rune"), # k cloak, o quest
    "Serpent A2 - Star Piece":                      AdvData(106021904, "Serpent Stacks"), # k cloak, o quest
    "Serpent A3 - Star Piece":                      AdvData(106031705, "Serpent Stacks"), # k cloak
    "Serpent A4 - NW - Star Piece":                 AdvData(106040304, "Serpent Stacks Post-Rune"), # o quest, t quest
    "Serpent A4 - N - Star Piece":                  AdvData(106040903, "Serpent Stacks Post-Rune"), # o quest, t quest
    "Serpent A6 - W - Star Piece":                  AdvData(106060204, "Serpent Stacks Post-Rune"), # s quest, o quest
    "Serpent A6 - E - Star Piece":                  AdvData(106062111, "Serpent Stacks Post-Rune"), # s quest, o quest
    "Serpent A7 - E - Star Piece":                  AdvData(106072212, "Serpent Stacks Post-Rune"), # o quest, r quest
    "Serpent A7 - W - Star Piece":                  AdvData(106070212, "Serpent Stacks Post-Rune"), # o quest, r quest
    "Serpent A8 - S - Star Piece":                  AdvData(106082011, "Serpent Stacks Post-Rune"), # o quest, d quest
    "Serpent A8 - N - Star Piece":                  AdvData(106082009, "Serpent Stacks Post-Rune"), # o quest, d quest

    "Locked A0 - Star Piece":                       AdvData(112012012, "Locked"),

    # In the future, could include milestones as locations. e.g. each of the steam achievements, plus extras.
}

notesanity_table = {
    # 24 checks
    "Stone B0 - Music Note":                        AdvData(101102012, "Stony Cliffs NW"), # topaz rune
    "Stone B2 - Music Note":                        AdvData(101121209, "Stony Cliffs Post-Rune"), # topaz quest
    "Stone B3 - Music Note":                        AdvData(101131011, "Stony Cliffs Post-Rune"), # topaz rune
    "Stone C1 - Music Note":                        AdvData(101211704, "Stony Cliffs"), #
    "Stone D1 - Music Note":                        AdvData(101310510, "Stony Cliffs"), # topaz quest
    "Stone D4 - Music Note":                        AdvData(101341907, "Stony Cliffs Post-Rune"), # topaz rune

    "Water A2 - Music Note":                        AdvData(103021807, "Tidal Reef Post-Rune"), # s rune
    "Water B0 - Music Note":                        AdvData(103100208, "Tidal Reef Post-Rune"), # s rune
    "Water C1 - Music Note":                        AdvData(103210611, "Tidal Reef"),
    "Water D1 - Music Note":                        AdvData(103312203, "Tidal Reef Post-Rune"), # s rune
    "Water E0 - Music Note":                        AdvData(103401810, "Tidal Reef Post-Rune"), # s rune
    "Water E2 - Music Note":                        AdvData(103421811, "Tidal Reef Post-Rune"), # s rune

    "Fire A2 - Music Note":                         AdvData(104021110, "Raging Volcano"),
    "Fire B0 - Music Note":                         AdvData(104101210, "Raging Volcano Post-Rune"), # r rune
    "Fire B2 - Music Note":                         AdvData(104121512, "Raging Volcano Post-Rune"), # r rune
    "Fire C3 - Music Note":                         AdvData(104231511, "Raging Volcano Post-Rune"), # r rune
    "Fire D3 - Music Note":                         AdvData(104332209, "Raging Volcano Post-Rune"), # r rune
    "Fire E1 - Music Note":                         AdvData(104412009, "Raging Volcano Post-Rune"), # r rune

    "Wind A0 - Music Note":                         AdvData(105002010, "Frozen Spire"),
    "Wind A2 - Music Note":                         AdvData(105021908, "Frozen Spire Post-Rune"), # d quest,
    "Wind B1 - Music Note":                         AdvData(105110910, "Frozen Spire"),
    "Wind C3 - Music Note":                         AdvData(105230208, "Frozen Spire Post-Rune"),  # d rune,
    "Wind D3 - Music Note":                         AdvData(105330512, "Frozen Spire Post-Rune"), # d quest
    "Wind E3 - Music Note":                         AdvData(105430307, "Frozen Spire Post-Rune"),  # d rune
}

circlet_table = { # TODO implement and add logic for these
    "Serpent A4 - Serpent Lock Shard":              AdvData(106041904, "Serpent Stacks Post-Rune"),
    "Serpent A5 - NE - Serpent Lock Shard":         AdvData(106052104, "Serpent Stacks Post-Rune"),
    "Serpent A5 - SE - Serpent Lock Shard":         AdvData(106052112, "Serpent Stacks Post-Rune"),
    "Serpent A5 - NW - Serpent Lock Shard":         AdvData(106050207, "Serpent Stacks Post-Rune"),
    "Serpent A5 - SW - Serpent Lock Shard":         AdvData(106050209, "Serpent Stacks Post-Rune"),
    "Serpent A6 - Serpent Lock Shard":              AdvData(106060711, "Serpent Stacks Post-Rune"),
    "Serpent A7 - Serpent Lock Shard":              AdvData(106072006, "Serpent Stacks Post-Rune"),
    "Serpent A8 - Serpent Lock Shard":              AdvData(106080508, "Serpent Stacks Post-Rune"),
    "Serpent A5 - Serpent Circlet":                 AdvData(106051108, "Serpent Stacks Post-Rune"),
    "Fire D3 - Obsidian":                           AdvData(104331811, "Raging Volcano Post-Rune"),  # Serpent Circlet
}

seashell_table = {

    # 24 checks
    "Water B2 - Shell":                             AdvData(109001, "Tidal Reef"),
    "Water C0 - Shell":                             AdvData(110034, "Tidal Reef"),
    "Water B0 - Shell":                             AdvData(113779, "Tidal Reef"),
    "Water B1 - Shell":                             AdvData(109727, "Tidal Reef"),
    "Water C1 - Shell":                             AdvData(109466, "Tidal Reef"),
    "Water C2 - Shell":                             AdvData(108836, "Tidal Reef"),
    "Water D2 - Shell":                             AdvData(109127, "Tidal Reef Post-Rune"), # s rune
    "Water A1 - Shell":                             AdvData(111286, "Tidal Reef"), # s rune
    "Water A0 - Shell":                             AdvData(111579, "Tidal Reef Post-Rune"), # s rune
    "Water A3 - Shell":                             AdvData(114803, "Tidal Reef"), # s rune
    "Water B3 - Shell":                             AdvData(110854, "Tidal Reef S"), # s rune
    "Water B4 - Shell":                             AdvData(126146, "Tidal Reef S"), # s rune
    "Water C4 - Shell":                             AdvData(126171, "Tidal Reef S"),
    "Water C3 - Shell":                             AdvData(108596, "Tidal Reef Post-Rune"), # s rune
    "Water D4 - Shell":                             AdvData(129544, "Tidal Reef Post-Rune"), # s rune
    "Water E4 - Shell":                             AdvData(125935, "Tidal Reef Post-Rune"), # s rune
    "Water E2 - Shell":                             AdvData(113315, "Tidal Reef Post-Rune"), # s rune
    "Water E1 - Shell":                             AdvData(113547, "Tidal Reef Post-Rune"), # s rune
    "Water E0 - Shell":                             AdvData(110713, "Tidal Reef Post-Rune"), # s rune
    "Water D3 - Shell":                             AdvData(113163, "Tidal Reef Post-Rune"), # s rune
    "Water A4 - Shell":                             AdvData(126066, "Tidal Reef S"),  # f flippers
    "Water D1 - Shell":                             AdvData(109899, "Tidal Reef"),  # f flippers
    "Water D0 - Shell":                             AdvData(110330, "Tidal Reef Post-Rune"),  # f flippers
    "Water A2 - Shell":                             AdvData(112462, "Tidal Reef Post-Rune"),  # f flippers

}

# 10 checks
jellyfish_table = {
    "Topaz Sea - Jellyfish":                        AdvData(108506, "Topaz Sea"),
    "Diamond Sea - Jellyfish":                      AdvData(108505, "Diamond Sea"),
    "Obsidian Sea - Jellyfish":                     AdvData(108512, "Obsidian Sea"),
    "Sapphire Sea - Jellyfish":                     AdvData(108503, "Sapphire Sea"),
    "Ruby Sea - W - Jellyfish":                     AdvData(108511, "Ruby Sea"),
    "Ruby Sea - E - Jellyfish":                     AdvData(108507, "Ruby Sea"),
    "Beast Sea - W - Jellyfish":                    AdvData(108508, "Beast Sea"),
    "Beast Sea - E - Jellyfish":                    AdvData(108510, "Beast Sea"),
    "Lost Sea - Jellyfish":                         AdvData(108504, "Lost Sea"),
    "Northeast Sea - Jellyfish":                    AdvData(108509, "Northeast Sea"),
}

# 24 checks
secrets_table = {

    "Ancient A1 - Discover Secret":                 AdvData(101044, "Ancient Isle"),

    "Stone E1 - Discover Secret":                   AdvData(107724, "Stony Cliffs"),
    "Stone D4 - Discover Secret":                   AdvData(106792, "Stony Cliffs Post-Rune"),

    "Rolling A0 - Discover Secret":                 AdvData(103790, "Rolling Rocks"),

    "Nunatak B0 - E - Discover Secret":             AdvData(123457, "Sea Nunatak"),
    "Nunatak B0 - SE - Discover Secret":            AdvData(123426, "Sea Nunatak"),
    "Nunatak B0 - CW - Discover Secret":            AdvData(123461, "Sea Nunatak"),
    "Nunatak B0 - W - Discover Secret":             AdvData(123447, "Sea Nunatak"),

    "Shoal A0 - W - Discover Secret":               AdvData(104364, "Shoal"),
    "Shoal A0 - E - Discover Secret":               AdvData(104321, "Shoal"),
    "Shoal A0 - SE - Discover Secret":              AdvData(104322, "Shoal"),

    "Aggro B1 - Discover Secret":                   AdvData(122712, "Aggro Crag"),
    "Aggro A0 - W - Discover Secret":               AdvData(122517, "Aggro Crag"),
    "Aggro A0 - E - Discover Secret":               AdvData(122488, "Aggro Crag"),

    "Sunken A0 - Discover Secret":                  AdvData(122982, "Sunken Island"),

    "Tropic A0 - Discover Secret":                  AdvData(103122, "Star Tropic"),

    "Lost B1 - CS - Discover Secret":               AdvData(128953, "Lost Landing"),
    "Lost B1 - W - Discover Secret":                AdvData(128951, "Lost Landing"),

    "Fire C4 - Discover Secret":                    AdvData(118109, "Raging Volcano Post-Rune"),
    "Fire C2 - Discover Secret":                    AdvData(115494, "Raging Volcano"),
    "Fire E1 - Discover Secret":                    AdvData(118553, "Raging Volcano Post-Rune"),

    "Wind A0 - Discover Secret":                    AdvData(120206, "Frozen Spire"),
    "Wind A1 - Discover Secret":                    AdvData(120347, "Frozen Spire"),
    "Wind D1 - Discover Secret":                    AdvData(121434, "Frozen Spire Post-Rune"),

}

# Est. 101 extra checks here.
locksanity_table = {
    "Ancient B3 - Lock":                            AdvData(100221, "Ancient Isle"),
    "Ancient B2 - Lock":                            AdvData(101289, "Ancient Isle"),
    "Ancient A3 - Lock":                            AdvData(100548, "Ancient Isle"),
    "Ancient C2 - 3x Lock":                         AdvData(100436, "Ancient Isle"),
    "Ancient A1 - 3x Lock":                         AdvData(101049, "Ancient Isle"), # access o sea

    "Stone C2 - Lock":                              AdvData(107588, "Stony Cliffs"),
    "Stone E1 - 3x Lock":                           AdvData(107761, "Stony Cliffs"),
    "Stone B1 - Lock":                              AdvData(107044, "Stony Cliffs NW"), # t rune

    "Water B2 - Lock":                              AdvData(108972, "Tidal Reef"),
    "Water C1 - 3x Lock":                           AdvData(109439, "Tidal Reef"),
    "Water D3 - Lock":                              AdvData(113120, "Tidal Reef Post-Rune"), # s rune

    "Fire E0 - 3x Lock (Fire)":                     AdvData(118309, "Raging Volcano NE"),
    "Fire A3 - Lock":                               AdvData(116779, "Raging Volcano Post-Rune"),
    "Fire D2 - Lock":                               AdvData(115819, "Raging Volcano"),
    "Fire D2 - 3x Lock":                            AdvData(115799, "Raging Volcano"),

    "Wind C3 - Lock":                               AdvData(120637, "Frozen Spire Post-Rune"),
    "Wind D3 - 3x Lock":                            AdvData(120553, "Frozen Spire"),
    "Wind D1 - Lock":                               AdvData(121455, "Frozen Spire Post-Rune"),
    "Wind A0 - Lock (Wind)":                        AdvData(120220, "Frozen Spire"),

    "Sanctum B2 - W - 3x Lock":                     AdvData(123943, "Sanctum"),
    "Sanctum B2 - E - 3x Lock":                     AdvData(123942, "Sanctum"),
    "Sanctum A1 - 3x Lock":                         AdvData(124157, "Sanctum"),
    "Sanctum C1 - 3x Lock":                         AdvData(124282, "Sanctum"),

    "Rolling B1 - 3x Lock":                         AdvData(104767, "Rolling Rocks Post-Rune"),

    "Sunken A1 - 3x Lock":                          AdvData(123081, "Sunken Island"),

    "Aggro A1 - 3x Lock":                           AdvData(122917, "Aggro Crag"),

    "Nunatak A0 - 3x Lock":                         AdvData(123383, "Sea Nunatak"),

    "Locked A0 - 6x Lock":                          AdvData(104286, "Locked"),

    "Lost A1 - Lock":                               AdvData(127286, "Lost Landing"),

    "Ancient C1 - Star Lock 1":                     AdvData(100984, "Ancient Isle"),

    "Overworld - Star Lock 3":                      AdvData(108488, "Topaz Sea"),
    "Overworld - Star Lock 15":                     AdvData(108494, "Topaz Sea"),
    "Overworld - Star Lock 30":                     AdvData(108499, "Diamond Sea"),
    "Overworld - Star Lock 45":                     AdvData(108516, "Obsidian Sea"),

    "Stone A1 - Star Lock 5":                       AdvData(107545, "Stony Cliffs NW"),
    "Stone C4 - Star Lock 15":                      AdvData(107259, "Stony Cliffs Post-Rune"),
    "Stone E3 - Star Lock 20":                      AdvData(106823, "Stony Cliffs Post-Rune"),
    "Stone Dungeon A1 - Star Lock 20":              AdvData(101941, "Stony Cliffs Post-Rune"),

    "Water A2 - Star Lock 30":                      AdvData(112443, "Tidal Reef Post-Rune"),

    "Rolling A0 - Star Lock 7":                     AdvData(103800, "Rolling Rocks"),
    "Sunken B0 - Star Lock 21":                     AdvData(123144, "Sunken Island"),
    "Lost B0 - Star Lock 30":                       AdvData(100181, "Lost Landing"),
    "Aggro B0 - Star Lock 35":                      AdvData(122670, "Aggro Crag"),
    "Nunatak B0 - Star Lock 49":                    AdvData(123481, "Sea Nunatak"),

    "Ancient B1 - Ancient Rune Lock":               AdvData(100251, "Ancient Isle"),

    "Stone C0 - Topaz Rune Lock":                   AdvData(108053, "Stony Cliffs Post-Rune"), #post-rune is inclusive of rune lock checks
    "Stone C1 - Topaz Rune Lock":                   AdvData(107476, "Stony Cliffs Post-Rune"),
    "Stone E1 - Topaz Rune Lock":                   AdvData(107758, "Stony Cliffs Post-Rune"),
    "Stone E2 - Topaz Rune Lock":                   AdvData(107666, "Stony Cliffs Post-Rune"),
    "Stone E3 - Topaz Rune Lock":                   AdvData(106822, "Stony Cliffs Post-Rune"),
    "Stone C4 - Topaz Rune Lock":                   AdvData(107252, "Stony Cliffs Post-Rune"),

    "Water C0 - Sapphire Rune Lock":                AdvData(110023, "Tidal Reef Post-Rune"),
    "Water B2 - Sapphire Rune Lock":                AdvData(108971, "Tidal Reef Post-Rune"),
    "Water A0 - Sapphire Rune Lock":                AdvData(111572, "Tidal Reef Post-Rune"),
    "Water A3 - Sapphire Rune Lock":                AdvData(114802, "Tidal Reef Post-Rune"),
    "Water D2 - N - Sapphire Rune Lock":            AdvData(109109, "Tidal Reef Post-Rune"),
    "Water D2 - S - Sapphire Rune Lock":            AdvData(109106, "Tidal Reef Post-Rune"),
    "Water D0 - Sapphire Rune Lock":                AdvData(110316, "Tidal Reef Post-Rune"),
    "Water C3 - E - Sapphire Rune Lock":            AdvData(108592, "Tidal Reef Post-Rune"),
    "Water C3 - W - Sapphire Rune Lock":            AdvData(108593, "Tidal Reef Post-Rune"),
    "Water B3 - Sapphire Rune Lock":                AdvData(110851, "Tidal Reef Post-Rune"),

    "Fire A1 - S - Ruby Rune Lock":                 AdvData(116434, "Raging Volcano Post-Rune"),
    "Fire A1 - E - Ruby Rune Lock":                 AdvData(116436, "Raging Volcano Post-Rune"),
    "Fire A2 - Ruby Rune Lock":                     AdvData(115237, "Raging Volcano Post-Rune"),
    "Fire A3 - Ruby Rune Lock":                     AdvData(116778, "Raging Volcano Post-Rune"),
    "Fire B2 - N - Ruby Rune Lock":                 AdvData(115374, "Raging Volcano Post-Rune"),
    "Fire B2 - S - Ruby Rune Lock":                 AdvData(115375, "Raging Volcano Post-Rune"),
    "Fire C0 - Ruby Rune Lock":                     AdvData(116200, "Raging Volcano Post-Rune"),
    "Fire C1 - Ruby Rune Lock":                     AdvData(115702, "Raging Volcano Post-Rune"),
    "Fire C3 - S - Ruby Rune Lock":                 AdvData(116304, "Raging Volcano Post-Rune"),
    "Fire C3 - W - Ruby Rune Lock":                 AdvData(116302, "Raging Volcano Post-Rune"),
    "Fire D1 - Ruby Rune Lock":                     AdvData(116005, "Raging Volcano Post-Rune"),
    "Fire E0 - Ruby Rune Lock":                     AdvData(118316, "Raging Volcano Post-Rune"),

    "Wind C3 - Diamond Rune Lock":                  AdvData(120636, "Frozen Spire Post-Rune"),
    "Wind D4 - Diamond Rune Lock":                  AdvData(122402, "Frozen Spire Post-Rune"),
    "Wind E3 - Diamond Rune Lock":                  AdvData(121758, "Frozen Spire Post-Rune"),
    "Wind E2 - W - Diamond Rune Lock":              AdvData(121659, "Frozen Spire Post-Rune"),
    "Wind E2 - E - Diamond Rune Lock":              AdvData(121666, "Frozen Spire Post-Rune"),
    "Wind E0 - Diamond Rune Lock":                  AdvData(120494, "Frozen Spire Post-Rune"),
    "Wind D1 - Diamond Rune Lock":                  AdvData(121454, "Frozen Spire Post-Rune"),
    "Wind C2 - Diamond Rune Lock":                  AdvData(121372, "Frozen Spire Post-Rune"),
    "Wind C1 - Diamond Rune Lock":                  AdvData(121260, "Frozen Spire Post-Rune"),
    "Wind B1 - Diamond Rune Lock":                  AdvData(120915, "Frozen Spire Post-Rune"),
    "Wind B3 - Diamond Rune Lock":                  AdvData(121098, "Frozen Spire Post-Rune"),
    "Wind A2 - Diamond Rune Lock":                  AdvData(120736, "Frozen Spire Post-Rune"),

    "Serpent A2 - Elemental Rune Lock":             AdvData(104819, "Serpent Stacks"),
    "Serpent A1 - N - Obsidian Rune Lock":          AdvData(125703, "Serpent Stacks Post-Rune"),
    "Serpent A1 - W - Obsidian Rune Lock":          AdvData(125701, "Serpent Stacks Post-Rune"),
    "Serpent A1 - E - Obsidian Rune Lock":          AdvData(125689, "Serpent Stacks Post-Rune"),
    "Serpent A3 - Obsidian Rune Lock":              AdvData(103366, "Serpent Stacks Post-Rune"),

    "Rolling A1 - Ancient Rune Lock":               AdvData(104495, "Rolling Rocks Post-Rune"),
    "Rolling B0 - Ancient Rune Lock":               AdvData(104912, "Rolling Rocks Post-Rune"),

    "Sunken A0 - Ancient Rune Lock":                AdvData(123006, "Sunken Island"),
    "Sunken B1 - Ancient Rune Lock":                AdvData(123252, "Sunken Island"),

    "Aggro B1 - Ancient Rune Lock":                 AdvData(122860, "Aggro Crag"),
    "Aggro A1 - Ancient Rune Lock":                 AdvData(122919, "Aggro Crag"),

    "Nunatak B0 - Ancient Rune Lock":               AdvData(123480, "Sea Nunatak"),

    "Locked A0 - Ancient Rune Lock":                AdvData(104284, "Locked"),

    "Tropic A1 - Ancient Rune Lock":                AdvData(104457, "Star Tropic"),
    "Tropic B0 - Ancient Rune Lock":                AdvData(104247, "Star Tropic"),
    "Tropic B0 - Obsidian Rune Lock":               AdvData(104246, "Star Tropic"),

    "Shoal A0 - Ancient Rune Lock":                 AdvData(104388, "Shoal"),

}

# 196 checks
snakesanity_table = {
    "Ancient B3 - Snakeblock":                      AdvData(100223, "Ancient Isle"),
    "Ancient B2 - W - Snakeblock":                  AdvData(101292, "Ancient Isle"),
    "Ancient B2 - E - Snakeblock":                  AdvData(101294, "Ancient Isle"),
    "Ancient A3 - Snakeblock":                      AdvData(100550, "Ancient Isle"),
    "Ancient A1 - Snakeblock":                      AdvData(101050, "Ancient Isle"),
    "Ancient C2 - E - Snakeblock":                  AdvData(100429, "Ancient Isle"),
    "Ancient C2 - S - Snakeblock":                  AdvData(100424, "Ancient Isle"),
    "Ancient C2 - W - Snakeblock":                  AdvData(100423, "Ancient Isle"),
    "Ancient C3 - Snakeblock":                      AdvData(101434, "Ancient Isle"),

    "Stone D2 - Snakeblock":                        AdvData(107090, "Stony Cliffs"),
    "Stone E1 - W - Snakeblock":                    AdvData(107760, "Stony Cliffs"),
    "Stone C1 - Snakeblock":                        AdvData(107480, "Stony Cliffs"), # topaz Quest
    "Stone D1 - Snakeblock":                        AdvData(107164, "Stony Cliffs"), # topaz Quest
    "Stone E1 - E - Snakeblock":                    AdvData(107759, "Stony Cliffs Post-Rune"), # t quest
    "Stone E0 - Snakeblock":                        AdvData(108233, "Stony Cliffs Post-Rune"),
    "Stone B1 - W - Snakeblock":                    AdvData(107048, "Stony Cliffs NW"),
    "Stone B0 - Snakeblock":                        AdvData(108013, "Stony Cliffs NW"),
    "Stone A2 - N - Snakeblock":                    AdvData(106853, "Stony Cliffs NW"),
    "Stone A2 - S - Snakeblock":                    AdvData(106852, "Stony Cliffs Post-Rune"),
    "Stone A3 - Snakeblock":                        AdvData(107422, "Stony Cliffs Post-Rune"),
    "Stone B3 - S - Snakeblock":                    AdvData(108107, "Stony Cliffs Post-Rune"),
    "Stone A4 - W - Snakeblock":                    AdvData(107712, "Stony Cliffs Post-Rune"),
    "Stone A0 - Snakeblock":                        AdvData(108155, "Stony Cliffs NW"),
    "Stone B1 - E - Snakeblock":                    AdvData(107050, "Stony Cliffs NW"),
    "Stone B4 - Snakeblock":                        AdvData(106956, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Stone A4 - E - Snakeblock":                    AdvData(107713, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Stone C4 - Snakeblock":                        AdvData(107256, "Stony Cliffs Post-Rune"), # t quest
    "Stone B3 - N - Snakeblock":                    AdvData(108108, "Stony Cliffs Post-Rune"),
    "Stone B2 - W - Snakeblock":                    AdvData(107366, "Stony Cliffs Post-Rune"),
    "Stone B2 - E - Snakeblock":                    AdvData(107367, "Stony Cliffs Post-Rune"),
    "Stone C2 - Snakeblock":                        AdvData(107591, "Stony Cliffs Post-Rune"),
    "Stone E4 - Snakeblock":                        AdvData(107810, "Stony Cliffs Post-Rune"),
    "Stone Dungeon C4 - Snakeblock":                AdvData(102913, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon C3 - Snakeblock":                AdvData(101712, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon B2 - E - Snakeblock":            AdvData(102663, "Stony Cliffs Post-Rune"),
    "Stone Dungeon B2 - W - Snakeblock":            AdvData(102664, "Stony Cliffs Post-Rune"),
    "Stone Dungeon B2 - N - Snakeblock":            AdvData(102667, "Stony Cliffs Post-Rune"),
    "Stone Dungeon B1 - Snakeblock":                AdvData(124810, "Stony Cliffs Post-Rune"),
    "Stone Dungeon D2 - E - Snakeblock":            AdvData(102291, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D2 - CE - Snakeblock":           AdvData(102286, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D2 - W - Snakeblock":            AdvData(102290, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D2 - CW - Snakeblock":           AdvData(102287, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D1 - W - Snakeblock":            AdvData(102862, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D1 - CS - Snakeblock":           AdvData(102860, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon D1 - CN - Snakeblock":           AdvData(102861, "Stony Cliffs"),
    "Stone Dungeon D1 - E - Snakeblock":            AdvData(102863, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon E1 - Snakeblock":                AdvData(125459, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon E2 - Snakeblock":                AdvData(102455, "Stony Cliffs Post-Rune"), # t quest
    "Stone Dungeon C1 - Snakeblock":                AdvData(101827, "Stony Cliffs NW"), # t quest, #g gloves

    "Rolling B0 - Snakeblock":                      AdvData(104885, "Rolling Rocks Post-Rune"),

    "Aggro B1 - E - Snakeblock":                    AdvData(122861, "Aggro Crag"), # 35 stars
    "Aggro B1 - W - Snakeblock":                    AdvData(122832, "Aggro Crag"), # 35 stars, R quest,A rune
    "Aggro B0 - E - Snakeblock":                    AdvData(122673, "Aggro Crag"),
    "Aggro B0 - W - Snakeblock":                    AdvData(122672, "Aggro Crag"), # 35 stars, R quest, A rune, s shirt

    "Locked A0 - E - Snakeblock":                   AdvData(104287, "Locked"),
    "Locked A0 - C - Snakeblock":                   AdvData(104301, "Locked"),
    "Locked A0 - W - Snakeblock":                   AdvData(104292, "Locked"),

    "Nunatak A1 - Snakeblock":                      AdvData(123363, "Sea Nunatak"), # a rune, d quest?

    "Shoal A0 - Snakeblock":                        AdvData(104391, "Shoal"), # a rune, k cloak

    "Lost B1 - Snakeblock":                         AdvData(128960, "Lost Landing"), # 30 Stars, p flute

    "Tropic A0 - W - Snakeblock":                   AdvData(103230, "Star Tropic"), # k cloak
    "Tropic A0 - C - Snakeblock":                   AdvData(103234, "Star Tropic"), # k cloak
    "Tropic A0 - E - Snakeblock":                   AdvData(103236, "Star Tropic"), # k cloak
    "Tropic B0 - N - Snakeblock":                   AdvData(104249, "Star Tropic"), # k cloak
    "Tropic B0 - S - Snakeblock":                   AdvData(104245, "Star Tropic"), # k cloak

    "Overworld - Sapphire Sea - Damsnake":          AdvData(108520, "Sapphire Sea"),
    "Overworld - Beast Sea - Damsnake":             AdvData(108493, "Beast Sea"),
    "Overworld - Lost Sea - Damsnake":              AdvData(108515, "Lost Sea"),
    "Overworld - Northeast Sea - Damsnake":         AdvData(108513, "Northeast Sea"),

    "Water C2 - W - Snakeblock":                    AdvData(108781, "Tidal Reef"),
    "Water C2 - SE - Snakeblock":                   AdvData(108786, "Tidal Reef"),
    "Water D2 - W - Snakeblock":                    AdvData(109099, "Tidal Reef"),
    "Water C1 - E - Snakeblock":                    AdvData(109448, "Tidal Reef"),
    "Water C1 - CE - Snakeblock":                   AdvData(109443, "Tidal Reef"),
    "Water C2 - NE - Snakeblock":                   AdvData(108780, "Tidal Reef"),
    "Water C2 - CE - Snakeblock":                   AdvData(108778, "Tidal Reef"),
    "Water B1 - SE - Snakeblock":                   AdvData(109697, "Tidal Reef"),
    "Water B1 - C - Snakeblock":                    AdvData(109695, "Tidal Reef"),
    "Water C1 - W - Snakeblock":                    AdvData(109441, "Tidal Reef"),
    "Water C1 - CW - Snakeblock":                   AdvData(109442, "Tidal Reef"),
    "Water B0 - E - Snakeblock":                    AdvData(113766, "Tidal Reef"), # s quest
    "Water B0 - C - Snakeblock":                    AdvData(113757, "Tidal Reef"), # s quest, f flippers
    "Water B2 - NE - Snakeblock":                   AdvData(108963, "Tidal Reef"), # s quest,
    "Water B2 - C - Snakeblock":                    AdvData(108968, "Tidal Reef"), # s quest,
    "Water B3 - Snakeblock":                        AdvData(110853, "Tidal Reef"),
    "Water D0 - W - Snakeblock":                    AdvData(110313, "Tidal Reef"),
    "Water D0 - E - Snakeblock":                    AdvData(110315, "Tidal Reef Post-Rune"),
    "Water D1 - Snakeblock":                        AdvData(109881, "Tidal Reef Post-Rune"),
    "Water D2 - C - Snakeblock":                    AdvData(109096, "Tidal Reef Post-Rune"), # f flippers
    "Water D2 - E - Snakeblock":                    AdvData(109107, "Tidal Reef Post-Rune"), # f flippers
    "Water E1 - W - Snakeblock":                    AdvData(113541, "Tidal Reef Post-Rune"), # f flippers
    "Water E1 - E - Snakeblock":                    AdvData(113544, "Tidal Reef Post-Rune"), # f flippers
    "Water E2 - E - Snakeblock":                    AdvData(113307, "Tidal Reef Post-Rune"), # f flippers
    "Water E2 - W - Snakeblock":                    AdvData(113308, "Tidal Reef Post-Rune"),
    "Water E3 - Snakeblock":                        AdvData(114089, "Tidal Reef Post-Rune"),
    "Water D3 - Snakeblock":                        AdvData(113121, "Tidal Reef Post-Rune"),
    "Water A0 - W - Snakeblock":                    AdvData(111573, "Tidal Reef Post-Rune"),
    "Water A0 - S - Snakeblock":                    AdvData(111571, "Tidal Reef Post-Rune"), # f flippers
    "Water A2 - Snakeblock":                        AdvData(112437, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Water A3 - Snakeblock":                        AdvData(114801, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Water B4 - Snakeblock":                        AdvData(126139, "Tidal Reef S"),
    "Water B0 - Snakeblock":                        AdvData(113765, "Tidal Reef Post-Rune"),

    "Fire B2 - W - Snakeblock":                     AdvData(115367, "Raging Volcano"),
    "Fire B2 - CW - Snakeblock":                    AdvData(115362, "Raging Volcano"),
    "Fire B2 - CE - Snakeblock":                    AdvData(115366, "Raging Volcano"),
    "Fire B2 - E - Snakeblock":                     AdvData(115356, "Raging Volcano"),
    "Fire B2 - SW - Snakeblock":                    AdvData(115370, "Raging Volcano Post-Rune"),
    "Fire C2 - W - Snakeblock":                     AdvData(115500, "Raging Volcano"),
    "Fire C2 - NE - Snakeblock":                    AdvData(115511, "Raging Volcano"),
    "Fire C2 - E - Snakeblock":                     AdvData(115501, "Raging Volcano"),
    "Fire D2 - W - Snakeblock":                     AdvData(115802, "Raging Volcano"),
    "Fire D2 - C - Snakeblock":                     AdvData(115810, "Raging Volcano"),
    "Fire D2 - NE - Snakeblock":                    AdvData(115800, "Raging Volcano"),
    "Fire D2 - SE - Snakeblock":                    AdvData(115803, "Raging Volcano Post-Rune"),
    "Fire D1 - SW - Snakeblock":                    AdvData(115988, "Raging Volcano"),
    "Fire D1 - W - Snakeblock":                     AdvData(115991, "Raging Volcano"),
    "Fire D1 - C - Snakeblock":                     AdvData(115993, "Raging Volcano Post-Rune"),
    "Fire D1 - NE - Snakeblock":                    AdvData(116001, "Raging Volcano Post-Rune"),
    "Fire D1 - SE - Snakeblock":                    AdvData(116000, "Raging Volcano Post-Rune"), # S shirt
    "Fire C1 - Snakeblock":                         AdvData(115683, "Raging Volcano"),
    "Fire B1 - Snakeblock":                         AdvData(116901, "Raging Volcano"), # s shirt
    "Fire B0 - Snakeblock":                         AdvData(119347, "Raging Volcano Post-Rune"),
    "Fire A1 - E - Snakeblock":                     AdvData(116435, "Raging Volcano Post-Rune"),
    "Fire A1 - NE - Snakeblock":                    AdvData(116438, "Raging Volcano Post-Rune"),
    "Fire A0 - E - Snakeblock":                     AdvData(116597, "Raging Volcano Post-Rune"),
    "Fire A0 - W - Snakeblock":                     AdvData(116603, "Raging Volcano Post-Rune"),
    "Fire A3 - E - Snakeblock":                     AdvData(116771, "Raging Volcano Post-Rune"),
    "Fire A3 - SE - Snakeblock":                    AdvData(116773, "Raging Volcano Post-Rune"),
    "Fire A3 - S - Snakeblock":                     AdvData(116774, "Raging Volcano Post-Rune"),
    "Fire A3 - W - Snakeblock":                     AdvData(116776, "Raging Volcano Post-Rune"),
    "Fire A4 - Snakeblock":                         AdvData(117784, "Raging Volcano Post-Rune"),
    "Fire B4 - W - Snakeblock":                     AdvData(118465, "Raging Volcano Post-Rune"), # r quest
    "Fire B4 - E - Snakeblock":                     AdvData(118455, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - CW - Snakeblock":                    AdvData(118773, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - W - Snakeblock":                     AdvData(118783, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - CE - Snakeblock":                    AdvData(118784, "Raging Volcano Post-Rune"), # r quest
    "Fire B3 - E - Snakeblock":                     AdvData(118780, "Raging Volcano Post-Rune"),
    "Fire C3 - E - Snakeblock":                     AdvData(116307, "Raging Volcano Post-Rune"), # r quest
    "Fire C3 - W - Snakeblock":                     AdvData(116301, "Raging Volcano Post-Rune"),
    "Fire C4 - NE - Snakeblock":                    AdvData(118129, "Raging Volcano Post-Rune"),
    "Fire C4 - SE - Snakeblock":                    AdvData(118122, "Raging Volcano Post-Rune"),
    "Fire D4 - W - Snakeblock":                     AdvData(118017, "Raging Volcano Post-Rune"),
    "Fire D4 - E - Snakeblock":                     AdvData(118018, "Raging Volcano Post-Rune"),# s shirt
    "Fire E4 - E - Snakeblock":                     AdvData(117925, "Raging Volcano Post-Rune"),
    "Fire E4 - CE - Snakeblock":                    AdvData(117917, "Raging Volcano Post-Rune"), # s shirt
    "Fire E4 - W - Snakeblock":                     AdvData(117924, "Raging Volcano Post-Rune"), # s shirt
    "Fire D3 - W - Snakeblock":                     AdvData(118990, "Raging Volcano Post-Rune"), # s shirt
    "Fire D3 - E - Snakeblock":                     AdvData(119003, "Raging Volcano Post-Rune"), # s shirt, r quest
    "Fire D3 - SW - Snakeblock":                    AdvData(119001, "Raging Volcano Post-Rune"), # s shirt, r quest

    "Wind C4 - E - Snakeblock":                     AdvData(120164, "Frozen Spire"),
    "Wind C4 - C - Snakeblock":                     AdvData(120167, "Frozen Spire"),
    "Wind C4 - N - Snakeblock":                     AdvData(120156, "Frozen Spire"),
    "Wind D4 - Snakeblock":                         AdvData(122398, "Frozen Spire"),
    "Wind B3 - SW - Snakeblock":                    AdvData(121094, "Frozen Spire"),
    "Wind B3 - CE - Snakeblock":                    AdvData(121105, "Frozen Spire"), # k cloak
    "Wind B3 - NE - Snakeblock":                    AdvData(121103, "Frozen Spire"), # k cloak
    "Wind A3 - Snakeblock":                         AdvData(120826, "Frozen Spire"), # D quest
    "Wind A2 - SW - Snakeblock":                    AdvData(120730, "Frozen Spire"),
    "Wind A2 - SE - Snakeblock":                    AdvData(120735, "Frozen Spire"), # D quest
    "Wind B2 - E - Snakeblock":                     AdvData(120993, "Frozen Spire"),
    "Wind B2 - SW - Snakeblock":                    AdvData(121002, "Frozen Spire"), # k cloak
    "Wind B4 - Snakeblock":                         AdvData(121162, "Frozen Spire"), # k cloak
    "Wind B1 - Snakeblock":                         AdvData(120911, "Frozen Spire"),
    "Wind D2 - SE - Snakeblock":                    AdvData(121524, "Frozen Spire"),
    "Wind D2 - SW - Snakeblock":                    AdvData(121527, "Frozen Spire"),
    "Wind B0 - W - Snakeblock":                     AdvData(120364, "Frozen Spire"),
    "Wind B0 - E - Snakeblock":                     AdvData(120362, "Frozen Spire"),
    "Wind C0 - Snakeblock":                         AdvData(120406, "Frozen Spire"),
    "Wind E4 - Snakeblock":                         AdvData(120276, "Frozen Spire Post-Rune"), # d quest
    "Wind E3 - Snakeblock":                         AdvData(121756, "Frozen Spire Post-Rune"), # d quest
    "Wind E1 - Snakeblock":                         AdvData(121559, "Frozen Spire Post-Rune"), # g gloves
    "Wind C1 - Snakeblock":                         AdvData(121259, "Frozen Spire"),
    "Wind C2 - Snakeblock":                         AdvData(121370, "Frozen Spire"), # d quest

    "Serpent A1 - W - Snakeblock":                  AdvData(125712, "Serpent Stacks Post-Rune"),
    "Serpent A1 - C - Snakeblock":                  AdvData(125704, "Serpent Stacks Post-Rune"), #o quest
    "Serpent A1 - CE - Snakeblock":                 AdvData(125690, "Serpent Stacks Post-Rune"), #o quest
    "Serpent A1 - E - Snakeblock":                  AdvData(125711, "Serpent Stacks Post-Rune"), #o quest
    "Serpent A6 - SW - Snakeblock":                 AdvData(126815, "Serpent Stacks Post-Rune"), #o quest, S quest, T quest
    "Serpent A6 - NW - Snakeblock":                 AdvData(126807, "Serpent Stacks Post-Rune"), #o quest, S quest, T quest
    "Serpent A6 - C - Snakeblock":                  AdvData(126804, "Serpent Stacks Post-Rune"), #o quest, S quest, T quest
    "Serpent A6 - E - Snakeblock":                  AdvData(126805, "Serpent Stacks Post-Rune"), #o quest, S quest, T quest
    "Serpent A8 - Snakeblock":                      AdvData(127076, "Serpent Stacks Post-Rune"), #o quest, all quests

    "Sanctum A2 - S - Snakeblock":                  AdvData(123858, "Sanctum"), #all quests
    "Sanctum A2 - C - Snakeblock":                  AdvData(123857, "Sanctum"), #all quests
    "Sanctum A2 - W - Snakeblock":                  AdvData(123856, "Sanctum"), #all quests
    "Sanctum A0 - E - Snakeblock":                  AdvData(124109, "Sanctum"), #all quests
    "Sanctum A0 - CE - Snakeblock":                 AdvData(124108, "Sanctum"), #all quests
    "Sanctum A0 - CW - Snakeblock":                 AdvData(124121, "Sanctum"), #all quests
    "Sanctum A0 - W - Snakeblock":                  AdvData(124111, "Sanctum"), #all quests
    "Sanctum C2 - E - Snakeblock":                  AdvData(124026, "Sanctum"), #all quests
    "Sanctum C2 - W - Snakeblock":                  AdvData(124023, "Sanctum"), #all quests
    "Sanctum C0 - W - Snakeblock":                  AdvData(124238, "Sanctum"), #all quests
    "Sanctum C0 - CSW - Snakeblock":                AdvData(124231, "Sanctum"), #all quests
    "Sanctum C0 - CNW - Snakeblock":                AdvData(124241, "Sanctum"), #all quests
    "Sanctum C0 - CN - Snakeblock":                 AdvData(124251, "Sanctum"), #all quests
    "Sanctum C0 - E - Snakeblock":                  AdvData(124250, "Sanctum"), #all quests
}

exclusion_table = {



}

events_table = {
}
