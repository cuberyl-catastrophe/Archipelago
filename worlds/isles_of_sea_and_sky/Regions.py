# (Region name, list of exits)

isles_of_sea_and_sky_regions: list[tuple[str, list[str]]] = [
    ("Menu",                            ["New Game"]),

    # - - - - - - - - - -
    # Overworld
    # - - - - - - - - - -
    ("Topaz Sea", [
        "Topaz Sea - Exit to Ruby Sea",
        "Topaz Sea - Exit to Eastern Sea",
        "Ancient Isle - East Entrance",
        "Stony Cliffs - East Turtle Entrance",
        "Rolling Rocks - West Turtle Entrance",
        "Rolling Rocks - East Turtle Entrance"
    ]),
    ("Sapphire Sea", [
        "Sapphire Sea - Exit to Obsidian Sea",
        "Stony Cliffs - West Turtle Entrance",
        "Tidal Reef - Turtle Entrance",
        "Aggro Crag - Turtle Entrance"
    ]),
    ("Obsidian Sea", [
        "Obsidian Sea - Whirlpool Exit",
        "Ancient Isle - West Turtle Entrance",
        "Serpent Stacks - Turtle Entrance",
        "Locked Key - Turtle Entrance"
    ]),
    ("Ruby Sea", [
        "Ruby Sea - Whirlpool Exit",
        "Raging Volcano - Turtle Entrance",
        "Sunken Island - Turtle Entrance",
        "Star Tropic - East Turtle Entrance"
    ]),
    ("Eastern Sea", [
        "Eastern Sea - Exit to Diamond Sea",
        "Eastern Sea - Whirlpool Exit",
        "Sea Nunatak - Turtle Entrance",
        "Eastern Shoal - Turtle Entrance"
    ]),
    ("Diamond Sea", [
        "Diamond Sea - Exit to Eastern Sea",
        "Frozen Spire - Turtle Entrance"
    ]),
    ("Beast Sea", [
        "Beast Sea - Exit to Eastern Sea",
        "Beast Ridge - Turtle Entrance"
    ]),
    ("Lost Sea", [
        "Lost Sea - Exit to Obsidian Sea",
        "Lost Sea - Whirlpool Exit",
        "Lost Landing - Turtle Entrance",
        "Star Tropic - West Turtle Entrance"
    ]),
    ("Forgotten Sea", [
        "Forgotten Sea - Exit to Diamond Sea",
        "Forgotten Sea - Whirlpool Exit"
    ]),

    # - - - - - - - - - -
    # Ancient Isle
    # - - - - - - - - - -
    ("Ancient Isle - Origin", [ # Currently one region to make sphere 1 larger. In the future it may get split into multiple regions
        "Ancient Isle - East Turtle Exit",
        "Ancient Isle - North Exit",
        "Phoenix Hub - Phoenix Anywhere Entrance"
    ]),
    ("Ancient Isle - West", [
        "Ancient Isle - West to Origin",
        "Ancient Isle - West Turtle Exit"
    ]),

    # - - - - - - - - - -
    # Stony Cliffs
    # - - - - - - - - - -
    ("Stony Cliffs - God Altar", [
        "Stony Cliffs - East Turtle Exit", 
        "Stony Cliffs - God Altar to North-East", 
        "Stony Cliffs - God Altar to South-East", 
        "Stony Cliffs - God Altar to South Coast", 
        "Stony Cliffs - God Altar to Phoenix",
        "Stony Cliffs - God Altar Music Cavern Entrance",
        "Stony Cliffs - God Altar East Cavern Entrance"
    ]),
    ("Stony Cliffs - North-East", [
        "Stony Cliffs - North-East to God Altar", 
        "Stony Cliffs - North-East Cavern Entrance"
    ]),
    ("Stony Cliffs - South-East", [
        "Stony Cliffs - South-East to God Altar", 
        "Stony Cliffs - South-East to Golden Stone", 
        "Stony Cliffs - South-East Cavern Entrance"
    ]),
    ("Stony Cliffs - South Coast", [
        "Stony Cliffs - South Coast to God Altar", 
        "Stony Cliffs - South Coast to South-East", 
        "Stony Cliffs - South Coast to South Star Stone", 
        "Stony Cliffs - South Coast South Cavern Entrance",
        "Stony Cliffs - South Coast Center Cavern Entrance"
    ]),
    ("Stony Cliffs - Phoenix", [
        "Stony Cliffs - Phoenix to God Altar", 
        "Stony Cliffs - Phoenix to North-West", 
        "Stony Cliffs - Phoenix to West Star Stone", 
        "Stony Cliffs - Phoenix Exit"
    ]),
    ("Stony Cliffs - North-West", [
        "Stony Cliffs - North-West Cavern Entrance"
    ]),
    ("Stony Cliffs - Tablet Slot", [
        "Stony Cliffs - Tablet Slot to South-West", 
        "Stony Cliffs - Tablet Slot to South Coast", 
        "Stony Cliffs - Tablet Slot Cavern Entrance"
    ]),
    ("Stony Cliffs - South-West", [
        "Stony Cliffs - South-West Cavern Entrance"
    ]),
    ("Stony Cliffs - West Star Stone", [
        "Stony Cliffs - West Star Stone to Phoenix", 
        "Stony Cliffs - West Turtle Exit" 
    ]),
    ("Stony Cliffs - South Star Stone", [
        "Stony Cliffs - South Star Stone to South-West", 
        "Stony Cliffs - South Star Stone to South Coast" 
    ]),
    ("Stony Cliffs - Golden Stone", [
        "Stony Cliffs - Golden Stone to South-East", 
        "Stony Cliffs - Golden Stone to Windy Cliff" 
    ]),
    ("Stony Cliffs - Windy Cliff", [
        "Stony Cliffs - Windy Cliff to Golden Stone", 
        "Stony Cliffs - Windy Cliff to South Coast" 
    ]),
    ("Stone Dungeon - North Tunnels", [
        "Stone Dungeon - North Tunnels to Dirt Chamber", 
        "Stone Dungeon - North Tunnels to Gopher Vault", 
        "Stone Dungeon - North Tunnels North-West Cavern Exit",
        "Stone Dungeon - North Tunnels Phoenix Cavern Exit" 
    ]),
    ("Stone Dungeon - South Tunnels", [
        "Stone Dungeon - South Tunnels to Vault Door", 
        "Stone Dungeon - South Tunnels South-West Cavern Exit",
        "Stone Dungeon - South Tunnels South Cavern Exit",
        "Stone Dungeon - South Tunnels South-East Cavern Exit"
    ]),
    ("Stone Dungeon - West Tunnels", [
        "Stone Dungeon - West Tunnels to Dirt Chamber",
        "Stone Dungeon - West Tunnels Tablet Slot Cavern Exit",
        "Stone Dungeon - West Tunnels Center Cavern Exit"
    ]),
    ("Stone Dungeon - Vault Door", [
        "Stone Dungeon - Vault Door to Gopher Vault",
        "Stone Dungeon - Vault Door to West Tunnels",
        "Stone Dungeon - Vault Door to North Tunnels",
        "Stone Dungeon - Vault Door to Earth Chamber",
        "Stone Dungeon - Vault Door to East Tunnels" 
    ]),
    ("Stone Dungeon - Gopher Vault", [
        "Stone Dungeon - Gopher Vault to Vault Door",
        "Stone Dungeon - Gopher Vault to North Tunnels"
    ]),
    ("Stone Dungeon - Dirt Chamber", [
        "Stone Dungeon - Dirt Chamber to North Tunnels" 
    ]),
    ("Stone Dungeon - Below Xylophone",  [
        "Stone Dungeon - Below Xylophone Cavern Exit"
    ]),
    ("Stone Dungeon Earth Chamber",         [
        "Stone Dungeon - Earth Chamber to East Tunnels", 
        "Stone Dungeon - Earth Chamber East Cavern Exit"
    ]),
    ("Stone Dungeon - East Tunnels",      []),

    # - - - - - - - - - -
    # Tidal Reef
    # - - - - - - - - - -
    ("Tidal Reef - God Altar", [
        "Tidal Reef - God Altar to Shell Puzzle",
        "Tidal Reef - God Altar to East",
        "Tidal Reef - God Altar to Phoenix",
        "Tidal Reef - God Altar to South-West",
        "Tidal Reef - God Altar to North-West Low Tide",
        "Tidal Reef - God Altar to West Star Stone",
        "Tidal Reef - God Altar to North-West",
        "Tidal Reef - Turtle Exit" 
    ]),
    ("Tidal Reef - Shell Puzzle", [
        "Tidal Reef - Shell Puzzle to God Altar", 
        "Tidal Reef - Shell Puzzle to East" 
    ]),
    ("Tidal Reef - East", [
        "Tidal Reef - East to Shell Puzzle",
        "Tidal Reef - East to God Altar"
    ]),
    ("Tidal Reef - Phoenix", [
        "Tidal Reef - Phoenix to God Altar",
        "Tidal Reef - Phoenix to South-West",
        "Tidal Reef - Phoenix Exit"
    ]),
    ("Tidal Reef - South-West", [
        "Tidal Reef - South-West to God Altar", 
        "Tidal Reef - South-West to Phoenix" 
    ]),
    ("Tidal Reef - West Star Stone", [
        "Tidal Reef - West Star Stone to God Altar", 
        "Tidal Reef - West Star Stone to South-West" 
    ]),
    ("Tidal Reef - North-West", [
        "Tidal Reef - North-West to God Altar", 
        "Tidal Reef - North-West to North-West Low Tide" 
    ]),
    ("Tidal Reef - North-West Low Tide", [
        "Tidal Reef - North-West Low Tide to God Altar" 
    ]),
    
    # - - - - - - - - - -
    # Raging Volcano
    # - - - - - - - - - -
    ("Raging Volcano - God Altar", [
        "Raging Volcano - God Altar to Phoenix", # Ruby Rune Stone
        "Raging Volcano - God Altar to South Coast", # Ruby Rune Stone
        "Raging Volcano - God Altar to Triple Ruby Pit", # Ruby Rune Stone
        "Raging Volcano - God Altar to Lyre", # Ruby Rune Stone
        "Raging Volcano - God Altar to Above Volcano", # Ruby Rune Stone
        "Raging Volcano - God Altar to Below Hot Spring", # Salamander Shirt
        "Raging Volcano - God Altar to North-West", # Ruby Rune Stone
        "Raging Volcano - God Altar to North-West Pass", # Ruby Rune Stone | Salamander Shirt
        "Raging Volcano - God Altar to Key Triplets", # Ruby Rune Stone
        "Raging Volcano - Turtle Exit"
    ]),
    ("Raging Volcano - Phoenix", [
        "Raging Volcano - Phoenix to God Altar", # Fire Elementals
        "Raging Volcano - Phoenix to Hot Spring", # Ruby Rune Stone
        "Raging Volcano - Phoenix Exit"
    ]),
    ("Raging Volcano - Hot Spring", [
        "Raging Volcano - Hot Spring to God Altar", # Salamander Shirt
        "Raging Volcano - Hot Spring to Phoenix" # Salamander Shirt
    ]),
    ("Raging Volcano - South Coast", [
        "Raging Volcano - South Coast to God Altar", # Ruby Rune Stone
        "Raging Volcano - South Coast to Triple Ruby Pit"
    ]),
    ("Raging Volcano - Triple Ruby Pit", [
        "Raging Volcano - Triple Ruby Pit to God Altar" # Ruby Rune Stone
    ]),
    ("Raging Volcano - Lyre", [
        "Raging Volcano - Lyre to God Altar",
        "Raging Volcano - Lyre to Triple Ruby Pit"
    ]),
    ("Raging Volcano - Above Volcano", [
        "Raging Volcano - Above Volcano to God Altar", # Ruby Rune Stone
        "Raging Volcano - Above Volcano to South Coast",
        "Raging Volcano - Above Volcano to Lyre",
        "Raging Volcano - Above Volcano to Idol Room West"
    ]),
    ("Raging Volcano - Idol Room West", [
        "Raging Volcano - Idol Room West to South Coast",
        "Raging Volcano - Idol Room West to Below Hot Spring"
    ]),
    ("Raging Volcano - Below Hot Spring", [
        "Raging Volcano - Below Hot Spring to God Altar",
        "Raging Volcano - Below Hot Spring to South Coast",
        "Raging Volcano - Below Hot Spring to Idol Room West" # Fire Elementals
    ]),
    ("Raging Volcano - North-West", [
        "Raging Volcano - North-West to God Altar" # Ruby Rune Stone
    ]),
    ("Raging Volcano - North-West Pass", [
        "Raging Volcano - North-West Pass to God Altar", # Ruby Rune Stone
        "Raging Volcano - North-West Pass to North-East",
        "Raging Volcano - North-West Pass to Geyser Pass" # Salamander Shirt
    ]),
    ("Raging Volcano - Key Triplets", [
        "Raging Volcano - Key Triplets to God Altar", # Ruby Rune Stone
        "Raging Volcano - Key Triplets to Geyser Pass" # Ruby Rune Stone
    ]),
    ("Raging Volcano - Geyser Pass", [
        "Raging Volcano - Geyser Pass to North-West",    
        "Raging Volcano - Geyser Pass to North-West Pass", # Salamander Shirt
        "Raging Volcano - Geyser Pass to Key Triplets" # Ruby Rune Stone
    ]),
    
    # - - - - - - - - - -
    # Frozen Spire
    # - - - - - - - - - -
    # TODO: Albatross logic and regioning
    ("Frozen Spire", [
        "Frozen Spire - Turtle Exit",
        "Frozen Spire - Spire to Post-Rune"
    ]),
    ("Frozen Spire - Post-Rune", [
        "Frozen Spire - Post-Rune to Spire",
        "Frozen Spire - Phoenix Exit"
    ]),
        
    # - - - - - - - - - -
    # Serpent Stacks
    # - - - - - - - - - -
    #TODO: Redo regioning to fit with the repository's new regioning standards
    ("Serpent Stacks - Head", []), 
    ("Serpent Stacks - Entrance", [
        "Serpent Stacks - Entrance to Post-Rune",
        "Serpent Stacks - Entrance to Head",
        "Serpent Stacks - Exit"
    ]),
    ("Serpent Stacks - Post-Rune", [
        "Serpent Stacks - Post-Rune to Core"
    ]), 
    ("Serpent Stacks - Core", [
        "Serpent Stacks - Core to Tail"
    ]),
    ("Serpent Stacks - Tail", []),

    # - - - - - - - - - -
    # Sanctum
    # - - - - - - - - - -
    ("Sanctum", [
        "Sanctum - Turtle Exit",
        "Sanctum - Elemental Rock Path"
    ]),
    ("Sanctum - Peak", []),
    
    # - - - - - - - - - -
    # Rolling Rocks
    # - - - - - - - - - -
    ("Rolling Rocks - West", [
        "Rolling Rocks - West to South-East", # Ancient Rune Stone
        "Rolling Rocks - West Turtle Exit"
    ]),
    ("Rolling Rocks - South-East", [
        "Rolling Rocks - South-East to West" # Ancient Rune Stone
    ]),
    ("Rolling Rocks - North-East", [
        "Rolling Rocks - North-East to South-East", # Ancient Rune Stone
        "Rolling Rocks - East Turtle Exit"
    ]),


    # - - - - - - - - - -
    # Sunken Island
    # - - - - - - - - - -
    ("Sunken Island - Turtle", [
        "Sunken Island - Turtle Exit"
    ]),

    # - - - - - - - - - -
    # Aggro Crag
    # - - - - - - - - - -
    ("Aggro Crag - East", [
            "Aggro Crag - East to South-West", # Star Pieces, Ancient Rune, Fire Elementals
            "Aggro Crag - Turtle Exit"
    ]),
    ("Aggro Crag - South-West", [
        "Aggro Crag - South-West to East", # Ancient Rune Stone
        "Aggro Crag - South-West to North-West"  # Salamander Shirt
    ]),
        ("Aggro Crag - North-West", [
        "Aggro Crag - North-West to South-West", # Salamander Shirt
        "Aggro Crag - North-West to East"
    ]),

    # - - - - - - - - - -
    # Sea Nunatak
    # - - - - - - - - - -
    ("Sea Nunatak - Turtle", [
        "Sea Nunatak - Turtle Exit"
    ]),

    # - - - - - - - - - -
    # Locked Key
    # - - - - - - - - - -
    ("Locked Key - Turtle", [
        "Locked Key - Turtle Exit"
    ]),

    # - - - - - - - - - -
    # Star Tropic
    # - - - - - - - - - -
    ("Star Tropic - West", [
        "Star Tropic - West to Star Pocket",
        "Star Tropic - West to Treasure Shore",  # Ancient Rune Stone
        "Star Tropic - West Turtle Exit"
    ]),
    ("Star Tropic - East", [
        "Star Tropic - North-East to Star Pocket", # Ancient Rune Stone
        "Star Tropic - East Turtle Exit"
    ]),
    ("Star Tropic - Star Pocket", [
        "Star Tropic - Star Pocket to East" # Ancient Rune Stone
    ]),
    ("Star Tropic - Treasure Shore", [
        "Star Tropic - Treasure Shore to West" # Ancient Rune Stone
    ]),

    # - - - - - - - - - -
    # Eastern Shoal
    # - - - - - - - - - -
    ("Eastern Shoal - Turtle", [
        "Eastern Shoal - Turtle to North-West", # Ancient Rune Stone
        "Eastern Shoal - Turtle Exit"
    ]),

    ("Eastern Shoal - North-West", [
        "Eastern Shoal - North-West to Turtle", # Ancient Rune Stone
    ]),

    # - - - - - - - - - -
    # Lost Landing
    # - - - - - - - - - -
    ("Lost Landing - Turtle", [
        "Lost Landing - Turtle to West", # Frog Flippers
        "Lost Landing - Turtle Exit"
    ]),
    ("Lost Landing - West", [
        "Lost Landing - West to Turtle" # Frog Flippers
    ]),
    ("Lost Landing - Staircase", [
        "Lost Landing - Staircase to Phoenix", # 30 star pieces
        "Lost Landing - Staircase to Turtle"
    ]),
    ("Lost Landing - Phoenix", [
        "Lost Landing - Phoenix to Staircase", # 30 star pieces
        "Lost Landing - Phoenix Exit"
    ]),

    # - - - - - - - - - -
    # Beast Ridge
    # - - - - - - - - - -
    ("Beast Ridge - Bellstone", [
        "Beast Ridge - Bellstone to Phoenix",
        "Beast Ridge - Turtle Exit"
    ]),
    ("Beast Ridge - Phoenix", [
        "Beast Ridge - Phoenix to Bellstone",
        "Beast Ridge - Phoenix Exit"
    ]),

    # - - - - - - - - - -
    # Phoenix Hub
    # - - - - - - - - - -
    ("Phoenix Hub", [
        "Lost Landing - Phoenix Entrance",
        "Stony Cliffs - Phoenix Entrance",
        "Tidal Reef - Phoenix Entrance",
        "Raging Volcano - Phoenix Entrance",
        "Frozen Spire - Phoenix Entrance",
        "Beast Ridge - Phoenix Entrance"
    ]),
]
# (Entrance, region pointed to)
mandatory_connections: list[tuple[str, str]] = [
    ("New Game",                                            "Ancient Isle - Origin"),
    
    # - - - - - - - - - -
    # Overworld
    # - - - - - - - - - -
    ("Topaz Sea - Exit to Eastern Sea",                     "Eastern Sea"),
    ("Diamond Sea - Exit to Eastern Sea",                   "Eastern Sea"),
    ("Eastern Sea - Whirlpool Exit",                        "Obsidian Sea"),
    ("Topaz Sea - Exit to Ruby Sea",                        "Ruby Sea"),
    ("Sapphire Sea - Exit to Obsidian Sea",                 "Obsidian Sea"),
    ("Obsidian Sea - Whirlpool Exit",                       "Eastern Sea"),
    ("Ruby Sea - Whirlpool Exit",                           "Beast Sea"),
    ("Eastern Sea - Exit to Diamond Sea",                   "Diamond Sea"),
    ("Forgotten Sea - Exit to Diamond Sea",                 "Diamond Sea"),
    ("Beast Sea - Exit to Eastern Sea",                     "Eastern Sea"),
    ("Lost Sea - Exit to Obsidian Sea",                     "Obsidian Sea"),
    ("Lost Sea - Whirlpool Exit",                           "Forgotten Sea"),
    ("Forgotten Sea - Whirlpool Exit",                      "Lost Sea"),

    # Area Entrances
    ("Ancient Isle - East Entrance",                        "Ancient Isle - Origin"),
    ("Ancient Isle - West Turtle Entrance",                 "Ancient Isle - West"),
    ("Stony Cliffs - East Turtle Entrance",                 "Stony Cliffs - God Altar"),
    ("Stony Cliffs - West Turtle Entrance",                 "Stony Cliffs - West Star Stone"),
    ("Tidal Reef - Turtle Entrance",                        "Tidal Reef - God Altar"),
    ("Raging Volcano - Turtle Entrance",                    "Raging Volcano - God Altar"),
    ("Frozen Spire - Turtle Entrance",                      "Frozen Spire"),
    ("Serpent Stacks - Turtle Entrance",                    "Serpent Stacks - Entrance"),
    ("Rolling Rocks - East Turtle Entrance",                "Rolling Rocks - North-East"),
    ("Rolling Rocks - West Turtle Entrance",                "Rolling Rocks - West"),
    ("Sunken Island - Turtle Entrance",                     "Sunken Island - Turtle"),
    ("Aggro Crag - Turtle Entrance",                        "Aggro Crag - East"),
    ("Sea Nunatak - Turtle Entrance",                       "Sea Nunatak - Turtle"),
    ("Locked Key - Turtle Entrance",                        "Locked Key - Turtle"),
    ("Star Tropic - West Turtle Entrance",                  "Star Tropic - West"),
    ("Star Tropic - East Turtle Entrance",                  "Star Tropic - East"),
    ("Eastern Shoal - Turtle Entrance",                     "Eastern Shoal - Turtle"),
    ("Lost Landing - Turtle Entrance",                      "Lost Landing - Turtle"),
    ("Beast Ridge - Turtle Entrance",                       "Beast Ridge - Bellstone"),

    # - - - - - - - - - -
    # Ancient Isle
    # - - - - - - - - - -
    ("Ancient Isle - West to Origin",                       "Ancient Isle - Origin"),
    ("Ancient Isle - East Turtle Exit",                     "Topaz Sea"),
    ("Ancient Isle - West Turtle Exit",                     "Obsidian Sea"),
    ("Ancient Isle - North Exit",                           "Sanctum"),
    ("Phoenix Hub - Phoenix Anywhere Entrance",             "Phoenix Hub"), 

    # - - - - - - - - - -
    # Stony Cliffs
    # - - - - - - - - - -
    ("Stony Cliffs - God Altar to North-East",              "Stony Cliffs - North-East"),
    ("Stony Cliffs - God Altar to South-East",              "Stony Cliffs - South-East"),
    ("Stony Cliffs - God Altar to South Coast",             "Stony Cliffs - South Coast"),
    ("Stony Cliffs - God Altar to Phoenix",                 "Stony Cliffs - Phoenix"),
    ("Stony Cliffs - God Altar Music Cavern Entrance",      "Stone Dungeon - Below Xylophone"),
    ("Stony Cliffs - God Altar East Cavern Entrance",       "Stone Dungeon Earth Chamber"),
    ("Stony Cliffs - North-East to God Altar",              "Stony Cliffs - God Altar"),
    ("Stony Cliffs - North-East Cavern Entrance",           "Stone Dungeon - North Tunnels"),
    ("Stony Cliffs - South-East to God Altar",              "Stony Cliffs - God Altar"),
    ("Stony Cliffs - South-East to Golden Stone",           "Stony Cliffs - Golden Stone"),
    ("Stony Cliffs - South-East Cavern Entrance",           "Stone Dungeon - South Tunnels"),
    ("Stony Cliffs - South Coast to God Altar",             "Stony Cliffs - God Altar"),
    ("Stony Cliffs - South Coast to South-East",            "Stony Cliffs - South-East"),
    ("Stony Cliffs - South Coast to South Star Stone",      "Stony Cliffs - South Star Stone"),
    ("Stony Cliffs - South Coast South Cavern Entrance",    "Stone Dungeon - South Tunnels"),
    ("Stony Cliffs - South Coast Center Cavern Entrance",   "Stone Dungeon - West Tunnels"),
    ("Stony Cliffs - Phoenix to God Altar",                 "Stony Cliffs - God Altar"),
    ("Stony Cliffs - Phoenix to North-West",                "Stony Cliffs - North-West"),
    ("Stony Cliffs - Phoenix to West Star Stone",           "Stony Cliffs - West Star Stone"),
    ("Stony Cliffs - North-West Cavern Entrance",           "Stone Dungeon - North Tunnels"),
    ("Stony Cliffs - Tablet Slot to South-West",            "Stony Cliffs - South-West"),
    ("Stony Cliffs - Tablet Slot to South Coast",           "Stony Cliffs - South Coast"),
    ("Stony Cliffs - Tablet Slot Cavern Entrance",          "Stone Dungeon - West Tunnels"),
    ("Stony Cliffs - South-West Cavern Entrance",           "Stone Dungeon - South Tunnels"),
    ("Stony Cliffs - West Star Stone to Phoenix",           "Stony Cliffs - Phoenix"),
    ("Stony Cliffs - South Star Stone to South-West",       "Stony Cliffs - South-West"),
    ("Stony Cliffs - South Star Stone to South Coast",      "Stony Cliffs - South Coast"),
    ("Stony Cliffs - Golden Stone to South-East",           "Stony Cliffs - South-East"),
    ("Stony Cliffs - Golden Stone to Windy Cliff",          "Stony Cliffs - Windy Cliff"),
    ("Stony Cliffs - Windy Cliff to Golden Stone",          "Stony Cliffs - Golden Stone"),
    ("Stony Cliffs - Windy Cliff to South Coast",           "Stony Cliffs - South Coast"),
    ("Stone Dungeon - North Tunnels to Dirt Chamber",       "Stone Dungeon - Dirt Chamber"),
    ("Stone Dungeon - North Tunnels to Gopher Vault",       "Stone Dungeon - Gopher Vault"),
    ("Stone Dungeon - North Tunnels North-West Cavern Exit","Stony Cliffs - North-West"),
    ("Stone Dungeon - North Tunnels Phoenix Cavern Exit",   "Stony Cliffs - Phoenix"),
    ("Stone Dungeon - South Tunnels to Vault Door",         "Stone Dungeon - Vault Door"),
    ("Stone Dungeon - South Tunnels South-West Cavern Exit","Stony Cliffs - South-West"),
    ("Stone Dungeon - South Tunnels South Cavern Exit",     "Stony Cliffs - South Coast"),
    ("Stone Dungeon - South Tunnels South-East Cavern Exit","Stony Cliffs - South-East"),
    ("Stone Dungeon - West Tunnels to Dirt Chamber",        "Stone Dungeon - Dirt Chamber"),
    ("Stone Dungeon - West Tunnels Tablet Slot Cavern Exit","Stony Cliffs - Tablet Slot"),
    ("Stone Dungeon - West Tunnels Center Cavern Exit",     "Stony Cliffs - South Coast"),
    ("Stone Dungeon - Vault Door to Gopher Vault",          "Stone Dungeon - Gopher Vault"),
    ("Stone Dungeon - Vault Door to West Tunnels",          "Stone Dungeon - West Tunnels"),
    ("Stone Dungeon - Vault Door to North Tunnels",         "Stone Dungeon - North Tunnels"),
    ("Stone Dungeon - Vault Door to Earth Chamber",         "Stone Dungeon Earth Chamber"),
    ("Stone Dungeon - Vault Door to East Tunnels",          "Stone Dungeon - East Tunnels"),
    ("Stone Dungeon - Gopher Vault to Vault Door",          "Stone Dungeon - Vault Door"),
    ("Stone Dungeon - Gopher Vault to North Tunnels",       "Stone Dungeon - North Tunnels"),
    ("Stone Dungeon - Dirt Chamber to North Tunnels",       "Stone Dungeon - North Tunnels"),
    ("Stone Dungeon - Below Xylophone Cavern Exit",         "Stony Cliffs - God Altar"),
    ("Stone Dungeon - Earth Chamber to East Tunnels",       "Stone Dungeon - East Tunnels"),
    ("Stone Dungeon - Earth Chamber East Cavern Exit",      "Stony Cliffs - God Altar"),
    
    ("Stony Cliffs - East Turtle Exit",                     "Topaz Sea"),
    ("Stony Cliffs - West Turtle Exit",                     "Sapphire Sea"),
    ("Stony Cliffs - Phoenix Exit",                         "Phoenix Hub"),

    # - - - - - - - - - -
    # Tidal Reef
    # - - - - - - - - - -
    ("Tidal Reef - God Altar to Shell Puzzle",              "Tidal Reef - Shell Puzzle"), 
    ("Tidal Reef - God Altar to East",                      "Tidal Reef - East"), 
    ("Tidal Reef - God Altar to Phoenix",                   "Tidal Reef - Phoenix"), 
    ("Tidal Reef - God Altar to South-West",                "Tidal Reef - South-West"), 
    ("Tidal Reef - God Altar to West Star Stone",           "Tidal Reef - West Star Stone"), 
    ("Tidal Reef - God Altar to North-West",                "Tidal Reef - North-West"), 
    ("Tidal Reef - Shell Puzzle to God Altar",              "Tidal Reef - God Altar"), 
    ("Tidal Reef - Shell Puzzle to East",                   "Tidal Reef - East"), 
    ("Tidal Reef - East to Shell Puzzle",                   "Tidal Reef - Shell Puzzle"), 
    ("Tidal Reef - East to God Altar",                      "Tidal Reef - God Altar"), 
    ("Tidal Reef - Phoenix to God Altar",                   "Tidal Reef - God Altar"), 
    ("Tidal Reef - Phoenix to South-West",                  "Tidal Reef - South-West"), 
    ("Tidal Reef - South-West to God Altar",                "Tidal Reef - God Altar"), 
    ("Tidal Reef - South-West to Phoenix",                  "Tidal Reef - Phoenix"), 
    ("Tidal Reef - God Altar to North-West Low Tide",       "Tidal Reef - North-West Low Tide"), 
    ("Tidal Reef - West Star Stone to God Altar",           "Tidal Reef - God Altar"), 
    ("Tidal Reef - West Star Stone to South-West",          "Tidal Reef - South-West"), 
    ("Tidal Reef - North-West to God Altar",                "Tidal Reef - God Altar"), 
    ("Tidal Reef - North-West to North-West Low Tide",      "Tidal Reef - North-West Low Tide"), 
    ("Tidal Reef - North-West Low Tide to God Altar",       "Tidal Reef - God Altar"),
    
    ("Tidal Reef - Turtle Exit",                            "Sapphire Sea"),
    ("Tidal Reef - Phoenix Exit",                           "Phoenix Hub"),

    # - - - - - - - - - -
    # Raging Volcano
    # - - - - - - - - - -
    ("Raging Volcano - God Altar to Phoenix",               "Raging Volcano - Phoenix"),
    ("Raging Volcano - God Altar to South Coast",           "Raging Volcano - South Coast"),
    ("Raging Volcano - God Altar to Triple Ruby Pit",       "Raging Volcano - Triple Ruby Pit"),
    ("Raging Volcano - God Altar to Lyre",                  "Raging Volcano - Lyre"),
    ("Raging Volcano - God Altar to Above Volcano",         "Raging Volcano - Above Volcano"),
    ("Raging Volcano - God Altar to Below Hot Spring",      "Raging Volcano - Below Hot Spring"),
    ("Raging Volcano - God Altar to North-West",            "Raging Volcano - North-West"),
    ("Raging Volcano - God Altar to North-West Pass",       "Raging Volcano - North-West Pass"),
    ("Raging Volcano - God Altar to Key Triplets",          "Raging Volcano - Key Triplets"),
    ("Raging Volcano - Phoenix to God Altar",               "Raging Volcano - God Altar"),
    ("Raging Volcano - Phoenix to Hot Spring",              "Raging Volcano - Hot Spring"),
    ("Raging Volcano - Hot Spring to God Altar",            "Raging Volcano - God Altar"),
    ("Raging Volcano - Hot Spring to Phoenix",              "Raging Volcano - Phoenix"),
    ("Raging Volcano - South Coast to God Altar",           "Raging Volcano - God Altar"),
    ("Raging Volcano - South Coast to Triple Ruby Pit",     "Raging Volcano - Triple Ruby Pit"),
    ("Raging Volcano - Triple Ruby Pit to God Altar",       "Raging Volcano - God Altar"),
    ("Raging Volcano - Lyre to God Altar",                  "Raging Volcano - God Altar"),
    ("Raging Volcano - Lyre to Triple Ruby Pit",            "Raging Volcano - Triple Ruby Pit"),
    ("Raging Volcano - Above Volcano to God Altar",         "Raging Volcano - God Altar"),
    ("Raging Volcano - Above Volcano to South Coast",       "Raging Volcano - South Coast"),
    ("Raging Volcano - Above Volcano to Lyre",              "Raging Volcano - Lyre"),
    ("Raging Volcano - Above Volcano to Idol Room West",    "Raging Volcano - Idol Room West"),
    ("Raging Volcano - Idol Room West to South Coast",      "Raging Volcano - South Coast"),
    ("Raging Volcano - Idol Room West to Below Hot Spring", "Raging Volcano - Below Hot Spring"),
    ("Raging Volcano - Below Hot Spring to God Altar",      "Raging Volcano - God Altar"),
    ("Raging Volcano - Below Hot Spring to South Coast",    "Raging Volcano - South Coast"),
    ("Raging Volcano - Below Hot Spring to Idol Room West", "Raging Volcano - Idol Room West"),
    ("Raging Volcano - North-West to God Altar",            "Raging Volcano - God Altar"),
    ("Raging Volcano - North-West Pass to God Altar",       "Raging Volcano - God Altar"),
    ("Raging Volcano - North-West Pass to North-East",      "Raging Volcano - North-West"),
    ("Raging Volcano - North-West Pass to Geyser Pass",     "Raging Volcano - Geyser Pass"),
    ("Raging Volcano - Key Triplets to God Altar",          "Raging Volcano - God Altar"),
    ("Raging Volcano - Key Triplets to Geyser Pass",        "Raging Volcano - Geyser Pass"),
    ("Raging Volcano - Geyser Pass to North-West",          "Raging Volcano - North-West"),
    ("Raging Volcano - Geyser Pass to North-West Pass",     "Raging Volcano - North-West Pass"),
    ("Raging Volcano - Geyser Pass to Key Triplets",        "Raging Volcano - Key Triplets"),
    
    ("Raging Volcano - Turtle Exit",                        "Ruby Sea"),
    ("Raging Volcano - Phoenix Exit",                       "Phoenix Hub"),

    # - - - - - - - - - -
    # Frozen Spire
    # - - - - - - - - - -
    ("Frozen Spire - Spire to Post-Rune",                   "Frozen Spire - Post-Rune"),
    ("Frozen Spire - Post-Rune to Spire",                   "Frozen Spire"),
    
    ("Frozen Spire - Turtle Exit",                          "Diamond Sea"),
    ("Frozen Spire - Phoenix Exit",                         "Phoenix Hub"),

    # - - - - - - - - - -
    # Serpent Stacks
    # - - - - - - - - - -
    ("Serpent Stacks - Exit",                               "Obsidian Sea"),
    ("Serpent Stacks - Entrance to Head",                   "Serpent Stacks - Head"),
    ("Serpent Stacks - Entrance to Post-Rune",              "Serpent Stacks - Post-Rune"),
    ("Serpent Stacks - Post-Rune to Core",                  "Serpent Stacks - Core"),
    ("Serpent Stacks - Core to Tail",                       "Serpent Stacks - Tail"),

    # - - - - - - - - - -
    # Sanctum
    # - - - - - - - - - -
    ("Sanctum - Turtle Exit",                               "Ancient Isle - Origin"),
    ("Sanctum - Elemental Rock Path",                       "Sanctum - Peak"),
    
    # - - - - - - - - - -
    # Rolling Rocks
    # - - - - - - - - - -
    ("Rolling Rocks - West to South-East",                  "Rolling Rocks - South-East"),
    ("Rolling Rocks - South-East to West",                  "Rolling Rocks - West"),
    ("Rolling Rocks - North-East to South-East",            "Rolling Rocks - South-East"),
    ("Rolling Rocks - West Turtle Exit",                    "Topaz Sea"),
    ("Rolling Rocks - East Turtle Exit",                    "Topaz Sea"),
    
    # - - - - - - - - - -
    # Sunken Island
    # - - - - - - - - - -
    ("Sunken Island - Turtle Exit",                         "Ruby Sea"),

    # - - - - - - - - - -
    # Aggro Crag
    # - - - - - - - - - -
    ("Aggro Crag - East to South-West",                     "Aggro Crag - South-West"),
    ("Aggro Crag - South-West to East",                     "Aggro Crag - East"),
    ("Aggro Crag - South-West to North-West",               "Aggro Crag - North-West"),
    ("Aggro Crag - North-West to South-West",               "Aggro Crag - South-West"),
    ("Aggro Crag - North-West to East",                     "Aggro Crag - East"),
    ("Aggro Crag - Turtle Exit",                            "Sapphire Sea"),

    # - - - - - - - - - -
    # Sea Nunatak
    # - - - - - - - - - -
    ("Sea Nunatak - Turtle Exit",                           "Eastern Sea"),
    
    # - - - - - - - - - -
    # Locked Key
    # - - - - - - - - - -
    ("Locked Key - Turtle Exit",                            "Obsidian Sea"),
    
    # - - - - - - - - - -
    # Star Tropic
    # - - - - - - - - - -
    ("Star Tropic - East Turtle Exit",                      "Ruby Sea"),
    ("Star Tropic - West Turtle Exit",                      "Lost Sea"),
    ("Star Tropic - West to Star Pocket",                   "Star Tropic - Star Pocket"),
    ("Star Tropic - West to Treasure Shore",                "Star Tropic - Treasure Shore"),
    ("Star Tropic - North-East to Star Pocket",             "Star Tropic - Star Pocket"),
    ("Star Tropic - Star Pocket to East",                   "Star Tropic - East"),
    ("Star Tropic - Treasure Shore to West",                "Star Tropic - West"),
    
    # - - - - - - - - - -
    # Eastern Shoal
    # - - - - - - - - - -
    ("Eastern Shoal - Turtle to North-West",                "Eastern Shoal - North-West"),
    ("Eastern Shoal - North-West to Turtle",                "Eastern Shoal - Turtle"),
    ("Eastern Shoal - Turtle Exit",                         "Eastern Sea"),
    
    # - - - - - - - - - -
    # Lost Landing
    # - - - - - - - - - -
    ("Lost Landing - Turtle to West",                       "Lost Landing - West"),
    ("Lost Landing - West to Turtle",                       "Lost Landing - Turtle"),
    ("Lost Landing - Staircase to Phoenix",                 "Lost Landing - Phoenix"),
    ("Lost Landing - Staircase to Turtle",                  "Lost Landing - Turtle"),
    ("Lost Landing - Phoenix to Staircase",                 "Lost Landing - Staircase"),

    ("Lost Landing - Turtle Exit",                          "Lost Sea"),
    ("Lost Landing - Phoenix Exit",                         "Phoenix Hub"),
    
    # - - - - - - - - - -
    # Beast Ridge
    # - - - - - - - - - -
    ("Beast Ridge - Bellstone to Phoenix",                  "Beast Ridge - Phoenix"),
    ("Beast Ridge - Phoenix to Bellstone",                  "Beast Ridge - Bellstone"),
    ("Beast Ridge - Turtle Exit",                           "Beast Sea"),
    ("Beast Ridge - Phoenix Exit",                          "Phoenix Hub"),
    
    # - - - - - - - - - -
    # Phoenix Hub
    # - - - - - - - - - -
    ("Stony Cliffs - Phoenix Entrance",                     "Stony Cliffs - Phoenix"),
    ("Tidal Reef - Phoenix Entrance",                       "Tidal Reef - Phoenix"),
    ("Raging Volcano - Phoenix Entrance",                   "Raging Volcano - Phoenix"),
    ("Frozen Spire - Phoenix Entrance",                     "Frozen Spire - Post-Rune"),
    ("Lost Landing - Phoenix Entrance",                     "Lost Landing - Phoenix"),
    ("Beast Ridge - Phoenix Entrance",                      "Beast Ridge - Phoenix"),
]

