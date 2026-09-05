from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachRegion, CanReachEntrance, Has

from .Options import PhoenixAnywhere, ShuffleNotes, ShuffleMeteorites, RequireSerpentClues, WarpsInLogic

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld

# Sets rules on entrances and advancements that are always applied
def set_rules(world: "IslesOfSeaAndSkyWorld"):
    # Entrances
    
    # - - - - - - - - - -
    # Overworld
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Topaz Sea - Exit to Eastern Sea"),
                   Has("Star Piece", 3))  # Diamond Sea

    world.set_rule(world.get_entrance("Topaz Sea - Exit to Ruby Sea"),
                   Has("Star Piece", 15))  # Ruby Sea

    world.set_rule(world.get_entrance("Eastern Sea - Exit to Diamond Sea"),
                   Has("Star Piece", 30))  # North Diamond Sea

    world.set_rule(world.get_entrance("Diamond Sea - Exit to Eastern Sea"),
                   Has("Star Piece", 30))  # Diamond Sea

    world.set_rule(world.get_entrance("Serpent Stacks - Turtle Entrance"),
                   Has("Star Piece", 45))  # Serpent Stacks
    
    # - - - - - - - - - -
    # Ancient Isle
    # - - - - - - - - - -
    ## Required for completion detection
    world.set_rule(world.get_entrance("Ancient Isle - North Exit"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals"))  # To Sanctum

    # - - - - - - - - - -
    # Stony Cliffs
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Stony Cliffs - God Altar to North-East"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - North-East to God Altar"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - God Altar to South-East"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - South-East to God Altar"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - God Altar to South Coast"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - God Altar to Phoenix"),
                   Has("Topaz Rune Stone"))
    world.set_rule(world.get_entrance("Stony Cliffs - Phoenix to God Altar"),
                   Has("Topaz Rune Stone"))

    world.set_rule(world.get_entrance("Stony Cliffs - God Altar East Cavern Entrance"),
                   Has("Kite Cloak"))

    world.set_rule(world.get_entrance("Stony Cliffs - South-East to Golden Stone"),
                   Has("Star Piece", 20))
    world.set_rule(world.get_entrance("Stony Cliffs - Golden Stone to South-East"),
                   Has("Star Piece", 20))

    world.set_rule(world.get_entrance("Stony Cliffs - South Coast to South Star Stone"),
                   Has("Star Piece", 15))
    world.set_rule(world.get_entrance("Stony Cliffs - South Star Stone to South Coast"),
                   Has("Star Piece", 15) | (Has("Awaken Earth Elementals") & Has("Gopher Gloves")))

    world.set_rule(world.get_entrance("Stony Cliffs - Phoenix to West Star Stone"),
                   Has("Star Piece", 5))
    world.set_rule(world.get_entrance("Stony Cliffs - West Star Stone to Phoenix"),
                   Has("Star Piece", 5))

    world.set_rule(world.get_entrance("Stony Cliffs - Golden Stone to Windy Cliff"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_entrance("Stone Dungeon - North Tunnels to Dirt Chamber"),
                   Has("Gopher Gloves"))
    world.set_rule(world.get_entrance("Stone Dungeon - Dirt Chamber to North Tunnels"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_entrance("Stone Dungeon - North Tunnels to Gopher Vault"),
                   Has("Gopher Gloves"))
    world.set_rule(world.get_entrance("Stone Dungeon - Gopher Vault to North Tunnels"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_entrance("Stone Dungeon - South Tunnels to Vault Door"),
                   Has("Awaken Earth Elementals"))
    world.set_rule(world.get_entrance("Stone Dungeon - Earth Chamber East Cavern Exit"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_entrance("Stone Dungeon - Vault Door to Earth Chamber"),
                   CanReachRegion("Stone Dungeon - Below Xylophone"))

    world.set_rule(world.get_entrance("Stone Dungeon - Vault Door to Gopher Vault"),
                   CanReachRegion("Stony Cliffs - North-West")
                   & CanReachRegion("Stony Cliffs - North-East")
                   & CanReachRegion("Stony Cliffs - South-West")
                   & CanReachRegion("Stony Cliffs - South-East"))
    world.set_rule(world.get_entrance("Stone Dungeon - Gopher Vault to Vault Door"),
                   CanReachRegion("Stony Cliffs - North-West")
                   & CanReachRegion("Stony Cliffs - North-East")
                   & CanReachRegion("Stony Cliffs - South-West")
                   & CanReachRegion("Stony Cliffs - South-East"))

    world.set_rule(world.get_entrance("Stony Cliffs - Phoenix Exit"),
                   Has("Phoenix Flute"))

    # - - - - - - - - - -
    # Tidal Reef
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Tidal Reef - God Altar to Shell Puzzle"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to East"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to Phoenix"),
                   Has("Sapphire Rune Stone")
                   | Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to South-West"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to North-West Low Tide"),
                   Has("Awaken Water Elementals")
                   | Has("Kite Cloak"))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to West Star Stone"),
                   Has("Frog Flippers")
                   | (Has("Awaken Water Elementals")
                      & Has("Star Piece", 30)
                   ))

    world.set_rule(world.get_entrance("Tidal Reef - God Altar to North-West"),
                   Has("Sapphire Rune Stone")
                   | Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Tidal Reef - Shell Puzzle to East"),
                   Has("Frog Flippers")
                   | Has("Awaken Water Elementals"))

    world.set_rule(world.get_entrance("Tidal Reef - Phoenix to God Altar"),
                   Has("Sapphire Rune Stone")
                   | Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Tidal Reef - Phoenix to South-West"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Tidal Reef - South-West to God Altar"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_entrance("Tidal Reef - South-West to Phoenix"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Tidal Reef - Phoenix Exit"),
                   Has("Phoenix Flute"))

    # - - - - - - - - - -
    # Raging Volcano
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Phoenix"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to South Coast"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Triple Ruby Pit"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Lyre"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Above Volcano"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Below Hot Spring"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to North-West"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to North-West Pass"),
                   Has("Ruby Rune Stone")
                   | Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - God Altar to Key Triplets"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Phoenix to God Altar"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_entrance("Raging Volcano - Phoenix to Hot Spring"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Hot Spring to God Altar"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - Hot Spring to Phoenix"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - South Coast to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Triple Ruby Pit to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Above Volcano to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Below Hot Spring to Idol Room West"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_entrance("Raging Volcano - North-West to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - North-West Pass to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - North-West Pass to Geyser Pass"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - Key Triplets to God Altar"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Key Triplets to Geyser Pass"),
                   Has("Ruby Rune Stone"))
    world.set_rule(world.get_entrance("Raging Volcano - Geyser Pass to North-West Pass"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Raging Volcano - Geyser Pass to Key Triplets"),
                   Has("Ruby Rune Stone"))

    # - - - - - - - - - -
    # Frozen Spire
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Frozen Spire - Spire to Post-Rune"),
                   Has("Diamond Rune Stone"))  # Frozen Spire Post-Rune

    # - - - - - - - - - -
    # Serpent Stacks
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Serpent Stacks - Entrance to Head"),
                   Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone"))
    world.set_rule(world.get_entrance("Serpent Stacks - Entrance to Post-Rune"),
                   Has("Obsidian Rune Stone"))  # Serpent Stacks Post-Rune
    world.set_rule(world.get_entrance("Serpent Stacks - Post-Rune to Core"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Shadow Elementals"))
    world.set_rule(world.get_entrance("Serpent Stacks - Core to Tail"),
                    Has("Awaken Water Elementals")
                    | ( Has("Kite Cloak")
                        & Has("Awaken Fire Elementals")
                    ))
    
    # - - - - - - - - - -
    # Sanctum
    # - - - - - - - - - -
    ## Required for completion detection
    world.set_rule(world.get_entrance("Sanctum - Elemental Rock Path"),
                   Has("Sanctum Shard Hit - Earth")
                   & Has("Sanctum Shard Hit - Water")
                   & Has("Sanctum Shard Hit - Fire")
                   & Has("Sanctum Shard Hit - Wind"))  # Sanctum Peak
    
    # - - - - - - - - - -
    # Rolling Rocks
    # - - - - - - - - - - 
    world.set_rule(world.get_entrance("Rolling Rocks - West to South-East"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Rolling Rocks - South-East to West"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Rolling Rocks - North-East to South-East"),
                   Has("Ancient Rune Stone"))
    
    # - - - - - - - - - -
    # Sunken Island
    # - - - - - - - - - -

    # - - - - - - - - - -
    # Aggro Crag
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Aggro Crag - East to South-West"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals")
                   & Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Aggro Crag - South-West to East"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Aggro Crag - South-West to North-West"),
                   Has("Salamander Shirt"))
    world.set_rule(world.get_entrance("Aggro Crag - North-West to South-West"),
                   Has("Salamander Shirt"))

    # - - - - - - - - - -
    # Sea Nunatak
    # - - - - - - - - - -

    # - - - - - - - - - -
    # Locked Key
    # - - - - - - - - - -

    # - - - - - - - - - -
    # Star Tropic
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Star Tropic - West to Treasure Shore",),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Star Tropic - Treasure Shore to West"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Star Tropic - North-East to Star Pocket"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Star Tropic - Star Pocket to East"),
                   Has("Ancient Rune Stone"))

    # - - - - - - - - - -
    # Eastern Shoal
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Eastern Shoal - Turtle to North-West"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_entrance("Eastern Shoal - North-West to Turtle"),
                   Has("Ancient Rune Stone"))
    
    # - - - - - - - - - -
    # Lost Landing
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Lost Landing - Turtle to West"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Lost Landing - West to Turtle"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_entrance("Lost Landing - Staircase to Phoenix"),
                   Has("Star Piece", 30))

    world.set_rule(world.get_entrance("Lost Landing - Phoenix to Staircase"),
                   Has("Star Piece", 30))

    
    # - - - - - - - - - -
    # Beast Ridge
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Beast Ridge - Bellstone to Phoenix"),
                   Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))
    world.set_rule(world.get_entrance("Beast Ridge - Phoenix to Bellstone"),
                   Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))
    

    # - - - - - - - - - -
    # Phoenix Hub
    # - - - - - - - - - -
    world.set_rule(world.get_entrance("Phoenix Hub - Phoenix Anywhere Entrance"),
                   Has("Phoenix Flute",
                       options=[OptionFilter(PhoenixAnywhere, PhoenixAnywhere.option_true)]))  # Phoenix Hub
    
    world.set_rule(world.get_entrance("Stony Cliffs - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Tidal Reef - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Raging Volcano - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Frozen Spire - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Beast Ridge - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Lost Landing - Phoenix Exit"),
                   Has("Phoenix Flute"))  # Phoenix Hub

    world.set_rule(world.get_entrance("Stony Cliffs - Phoenix Entrance"),
                   Has("Phoenix Flute"))
    world.set_rule(world.get_entrance("Tidal Reef - Phoenix Entrance"),
                   Has("Phoenix Flute"))  # Tidal Reef
    world.set_rule(world.get_entrance("Raging Volcano - Phoenix Entrance"),
                   Has("Phoenix Flute"))  # Raging Volcano NE
    world.set_rule(world.get_entrance("Frozen Spire - Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & Has("Diamond Rune Stone"))  # Frozen Spire
    world.set_rule(world.get_entrance("Lost Landing - Phoenix Entrance"),
                   Has("Phoenix Flute"))  # Lost Landing
    world.set_rule(world.get_entrance("Beast Ridge - Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & CanReachRegion("Beast Ridge - Phoenix"))


    # - - - - - - - - - -
    # Circlet Content
    # - - - - - - - - - -
    if world.options.circlet_content_enabled:
        # Serpent Stacks lock quest
        world.set_rule(world.get_entrance("Serpent Stacks - Core to Serpent Lock"),
                       Has("Serpent Lock Shard", 4))

        world.set_rule(world.get_entrance("Serpent Stacks - Solve A2 Puzzles"),
                       Has("Serpent Circlet")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals")
                       & Has("Awaken Fire Elementals")
                       & Has("Awaken Wind Elementals")
                       & Has("Awaken Shadow Elementals")
                       & CanReachRegion("Serpent Stacks - Post-Rune")
                       & CanReachRegion("Serpent Stacks - Core")
                       & CanReachRegion("Serpent Stacks - Tail")
                       & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                          | CanReachRegion("Tidal Reef - God Altar")
                          ))

        # New Stony Cliffs Room
        world.set_rule(world.get_entrance("Stony Cliffs - God Altar to Giant Wheel"),
                       Has("Serpent Circlet")
                       & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                          | CanReachRegion("Rolling Rocks - South-East")
                          ))

        # Shoal Expansion
        world.set_rule(world.get_entrance("Eastern Shoal - North-West to South"),
                       Has("Serpent Circlet")
                       & Has("Kite Cloak"))
        world.set_rule(world.get_entrance("Eastern Shoal - South to North-East"),
                       [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                       | CanReachRegion("Frozen Spire"))
        # Forgotten Lagoon
        world.set_rule(world.get_entrance("Forgotten Lagoon - Turtle to North"),
                       Has("Serpent Circlet")
                       & Has("Ancient Rune Stone")
                       & Has("Ancient Key", 66))
        world.set_rule(world.get_entrance("Forgotten Lagoon - North to South"),
                       Has("Frog Flippers")
                       & Has("Ancient Key", 67)
                       & Has("Star Piece", 70))

    # - - - - - - - - - -
    # Meteorite Content
    # - - - - - - - - - -
    # Star Tropic Warp can be used to access lost and forgotten seas without phoenix flute
    if world.options.warps_in_logic:
        world.set_rule(world.get_entrance("Stony Cliffs - Warp Exit"),
                       Has("Ancient Key", 7))

        world.set_rule(world.get_entrance("Star Tropic - Warp Entrance"),
                       Has("Warp Pattern - Tropic")
                       | ([OptionFilter(WarpsInLogic, WarpsInLogic.option_true),
                           OptionFilter(ShuffleMeteorites, ShuffleMeteorites.option_false)]
                          & CanReachEntrance("Stony Cliffs - Warp Exit")
                          & CanReachEntrance("Tidal Reef - Warp Exit")
                          & CanReachEntrance("Raging Volcano - Warp Exit")
                          & CanReachEntrance("Frozen Spire - Warp Exit")
                          ))

    if world.options.shuffle_meteorites:
        # Ancient Cavern
        world.set_rule(world.get_entrance("Ancient Isle - Cavern Entrance"),
                       CanReachRegion("Stony Cliffs - God Altar")
                       & Has("Awaken Earth Elementals")
                       & CanReachRegion("Tidal Reef - God Altar")
                       & Has("Awaken Water Elementals")
                       & CanReachRegion("Raging Volcano - God Altar")
                       & Has("Awaken Fire Elementals")
                       & CanReachRegion("Frozen Spire")
                       & Has("Awaken Wind Elementals"))

        # Warp Hub
        world.set_rule(world.get_entrance("Stony Cliffs - Warp Entrance"),
                       Has("Warp Pattern - Earth"))
        world.set_rule(world.get_entrance("Tidal Reef - Warp Entrance"),
                       Has("Warp Pattern - Water"))
        world.set_rule(world.get_entrance("Raging Volcano - Warp Entrance"),
                       Has("Warp Pattern - Fire"))
        world.set_rule(world.get_entrance("Frozen Spire - Warp Entrance"),
                       Has("Warp Pattern - Wind"))

        world.set_rule(world.get_entrance("Lost Landing - Warp Entrance"),
                       Has("Warp Pattern - Lost"))
                    #    | ([OptionFilter(WarpsInLogic, WarpsInLogic.option_true),
                    #        OptionFilter(ShuffleMeteorites, ShuffleMeteorites.option_false)]
                    #       & CanReachRegion("Lost Landing - Staircase")

        world.set_rule(world.get_entrance("Ancient Cavern - Warp Entrance"),
                       Has("Warp Pattern - Ancient"))
                    #    | ([OptionFilter(WarpsInLogic, WarpsInLogic.option_true),
                    #        OptionFilter(ShuffleMeteorites, ShuffleMeteorites.option_false)]
                    #       & CanReachRegion("Ancient Cavern - South")

        world.set_rule(world.get_entrance("Totem - Warp Entrance"),
                       Has("Warp Pattern - Compass"))
                    #    | ([OptionFilter(WarpsInLogic, WarpsInLogic.option_true),
                    #        OptionFilter(ShuffleMeteorites, ShuffleMeteorites.option_false)]
                    #       & CanReachRegion("Lost Landing - Compass")

        if world.options.circlet_content_enabled: # Phoenix Egg meteorite requires the serpent circlet
            world.set_rule(world.get_entrance("Forgotten Lagoon - Phoenix Entrance"),
                           Has("Serpent Circlet")
                           & CanReachRegion("Ancient Isle - Origin")
                           & CanReachRegion("Sunken Island - Turtle")
                           & Has("Frog Flippers")
                           & CanReachRegion("Aggro Crag - South-West")
                           & CanReachRegion("Sanctum")
                           & Has("Ancient Key", 51)
                           & CanReachRegion("Lost Landing - Turtle")
                           & CanReachRegion("Star Tropic - East")
                           & CanReachRegion("Phoenix Hub")) # Phoenix Flute is also mandatory to turn in the eggs

            world.set_rule(world.get_entrance("Forgotten Lagoon - Meteorite to North"),
                           Has("Frog Flippers"))

    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Overworld - Star Lock 3"),
                       Has("Star Piece", 3))
        world.set_rule(world.get_location("Overworld - Star Lock 15"),
                       Has("Star Piece", 15))
        world.set_rule(world.get_location("Overworld - Star Lock 30"),
                       Has("Star Piece", 30))
        world.set_rule(world.get_location("Overworld - Star Lock 45"),
                       Has("Star Piece", 45))


    ### Locations

    # Legendary Item Locations

    world.set_rule(world.get_location("Water A4 - Frog Flippers"),
                   CanReachRegion("Tidal Reef - God Altar")
                   & CanReachRegion("Tidal Reef - East")
                   & CanReachRegion("Tidal Reef - Shell Puzzle")
                   & CanReachRegion("Tidal Reef - Phoenix")
                   & CanReachRegion("Tidal Reef - North-West")
    )

    world.set_rule(world.get_location("Fire E0 - Salamander Shirt"),
                   Has("Fire Key", 3))

    world.set_rule(world.get_location("Wind A0 - Kite Cloak"),
                   Has("Awaken Wind Elementals")
                   | Has("Kite Cloak"))  # since Eggs and Wind key are broken, don't include

    # Quests
    world.set_rule(world.get_location("Stone C0 - Topaz Quest Complete"),
                   Has("Topaz", 6))

    world.set_rule(world.get_location("Water C0 - Sapphire Quest Complete"),
                   Has("Sapphire", 6))

    world.set_rule(world.get_location("Fire C0 - Ruby Quest Complete"),
                   Has("Ruby", 6))

    world.set_rule(world.get_location("Wind C2 - Diamond Quest Complete"),
                   Has("Diamond", 6))

    world.set_rule(world.get_location("Serpent A1 - Obsidian Quest Complete"),
                   Has("Obsidian Rune Stone")
                   & Has("Obsidian", 9))

    # Islands and their Locations
    set_ancient_isle(world)
    set_rolling_rocks(world)
    set_sunken_island(world)
    set_aggro_crag(world)
    set_sea_nunatak(world)
    set_locked_key(world)
    set_star_tropic(world)
    set_eastern_shoal(world)
    set_lost_landing(world)


    set_stony_cliffs(world)
    set_tidal_reef(world)
    set_raging_volcano(world)
    set_frozen_spire(world)
    set_serpent_stacks(world)
    set_beast_bridge(world)
    set_sanctum(world)

    set_mysterious(world)
    set_meteorites(world)


def set_ancient_isle(world: "IslesOfSeaAndSkyWorld"):

    # Ancient Keys
    world.set_rule(world.get_location("Ancient A1 - Star Piece"),
                   Has("Ancient Key", 17))

    world.set_rule(world.get_location("Ancient B1 - Star Piece"),
                   Has("Ancient Key", 17)
                   & Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Ancient A2 - NW - Ancient Key"),
                   Has("Awaken Earth Elementals"))  # and CanReachRegion("Topaz Sea")

    # Sphere 1 checks
    '''world.set_rule(world.get_location("Ancient A1 - Ancient Key"),
                   Has("Ancient Key"))

    world.set_rule(world.get_location("Ancient A2 - SE - Ancient Key"),
                   Has("Ancient Key"))

    world.set_rule(world.get_location("Ancient A3 - N - Ancient Key"),
                   Has("Ancient Key", 2))
    world.set_rule(world.get_location("Ancient A3 - S - Ancient Key"),
                   Has("Ancient Key"))
    world.set_rule(world.get_location("Ancient A3 - E - Ancient Key"),
                   Has("Ancient Key", 2))

    world.set_rule(world.get_location("Ancient C2 - Ancient Key"),
                   Has("Ancient Key", 3))
    world.set_rule(world.get_location("Ancient C3 - Ancient Key"),
                   Has("Ancient Key", 3))
    world.set_rule(world.get_location("Ancient C1 - Ancient Key"),
                   Has("Star Piece")
                   & Has("Ancient Key", 6))

    world.set_rule(world.get_location("Ancient C0 - Star Piece"),
                   Has("Ancient Key", 6))'''

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Ancient A1 - 3x Lock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 17))

        world.set_rule(world.get_location("Ancient B3 - Lock"),
                       Has("Ancient Key", 1))

        world.set_rule(world.get_location("Ancient A3 - Lock"),
                       Has("Ancient Key", 2))

        world.set_rule(world.get_location("Ancient B2 - Lock"),
                       Has("Ancient Key", 3))

        world.set_rule(world.get_location("Ancient C2 - 3x Lock"),
                       Has("Ancient Key", 6))

        world.set_rule(world.get_location("Ancient C1 - Star Lock 1"),
                       Has("Star Piece")
                       & Has("Ancient Key", 6))

        world.set_rule(world.get_location("Ancient B1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Ancient B3 - Snakeblock"),
                       Has("Ancient Key"))

        world.set_rule(world.get_location("Ancient B2 - W - Snakeblock"),
                       Has("Ancient Key"))

        world.set_rule(world.get_location("Ancient A3 - Snakeblock"),
                       Has("Ancient Key", 2))

        world.set_rule(world.get_location("Ancient B2 - E - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - E - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - S - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - W - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C3 - Snakeblock"),
                       Has("Ancient Key", 3))

        world.set_rule(world.get_location("Ancient A1 - Snakeblock"),
                       CanReachRegion("Obsidian Sea"))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Ancient A1 - Discover Secret"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 17))


