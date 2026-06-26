from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, DeathLink, OptionGroup
from dataclasses import dataclass

class RouteRequired(Choice):
    """
    Main route of the game required to win.
    """
    display_name = "Required Route"
    option_normal_ending = 0
    option_secret_ending = 1
    option_all_gems = 2
    default = 0

class EnableGemsanity(DefaultOnToggle):
    """
    Turn all gems in the game into location checks.
    """
    display_name = "Enable Gemsanity"

class EnableNotesanity(DefaultOnToggle):
    """
    Turn all music notes in the game into location checks. Music puzzles will be filled progressively from stoney cliffs to frozen spire.
    """
    display_name = "Enable Notesanity"

class ShuffleElementalQuests(DefaultOnToggle):
    """
    Shuffle awakening the elementals into the item pool.
    """
    display_name = "Shuffle Elemental Quests"

class ShuffleBeastBells(DefaultOnToggle):
    """
    Shuffle the bell hits in the item pool. You need all 4 to access the flute location.
    """
    display_name = "Shuffle Beast Bell Hits"

class ShuffleSanctumHits(DefaultOnToggle):
    """
    Shuffle the four elemental sanctum hits into the item pool. You need all 4 to access the end of sanctum.
    """
    display_name = "Shuffle Sanctum Hits"

class EnableLocksanity(Toggle):
    """
    Turn all locks in the game into location checks. This includes big 3x locks, all Rune Stone locks, and other specialty locks
    """
    display_name = "Enable Locksanity"

class EnableSnakesanity(Toggle):
    """
    Turn all snake blocks in the game into location checks. (Snake block = Green directional block with an arrowhead on top)
    """
    display_name = "Enable Snakesanity"

class EnableSecretsanity(Toggle):
    """
    Turns a number of in-game secrets in to location checks. These include secret paths, and disguised blocks.
    """
    display_name = "Enable Secretsanity"

class IncludeSeashells(Toggle):
    """
    Enable seashells on Tidal Reef for extra checks
    """
    display_name = "Include Seashells"

class IncludeJellyfish(Toggle):
    """
    Enable jellyfish in the Overworld for extra checks
    """
    display_name = "Include Jellyfish"

class PhoenixAnywhere(Toggle):
    """
    You can summon the Phoenix in any non-overworld location by pressing: 'E', if you have the Phoenix Flute.
    """
    display_name = "Summon Phoenix Anywhere"

class FillerComposition(Choice):
    """
    Determines what items are sent as Filler, allowing you to make faster progress depending on the option selected.
    Default: only allows Seashells as filler.
    Extra Goodies: adds Ancient Keys, Star Pieces, and Gems to the filler pool.
    Only Goodies: replaces the entire filler pool with Ancient Keys, Star Pieces and Gems.
     """
    display_name = "Filler Composition"
    option_default = 0
    option_extra_goodies = 1
    option_only_goodies = 2
    default = 0

class DeathLinkAmnesty(Range):
    """
    Determines the amount of deaths you must have before a deathlink is sent to the server.
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 10
    default = 3

class Traps(Choice):
    """
    When enabled, transforms filler items into traps instead.
    """
    display_name = "Traps"
    option_no_traps = 0
    option_some_traps = 1
    option_plenty_traps = 2
    default = 0

class AltRoomRandomizer(Toggle):
    """
    When enabled, the game chooses random alternate rooms from the selection in 'Alt Rooms'
    This folder is copied from the apworld into the modded program folder (Should be different than the steam install)
    though you copy the 'Alt Rooms' folder and place it there yourself.
    EARLY DEVELOPMENT! lOTS OF BUGS
    """
    display_name = "Alt Room Randomizer"


@dataclass
class IslesOfSeaAndSkyOptions(PerGameCommonOptions):
    route_required:                             RouteRequired
    enable_gemsanity:                           EnableGemsanity
    enable_notesanity:                          EnableNotesanity
    enable_locksanity:                          EnableLocksanity
    enable_snakesanity:                         EnableSnakesanity
    include_seashells:                          IncludeSeashells
    include_jellyfish:                          IncludeJellyfish
    shuffle_elemental_quests:                   ShuffleElementalQuests
    shuffle_beast_bells:                        ShuffleBeastBells
    shuffle_sanctum_hits:                       ShuffleSanctumHits
    phoenix_anywhere:                           PhoenixAnywhere
    filler_composition:                         FillerComposition
    secretsanity:                               EnableSecretsanity
    death_link:                                 DeathLink
    death_amnesty_total:                        DeathLinkAmnesty
    traps:                                      Traps
    alt_rooms:                                  AltRoomRandomizer

isles_of_sea_and_sky_option_groups = [
    OptionGroup("Goal", [
        RouteRequired
    ]),

    OptionGroup("Checks", [
        EnableGemsanity,
        EnableNotesanity,
        ShuffleElementalQuests,
        ShuffleBeastBells,
        ShuffleSanctumHits
    ]),

    OptionGroup("QOL", [
        PhoenixAnywhere,
        FillerComposition
    ]),

    OptionGroup("Extra Checks", [
        EnableLocksanity,
        EnableSnakesanity,
        EnableSecretsanity,
        IncludeSeashells,
        IncludeJellyfish
    ]),

    OptionGroup("Randomizer", [
        AltRoomRandomizer
    ]),

    OptionGroup("Death Link", [
        DeathLink,
        DeathLinkAmnesty
    ]),

    OptionGroup("Traps", [
        Traps,
    ]),
]