circlet_regions: list[tuple[str, list[str]]] = [
    # new connections from existing regions
    ("Forgotten Sea", ["Forgotten Lagoon - Turtle Entrance"]),
    
    ("Stony Cliffs - God Altar", ["Stony Cliffs - God Altar to Giant Wheel"]),
    ("Serpent Stacks - Core", ["Serpent Stacks - Core to Serpent Lock"]),
    ("Serpent Stacks - Entrance", ["Serpent Stacks - Solve A2 Puzzles"]),
    ("Eastern Shoal - North-West", ["Eastern Shoal - North-West to South"]),

    # Completely new regions
    ("Stony Cliffs - Giant Wheel", []), # Dead end room with 1 entrance, no backwards logic needed.
    ("Serpent Stacks - Serpent Lock", []), # Lock Room A5 with 4 lock shards
    ("Serpent Stacks - A2 Pyramidions", []), # Able to see the code at Water A3

    ("Eastern Shoal - South", ["Eastern Shoal - South to North-East"]),
    ("Eastern Shoal - North-East", []),

    ("Forgotten Lagoon - Turtle", [
        "Forgotten Lagoon - Turtle to North",
        "Forgotten Lagoon - Turtle Exit"
    ]),
    ("Forgotten Lagoon - North", [
        "Forgotten Lagoon - North to Turtle",
        "Forgotten Lagoon - North to South"
    ]),
    ("Forgotten Lagoon - South", []),
]