def set_rolling_rocks(world: "IslesOfSeaAndSkyWorld"):

    # - - - - - - - - - -
    # Topaz
    world.set_rule(world.get_location("Rolling A0 - Topaz"),
                   Has("Star Piece", 7)
                   & Has("Awaken Earth Elementals"))

    # - - - - - - - - - -
    # Obsidian
    world.set_rule(world.get_location("Rolling A1 - Obsidian"),
                   Has("Star Piece", 7)
                   & Has("Gopher Gloves")
                   & Has("Awaken Earth Elementals"))

    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Rolling A0 - Star Piece"),
                   Has("Star Piece", 7)
                   & (Has("Awaken Earth Elementals") | Has("Frog Flippers")))


    world.set_rule(world.get_location("Rolling B0 - Star Piece"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Rolling B1 - Star Piece"),
                   Has("Ancient Key", 14))
    
    # - - - - - - - - - -
    # Big Bell
    world.set_rule(world.get_location("Rolling B0 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Rolling"))
                   


    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Rolling B1 - 3x Lock"),
                       Has("Ancient Key", 14))

        world.set_rule(world.get_location("Rolling A0 - Star Lock 7"),
                       Has("Star Piece", 7))


    if False: # world.options.enable_snakesanity:
        pass

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Rolling A0 - Discover Secret"),
                       Has("Star Piece", 7)
                       & Has("Gopher Gloves"))


