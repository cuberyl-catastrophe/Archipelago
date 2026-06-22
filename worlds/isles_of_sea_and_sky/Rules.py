from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld


def _isles_of_sea_and_sky_is_route(self, route: int):
    if route == 0:
        return self.options.route_required.current_key == "normal_ending"
    if route == 1:
        return self.options.route_required.current_key == "secret_ending"
    if route == 2:
        return self.options.route_required.current_key == "all_gems"
    return False


# Sets rules on entrances and advancements that are always applied
def set_rules(self):

    player = self.player
    multiworld = self.multiworld

    ### WILL IMPACT PERFORMANCE OF GAME GENERATION
    # self.explicit_indirect_conditions = False

    set_rechecks(self)

    ### Entrances
    set_rule(multiworld.get_entrance("Ancient West Exit", player),
             lambda state: state.can_reach("Ruby Sea", "Region", player))  # Obsidian Sea

    '''set_rule(multiworld.get_entrance("Ancient East Exit", player),
             lambda state: state.has("Ancient Key", player, 6)
             and state.has("Star Piece", player))  # Topaz Sea'''


    ## Required for completion detection
    set_rule(multiworld.get_entrance("Ancient North Exit", player),
             lambda state: state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player)
                           and state.has("Awaken Fire Elementals", player)
                           and state.has("Awaken Wind Elementals", player) ) # Sanctum

    ## Required for completion detection
    set_rule(multiworld.get_entrance("Elemental Rock Path", player),
             lambda state: state.has("Sanctuary Bellstone Hit - Earth", player)
                           and state.has("Sanctuary Bellstone Hit - Water", player)
                           and state.has("Sanctuary Bellstone Hit - Fire", player)
                           and state.has("Sanctuary Bellstone Hit - Wind", player) ) # Sanctum Peak


    set_rule(multiworld.get_entrance("Diamond Sea West Entrance", player),
                 lambda state: state.has("Star Piece", player, 3))  # Diamond Sea

    set_rule(multiworld.get_entrance("Stony Exit To Post-Rune", player),
             lambda state: state.has("Topaz Rune Stone", player))  # Stony Cliffs Post-Rune
    set_rule(multiworld.get_entrance("Stony West Exit", player),
             lambda state: state.has("Topaz Rune Stone", player ) )  # Stony Cliffs NW
    set_rule(multiworld.get_entrance("Stony NW East Exit", player),
             lambda state: state.has("Topaz Rune Stone", player) )  # Stony Cliffs
    set_rule(multiworld.get_entrance("Stony NW West Exit", player),
             lambda state: state.has("Star Piece", player, 5) ) # Sapphire Sea

    set_rule(multiworld.get_entrance("Stony West Entrance", player),
             lambda state: state.has("Star Piece", player, 5))  # Stony NW



    # NOTE: state.has only works with items classified as progression

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 15))  # Ruby Sea

    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # North Diamond Sea

    set_rule(multiworld.get_entrance("North Diamond Sea South Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # Diamond Sea
    set_rule(multiworld.get_entrance("North Diamond Sea East Exit", player),
             lambda state: state.can_reach("Lost Sea", "Region", player))  # Northeast Sea


    set_rule(multiworld.get_entrance("Serpent Entrance", player),
             lambda state: state.has("Star Piece", player, 45))  # Serpent Stacks

    set_rule(multiworld.get_entrance("Tidal S Exit", player),
             lambda state: state.has("Sapphire Rune Stone", player)
                           or state.has("Frog Flippers", player))  # Tidal Reef
    set_rule(multiworld.get_entrance("Tidal Exit To Post-Rune", player),
             lambda state: (state.has("Sapphire Rune Stone", player)))  # Tidal Reef Post-Rune
    set_rule(multiworld.get_entrance("Tidal S Exit To Post-Rune", player),
             lambda state: (state.has("Sapphire Rune Stone", player)))  # Tidal Reef Post-Rune
    set_rule(multiworld.get_entrance("Tidal Exit To S", player),
             lambda state: state.has("Sapphire Rune Stone", player)
                           or state.has("Frog Flippers", player))  # Tidal Reef S
    set_rule(multiworld.get_entrance("Tidal S Entrance From Post-Rune", player),
             lambda state: (state.has("Frog Flippers", player)))  # Tidal Reef S

    set_rule(multiworld.get_entrance("Raging Exit To Post-Rune", player),
             lambda state: (state.has("Ruby Rune Stone", player))) # Raging Volcano Post-Rune
    set_rule(multiworld.get_entrance("Raging NE Exit", player),
             lambda state: state.has("Awaken Fire Elementals", player)
                           or state.can_reach("Raging Volcano Post-Rune", "Region", player)
                           or (state.has("Ruby Rune Stone", player)
                               and state.has("Salamander Shirt", player)) )  # Raging Volcano
    set_rule(multiworld.get_entrance("Raging Exit To NE", player),
             lambda state: (state.has("Ruby Rune Stone", player))) # Raging Volcano NE

    set_rule(multiworld.get_entrance("Frozen Exit To Post-Rune", player),
             lambda state: (state.has("Diamond Rune Stone", player)))  # Frozen Spire Post-Rune

    set_rule(multiworld.get_entrance("Serpent Exit To Post-Rune", player),
             lambda state: (state.has("Obsidian Rune Stone", player)))  # Serpent Stacks Post-Rune


    set_rule(multiworld.get_entrance("Star West Exit", player),
             lambda state: (state.can_reach("Lost Sea", "Region", player)))  # Lost Sea | Gen Failures
    set_rule(multiworld.get_entrance("Star East Exit", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Lost Sea
    set_rule(multiworld.get_entrance("Star East Entrance", player),
             lambda state: state.has("Ancient Rune Stone", player)
                            and state.can_reach("Lost Sea", "Region", player) )  # Star Tropic

    set_rule(multiworld.get_entrance("Rolling Exit To Post-Rune", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Rolling Rocks Post-Rune

    set_rule(multiworld.get_entrance("Shoal Entrance", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Shoal

    set_rule(multiworld.get_entrance("Locked Entrance", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)))

    set_rule(multiworld.get_entrance("Beast Entrance", player),
             lambda state: state.has("Beast Bellstone Hit - Rolling", player)
                           and state.has("Beast Bellstone Hit - Sunken", player)
                           and state.has("Beast Bellstone Hit - Aggro", player)
                           and state.has("Beast Bellstone Hit - Nunatak", player))

    set_rule(multiworld.get_entrance("Abstract Phoenix Exit", player),
             lambda state: state.has("Phoenix Flute", player)
                           and self.options.phoenix_anywhere.value)  # Phoenix Hub
    set_rule(multiworld.get_entrance("Beast Bridge Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) )  # Phoenix Hub
    set_rule(multiworld.get_entrance("Stony Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Tidal Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Raging Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Frozen Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) and state.has("Diamond Rune Stone", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Lost Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub

    set_rule(multiworld.get_entrance("Beast Bridge Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Beast Bellstone Hit - Rolling", player)
                           and state.has("Beast Bellstone Hit - Sunken", player)
                           and state.has("Beast Bellstone Hit - Aggro", player)
                           and state.has("Beast Bellstone Hit - Nunatak", player))  # Beast Bridge
    set_rule(multiworld.get_entrance("Stony Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player))  # Stony Cliffs
    set_rule(multiworld.get_entrance("Tidal Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                            and ( state.has("Sapphire Rune Stone", player) or state.has("Frog Flippers", player) ) )  # Tidal Reef
    set_rule(multiworld.get_entrance("Raging Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player) )  # Raging Volcano NE
    set_rule(multiworld.get_entrance("Frozen Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Diamond Rune Stone", player) )  # Frozen Spire
    set_rule(multiworld.get_entrance("Lost Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Star Piece", player, 30) )  # Lost Landing


    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Overworld - Star Lock 3", player),
                 lambda state: state.has("Star Piece", player, 3))
        set_rule(multiworld.get_location("Overworld - Star Lock 15", player),
                 lambda state: state.has("Star Piece", player, 15))
        set_rule(multiworld.get_location("Overworld - Star Lock 30", player),
                 lambda state: state.has("Star Piece", player, 30))
        set_rule(multiworld.get_location("Overworld - Star Lock 45", player),
                 lambda state: state.has("Star Piece", player, 45))

    
    ### Locations

    # Legendary Item Locations
    set_rule(multiworld.get_location("Stone Dungeon C1 - Gopher Gloves", player),
             lambda state: (state.has("Topaz Rune Stone", player)
                           and state.has("Awaken Earth Elementals", player))
                           or state.has("Gopher Gloves", player) )

    set_rule(multiworld.get_location("Water A4 - Frog Flippers", player),
             lambda state: state.has("Sapphire Rune Stone", player))

    set_rule(multiworld.get_location("Fire E0 - Salamander Shirt", player),
             lambda state: state.has("Fire Key", player, 3))

    set_rule(multiworld.get_location("Wind A0 - Kite Cloak", player),
             lambda state: state.has("Diamond Rune Stone", player)
                           and (state.has("Awaken Wind Elementals", player)
                                or state.has("Kite Cloak", player)) ) # since Eggs and Wind key are broken, don't include

    set_rule(multiworld.get_location("Serpent A1 - Serpent Circlet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player)
                           and state.has("Obsidian Rune Stone", player)
                           and state.has("Obsidian", player, 9))

    # Quests
    set_rule(multiworld.get_location("Stone C0 - Topaz Quest Complete", player),
             lambda state: state.has("Topaz", player, 6))

    set_rule(multiworld.get_location("Water C0 - Sapphire Quest Complete", player),
             lambda state: state.has("Sapphire", player, 6))

    set_rule(multiworld.get_location("Fire C0 - Ruby Quest Complete", player),
             lambda state: state.has("Ruby", player, 6))

    set_rule(multiworld.get_location("Wind C2 - Diamond Quest Complete", player),
             lambda state: state.has("Diamond", player, 6))

    # Islands and their Locations
    set_ancient_isle(self)
    set_rolling_rocks(self)
    set_sunken_island(self)
    set_aggro_crag(self)
    set_sea_nunatak(self)
    set_locked(self)
    set_star_tropic(self)
    set_shoal(self)
    set_lost_landing(self)


    set_stony_cliffs(self)
    set_tidal_reef(self)
    set_raging_volcano(self)
    set_frozen_spire(self)
    set_serpent_stacks(self)
    set_beast_bridge(self)
    set_sanctum(self)





def set_ancient_isle(self):

    player = self.player
    multiworld = self.multiworld

    # Collectables
    set_rule(multiworld.get_location("Ancient A1 - Star Piece", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                            and state.has("Ancient Key", player, 17) )

    set_rule(multiworld.get_location("Ancient B1 - Star Piece", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                           and state.has("Ancient Rune Stone", player)
                           and state.has("Ancient Key", player, 17) )

    set_rule(multiworld.get_location("Ancient A2 - NW - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player)
             )#and state.can_reach("Topaz Sea", "Region", player))

    '''set_rule(multiworld.get_location("Ancient A1 - Ancient Key", player),
             lambda state: state.has("Ancient Key", player))

    set_rule(multiworld.get_location("Ancient A2 - SE - Ancient Key", player),
             lambda state: state.has("Ancient Key", player))

    set_rule(multiworld.get_location("Ancient A3 - N - Ancient Key", player),
             lambda state: state.has("Ancient Key", player, 2))
    set_rule(multiworld.get_location("Ancient A3 - S - Ancient Key", player),
             lambda state: state.has("Ancient Key", player))
    set_rule(multiworld.get_location("Ancient A3 - E - Ancient Key", player),
             lambda state: state.has("Ancient Key", player, 2))

    set_rule(multiworld.get_location("Ancient C2 - Ancient Key", player),
             lambda state: state.has("Ancient Key", player, 3))
    set_rule(multiworld.get_location("Ancient C3 - Ancient Key", player),
             lambda state: state.has("Ancient Key", player, 3))
    set_rule(multiworld.get_location("Ancient C1 - Ancient Key", player),
             lambda state: state.has("Star Piece", player)
                               and state.has("Ancient Key", player, 6))

    set_rule(multiworld.get_location("Ancient C0 - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 6))'''

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Ancient A1 - 3x Lock", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                           and state.has("Ancient Key", player, 17))

        set_rule(multiworld.get_location("Ancient B3 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 1))

        set_rule(multiworld.get_location("Ancient A3 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 2))

        set_rule(multiworld.get_location("Ancient B2 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 3))

        set_rule(multiworld.get_location("Ancient C2 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 6))

        set_rule(multiworld.get_location("Ancient C1 - Star Lock 1", player),
                 lambda state: state.has("Star Piece", player)
                               and state.has("Ancient Key", player, 6))

        set_rule(multiworld.get_location("Ancient B1 - Ancient Rune Lock", player),
             lambda state: state.has("Ancient Rune Stone", player))

    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Ancient B3 - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player))

        set_rule(multiworld.get_location("Ancient B2 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player))

        set_rule(multiworld.get_location("Ancient A3 - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 2))

        set_rule(multiworld.get_location("Ancient B2 - E - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Ancient C2 - E - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Ancient C2 - S - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Ancient C2 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Ancient C3 - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 3))

        set_rule(multiworld.get_location("Ancient A1 - Snakeblock", player),
                lambda state: state.can_reach("Obsidian Sea", "Region", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Ancient A1 - Discover Secret", player),
                 lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                           and state.has("Ancient Key", player, 17))


def set_rolling_rocks(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Rolling A0 - Topaz", player),
             lambda state: state.has("Star Piece", player, 7)
                           and state.has("Awaken Earth Elementals", player) )

    set_rule(multiworld.get_location("Rolling A1 - Obsidian", player),
             lambda state: state.has("Star Piece", player, 7)
                           and state.has("Gopher Gloves", player)
                           and state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Rolling A0 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 7)
                           and (state.has("Awaken Earth Elementals", player) or state.has("Frog Flippers", player) ) )


    set_rule(multiworld.get_location("Rolling B1 - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 14))

    set_rule(multiworld.get_location("Rolling B0 - Star Piece", player),
             lambda state: state.has("Gopher Gloves", player))



    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Rolling B1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 14))

        set_rule(multiworld.get_location("Rolling A0 - Star Lock 7", player),
                 lambda state: state.has("Star Piece", player, 7))


    if self.options.enable_snakesanity.value:
        pass

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Rolling A0 - Discover Secret", player),
                 lambda state: state.has("Star Piece", player, 7)
                               and state.has("Gopher Gloves", player))

def set_sunken_island(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Sunken B1 - Big Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Sunken B0 - Sapphire", player),
             lambda state: state.has("Star Piece", player, 21)
             and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Sunken B0 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 21)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Sunken A1 - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 34)
                               and state.has("Ancient Rune Stone", player) )

    set_rule(multiworld.get_location("Sunken A0 - Obsidian", player),
             lambda state: state.has("Frog Flippers", player))

    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Sunken A1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 34)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Sunken B0 - Star Lock 21", player),
                 lambda state: state.has("Star Piece", player, 21))

        set_rule(multiworld.get_location("Sunken A0 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Sunken B1 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

def set_aggro_crag(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Aggro A1 - Big Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Aggro B1 - Ruby", player),
             lambda state: state.has("Star Piece", player, 35)
             and state.has("Awaken Fire Elementals", player) )

    set_rule(multiworld.get_location("Aggro B1 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Aggro B0 - Obsidian", player),
             lambda state: state.has("Ancient Rune Stone", player)
                            and state.has("Star Piece", player, 35)
                            and state.has("Awaken Fire Elementals", player)
                            and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Aggro A1 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Awaken Fire Elementals", player)
                           and state.has("Ancient Rune Stone", player))

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Aggro A1 - 3x Lock", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 42))

        set_rule(multiworld.get_location("Aggro B0 - Star Lock 35", player),
                 lambda state: state.has("Star Piece", player, 35))

        set_rule(multiworld.get_location("Aggro B1 - Ancient Rune Lock", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Aggro A1 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Aggro B1 - E - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 35))

        set_rule(multiworld.get_location("Aggro B1 - W - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Aggro B0 - W - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Ancient Rune Stone", player)
                               and state.has("Salamander Shirt", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Aggro A0 - W - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Aggro A0 - E - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Star Piece", player, 35)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Salamander Shirt", player))

def set_sea_nunatak(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Nunatak A1 - Big Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Nunatak A1 - Ancient Key", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Awaken Wind Elementals", player)
             and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Nunatak B0 - Diamond", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Nunatak B0 - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Nunatak A0 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 26) )

    set_rule(multiworld.get_location("Nunatak B1 - Obsidian", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Star Piece", player, 49)
                           and state.has("Kite Cloak", player) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Nunatak A0 - 3x Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 26))

        set_rule(multiworld.get_location("Nunatak B0 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Nunatak B0 - Star Lock 49", player),
                 lambda state: state.has("Star Piece", player, 49))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Nunatak A1 - Snakeblock", player),
                     lambda state: state.has("Ancient Rune Stone", player)
                     and state.has("Awaken Wind Elementals", player)
                     and state.has("Star Piece", player, 49))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Nunatak B0 - E - Discover Secret", player),
                 lambda state: state.has("Awaken Wind Elementals", player)
                               and state.has("Star Piece", player, 49)
                               and state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Nunatak B0 - SE - Discover Secret", player),
                 lambda state: state.has("Awaken Wind Elementals", player)
                               and state.has("Star Piece", player, 49)
                               and state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Nunatak B0 - CW - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Awaken Wind Elementals", player)
                               and state.has("Star Piece", player, 49))
        set_rule(multiworld.get_location("Nunatak B0 - W - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Awaken Wind Elementals", player)
                               and state.has("Star Piece", player, 49))

def set_locked(self):
    player = self.player
    multiworld = self.multiworld
    set_rule(multiworld.get_location("Locked A0 - Ancient Rune Stone", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                           and state.has("Ancient Key", player, 23))  # Makes this 'unreachable'

    set_rule(multiworld.get_location("Locked A0 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Locked A0 - 6x Lock", player),
                 lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                               and state.has("Ancient Key", player, 23))

        set_rule(multiworld.get_location("Locked A0 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Locked A0 - E - Snakeblock", player),
                 lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                               and state.has("Ancient Key", player, 23))
        set_rule(multiworld.get_location("Locked A0 - C - Snakeblock", player),
                 lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                               and state.has("Ancient Key", player, 23))
        set_rule(multiworld.get_location("Locked A0 - W - Snakeblock", player),
                 lambda state: (state.can_reach("Ruby Sea", "Region", player)
                            or state.can_reach("Sapphire Sea", "Region", player))
                               and state.has("Ancient Key", player, 23))

def set_star_tropic(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Tropic A1 - Ancient Key", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Tropic A1 - Topaz", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                         and state.has("Frog Flippers", player)
                         and state.has("Salamander Shirt", player)
                         and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Tropic A1 - Sapphire", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Tropic A1 - Ruby", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Tropic A1 - Diamond", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Tropic A1 - 1 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Tropic A1 - 2 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Tropic A1 - 3 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Tropic A1 - 4 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Tropic B0 - S - Star Piece", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               or (state.can_reach("Lost Sea", "Region", player)
                                   and state.has("Kite Cloak", player) ))

    set_rule(multiworld.get_location("Tropic B0 - N - Star Piece", player),
             lambda state: state.has("Obsidian Rune Stone", player)
                       and state.has("Kite Cloak", player))


    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Tropic A1 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player) )

        set_rule(multiworld.get_location("Tropic B0 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Tropic B0 - Obsidian Rune Lock", player),
                 lambda state: state.has("Obsidian Rune Stone", player)
                           and state.has("Kite Cloak", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Tropic A0 - W - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Tropic A0 - C - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Tropic A0 - E - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Tropic B0 - N - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Tropic B0 - S - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Tropic A0 - Discover Secret", player),
                 lambda state: state.has("Kite Cloak", player))

def set_shoal(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Shoal A0 - Star Viewing Orb", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Shoal A0 - Star Piece", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Kite Cloak", player))

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Shoal A0 - Ancient Rune Lock", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:

        set_rule(multiworld.get_location("Shoal A0 - Snakeblock", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Kite Cloak", player))

    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Shoal A0 - E - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Shoal A0 - SE - Discover Secret", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Frog Flippers", player)
                               and state.has("Kite Cloak", player))

def set_lost_landing(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Lost A1 - Obsidian", player),
             lambda state: state.has("Star Piece", player, 30)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Lost B1 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 30) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Lost A1 - Lock", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player)
                                and state.has("Ancient Key", player, 48))

        set_rule(multiworld.get_location("Lost B0 - Star Lock 30", player),
                 lambda state: state.has("Star Piece", player, 30))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Lost B1 - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 30))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Lost B1 - CS - Discover Secret", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Lost B1 - W - Discover Secret", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player))


def set_serpent_stacks(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Serpent A1 - Obsidian Rune Stone", player),
             lambda state: state.has("Topaz Rune Stone", player)
                         and state.has("Sapphire Rune Stone", player)
                         and state.has("Ruby Rune Stone", player)
                         and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Serpent A1 - Obsidian", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Serpent A1 - W - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Serpent A1 - N - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Serpent A2 - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player) )

    set_rule(multiworld.get_location("Serpent A3 - Star Piece", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Serpent A4 - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Serpent A6 - W - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Serpent A6 - E - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Serpent A7 - W - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player)
                           and state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Serpent A7 - E - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player)
                           and state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Serpent A8 - N - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player)
                           and state.has("Awaken Fire Elementals", player)
                           and state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Serpent A8 - S - Star Piece", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Awaken Earth Elementals", player)
                           and state.has("Awaken Water Elementals", player)
                           and state.has("Awaken Fire Elementals", player)
                           and state.has("Awaken Wind Elementals", player))

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Serpent A2 - Elemental Rune Lock", player),
                 lambda state: state.has("Topaz Rune Stone", player)
                               and state.has("Sapphire Rune Stone", player)
                               and state.has("Ruby Rune Stone", player)
                               and state.has("Diamond Rune Stone", player))

        set_rule(multiworld.get_location("Serpent A1 - N - Obsidian Rune Lock", player),
                 lambda state: state.has("Topaz Rune Stone", player)
                               and state.has("Sapphire Rune Stone", player)
                               and state.has("Ruby Rune Stone", player)
                               and state.has("Diamond Rune Stone", player))

        set_rule(multiworld.get_location("Serpent A1 - W - Obsidian Rune Lock", player),
                 lambda state: state.has("Topaz Rune Stone", player)
                               and state.has("Sapphire Rune Stone", player)
                               and state.has("Ruby Rune Stone", player)
                               and state.has("Diamond Rune Stone", player))

        set_rule(multiworld.get_location("Serpent A1 - E - Obsidian Rune Lock", player),
                 lambda state: state.has("Topaz Rune Stone", player)
                               and state.has("Sapphire Rune Stone", player)
                               and state.has("Ruby Rune Stone", player)
                               and state.has("Diamond Rune Stone", player)
                               and state.has("Serpent Circlet", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Serpent A1 - C - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player) and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Serpent A1 - CE - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Serpent A1 - E - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Serpent A6 - SW - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Awaken Earth Elementals", player)
                               and state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Serpent A6 - NW - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Awaken Earth Elementals", player)
                               and state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Serpent A6 - C - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Awaken Earth Elementals", player)
                               and state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Serpent A6 - E - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Awaken Earth Elementals", player)
                               and state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Serpent A8 - Snakeblock", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Awaken Earth Elementals", player)
                               and state.has("Awaken Water Elementals", player)
                               and state.has("Awaken Fire Elementals", player)
                               and state.has("Awaken Wind Elementals", player))

def set_stony_cliffs(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Stone Dungeon A1 - Gold Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                         and state.has("Star Piece", player, 20)
                         and state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone E3 - Blue Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Star Piece", player, 20))

    set_rule(multiworld.get_location("Stone C0 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone B4 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Stone Dungeon C1 - Ancient Key", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Stone Dungeon D0 - Ancient Key", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Stone Dungeon B1 - Ancient Key", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Stone B0 - NW1 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player))
    set_rule(multiworld.get_location("Stone B0 - NW2 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player))
    set_rule(multiworld.get_location("Stone B0 - NW3 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone A2 - Ancient Key", player),
             lambda state: state.has("Blue Stone Tablet", player)
                           and state.has("Gold Stone Tablet", player))

    set_rule(multiworld.get_location("Stone Dungeon D2 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player))


    set_rule(multiworld.get_location("Stone Dungeon C1 - Topaz", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Stone C2 - E - Topaz", player),
             lambda state: state.has("Ancient Key", player, 7))

    set_rule(multiworld.get_location("Stone A2 - Obsidian", player),
             lambda state: state.has("Blue Stone Tablet", player)
                           and state.has("Gold Stone Tablet", player))

    set_rule(multiworld.get_location("Stone C1 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone B2 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone B4 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Stone C4 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Stone C0 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone Dungeon E1 - Star Piece", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone Dungeon E2 - Star Piece", player),
             lambda state: (state.has("Awaken Earth Elementals", player) or state.can_reach("Stony Cliffs NW", "Region", player))
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Stone Dungeon E2 - Ancient Key", player),
             lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )

    set_rule(multiworld.get_location("Stone Dungeon C3 - Star Piece", player),
                 lambda state: state.has("Awaken Earth Elementals", player)  or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )

    set_rule(multiworld.get_location("Stone Dungeon C1 - Star Piece", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Stone Dungeon B1 - Star Piece", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Stone A1 - Star Piece", player),
             lambda state: state.has("Star Piece", player, 5))

    set_rule(multiworld.get_location("Stone E1 - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 10))

    set_rule(multiworld.get_location("Stone B2 - Music Note", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone D1 - Music Note", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone Dungeon C2 - Open Topaz Door", player),
             lambda state: state.has("Awaken Earth Elementals", player))

    set_rule(multiworld.get_location("Stone Dungeon E1 - Tablet Puzzle Clue", player),
             lambda state: (state.has("Awaken Earth Elementals", player) and state.has("Topaz Rune Stone", player))
                           or state.has("Kite Cloak", player))


    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Stone C2 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 7))

        set_rule(multiworld.get_location("Stone E1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 10))

        set_rule(multiworld.get_location("Stone B1 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 11))

        set_rule(multiworld.get_location("Stone A1 - Star Lock 5", player),
                 lambda state: state.has("Star Piece", player, 5))

        set_rule(multiworld.get_location("Stone C4 - Star Lock 15", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Awaken Earth Elementals", player) )

        set_rule(multiworld.get_location("Stone E3 - Star Lock 20", player),
                 lambda state: state.has("Star Piece", player, 20))

        set_rule(multiworld.get_location("Stone Dungeon A1 - Star Lock 20", player),
                 lambda state: state.has("Star Piece", player, 20)
                               and state.has("Gopher Gloves", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Stone C1 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone D1 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone E1 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone C4 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone Dungeon C4 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone Dungeon C3 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon B2 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D2 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D2 - CE - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D2 - W - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D2 - CW - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D1 - W - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D1 - CS - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon D1 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )
        set_rule(multiworld.get_location("Stone Dungeon E1 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player))
        set_rule(multiworld.get_location("Stone Dungeon E2 - Snakeblock", player),
                 lambda state: state.has("Awaken Earth Elementals", player) or (state.can_reach("Stony Cliffs NW", "Region", player) and state.has("Gopher Gloves", player) ) )


        set_rule(multiworld.get_location("Stone Dungeon C1 - Snakeblock", player),
                 lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

        set_rule(multiworld.get_location("Stone B4 - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Gopher Gloves", player))
        set_rule(multiworld.get_location("Stone A4 - E - Snakeblock", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Gopher Gloves", player)
                               and state.has("Awaken Earth Elementals", player))

    # Secretsanity
    if self.options.secretsanity.value:
        pass

def set_tidal_reef(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Water A0 - S - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water A2 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water B3 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water C3 - NE1 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))
    set_rule(multiworld.get_location("Water C3 - NE2 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))
    set_rule(multiworld.get_location("Water C3 - NE3 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water D1 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water D0 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water C0 - Ancient Key", player),
             lambda state: state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water D2 - Ancient Key", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water C2 - N - Sapphire", player),
             lambda state: state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water A1 - Sapphire", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water C0 - Star Piece", player),
             lambda state: state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water C2 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player) and state.has("Awaken Water Elementals", player)  )

    set_rule(multiworld.get_location("Water D2 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Kite Cloak", player) )

    set_rule(multiworld.get_location("Water D3 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Awaken Water Elementals", player))

    set_rule(multiworld.get_location("Water E0 - W - Star Piece", player),
             lambda state: state.has("Awaken Water Elementals", player)
                           or state.has("Kite Cloak", player) )

    set_rule(multiworld.get_location("Water E0 - E - Star Piece", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water E2 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Water B1 - Star Piece", player),
             lambda state: state.has("Awaken Water Elementals", player)
             and state.has("Frog Flippers", player) )

    set_rule(multiworld.get_location("Water A2 - N - Star Piece", player),
             lambda state: state.has("Awaken Water Elementals", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Water A2 - S - Star Piece", player),
             lambda state: state.has("Awaken Water Elementals", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Water A4 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player) )

    set_rule(multiworld.get_location("Water C1 - W - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 32))

    # IncludeShells
    if self.options.include_seashells.value:

        set_rule(multiworld.get_location("Water B2 - Shell", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water B3 - Shell", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Phoenix Flute", player)
                               or state.has("Sapphire Rune Stone", player) )


        set_rule(multiworld.get_location("Water B0 - Shell", player),
                 lambda state: state.has("Awaken Water Elementals", player))

        set_rule(multiworld.get_location("Water D1 - Shell", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water A4 - Shell", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water D0 - Shell", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water A2 - Shell", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water A3 - Shell", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Sapphire Rune Stone", player))

    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Water B2 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 29))

        set_rule(multiworld.get_location("Water C1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 32))

        set_rule(multiworld.get_location("Water D3 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 33))

        set_rule(multiworld.get_location("Water A2 - Star Lock 30", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Awaken Water Elementals", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Water B0 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Water B0 - C - Snakeblock", player),
                 lambda state: state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Water B1 - C - Snakeblock", player),
                 lambda state: state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Water B1 - SE - Snakeblock", player),
                 lambda state: state.has("Awaken Water Elementals", player) or state.has("Kite Cloak",player))


        set_rule(multiworld.get_location("Water D2 - C - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Water D2 - E - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Water D3 - Snakeblock", player),
                 lambda state: state.has("Awaken Water Elementals", player))
        set_rule(multiworld.get_location("Water E1 - W - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Water E1 - E - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Water E2 - E - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Water A0 - S - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Water A2 - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Awaken Water Elementals", player)
                               and state.has("Star Piece", player, 30))

        set_rule(multiworld.get_location("Water A3 - Snakeblock", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Awaken Water Elementals", player)
                               and state.has("Star Piece", player, 30))

def set_raging_volcano(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Fire A2 - S - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire B4 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire A1 - NE - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Fire A1 - E - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Fire A1 - S - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire B1 - N1 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Fire B1 - N2 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Fire B1 - N3 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire C1 - NE - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player)
                           and state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire C1 - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire C0 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire C1 - SW - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire C3 - Ancient Key", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire D4 - Ancient Key", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire D0 - Ruby", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire E0 - Obsidian", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire B4 - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire C0 - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire D1 - N - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player))
    set_rule(multiworld.get_location("Fire D1 - S - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 38))

    set_rule(multiworld.get_location("Fire D3 - S - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire D3 - W - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire E3 - Star Piece", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire D4 - Star Piece", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Awaken Fire Elementals", player))

    set_rule(multiworld.get_location("Fire E1 - E - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Fire E1 - W - Star Piece", player),
             lambda state: state.has("Awaken Fire Elementals", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire E0 - Star Piece", player),
             lambda state: state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Fire B0 - Music Note", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Fire D3 - Music Note", player),
             lambda state: state.has("Salamander Shirt", player))


    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Fire D2 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 35))

        set_rule(multiworld.get_location("Fire D2 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 38))

        set_rule(multiworld.get_location("Fire A3 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 39))

        set_rule(multiworld.get_location("Fire E0 - 3x Lock (Fire)", player),
                 lambda state: state.has("Fire Key", player, 3))

        set_rule(multiworld.get_location("Fire A1 - E - Ruby Rune Lock", player),
                 lambda state: state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Fire B2 - N - Ruby Rune Lock", player),
                 lambda state: state.has("Salamander Shirt", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Fire B4 - W - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire B4 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire B3 - CW - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire B3 - W - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire B3 - CE - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire C3 - E - Snakeblock", player),
                 lambda state: state.has("Awaken Fire Elementals", player))


        set_rule(multiworld.get_location("Fire D1 - SE - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire D1 - SW - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 38))
        set_rule(multiworld.get_location("Fire B1 - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire D4 - E - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire E4 - CE - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire E4 - W - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire D3 - W - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire D2 - SE - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire A1 - E - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Fire D3 - E - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player)
                               and state.has("Awaken Fire Elementals", player))
        set_rule(multiworld.get_location("Fire D3 - SW - Snakeblock", player),
                 lambda state: state.has("Salamander Shirt", player)
                               and state.has("Awaken Fire Elementals", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Fire C2 - Discover Secret", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Fire E1 - Discover Secret", player),
                 lambda state: state.has("Salamander Shirt", player))

def set_frozen_spire(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Wind D4 - NW1 - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))
    set_rule(multiworld.get_location("Wind D4 - NW2 - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))
    set_rule(multiworld.get_location("Wind D4 - NW3 - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind D4 - Star Piece", player),
             lambda state: state.has("Ancient Key", player, 45))

    set_rule(multiworld.get_location("Wind D3 - Ancient Key", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind A3 - Ancient Key", player),
             lambda state: state.has("Kite Cloak", player) or state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind C2 - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E2 - NE - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E2 - S - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E4 - E - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind E4 - SW - Ancient Key", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind C3 - Diamond", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           and state.has("Ancient Key", player, 46))
    set_rule(multiworld.get_location("Wind D1 - E - Diamond", player),
             lambda state: state.has("Kite Cloak", player)
                           or state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind B3 - Star Piece", player),
             lambda state: state.has("Kite Cloak", player)
                               and state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind A3 - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind B2 - N - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player)
                           or state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind C2 - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind D2 - Star Piece", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind E2 - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E4 - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E1 - Star Piece", player),
             lambda state: state.has("Kite Cloak", player)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Wind A0 - Star Piece", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind C3 - NE - Star Piece", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind A2 - Music Note", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind D3 - Music Note", player),
             lambda state: state.has("Awaken Wind Elementals", player))

    set_rule(multiworld.get_location("Wind E3 - Music Note", player),
             lambda state: state.has("Awaken Wind Elementals", player))


    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Wind D3 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 45))

        set_rule(multiworld.get_location("Wind C3 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 46)
                               and state.has("Awaken Wind Elementals", player))

        set_rule(multiworld.get_location("Wind D1 - Lock", player),
                 lambda state: state.has("Ancient Key", player, 47) )

        set_rule(multiworld.get_location("Wind A0 - Lock (Wind)", player),
                 lambda state: state.has("Diamond Rune Stone", player)) # Remove later when wind key item is fixed

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Wind A2 - SE - Snakeblock", player),
                 lambda state: state.has("Awaken Wind Elementals", player))
        set_rule(multiworld.get_location("Wind E4 - Snakeblock", player),
                 lambda state: state.has("Awaken Wind Elementals", player))
        set_rule(multiworld.get_location("Wind E3 - Snakeblock", player),
                 lambda state: state.has("Awaken Wind Elementals", player))
        set_rule(multiworld.get_location("Wind C2 - Snakeblock", player),
                 lambda state: state.has("Awaken Wind Elementals", player))

        set_rule(multiworld.get_location("Wind B3 - CE - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Wind B3 - NE - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Wind B2 - SW - Snakeblock", player),
                 lambda state: state.has("Awaken Wind Elementals", player))
        set_rule(multiworld.get_location("Wind B4 - Snakeblock", player),
                 lambda state: state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Wind E1 - Snakeblock", player),
                 lambda state: state.has("Gopher Gloves", player)
                               and state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Wind D4 - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 45))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Wind D1 - Discover Secret", player),
                 lambda state: state.has("Kite Cloak", player)
                               and state.has("Ancient Key", player, 47))

def set_beast_bridge(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Beast A0 - Phoenix Flute", player),
             lambda state: state.can_reach("Beast Bridge", "Region", player)
                           and state.has("Beast Bellstone Hit - Rolling", player)
                           and state.has("Beast Bellstone Hit - Sunken", player)
                           and state.has("Beast Bellstone Hit - Aggro", player)
                           and state.has("Beast Bellstone Hit - Nunatak", player))

    set_rule(multiworld.get_location("Beast A1 - Bellstone", player),
             lambda state: state.has("Beast Bellstone Hit - Rolling", player)
                           and state.has("Beast Bellstone Hit - Sunken", player)
                           and state.has("Beast Bellstone Hit - Aggro", player)
                           and state.has("Beast Bellstone Hit - Nunatak", player))

def set_sanctum(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Sanctum A2 - Topaz Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 51))

    set_rule(multiworld.get_location("Sanctum C2 - Sapphire Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 54))

    set_rule(multiworld.get_location("Sanctum A0 - Diamond Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 57))

    set_rule(multiworld.get_location("Sanctum C0 - Ruby Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 60))


    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Sanctum B2 - W - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 51))

        set_rule(multiworld.get_location("Sanctum B2 - E - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 54))

        set_rule(multiworld.get_location("Sanctum A1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 57))

        set_rule(multiworld.get_location("Sanctum C1 - 3x Lock", player),
                 lambda state: state.has("Ancient Key", player, 60))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Sanctum A2 - S - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 51))
        set_rule(multiworld.get_location("Sanctum A2 - C - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 51))
        set_rule(multiworld.get_location("Sanctum A2 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 51))

        set_rule(multiworld.get_location("Sanctum C2 - E - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 54))
        set_rule(multiworld.get_location("Sanctum C2 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 54))

        set_rule(multiworld.get_location("Sanctum A0 - E - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Sanctum A0 - CW - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Sanctum A0 - CE - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Sanctum A0 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 57))

        set_rule(multiworld.get_location("Sanctum C0 - W - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Sanctum C0 - CSW - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Sanctum C0 - CNW - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Sanctum C0 - CN - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Sanctum C0 - E - Snakeblock", player),
                 lambda state: state.has("Ancient Key", player, 60))

def set_rechecks(self):
    # Rechecks reachability later in the fill sweep, so that some unreachable locations can
    # be registered correctly.

    player = self.player
    multiworld = self.multiworld

    multiworld.register_indirect_condition(multiworld.get_region("Ruby Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Sapphire Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Ruby Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Sapphire Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Raging Volcano Post-Rune", player),
                                           multiworld.get_entrance("Raging NE Exit", player))


    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("North Diamond Sea East Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star East Entrance", player))


    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    # Later ancient isle checks, and the Locked region
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Nunatak Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Sunken Entrance", player))

def set_completion_rules(self):
    player = self.player
    multiworld = self.multiworld

    # Normal Ending

    if _isles_of_sea_and_sky_is_route(self, 0):
        multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)

    # Secret Ending
    elif _isles_of_sea_and_sky_is_route(self, 1):
        multiworld.completion_condition[player] = lambda state: (state.can_reach("Sanctum Peak", "Region", player)
                                                                 and state.has("Star Piece", player, 91))
    # All Gems
    elif _isles_of_sea_and_sky_is_route(self, 2):
        multiworld.completion_condition[player] = lambda state: (state.has("Topaz", player, 12)
                                                                 and state.has("Sapphire", player, 12)
                                                                 and state.has("Ruby", player, 12)
                                                                 and state.has("Diamond", player, 12)
                                                                 and state.has("Obsidian", player, 12))