circlet_connections: list[tuple[str, str]] = [
    ("Forgotten Lagoon - Turtle Entrance", "Forgotten Lagoon - Turtle"),
    
    ("Stony Cliffs - God Altar to Giant Wheel", "Stony Cliffs - Giant Wheel"),
    ("Serpent Stacks - Core to Serpent Lock", "Serpent Stacks - Serpent Lock"),
    ("Serpent Stacks - Solve A2 Puzzles", "Serpent Stacks - A2 Pyramidions"),

    ("Eastern Shoal - North-West to South", "Eastern Shoal - South"),
    ("Eastern Shoal - South to North-East", "Eastern Shoal - North-East"),

    ("Forgotten Lagoon - Turtle to North", "Forgotten Lagoon - North"),
    ("Forgotten Lagoon - North to Turtle", "Forgotten Lagoon - Turtle"),
    ("Forgotten Lagoon - North to South", "Forgotten Lagoon - South"),
    ("Forgotten Lagoon - Turtle Exit", "Forgotten Sea")
]

# Warp Logic allows for using warps to enter star tropic and the lost / forgotten seas without the phoenix flue
warp_logic_regions: list[tuple[str, list[str]]] = [
    ("Stony Cliffs - God Altar", ["Stony Cliffs - Warp Exit"]),
    ("Tidal Reef - Phoenix", ["Tidal Reef - Warp Exit"]),
    ("Raging Volcano - God Altar", ["Raging Volcano - Warp Exit"]),
    ("Frozen Spire", ["Frozen Spire - Warp Exit"]),

    ("Warp Hub", ["Star Tropic - Warp Entrance"]),
    ("Star Tropic - Meteorite", ["Star Tropic - Meteorite to Treasure Shore"])
]