def set_sunken_island(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Sapphire
    world.set_rule(world.get_location("Sunken B0 - Sapphire"),
                   Has("Star Piece", 21)
                   & Has("Awaken Water Elementals"))
    # - - - - - - - - - -
    # Obsidian
    world.set_rule(world.get_location("Sunken A0 - Obsidian"),
                   Has("Frog Flippers"))
    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Sunken B0 - Star Piece"),
                   Has("Star Piece", 21)
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Sunken A1 - Star Piece"),
                   Has("Ancient Key", 34)
                   & Has("Ancient Rune Stone"))
    
    # - - - - - - - - - -
    # Big Bell
    world.set_rule(world.get_location("Sunken B1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_location("Sunken B1 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Sunken"))


    # Locksanity
    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Sunken A1 - 3x Lock"),
                       Has("Ancient Key", 34)
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Sunken B0 - Star Lock 21"),
                       Has("Star Piece", 21))

        world.set_rule(world.get_location("Sunken A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Sunken B1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))


def set_aggro_crag(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Ruby
    world.set_rule(world.get_location("Aggro B1 - Ruby"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals"))
    
    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Aggro A1 - Star Piece"),
                   Has("Ancient Key", 42))
    world.set_rule(world.get_location("Aggro B1 - Star Piece"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals"))
    # - - - - - - - - - -
    # Big Bell
    world.set_rule(world.get_location("Aggro A1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_location("Aggro A1 - Big Bell Star Piece"),
                       Has("Big Bell Hit - Aggro"))


    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Aggro A1 - 3x Lock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone")
                       & Has("Ancient Key", 42))

        world.set_rule(world.get_location("Aggro B0 - Star Lock 35"),
                       Has("Star Piece", 35))

        world.set_rule(world.get_location("Aggro B1 - Ancient Rune Lock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Aggro A1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Aggro B1 - E - Snakeblock"),
                       Has("Star Piece", 35))

        world.set_rule(world.get_location("Aggro B1 - W - Snakeblock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Aggro B0 - W - Snakeblock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone")
                       & Has("Salamander Shirt"))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Aggro A0 - W - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Salamander Shirt"))

        world.set_rule(world.get_location("Aggro A0 - E - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Salamander Shirt"))


def set_sea_nunatak(world: "IslesOfSeaAndSkyWorld"):

    # - - - - - - - - - -
    # Ancient Key
    world.set_rule(world.get_location("Nunatak A1 - Ancient Key"),
                   Has("Ancient Rune Stone")
                   & Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))
    # - - - - - - - - - -
    # Diamond
    world.set_rule(world.get_location("Nunatak B0 - Diamond"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))
    # - - - - - - - - - -
    # Obsidian
    world.set_rule(world.get_location("Nunatak B1 - Obsidian"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49)
                   & Has("Kite Cloak"))
    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Nunatak B0 - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))

    world.set_rule(world.get_location("Nunatak A0 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Ancient Key", 26))
    # - - - - - - - - - -
    # Big Bell    
    world.set_rule(world.get_location("Nunatak A1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))
    world.set_rule(world.get_location("Nunatak A1 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Nunatak"))
    
    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Nunatak A0 - 3x Lock"),
                       Has("Ancient Rune Stone")
                       & Has("Ancient Key", 26))

        world.set_rule(world.get_location("Nunatak B0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Nunatak B0 - Star Lock 49"),
                       Has("Star Piece", 49))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Nunatak A1 - Snakeblock"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Nunatak B0 - E - Discover Secret"),
                       Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49)
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Nunatak B0 - SE - Discover Secret"),
                       Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49)
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Nunatak B0 - CW - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))
        world.set_rule(world.get_location("Nunatak B0 - W - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))


def set_locked_key(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Special Items
    world.set_rule(world.get_location("Locked A0 - Ancient Rune Stone"),
                   (CanReachRegion("Ruby Sea")
                    | CanReachRegion("Sapphire Sea"))
                   & Has("Ancient Key", 23))  # Makes this 'unreachable'

    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Locked A0 - Star Piece"),
                   Has("Ancient Rune Stone"))

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Locked A0 - 6x Lock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))

        world.set_rule(world.get_location("Locked A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Locked A0 - E - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))
        world.set_rule(world.get_location("Locked A0 - C - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))
        world.set_rule(world.get_location("Locked A0 - W - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))


def set_star_tropic(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Gems
    world.set_rule(world.get_location("Tropic A1 - Topaz"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Sapphire"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Ruby"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Diamond"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))
    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Tropic A1 - Star Piece 1"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Tropic A1 - Star Piece 2"),
                   Has("Gopher Gloves")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Tropic A1 - Star Piece 3"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Tropic A1 - Star Piece 4"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic B0 - N - Star Piece"),
                   Has("Obsidian Rune Stone"))


    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Tropic A1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Tropic B0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Tropic B0 - Obsidian Rune Lock"),
                       Has("Obsidian Rune Stone")
                       & Has("Kite Cloak"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Tropic A0 - W - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic A0 - C - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic A0 - E - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic B0 - N - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic B0 - S - Snakeblock"),
                       Has("Kite Cloak"))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Tropic A0 - Discover Secret"),
                       Has("Kite Cloak"))


def set_eastern_shoal(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Special Items
    world.set_rule(world.get_location("Shoal A0 - Star Viewing Orb"),
                   Has("Ancient Rune Stone"))

    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Shoal A0 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Frog Flippers")
                   & Has("Kite Cloak"))
    

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Shoal A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:

        world.set_rule(world.get_location("Shoal A0 - Snakeblock"),
                       Has("Ancient Rune Stone")
                       & Has("Kite Cloak"))

    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Shoal A0 - E - Discover Secret"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Shoal A0 - SE - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Frog Flippers")
                       & Has("Kite Cloak"))


def set_lost_landing(world: "IslesOfSeaAndSkyWorld"):
    # - - - - - - - - - -
    # Obsidian
    world.set_rule(world.get_location("Lost A1 - Obsidian"),
                   Has("Ancient Key", 48))

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Lost A1 - Lock"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers")
                       & Has("Ancient Key", 48))

        world.set_rule(world.get_location("Lost B0 - Star Lock 30"),
                       Has("Star Piece", 30))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Lost B1 - Snakeblock"),
                       Has("Star Piece", 30))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Lost B1 - CS - Discover Secret"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers"))

        world.set_rule(world.get_location("Lost B1 - W - Discover Secret"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers"))


def set_serpent_stacks(world: "IslesOfSeaAndSkyWorld"):

    # Head: Requires all 4 elemental runes
    world.set_rule(world.get_location("Serpent A1 - Obsidian"),
                   Has("Obsidian Rune Stone"))

    world.set_rule(world.get_location("Serpent A1 - W - Star Piece"),
                   Has("Obsidian Rune Stone")
                   & Has("Awaken Shadow Elementals"))

    world.set_rule(world.get_location("Serpent A1 - N - Star Piece"),
                   Has("Obsidian Rune Stone")
                   & Has("Awaken Shadow Elementals"))

    # Entrance
    world.set_rule(world.get_location("Serpent A2 - Star Piece"),
                   Has("Awaken Shadow Elementals"))

    # Post-Rune: Requires Obsidian Rune
    # Core: Requires Shadow Elementals and Earth Elementals
    world.set_rule(world.get_location("Serpent A6 - W - Star Piece"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Serpent A6 - E - Star Piece"),
                   Has("Awaken Water Elementals"))
    

    # Tail: Requires Water Elementals or Fire Elementals with Kite Cloak
    world.set_rule(world.get_location("Serpent A7 - W - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Serpent A7 - E - Star Piece"),
                   Has("Awaken Fire Elementals"))
    

    world.set_rule(world.get_location("Serpent A8 - N - Star Piece"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Serpent A8 - S - Star Piece"),
                   Has("Awaken Wind Elementals"))
    
    
    if world.options.circlet_content_enabled:
        world.set_rule(world.get_location("Serpent A4 - Serpent Lock Shard"),
                    Has("Awaken Earth Elementals")
                    & Has("Gopher Gloves"))
        world.set_rule(world.get_location("Serpent A6 - Serpent Lock Shard"),
                    Has("Awaken Water Elementals")
                    | Has("Kite Cloak"))
        world.set_rule(world.get_location("Serpent A7 - Serpent Lock Shard"),
                    Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Serpent A8 - Serpent Lock Shard"),
                    Has("Awaken Wind Elementals"))
        # Serpent Lock: Requires 4 serpent lock shards at the Serpent Core
        world.set_rule(world.get_location("Serpent A5 - Serpent Circlet"),
                    Has("Serpent Lock Shard", 8))

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Serpent A2 - Elemental Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - N - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - W - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - E - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone")
                       & Has("Awaken Shadow Elementals"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Serpent A1 - C - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A1 - CE - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A1 - E - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A6 - SW - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - NW - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - C - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - E - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A8 - Snakeblock"),
                       Has("Awaken Shadow Elementals")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals")
                       & Has("Awaken Fire Elementals")
                       & Has("Awaken Wind Elementals"))


def set_stony_cliffs(world: "IslesOfSeaAndSkyWorld"):

    # - - - - - - - - - -
    # Ancient Keys
    world.set_rule(world.get_location("Stone B0 - NW1 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   & Has("Ancient Key", 11))
    world.set_rule(world.get_location("Stone B0 - NW2 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   & Has("Ancient Key", 11))
    world.set_rule(world.get_location("Stone B0 - NW3 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   & Has("Ancient Key", 11))

    world.set_rule(world.get_location("Stone B4 - Ancient Key"),
                   Has("Awaken Earth Elementals"))  # There is a clever solution get this without gopher gloves

    world.set_rule(world.get_location("Stone C0 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   | Has("Kite Cloak"))

    world.set_rule(world.get_location("Stone D3 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   & Has("Gopher Gloves"))
    
    world.set_rule(world.get_location("Stone E2 - Ancient Key"),
                   Has("Topaz Rune Stone")
                   & Has("Ruby Rune Stone"))

    world.set_rule(world.get_location("Stone Dungeon B1 - Ancient Key"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone Dungeon C1 - Ancient Key"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone Dungeon D0 - Ancient Key"),
                   Has("Gopher Gloves"))
    # - - - - - - - - - -
    # Topaz
    world.set_rule(world.get_location("Stone B0 - Topaz"),
                   Has("Ancient Key", 11))
    
    world.set_rule(world.get_location("Stone C0 - Topaz"),
                   Has("Topaz Rune Stone"))

    world.set_rule(world.get_location("Stone C2 - E - Topaz"),
                   Has("Ancient Key", 7))

    world.set_rule(world.get_location("Stone Dungeon C1 - Topaz"),
                   Has("Gopher Gloves"))

    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Stone B2 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone B4 - Star Piece"),
                   Has("Awaken Earth Elementals"))  # Gloves also not needed

    world.set_rule(world.get_location("Stone C0 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone C1 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone C4 - Star Piece"),
                   Has("Awaken Earth Elementals")
                   & Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone D3 - N - Star Piece"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Wind Elementals")
                   & Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone D3 - S - Star Piece"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Stone E1 - Star Piece"),
                   Has("Ancient Key", 10))

    world.set_rule(world.get_location("Stone Dungeon B1 - Star Piece"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone Dungeon C1 - Star Piece"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone Dungeon E1 - Star Piece"),
                   Has("Awaken Earth Elementals")
                    # Kite Cloak lets you reach an alternate entrance that skips this puzzle
                   | CanReachEntrance("Stony Cliffs - God Altar East Cavern Entrance"))

    world.set_rule(world.get_location("Stone Dungeon E2 - Star Piece"),
                   Has("Gopher Gloves")
                   & Has("Frog Flippers"))

    # - - - - - - - - - -
    # Tablets
    world.set_rule(world.get_location("Stone E3 - Gold Stone Tablet"),
                   CanReachRegion("Stone Dungeon - South Tunnels")
                   & CanReachRegion("Stone Dungeon - West Tunnels")
                   & CanReachRegion("Stone Dungeon Earth Chamber"))
    world.set_rule(world.get_location("Stone Dungeon A1 - Blue Stone Tablet"),
                    CanReachRegion("Stony Cliffs - Phoenix")
                    & CanReachRegion("Stony Cliffs - Tablet Slot")
                    & CanReachRegion("Stony Cliffs - North-East")
                    & Has("Star Piece", 20))

    # - - - - - - - - - -
    # Topaz Door
    world.set_rule(world.get_location("Stone Dungeon C2 - Open Topaz Door"),
                   CanReachRegion("Stony Cliffs - North-East")
                   & CanReachRegion("Stony Cliffs - South-West")
                   & CanReachRegion("Stony Cliffs - South-East"))
    
    
    # - - - - - - - - - -
    # Tablet Puzzle
    world.set_rule(world.get_location("Stone A2 - Tablet Puzzle Star Piece"),
                    Has("Blue Stone Tablet")
                    & Has("Gold Stone Tablet"))
    world.set_rule(world.get_location("Stone A2 - Ancient Key"),
                   Has("Blue Stone Tablet")
                   & Has("Gold Stone Tablet"))
    world.set_rule(world.get_location("Stone A2 - Obsidian"),
                   Has("Blue Stone Tablet")
                   & Has("Gold Stone Tablet"))

    # - - - - - - - - - -
    # Music Puzzle
    locations = [
        world.get_location("Stone D1 - Music Puzzle Star Piece 1"),
        world.get_location("Stone D1 - Music Puzzle Star Piece 2"),
        world.get_location("Stone D1 - Music Puzzle Star Piece 3")
    ]
    rules = (Has("Awaken Earth Elementals")
            & ( ([OptionFilter(ShuffleNotes, ShuffleNotes.option_true)] & Has("Music Note", 6))
                | ([OptionFilter(ShuffleNotes, ShuffleNotes.option_false)] & Has("Ancient Key", 11)
                   & CanReachRegion("Stony Cliffs - Phoenix") & CanReachRegion("Stony Cliffs - South Coast"))
                )
            )
    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules

    # Notesanity
    if world.options.shuffle_notes:
        world.set_rule(world.get_location("Stone B0 - Music Note"),
                       Has("Ancient Key", 11))

        world.set_rule(world.get_location("Stone D1 - Music Note"),
                       Has("Awaken Earth Elementals"))

    # Locksanity
    if False: # world.options.enable_locksanity:

        world.set_rule(world.get_location("Stone C2 - Lock"),
                       Has("Ancient Key", 7))

        world.set_rule(world.get_location("Stone E1 - 3x Lock"),
                       Has("Ancient Key", 10))

        world.set_rule(world.get_location("Stone B1 - Lock"),
                       Has("Ancient Key", 11))

        world.set_rule(world.get_location("Stone A1 - Star Lock 5"),
                       Has("Star Piece", 5))

        world.set_rule(world.get_location("Stone C4 - Star Lock 15"),
                       Has("Star Piece", 15)
                       & Has("Awaken Earth Elementals"))

        world.set_rule(world.get_location("Stone E3 - Star Lock 20"),
                       Has("Star Piece", 20))

        world.set_rule(world.get_location("Stone Dungeon A1 - Star Lock 20"),
                       Has("Star Piece", 20)
                       & Has("Gopher Gloves"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Stone C1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone D1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone E1 - E - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone C4 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon C4 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon C3 - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon B2 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - CE - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - W - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - CW - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - W - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - CS - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon E1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon E2 - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))


        world.set_rule(world.get_location("Stone Dungeon C1 - Snakeblock"),
                       Has("Gopher Gloves")
                       & (CanReachRegion("Stony Cliffs NW")
                          | (CanReachRegion("Stony Cliffs Post-Rune")
                             & Has("Topaz Rune Stone"))))

        world.set_rule(world.get_location("Stone B4 - Snakeblock"),
                       Has("Star Piece", 15)
                       & Has("Gopher Gloves"))
        world.set_rule(world.get_location("Stone A4 - E - Snakeblock"),
                       Has("Star Piece", 15)
                       & Has("Gopher Gloves")
                       & Has("Awaken Earth Elementals"))

    # Secretsanity
    if False: # world.options.secretsanity:
        pass


def set_tidal_reef(world: "IslesOfSeaAndSkyWorld"):

    # - - - - - - - - - -
    # Ancient Keys
    world.set_rule(world.get_location("Water A0 - S - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water A2 - Ancient Key"),
                   Has("Awaken Water Elementals")
                   & (Has("Kite Cloak")
                      | Has("Star Piece", 30)
                     ))

    world.set_rule(world.get_location("Water B3 - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water C0 - Ancient Key"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water C3 - W - Ancient Key"),
                   Has("Sapphire Rune Stone")
                   & Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Water C3 - NE1 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))
    world.set_rule(world.get_location("Water C3 - NE2 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))
    world.set_rule(world.get_location("Water C3 - NE3 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D0 - Ancient Key"),
                   Has("Sapphire Rune Stone")
                   & Has("Frog Flippers"))

    world.set_rule(world.get_location("Water D1 - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water D2 - Ancient Key"),
                   Has("Sapphire Rune Stone")
                   & Has("Awaken Water Elementals"))

    # - - - - - - - - - -
    # Sapphires
    world.set_rule(world.get_location("Water A1 - Sapphire"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water B2 - S - Sapphire"),
                   Has("Ancient Key", 29))

    world.set_rule(world.get_location("Water C0 - Sapphire"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_location("Water C2 - N - Sapphire"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D2 - N - Sapphire"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_location("Water D3 - Sapphire"),
                       Has("Ancient Key", 33))

    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Water A2 - S - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Frog Flippers"))

    world.set_rule(world.get_location("Water A4 - Star Piece"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water B1 - Star Piece"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water C0 - Star Piece"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water C1 - W - Star Piece"),
                   Has("Ancient Key", 32))

    world.set_rule(world.get_location("Water C2 - Star Piece"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D2 - Star Piece"),
                   Has("Frog Flippers")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Water D3 - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Ancient Key", 33))

    world.set_rule(world.get_location("Water E0 - W - Star Piece"),
                   Has("Awaken Water Elementals")
                   | Has("Kite Cloak"))

    world.set_rule(world.get_location("Water E0 - E - Star Piece"),
                    Has("Frog Flippers")
                    & Has ("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water E2 - Star Piece"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water E3 - NE - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Water E3 - SW - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Awaken Earth Elementals"))

    # - - - - - - - - - -
    # Shell Puzzle
    locations = [
        world.get_location("Water C4 - Shell Puzzle Star Piece"),
        world.get_location("Water C4 - Ancient Key"),
        world.get_location("Water C4 - Obsidian")
    ]
    # TODO: tighten logic, what regions do shells exist in?
    # Similar to Ice Spire Albatrosses, we want to eventually be able to calculate
    # where the shells are placed on the server to account for them in logic perfectly.
    rules = (Has("Frog Flippers")
             & Has("Sapphire Rune Stone"))  
    
    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules

    # - - - - - - - - - -
    # Music Puzzle
    locations = [
        world.get_location("Water B0 - Music Puzzle Star Piece 1"),
        world.get_location("Water B0 - Music Puzzle Star Piece 2"),
        world.get_location("Water B0 - Music Puzzle Star Piece 3")
    ]
    rules = (Has("Awaken Water Elementals") # Mandator
             & (
                 Has("Music Note", 12)) # Music notes needed if notesanity is off
                 | ( # Music note regions must be reachable if notesanity is on
                     [OptionFilter(ShuffleNotes, ShuffleNotes.option_false)]
                     & (Has("Sapphire Rune Stone") | Has("Frog Flippers"))
                        & CanReachRegion("Tidal Reef - North-West Low Tide")
                        & CanReachRegion("Tidal Reef - East")
    ))

    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules

    # - - - - - - - - - -
    # Notes
    if world.options.shuffle_notes:
        world.set_rule(world.get_location("Water A2 - Music Note"),
                    Has("Sapphire Rune Stone") | Has("Frog Flippers"))

    # IncludeShells
    if False: # world.options.include_seashells:

        world.set_rule(world.get_location("Water B2 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water B3 - Shell"),
                       Has("Frog Flippers")
                       | Has("Phoenix Flute")
                       | Has("Sapphire Rune Stone"))


        world.set_rule(world.get_location("Water B0 - Shell"),
                       Has("Awaken Water Elementals"))

        world.set_rule(world.get_location("Water D1 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A4 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water D0 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A2 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A3 - Shell"),
                       Has("Frog Flippers")
                       | Has("Sapphire Rune Stone"))

    # Locksanity
    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Water B2 - Lock"),
                       Has("Ancient Key", 29))

        world.set_rule(world.get_location("Water C1 - 3x Lock"),
                       Has("Ancient Key", 32))

        world.set_rule(world.get_location("Water D3 - Lock"),
                       Has("Ancient Key", 33))

        world.set_rule(world.get_location("Water A2 - Star Lock 30"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals"))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Water B0 - E - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B0 - C - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B1 - C - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B1 - SE - Snakeblock"),
                       Has("Awaken Water Elementals") | Has("Kite Cloak"))


        world.set_rule(world.get_location("Water D2 - C - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water D2 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water D3 - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water E1 - W - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water E1 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water E2 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water A0 - S - Snakeblock"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A2 - Snakeblock"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals")
                       & Has("Star Piece", 30))

        world.set_rule(world.get_location("Water A3 - Snakeblock"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals")
                       & Has("Star Piece", 30))


def set_raging_volcano(world: "IslesOfSeaAndSkyWorld"):
    
    # - - - - - - - - - -
    # Ancient Keys
    world.set_rule(world.get_location("Fire A1 - SE - Ancient Key"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire A1 - SW - Ancient Key"),
                   Has("Ruby Rune Stone")
                   & Has("Topaz Rune Stone"))

    world.set_rule(world.get_location("Fire A2 - S - Ancient Key"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire B1 - N1 - Ancient Key"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Fire B1 - N2 - Ancient Key"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Fire B1 - N3 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire B4 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C0 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C1 - NE - Ancient Key"),
                   Has("Awaken Fire Elementals")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire C1 - SW - Ancient Key"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire C3 - Ancient Key"),
                   Has("Ruby Rune Stone")
                   & Has("Awaken Fire Elementals"))

    # - - - - - - - - - -
    # Ruby
    world.set_rule(world.get_location("Fire A3 - NW - Ruby"),
                   Has("Ancient Key", 39))

    world.set_rule(world.get_location("Fire C0 - Ruby"),
                   Has("Ruby Rune Stone"))

    world.set_rule(world.get_location("Fire D0 - Ruby"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire D1 - Ruby"),
                   Has("Ruby Rune Stone")
                   | CanReachEntrance("Raging Volcano - God Altar to Phoenix"))

    world.set_rule(world.get_location("Fire D2 - W - Ruby"),
                   Has("Ancient Key", 35))

    # - - - - - - - - - -
    # Obsidian
    world.set_rule(world.get_location("Fire E0 - Obsidian"),
                   Has("Salamander Shirt"))

    # - - - - - - - - - -
    # Star Pieces

    world.set_rule(world.get_location("Fire B4 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C0 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C1 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire D1 - N - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire D1 - S - Star Piece"),
                   Has("Ancient Key", 38))

    world.set_rule(world.get_location("Fire D3 - W - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire D3 - S - Star Piece"),
                   Has("Awaken Fire Elementals") & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire D4 - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Fire E0 - Star Piece"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire E1 - W - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire E1 - E - Star Piece"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire E3 - S - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Fire E3 - SE - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Awaken Water Elementals"))

    # - - - - - - - - - -
    # Idol Puzzle
    locations = [
        world.get_location("Fire D4 - Ancient Key"),
        world.get_location("Fire D4 - Obsidian"),
        world.get_location("Fire D4 - Idol Puzzle Star Piece")
    ]
    # TODO: Server side puzzle generation to account for idol positions in logic
    rules = (
        CanReachRegion("Raging Volcano - God Altar")
        & CanReachRegion("Raging Volcano - Phoenix")
        & CanReachRegion("Raging Volcano - Hot Spring")
        & CanReachRegion("Raging Volcano - Below Hot Spring")
        & CanReachRegion("Raging Volcano - Lyre")
        & CanReachRegion("Raging Volcano - North-West")
        & (CanReachRegion("Raging Volcano - North-West Pass")
           | CanReachRegion("Raging Volcano - Geyser Pass"))
    )
    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules

    # - - - - - - - - - -
    # Music Puzzle
    locations = [
        world.get_location("Fire B3 - Music Puzzle Star Piece 1"),
        world.get_location("Fire B3 - Music Puzzle Star Piece 2"),
        world.get_location("Fire B3 - Music Puzzle Star Piece 3")
    ]
    rules = (
        Has("Awaken Fire Elementals")
        & (Has("Music Note", 18)
           | ([OptionFilter(ShuffleNotes, ShuffleNotes.option_false)]
              & CanReachRegion("Raging Volcano - God Altar")
              & CanReachRegion("Raging Volcano - Key Triplets")
              & CanReachRegion("Raging Volcano - Lyre")
              & CanReachRegion("Raging Volcano - Idol Room West")
              & CanReachRegion("Raging Volcano - Below Hot Spring")
              & CanReachRegion("Raging Volcano - Hot Spring")
              )
        ))
    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules

    # Locksanity
    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Fire D2 - Lock"),
                       Has("Ancient Key", 35))

        world.set_rule(world.get_location("Fire D2 - 3x Lock"),
                       Has("Ancient Key", 38))

        world.set_rule(world.get_location("Fire A3 - Lock"),
                       Has("Ancient Key", 39))

        world.set_rule(world.get_location("Fire E0 - 3x Lock (Fire)"),
                       Has("Fire Key", 3))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Fire B4 - W - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B4 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - CW - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - W - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - CE - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire C3 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))


        world.set_rule(world.get_location("Fire D1 - SE - Snakeblock"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire D1 - SW - Snakeblock"),
                       Has("Ancient Key", 38))
        world.set_rule(world.get_location("Fire B1 - Snakeblock"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire D3 - W - Snakeblock"),
                       Has("Salamander Shirt"))

        world.set_rule(world.get_location("Fire D3 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire D3 - SW - Snakeblock"),
                       Has("Awaken Fire Elementals"))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Fire C2 - Discover Secret"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire E1 - Discover Secret"),
                       Has("Salamander Shirt"))


def set_frozen_spire(world: "IslesOfSeaAndSkyWorld"):

    # - - - - - - - - - -
    # Ancient Keys
    world.set_rule(world.get_location("Wind A3 - Ancient Key"),
                   Has("Kite Cloak") | Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind C2 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D3 - Ancient Key"),
                   Has("Kite Cloak"))
    world.set_rule(world.get_location("Wind D4 - NW1 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D4 - NW2 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D4 - NW3 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D4 - E - Ancient Key"),
                   Has("Sapphire Rune Stone"))
    world.set_rule(world.get_location("Wind E2 - NE - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind E2 - S - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind E4 - E - Ancient Key"),
                   Has("Awaken Wind Elementals")
                   & Has("Kite Cloak"))
    world.set_rule(world.get_location("Wind E4 - SW - Ancient Key"),
                   Has("Awaken Wind Elementals")
                   & Has("Kite Cloak"))
    
    # - - - - - - - - - -
    # Diamond
    world.set_rule(world.get_location("Wind C3 - Diamond"),
                   Has("Awaken Wind Elementals")
                   & Has("Ancient Key", 46))
    world.set_rule(world.get_location("Wind D1 - E - Diamond"),
                   (Has("Kite Cloak")
                   | Has("Awaken Wind Elementals"))
                    & Has("Ancient Key", 47))
    
    # - - - - - - - - - -
    # Star Pieces
    world.set_rule(world.get_location("Wind A0 - Star Piece"),
                   Has("Kite Cloak"))
    world.set_rule(world.get_location("Wind A3 - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind B1 - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind B2 - N - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind B2 - S - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind B3 - Star Piece"),
                   Has("Kite Cloak")
                   & Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind C2 - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind C3 - NE - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D2 - Star Piece"),
                   Has("Kite Cloak"))
    world.set_rule(world.get_location("Wind D4 - Star Piece"),
                   Has("Ancient Key", 45))
    world.set_rule(world.get_location("Wind E1 - W - Star Piece"),
                   Has("Kite Cloak")
                   & Has("Gopher Gloves")
                   & Has("Ancient Key", 47))
                
    world.set_rule(world.get_location("Wind E1 - SE - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Wind E1 - SW - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Wind E2 - Star Piece"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind E4 - Star Piece"),
                   Has("Awaken Wind Elementals"))
    
    # - - - - - - - - - -
    # Music Puzzle
    locations = [
        world.get_location("Wind B4 - Music Puzzle Star Piece 1"),
        world.get_location("Wind B4 - Music Puzzle Star Piece 2"),
        world.get_location("Wind B4 - Music Puzzle Star Piece 3")
    ]
    rules = (
        Has("Awaken Wind Elementals")
        & ([OptionFilter(ShuffleNotes, ShuffleNotes.option_false)] | Has("Music Note", 24))
    )
    for i in range(0,3): world.set_rule(locations[i], rules);
    del locations; del rules
                   

    # Notesanity
    if world.options.shuffle_notes:
        world.set_rule(world.get_location("Wind B1 - Music Note"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind D3 - Music Note"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind E3 - Music Note"),
                       Has("Awaken Wind Elementals"))

    # TODO: Implement Eggs and Ice Key randomization
    # This will involve calculating egg placements on the server side
    
    # Locksanity
    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Wind D3 - 3x Lock"),
                       Has("Ancient Key", 45))

        world.set_rule(world.get_location("Wind C3 - Lock"),
                       Has("Ancient Key", 46)
                       & Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind D1 - Lock"),
                       Has("Ancient Key", 47))

        world.set_rule(world.get_location("Wind A0 - Lock (Wind)"),
                       Has("Diamond Rune Stone"))  # Remove later when wind key item is fixed

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Wind A2 - SE - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind E4 - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind E3 - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind C2 - Snakeblock"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind B3 - CE - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Wind B3 - NE - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Wind B2 - SW - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind B4 - Snakeblock"),
                       Has("Kite Cloak"))

        world.set_rule(world.get_location("Wind E1 - Snakeblock"),
                       Has("Gopher Gloves")
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Wind D4 - Snakeblock"),
                       Has("Ancient Key", 45))

    # Secretsanity
    if False: # world.options.secretsanity:
        world.set_rule(world.get_location("Wind D1 - Discover Secret"),
                       Has("Kite Cloak")
                       & Has("Ancient Key", 47))


def set_beast_bridge(world: "IslesOfSeaAndSkyWorld"):
    world.set_rule(world.get_location("Beast A1 - Big Bell Stone"),
                   Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))


def set_sanctum(world: "IslesOfSeaAndSkyWorld"):
    # Assume we have all 4 elementals
    world.set_rule(world.get_location("Sanctum A2 - Topaz Shard Hit"),
                   Has("Ancient Key", 51))

    world.set_rule(world.get_location("Sanctum C2 - Sapphire Shard Hit"),
                   Has("Ancient Key", 54))

    world.set_rule(world.get_location("Sanctum A0 - Diamond Shard Hit"),
                   Has("Ancient Key", 57))
    # You can get this one by taking the secret passage from Sanctum B1
    # world.set_rule(world.get_location("Sanctum C0 - Ruby Shard Hit"),
    #                Has("Ancient Key", 60))


    # Locksanity
    if False: # world.options.enable_locksanity:
        world.set_rule(world.get_location("Sanctum B2 - W - 3x Lock"),
                       Has("Ancient Key", 51))

        world.set_rule(world.get_location("Sanctum B2 - E - 3x Lock"),
                       Has("Ancient Key", 54))

        world.set_rule(world.get_location("Sanctum A1 - 3x Lock"),
                       Has("Ancient Key", 57))

        world.set_rule(world.get_location("Sanctum C1 - 3x Lock"),
                       Has("Ancient Key", 60))

    # Snakesanity
    if False: # world.options.enable_snakesanity:
        world.set_rule(world.get_location("Sanctum A2 - S - Snakeblock"),
                       Has("Ancient Key", 51))
        world.set_rule(world.get_location("Sanctum A2 - C - Snakeblock"),
                       Has("Ancient Key", 51))
        world.set_rule(world.get_location("Sanctum A2 - W - Snakeblock"),
                       Has("Ancient Key", 51))

        world.set_rule(world.get_location("Sanctum C2 - E - Snakeblock"),
                       Has("Ancient Key", 54))
        world.set_rule(world.get_location("Sanctum C2 - W - Snakeblock"),
                       Has("Ancient Key", 54))

        world.set_rule(world.get_location("Sanctum A0 - E - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - CW - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - CE - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - W - Snakeblock"),
                       Has("Ancient Key", 57))

        world.set_rule(world.get_location("Sanctum C0 - W - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CSW - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CNW - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CN - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - E - Snakeblock"),
                       Has("Ancient Key", 60))

def set_mysterious(world: "IslesOfSeaAndSkyWorld"):
    if world.options.circlet_content_enabled:
        world.set_rule(world.get_location("Stone D0 Serpent Secret - Pyramidion"),
                       Has("Star Piece", 35))
        world.set_rule(world.get_location("Stone D1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Water A3 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Aggro Crag - East")
                        ))
        world.set_rule(world.get_location("Fire D3 Serpent Secret - Obsidian"),
                        Has("Awaken Fire Elementals")
                        & Has("Salamander Shirt")
                        & Has("Serpent Circlet"))

        world.set_rule(world.get_location("Fire E3 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Awaken Fire Elementals")
                        & Has("Awaken Water Elementals")
                        & CanReachRegion("Raging Volcano - North-West")
                        & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Sunken Island - Turtle")
                        ))
        world.set_rule(world.get_location("Wind A1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet"))
            
        world.set_rule(world.get_location("Wind E3 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Awaken Wind Elementals")
                        & Has("Awaken Earth Elementals")
                        & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Sea Nunatak - Turtle")
                        ))
        world.set_rule(world.get_location("Rolling A0 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Star Piece", 7)
                        & Has("Awaken Earth Elementals")
                        & Has("Gopher Gloves"))
        
        world.set_rule(world.get_location("Rolling B1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Ancient Key", 14)
                        & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | (CanReachRegion("Raging Volcano - God Altar")
                               | CanReachRegion("Raging Volcano - North-West"))
                        ))
        world.set_rule(world.get_location("Sunken A1 Serpent Secret - Ancient Key"),
                        Has ("Serpent Circlet")
                        & Has("Ancient Key", 34)
                        & Has("Ancient Rune Stone")
                        & (
                            [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Sea Nunatak - Turtle")
                        ))

        world.set_rule(world.get_location("Sunken B0 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Star Piece", 21)
                        & Has("Awaken Water Elementals")
                        & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                        | CanReachRegion("Frozen Spire - Post-Rune")
                        ))
        world.set_rule(world.get_location("Aggro A0 Serpent Secret - Obsidian"),
                        Has("Serpent Circlet")
                        & (
                            [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Star Tropic - West")
                        ))
        
        world.set_rule(world.get_location("Aggro B1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Star Piece", 35)
                        & Has("Awaken Fire Elementals")
                        & (
                            [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Stony Cliffs - Giant Wheel")
                        ))
        world.set_rule(world.get_location("Nunatak A1 Serpent Secret - Obsidian"),
                        Has("Serpent Circlet")
                        & Has("Ancient Rune Stone")
                        & Has("Awaken Wind Elementals")
                        & Has("Star Piece", 49)
                        & (
                            [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Aggro Crag - East"))
                        )
        
        world.set_rule(world.get_location("Nunatak B0 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Awaken Wind Elementals")
                        & Has("Star Piece", 49)
                        & (
                            [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                            | CanReachRegion("Serpent Stacks - Tail")) # and wind elementals
                        )

        world.set_rule(world.get_location("Tropic A1 Serpent Secret - Obsidian"),
                CanReachRegion("Star Tropic - West") # Through Ancient Rune or Lost Sea)
                & Has ("Serpent Circlet")
                & (
                    [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                    | CanReachRegion("Sunken Island - Turtle"))
                )
        world.set_rule(world.get_location("Serpent A5 Serpent Secret - Pyramidion"),
                    Has("Serpent Circlet"))
        
        world.set_rule(world.get_location("Serpent A9 - Pyramidion"),
                    Has("Serpent Circlet")
                    & Has("Awaken Wind Elementals"))
        
        world.set_rule(world.get_location("Sanctum A1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C1 Serpent Secret - Pyramidion"),
                        Has("Serpent Circlet")
                        & Has("Ancient Key", 60))
        
        # This puzzle is random per save, RequireSerpentClues is ignored
        world.set_rule(world.get_location("Shoal A0 - Pattern Puzzle Pyramidion"),
                   CanReachRegion("Stony Cliffs - South Coast"))
        # This puzzle is random per save, RequireSerpentClues is ignored
        world.set_rule(world.get_location("Shoal A1 - Pattern Puzzle Pyramidion"),
                   CanReachRegion("Tidal Reef - East"))
    
        world.set_rule(world.get_location("Shoal B0 - Pattern Puzzle Pyramidion"),
                   [OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                    | CanReachRegion("Frozen Spire - Post-Rune") )
        
        world.set_rule(world.get_location("Shoal B1 - Pyramidion"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals")
                   & Has("Frog Flippers"))
        world.set_rule(world.get_location("Shoal B1 - Pattern Puzzle Pyramidion"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals")
                   & Has("Frog Flippers")
                   & ([OptionFilter(RequireSerpentClues, RequireSerpentClues.option_false)]
                      | (CanReachRegion("Raging Volcano - North-West")
                         | CanReachRegion("Raging Volcano - Key Triplets")
                         | CanReachRegion("Raging Volcano - North-West Pass")
                         | CanReachRegion("Raging Volcano - Geyser Pass"))
                    ))
    
        world.set_rule(world.get_location("Lagoon B0 Serpent Secret - Pyramidion"),
                   Has("Kite Cloak"))
    
        world.set_rule(world.get_location("Lagoon B1 Serpent Secret - W - Pyramidion"),
                    CanReachRegion("Phoenix Hub")
                    & CanReachEntrance("Beast Ridge - Turtle Entrance")
                    & CanReachEntrance("Raging Volcano - God Altar to Phoenix") # Ruby rune stone is mandatory, this entrance should be reachable iff we can complete the raging volcano part of this chain
                    & CanReachEntrance("Stony Cliffs - Phoenix to West Star Stone")
                    & CanReachEntrance("Tidal Reef - Turtle Entrance")
                    & CanReachEntrance("Tidal Reef - Turtle Exit")
                    & CanReachEntrance("Lost Landing - Phoenix to Staircase")
                    )
        
        # TODO Account for alternate solution at Wind E4
        world.set_rule(world.get_location("Lagoon B1 Serpent Secret - C - Pyramidion"),
                    CanReachRegion("Raging Volcano - North-West")
                    )

        world.set_rule(world.get_location("Lagoon B1 Serpent Secret - E - Pyramidion"),
                    (Has("Awaken Earth Elementals")
                        & CanReachRegion("Stony Cliffs - God Altar"))
                    | (Has("Awaken Water Elementals")
                        & CanReachRegion("Tidal Reef - God Altar"))
                    | (Has("Awaken Fire Elementals")
                        & CanReachRegion("Raging Volcano - Lyre"))
                    | (Has("Awaken Wind Elementals")
                        & CanReachRegion("Frozen Spire - Post-Rune"))
                )

def set_meteorites(world: "IslesOfSeaAndSkyWorld"):
    # Warp
    if world.options.shuffle_meteorites:
        world.set_rule(world.get_location("Stone C2 - Earth Warp Pattern"),
                    Has("Ancient Key", 7))

        world.set_rule(world.get_location("Warp ?? - Tropic Warp Pattern"),
                    Has("Warp Pattern - Earth")
                    & Has("Warp Pattern - Water")
                    & Has("Warp Pattern - Fire")
                    & Has("Warp Pattern - Wind"))

def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):

    route = world.options.route_required.current_key

    if route == "normal_ending":
        world.set_completion_rule(CanReachRegion("Sanctum - Peak"))
    elif route == "secret_ending":
        world.set_completion_rule(CanReachRegion("Sanctum - Peak")
                                  & Has("Star Piece", world.options.star_pieces_required.value))
    elif route == "mysterious_ending":
        world.set_completion_rule(CanReachRegion("Sanctum - Peak")
                                  & Has("Star Piece", world.options.star_pieces_required.value)
                                  & Has("Pyramidion", world.options.pyramidions_required.value))
    elif route == "all_gems":
        world.set_completion_rule(Has("Topaz", 12)
                                  & Has("Sapphire", 12)
                                  & Has("Ruby", 12)
                                  & Has("Diamond", 12)
                                  & Has("Obsidian", 18 if world.options.shuffle_pyramidions else 14))