warp_logic_connections: list[tuple[str, str]] = [
    ("Stony Cliffs - Warp Exit", "Warp Hub"),
    ("Tidal Reef - Warp Exit", "Warp Hub"),
    ("Raging Volcano - Warp Exit", "Warp Hub"),
    ("Frozen Spire - Warp Exit", "Warp Hub"),

    ("Star Tropic - Warp Entrance", "Star Tropic - Meteorite"),
    ("Star Tropic - Meteorite to Treasure Shore", "Star Tropic - Treasure Shore")
]

meteorite_regions: list[tuple[str, list[str]]] = [
    ("Warp Hub", [
        "Stony Cliffs - Warp Entrance",
        "Tidal Reef - Warp Entrance",
        "Raging Volcano - Warp Entrance",
        "Frozen Spire - Warp Entrance",
        "Ancient Cavern - Warp Entrance",
        "Lost Landing - Warp Entrance",
        "Totem - Warp Entrance"
    ]),

    ("Ancient Isle - Origin", ["Ancient Isle - Cavern Entrance"]),
    ("Ancient Cavern - South", ["Ancient Cavern - South Cavern Exit"]),
    ("Ancient Cavern - North", ["Ancient Cavern - North to South"]),

    ("Lost Landing - Compass", ["Lost Landing - Compass to Landing"]),
    ("Totem", []),
]

meteorite_connections: list[tuple[str, str]] = [
    ("Stony Cliffs - Warp Entrance", "Stony Cliffs - God Altar"),
    ("Tidal Reef - Warp Entrance", "Tidal Reef - Phoenix"),
    ("Raging Volcano - Warp Entrance", "Raging Volcano - God Altar"),
    ("Frozen Spire - Warp Entrance", "Frozen Spire"),
    ("Ancient Cavern - Warp Entrance", "Ancient Cavern - North"),
    ("Lost Landing - Warp Entrance", "Lost Landing - Compass"),
    ("Totem - Warp Entrance", "Totem"),

    ("Ancient Isle - Cavern Entrance", "Ancient Cavern - South"),
    ("Ancient Cavern - South Cavern Exit", "Ancient Isle - Origin"),
    ("Ancient Cavern - North to South", "Ancient Cavern - South"),

    ("Lost Landing - Compass to Landing", "Lost Landing - West"),

]

circlet_meteorite_regions: list[tuple[str, list[str]]] = [
    ("Beast Ridge - Bellstone", [
        "Forgotten Lagoon - Phoenix Entrance"
    ]),
    ("Forgotten Lagoon - Meteorite", [
        "Forgotten Lagoon - Meteorite to North" # Frog Flippers
    ]),
]

circlet_meteorite_connections: list[tuple[str, str]] = [
    ("Forgotten Lagoon - Phoenix Entrance", "Forgotten Lagoon - Meteorite"),
    ("Forgotten Lagoon - Meteorite to North", "Forgotten Lagoon - North"),
]