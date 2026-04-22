import discord
from discord.ext import commands
from discord import app_commands
import random
import os
from datetime import datetime

# ─── CẤU HÌNH ────────────────────────────────────────────────
# Token — đọc cả TOKEN lẫn DISCORD_TOKEN
TOKEN = os.environ.get("TOKEN") or os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ Không tìm thấy TOKEN! Hãy đặt biến TOKEN hoặc DISCORD_TOKEN trong Railway Variables.")

MAX_GUESSES = 6

# ─── WORDLIST (2,578 từ, 4–7 chữ cái) ───────────────────────
WORD_LIST = {
    4: [  # 1030 words
        "able", "aces", "ache", "acid", "acre", "acts", "aged", "ages", "aide", "aids",
        "aims", "ales", "alga", "aloe", "also", "alto", "alum", "amen", "amid", "amok",
        "amps", "ands", "anew", "ankh", "ants", "arch", "area", "aria", "arid", "army",
        "arts", "arty", "asks", "asps", "atom", "atop", "auks", "aunt", "avid", "awed",
        "awes", "awls", "axes", "axle", "axon", "ayes", "bade", "bags", "bail", "bait",
        "bale", "balk", "ball", "balm", "band", "bane", "bang", "bank", "barb", "bark",
        "barn", "bars", "base", "bash", "bask", "bass", "bast", "bath", "bats", "baud",
        "bawl", "bays", "bead", "beak", "beam", "bean", "bear", "beat", "beck", "beds",
        "been", "beer", "bees", "beet", "bell", "belt", "bend", "bent", "best", "bide",
        "bile", "bilk", "bill", "bind", "bite", "blew", "blob", "bloc", "blot", "blow",
        "blue", "blur", "boar", "bobs", "bode", "bogs", "bold", "bole", "bolt", "bond",
        "bone", "bong", "book", "boom", "boon", "boor", "boot", "bore", "born", "boss",
        "bout", "bowl", "boys", "brad", "brag", "bran", "brat", "brew", "brig", "brim",
        "brow", "buck", "buds", "bugs", "bulk", "bull", "bump", "bunk", "buns", "bunt",
        "buoy", "burl", "burn", "burp", "burr", "burs", "bury", "bust", "busy", "buys",
        "buzz", "cabs", "cafe", "cage", "calf", "calm", "came", "cane", "cape", "card",
        "care", "carp", "cart", "case", "cash", "cask", "cast", "cave", "cede", "cell",
        "chad", "chap", "char", "chat", "chef", "chew", "chin", "chip", "chop", "chow",
        "chum", "cite", "city", "clad", "clam", "clap", "claw", "clay", "clip", "clod",
        "clog", "clop", "clot", "cloy", "club", "clue", "coal", "coat", "coax", "cobs",
        "code", "coil", "cola", "cold", "colt", "coma", "come", "cone", "conk", "cons",
        "cook", "cool", "coop", "cope", "cord", "core", "corn", "cost", "coup", "cozy",
        "crag", "cram", "crew", "crib", "crop", "crow", "crud", "cube", "cubs", "cued",
        "cups", "curb", "cure", "curl", "curt", "cute", "cyan", "dabs", "dale", "dame",
        "damp", "dare", "dark", "darn", "dart", "dash", "data", "date", "daub", "dawn",
        "days", "daze", "dead", "deaf", "deal", "dean", "debt", "deck", "deed", "deem",
        "deep", "deer", "deft", "deli", "dell", "dent", "deny", "desk", "dice", "died",
        "diet", "dire", "disk", "diva", "dock", "dome", "done", "doom", "dork", "dorm",
        "dose", "dote", "down", "drab", "drag", "dram", "draw", "drew", "drip", "drop",
        "drug", "drum", "dual", "dubs", "dude", "duel", "dune", "dunk", "dusk", "dust",
        "each", "earl", "earn", "ease", "east", "eats", "edge", "edit", "eels", "egos",
        "elms", "emit", "envy", "epic", "erne", "etch", "even", "ever", "exam", "eyes",
        "face", "fact", "fade", "fail", "fain", "fake", "fall", "fang", "fare", "farm",
        "fast", "fate", "fawn", "faze", "fear", "feat", "feed", "feel", "feet", "fell",
        "felt", "fend", "fern", "fiat", "fife", "file", "fill", "film", "find", "fine",
        "fink", "fire", "fish", "fist", "flag", "flak", "flan", "flap", "flat", "flaw",
        "flea", "fled", "flew", "flip", "flit", "floe", "flog", "flop", "flow", "flue",
        "foal", "foam", "fobs", "fold", "fond", "font", "food", "fool", "foot", "ford",
        "fore", "fork", "form", "fort", "foul", "fowl", "fray", "free", "fret", "frog",
        "from", "fuel", "full", "fume", "fund", "furl", "fuse", "fuzz", "gabs", "gaga",
        "gage", "gale", "game", "gang", "garb", "gate", "gave", "gawk", "gaze", "gear",
        "geed", "gels", "gems", "gent", "germ", "gild", "gill", "gist", "glad", "glee",
        "glib", "glob", "glom", "glow", "glue", "glum", "gnar", "gnaw", "gobs", "gods",
        "gold", "golf", "gone", "goof", "gory", "gosh", "gown", "grab", "grad", "gram",
        "gray", "grep", "grew", "grid", "grim", "grin", "grip", "grit", "grog", "grow",
        "grub", "gull", "gulp", "gush", "gust", "guts", "hack", "hail", "hale", "hall",
        "halt", "hams", "hank", "hard", "hark", "harp", "hash", "haul", "have", "hawk",
        "haze", "head", "heal", "heap", "heat", "heel", "heft", "held", "help", "hemp",
        "hero", "high", "hike", "hill", "hilt", "hind", "hiss", "hive", "hoax", "hobo",
        "hock", "hold", "hole", "holt", "home", "hone", "hood", "hook", "hoop", "hoot",
        "hope", "horn", "host", "hour", "hove", "howl", "huge", "hulk", "hull", "hump",
        "hunk", "hurl", "hymn", "ibis", "idle", "inch", "iris", "iron", "isle", "itch",
        "jabs", "jack", "jade", "jail", "jamb", "java", "jeer", "jell", "jerk", "jest",
        "jibe", "jilt", "jive", "jolt", "joss", "jowl", "jump", "junk", "jury", "just",
        "keel", "keen", "kelp", "kick", "kill", "king", "kiss", "kite", "knob", "knot",
        "know", "lace", "lack", "lain", "lake", "lame", "land", "lane", "lank", "lard",
        "lark", "last", "lath", "laud", "lava", "lawn", "laze", "lazy", "lead", "leaf",
        "leak", "lean", "leap", "leer", "left", "lend", "lens", "lest", "levy", "liar",
        "lice", "lick", "lien", "lieu", "lily", "limb", "lime", "limp", "line", "link",
        "lion", "loin", "lore", "lose", "loud", "lout", "lure", "lurk", "lust", "lyre",
        "mace", "made", "mail", "maim", "main", "make", "male", "mall", "malt", "mama",
        "mana", "mane", "mast", "mate", "math", "maul", "maze", "mead", "meal", "meld",
        "melt", "mesa", "mesh", "mete", "mice", "mile", "milk", "mill", "mind", "mine",
        "mint", "moat", "mock", "mole", "molt", "monk", "moon", "moor", "mope", "morn",
        "mote", "mule", "mull", "murk", "musk", "mutt", "nabs", "nail", "name", "nape",
        "nark", "nave", "neap", "neck", "need", "nest", "news", "newt", "nibs", "nick",
        "nils", "nine", "nobs", "node", "noel", "norm", "nose", "nosh", "null", "numb",
        "oafs", "oaks", "oars", "oboe", "odds", "offs", "ogre", "oink", "omen", "once",
        "ones", "orbs", "orca", "ores", "over", "pact", "page", "paid", "pail", "pale",
        "palm", "pant", "park", "pave", "pawn", "peak", "peat", "peel", "peen", "peer",
        "pelt", "perk", "pest", "pick", "pier", "pike", "pill", "pine", "pink", "pint",
        "plod", "plop", "plot", "plow", "ploy", "plug", "plum", "plus", "poem", "poll",
        "polo", "pond", "pony", "pool", "poor", "pore", "port", "pose", "posh", "post",
        "pots", "pour", "prim", "prod", "prop", "pros", "prow", "puck", "pull", "pump",
        "pure", "push", "putt", "quay", "quip", "quit", "quiz", "race", "rack", "rail",
        "rain", "rake", "ramp", "rang", "rank", "rant", "rape", "rare", "rash", "rasp",
        "rave", "raze", "real", "reap", "reef", "reek", "rely", "rend", "rent", "rest",
        "rile", "rime", "rind", "riot", "rise", "risk", "road", "roam", "roar", "robe",
        "rock", "rode", "roll", "romp", "roof", "room", "root", "rope", "rose", "rout",
        "rove", "rude", "ruff", "rule", "rump", "rune", "ruse", "rush", "rusk", "rust",
        "sack", "safe", "sage", "sail", "sane", "sank", "sans", "sash", "save", "scab",
        "scam", "scar", "scud", "seam", "sect", "seed", "seep", "self", "send", "serf",
        "sewn", "shed", "shin", "ship", "shoe", "shop", "shot", "shun", "shut", "sigh",
        "silk", "sill", "silt", "sink", "site", "size", "skid", "skim", "skip", "slab",
        "slap", "slew", "slid", "slim", "slip", "slit", "slob", "slop", "slow", "slug",
        "slum", "slur", "smew", "smog", "snag", "snap", "snit", "snob", "snot", "snub",
        "soak", "soar", "sock", "soda", "soft", "soil", "sole", "some", "soot", "sort",
        "soul", "soup", "sour", "span", "spar", "spat", "spec", "sped", "spin", "spit",
        "spot", "spud", "spun", "stab", "star", "stay", "stem", "step", "stew", "stir",
        "stop", "stow", "stub", "stud", "stun", "such", "suit", "sulk", "sump", "sunk",
        "swab", "swam", "swap", "swat", "swig", "swim", "swum", "tack", "tail", "tale",
        "tame", "tamp", "tang", "tank", "tape", "task", "that", "thaw", "them", "thin",
        "thud", "tick", "tier", "tile", "tilt", "time", "tine", "tiny", "tips", "tire",
        "toad", "toil", "toll", "tomb", "tone", "tong", "took", "torn", "torr", "toss",
        "tour", "town", "trap", "trek", "trim", "trio", "trip", "trod", "troy", "true",
        "tube", "tuck", "tuna", "turf", "tusk", "tutu", "twig", "twin", "type", "ugly",
        "ulna", "undo", "upon", "urge", "used", "vane", "vats", "veal", "veer", "vent",
        "verb", "very", "vest", "veto", "vial", "vice", "view", "vile", "vine", "visa",
        "void", "vole", "volt", "wade", "waif", "wail", "wane", "ward", "warp", "wart",
        "wary", "wasp", "watt", "wavy", "weal", "wean", "welt", "wend", "whet", "whim",
        "whip", "wick", "wiki", "wild", "wile", "will", "wilt", "wimp", "wine", "wire",
        "wise", "wisp", "woke", "womb", "wont", "word", "wore", "worm", "worn", "wove",
        "wrap", "wren", "writ", "yams", "yaps", "yard", "yore", "zeal", "zest", "zinc",
    ],
    5: [  # 811 words
        "about", "above", "abuse", "actor", "acute", "admit", "adobe", "adult", "after", "agony",
        "agree", "ahead", "aided", "aioli", "aired", "alarm", "alien", "align", "alike", "allay",
        "allot", "allow", "alloy", "alone", "along", "altar", "amber", "amble", "amend", "among",
        "ample", "amuse", "angel", "anger", "angle", "angry", "annoy", "antic", "anvil", "apart",
        "apple", "apply", "aptly", "arbor", "ardor", "argue", "arise", "armor", "aroma", "arose",
        "array", "ashes", "aside", "asset", "atone", "attic", "audio", "audit", "augur", "aunts",
        "avoid", "await", "awake", "award", "aware", "awful", "badly", "bagel", "baked", "baker",
        "balmy", "bandy", "banjo", "baron", "basic", "basis", "batch", "beach", "beard", "beast",
        "began", "begun", "beige", "below", "berth", "bible", "binge", "birch", "birth", "black",
        "blade", "blame", "bland", "blank", "blare", "blast", "blaze", "bleed", "bless", "blind",
        "bliss", "block", "blood", "bloom", "blown", "board", "boast", "boggy", "boost", "booze",
        "boxer", "brace", "braid", "brain", "brake", "brand", "brave", "bread", "break", "breed",
        "bride", "brief", "bring", "brisk", "broth", "brown", "brush", "bully", "bunny", "cabin",
        "cable", "camel", "candy", "carry", "catch", "cause", "cedar", "chain", "chair", "chalk",
        "chaos", "chasm", "cheap", "cheat", "cheek", "chess", "chest", "child", "chime", "chimp",
        "choir", "chord", "chose", "churn", "cinch", "civic", "civil", "claim", "clang", "clank",
        "clash", "clasp", "class", "clean", "clear", "clerk", "cliff", "cling", "cloak", "close",
        "cloth", "cloud", "clout", "coast", "cobra", "comet", "comic", "comma", "coral", "couch",
        "could", "count", "court", "cover", "covet", "crack", "craft", "cramp", "crane", "crash",
        "craze", "crazy", "crest", "crime", "crimp", "crisp", "cross", "crowd", "crown", "cruel",
        "crumb", "crush", "crust", "cyber", "daddy", "daily", "dairy", "dance", "daunt", "dealt",
        "decay", "decoy", "delay", "depot", "derby", "devil", "dirty", "diver", "dizzy", "dodge",
        "dogma", "doing", "domed", "dopey", "doubt", "dough", "douse", "dowdy", "dowel", "drain",
        "drama", "drape", "drawn", "dread", "dream", "dress", "dried", "drift", "drink", "drive",
        "drone", "drove", "drown", "druid", "dusky", "dying", "eager", "early", "earth", "ebony",
        "edify", "eight", "elder", "elegy", "elite", "email", "ember", "empty", "endow", "enjoy",
        "epoch", "error", "evade", "evoke", "exact", "exalt", "exert", "exile", "exist", "exude",
        "faint", "fairy", "faith", "false", "fancy", "fatal", "feast", "fella", "ferry", "fetch",
        "fever", "fiery", "filed", "filet", "final", "finch", "fixed", "flair", "flame", "flank",
        "flare", "flash", "flask", "floor", "flora", "flour", "flown", "fluff", "flunk", "flute",
        "focus", "foggy", "foray", "forge", "forte", "forum", "freak", "fresh", "front", "froze",
        "fully", "gassy", "giant", "glass", "gloat", "globe", "gloom", "glory", "gloss", "glove",
        "glyph", "gnome", "going", "golem", "grabs", "grace", "grain", "grant", "grasp", "grate",
        "grave", "graze", "greed", "greet", "grief", "groan", "groin", "groom", "grove", "growl",
        "grown", "gruel", "gruff", "guile", "guise", "gusto", "hairy", "haven", "hawse", "hedge",
        "helix", "hence", "herbs", "heron", "honey", "horse", "hotel", "hound", "hover", "humid",
        "hurry", "ideal", "image", "infer", "ingot", "inner", "input", "inter", "inure", "islet",
        "issue", "ivory", "jalap", "joust", "juice", "juicy", "jumpy", "kayak", "knack", "knife",
        "knoll", "known", "label", "lance", "larva", "laser", "latch", "later", "lathe", "latte",
        "leach", "ledge", "legal", "lemon", "level", "lithe", "liver", "livid", "lobby", "lodge",
        "lofty", "logic", "loose", "lover", "lower", "loyal", "lucid", "magic", "major", "maker",
        "manga", "manor", "march", "marry", "mauve", "maxim", "mayor", "mercy", "merit", "merry",
        "might", "mince", "minim", "minor", "minus", "mirth", "miser", "modal", "model", "moody",
        "moral", "morph", "motto", "mound", "mourn", "mouth", "muddy", "mulch", "mural", "music",
        "nanny", "nasal", "nasty", "naval", "nervy", "never", "newly", "nicer", "night", "noble",
        "noise", "nonce", "notch", "novel", "ocean", "offer", "often", "olive", "onset", "opera",
        "opine", "optic", "orbit", "organ", "other", "otter", "ought", "outer", "owing", "oxide",
        "paddy", "paint", "panic", "paper", "parch", "party", "paste", "patch", "pause", "peach",
        "pearl", "penny", "peppy", "perch", "peril", "phase", "phone", "photo", "piano", "pilot",
        "pinch", "pitch", "pixie", "place", "plaid", "plain", "plane", "plank", "plant", "plate",
        "plaza", "plead", "pleat", "pluck", "plumb", "poach", "pound", "power", "prank", "prawn",
        "pride", "prime", "prior", "privy", "probe", "prong", "prose", "proud", "prove", "prowl",
        "prune", "psalm", "quaff", "quake", "qualm", "query", "quest", "quick", "quirk", "quota",
        "radar", "raise", "rally", "ramen", "range", "rapid", "raven", "reach", "ready", "realm",
        "rebel", "reign", "relax", "relay", "remit", "repay", "repel", "risky", "roomy", "rouge",
        "rough", "round", "rouse", "royal", "rumen", "sadly", "saint", "salve", "sandy", "sated",
        "sauce", "savvy", "scone", "score", "scour", "scout", "scowl", "seize", "serve", "setup",
        "seven", "shade", "shady", "shaft", "shale", "shame", "shape", "shark", "shawl", "sheen",
        "sheep", "sheer", "shelf", "shell", "shift", "shine", "shire", "shirt", "shoal", "shore",
        "showy", "shrub", "sigma", "silly", "sinew", "sixth", "sixty", "skill", "skull", "slant",
        "slave", "sleek", "sleet", "slick", "slide", "slope", "sloth", "smart", "smash", "smear",
        "smell", "smile", "smite", "smith", "smoky", "snare", "sneak", "snipe", "snowy", "sober",
        "solar", "solid", "solve", "sorry", "spade", "spare", "spark", "spawn", "speak", "speck",
        "speed", "spend", "spice", "spiky", "spill", "spine", "spire", "spoke", "spool", "sport",
        "spray", "squad", "squat", "stack", "stage", "stain", "stair", "stale", "stall", "stamp",
        "stand", "stare", "stark", "start", "stash", "state", "stays", "steal", "steam", "steel",
        "steep", "steer", "stern", "stiff", "still", "sting", "stock", "stoic", "stone", "stood",
        "stoop", "store", "stork", "storm", "story", "stout", "stove", "strap", "straw", "stray",
        "strut", "study", "sugar", "sunny", "super", "surge", "swamp", "swear", "sweep", "swept",
        "swift", "swipe", "swirl", "swoop", "table", "talon", "tapir", "tardy", "taste", "taunt",
        "tawny", "teach", "tense", "thane", "thank", "thick", "thief", "third", "thorn", "those",
        "three", "threw", "throe", "throw", "thump", "tiger", "tight", "tinge", "tired", "title",
        "token", "topaz", "totem", "touch", "tough", "tower", "toxic", "trace", "track", "trade",
        "trail", "train", "trait", "tramp", "trawl", "tread", "treat", "treks", "tribe", "trice",
        "trick", "tried", "trill", "troth", "trout", "truce", "truck", "trump", "trunk", "truss",
        "trust", "truth", "twice", "twine", "twirl", "twist", "ultra", "under", "unfed", "unify",
        "unite", "until", "upper", "usher", "valor", "valve", "vapor", "vault", "verse", "vicar",
        "video", "vigor", "visor", "vogue", "vouch", "wagon", "watch", "water", "weary", "weave",
        "wedge", "weedy", "weigh", "weird", "whale", "wheat", "wheel", "where", "while", "white",
        "whose", "widen", "wield", "wimpy", "witch", "witty", "wizen", "women", "world", "worry",
        "worth", "wound", "wrest", "yacht", "young", "youth", "zappy", "zebra", "zesty", "zilch",
        "zippy",
    ],
    6: [  # 430 words
        "aboard", "accent", "access", "accuse", "active", "actual", "adduce", "admire", "affect", "afford",
        "afraid", "agency", "agenda", "albeit", "amends", "amount", "animal", "ardent", "awhile", "beacon",
        "beauty", "before", "begins", "belief", "bestow", "blanch", "bleach", "blends", "blurry", "bodily",
        "border", "bounce", "branch", "breeze", "bright", "broken", "burden", "bypass", "canopy", "castle",
        "cattle", "caught", "change", "charge", "chilly", "choice", "chrome", "circle", "citrus", "clause",
        "clever", "client", "closed", "clutch", "coarse", "cobalt", "combat", "common", "cousin", "creamy",
        "credit", "crispy", "cursor", "custom", "cymbal", "dabble", "dagger", "damage", "dampen", "dangle",
        "darken", "dazzle", "debris", "decade", "decent", "deeply", "defeat", "define", "depict", "design",
        "differ", "dilute", "direct", "docile", "dollar", "domain", "donkey", "dreary", "drench", "driven",
        "drying", "during", "earthy", "easily", "edible", "effect", "either", "elbows", "embark", "empire",
        "employ", "ending", "endure", "engage", "enjoin", "enough", "enrich", "ensure", "entire", "equity",
        "escort", "evenly", "excite", "exempt", "exotic", "expand", "expect", "extend", "fabled", "factor",
        "fairly", "fallen", "fallow", "famine", "famous", "feline", "fellow", "fender", "ferret", "fierce",
        "filter", "finish", "firing", "firmly", "flashy", "flinch", "floppy", "flower", "fluent", "flying",
        "follow", "forage", "forego", "formal", "fossil", "foster", "freely", "frozen", "frugal", "fungus",
        "future", "gained", "galley", "gamble", "garlic", "gentle", "giggle", "gilded", "glossy", "goalie",
        "goblin", "golden", "goober", "gothic", "gravel", "grieve", "groovy", "grudge", "grumpy", "grunge",
        "guilty", "guitar", "gutter", "hamlet", "handle", "happen", "hardly", "hearty", "herald", "highly",
        "honest", "hugely", "hunger", "hurtle", "hustle", "hybrid", "hypnot", "ignite", "immune", "impact",
        "insane", "insect", "invade", "invoke", "island", "jagged", "jammed", "jangle", "jaunty", "jigsaw",
        "joyful", "joyous", "jumble", "kernel", "kettle", "kindle", "kingly", "knight", "latest", "lather",
        "lavish", "lawyer", "lively", "loathe", "locust", "lonely", "loosen", "loudly", "lovely", "lucent"'
        "lugged", "luster", "magnet", "manage", "marble", "market", "meadow", "midday", "mingle", "mishap",
        "missed", "modern", "modest", "module", "monkey", "mosaic", "motley", "muster", "myself", "mythic",
        "narrow", "nearly", "neatly", "nibble", "nickel", "nimble", "noodle", "normal", "nudged", "nuzzle",
        "obtain", "oddity", "office", "onward", "opaque", "orange", "orchid", "ordeal", "output", "oyster",
        "painty", "palace", "patrol", "patter", "pillar", "pirate", "placid", "plague", "planet", "plenty",
        "pliant", "pocket", "pollen", "portal", "poster", "potent", "prefer", "pretty", "profit", "prompt",
        "proper", "purple", "pursue", "puzzle", "radius", "rather", "rattle", "reason", "recent", "reckon",
        "reduce", "refuge", "remind", "remote", "render", "repair", "rescue", "reside", "resist", "result",
        "return", "reveal", "rhythm", "ribbon", "riches", "ridden", "riddle", "ripple", "robust", "roster",
        "rotate", "rugged", "rumble", "saddle", "safety", "samite", "savage", "scarce", "scorch", "scream",
        "screen", "scribe", "scroll", "secure", "select", "serene", "settle", "shadow", "shaman", "shrine",
        "simple", "single", "sketch", "slight", "sliver", "smooth", "sneeze", "socket", "soften", "solemn",
        "soothe", "sorted", "sought", "source", "speech", "sphere", "splice", "spoken", "spring", "squash",
        "stable", "stanza", "starve", "steady", "sticky", "stitch", "stolen", "stormy", "stream", "strict",
        "stride", "strike", "string", "strong", "struck", "studio", "subtle", "suffer", "summit", "sunlit",
        "superb", "supply", "surely", "swivel", "symbol", "tablet", "tackle", "talent", "tangle", "tartan",
        "taught", "tender", "tether", "thorny", "thrive", "tickle", "timber", "timely", "toasty", "toggle",
        "traced", "travel", "triple", "trophy", "turtle", "tuxedo", "twenty", "typify", "unborn", "unfair",
        "unfold", "unholy", "unkind", "unless", "upbeat", "uplift", "uproot", "upward", "usable", "useful",
        "vainly", "vanish", "velvet", "viable", "vision", "visual", "vivant", "wander", "warmth", "watery",
        "wheeze", "wholly", "wildly", "winded", "wisdom", "wooden", "worsen", "worthy", "yeoman", "zombie",
    ],
    7: [  # 307 words
        "abandon", "abridge", "absence", "adjourn", "advance", "agitate", "ailment", "alcohol", "amazing", "anatomy",
        "ancient", "appoint", "arrange", "article", "athlete", "attract", "auction", "average", "balance", "barrier",
        "bedroom", "benefit", "bicycle", "binding", "blanket", "blatant", "blossom", "bracket", "bravely", "breadth",
        "breathe", "brigade", "brother", "brought", "cabinet", "captain", "captive", "ceiling", "century", "chapter",
        "classic", "climate", "combine", "comfort", "command", "comment", "compact", "complex", "concern", "confine",
        "conform", "content", "context", "costume", "cottage", "council", "country", "courage", "culprit", "culture",
        "curious", "current", "dealing", "declare", "decline", "default", "deficit", "delight", "deposit", "descend",
        "deserve", "despite", "destroy", "develop", "devious", "diamond", "discard", "distant", "distort", "disturb",
        "dormant", "drawing", "drought", "durable", "dynamic", "eastern", "ecology", "educate", "embassy", "empower",
        "enchant", "endless", "enforce", "enhance", "enlarge", "episode", "examine", "exclaim", "exclude", "exhaust",
        "exhibit", "expense", "explain", "explore", "express", "extreme", "factory", "fantasy", "faraway", "fashion",
        "feature", "fertile", "fiction", "finding", "fishing", "fitting", "fixture", "flavour", "flowing", "flutter",
        "focused", "foreign", "forever", "freedom", "freight", "freshly", "furnish", "further", "gallant", "gateway",
        "general", "genuine", "glacier", "glimmer", "glimpse", "glitter", "godlike", "grading", "granite", "grocery",
        "grownup", "habitat", "harvest", "healthy", "heroine", "hideous", "highest", "highway", "hoisted", "holding",
        "hopeful", "hostile", "however", "humming", "hundred", "impulse", "intense", "invoice", "involve", "isolate",
        "journey", "justice", "kingdom", "knowing", "landing", "largely", "lasting", "lateral", "leading", "leisure",
        "lengthy", "literal", "logical", "loyalty", "mankind", "mapping", "massive", "medical", "meeting", "mention",
        "migrate", "miracle", "mission", "mixture", "monster", "monthly", "morning", "mystery", "natural", "neglect",
        "neutral", "nightly", "notable", "noticed", "novelty", "nowhere", "obscure", "obvious", "offered", "organic",
        "outcome", "outlast", "outline", "outside", "overall", "painful", "panther", "partner", "passage", "pathway",
        "patient", "pattern", "payment", "pension", "perfect", "persist", "picture", "pioneer", "plastic", "playful",
        "plunder", "pointed", "precise", "premium", "present", "prevent", "primary", "process", "produce", "profile",
        "program", "project", "protect", "provide", "publish", "purpose", "qualify", "quickly", "quietly", "radical",
        "raising", "ranking", "reality", "rebuild", "recover", "reflect", "refresh", "rejoice", "release", "relying",
        "remains", "renewal", "replace", "request", "reserve", "resolve", "respect", "restore", "roughly", "royalty",
        "scholar", "seaside", "servant", "setting", "shortly", "silence", "sincere", "skyline", "slender", "society",
        "somehow", "special", "station", "storage", "stretch", "student", "stumble", "subject", "suspend", "swiftly",
        "tangled", "texture", "theater", "through", "toppled", "tourist", "towards", "tragedy", "triumph", "trouble",
        "turnout", "typical", "uncover", "uniform", "unknown", "unusual", "venture", "village", "warrior", "welcome",
        "western", "whereas", "wishing", "wonders", "working", "written", "younger",
    ],
}

GREEN  = "🟩"
YELLOW = "🟨"
BLACK  = "⬛"

active_games: dict[int, dict] = {}

# ─── LEADERBOARD ─────────────────────────────────────────────
# { user_id: { "name": str, "wins": int, "losses": int,
#              "total_guesses": int, "best": int, "streak": int,
#              "max_streak": int, "points": int } }
leaderboard: dict[int, dict] = {}

# ─── TÍNH ĐIỂM ───────────────────────────────────────────────
# Điểm cơ bản theo số lượt đoán
BASE_POINTS = {1: 100, 2: 80, 3: 60, 4: 40, 5: 20, 6: 10}
# Bonus theo độ dài từ (4 chữ = 0, 5 = +5, 6 = +10, 7 = +20)
LENGTH_BONUS = {4: 0, 5: 5, 6: 10, 7: 20}
# Bonus chuỗi thắng: +5 điểm mỗi ván liên tiếp (tính sau khi cộng streak)
STREAK_BONUS = 5

def calc_points(tries: int, word_len: int, streak: int) -> dict:
    base    = BASE_POINTS.get(tries, 0)
    length  = LENGTH_BONUS.get(word_len, 0)
    streak_bonus = (streak - 1) * STREAK_BONUS  # streak=1 thì không có bonus
    total   = base + length + streak_bonus
    return {"base": base, "length": length, "streak_bonus": streak_bonus, "total": total}

def lb_update_win(uid: int, name: str, tries: int, word_len: int):
    p = leaderboard.setdefault(uid, {
        "name": name, "wins": 0, "losses": 0,
        "total_guesses": 0, "best": 999, "streak": 0, "max_streak": 0, "points": 0
    })
    p["name"]           = name
    p["wins"]          += 1
    p["total_guesses"] += tries
    p["best"]           = min(p["best"], tries)
    p["streak"]        += 1
    p["max_streak"]     = max(p["max_streak"], p["streak"])
    pts = calc_points(tries, word_len, p["streak"])
    p["points"] += pts["total"]
    return pts

def lb_update_loss(uid: int, name: str):
    p = leaderboard.setdefault(uid, {
        "name": name, "wins": 0, "losses": 0,
        "total_guesses": 0, "best": 999, "streak": 0, "max_streak": 0, "points": 0
    })
    p["name"]    = name
    p["losses"] += 1
    p["streak"]  = 0

# ─── LOGIC ───────────────────────────────────────────────────
def evaluate_guess(secret: str, guess: str) -> list[str]:
    wlen = len(secret)
    result = [BLACK] * wlen
    secret_chars = list(secret)
    guess_chars  = list(guess)

    for i in range(wlen):
        if guess_chars[i] == secret_chars[i]:
            result[i] = GREEN
            secret_chars[i] = None
            guess_chars[i]  = None

    for i in range(wlen):
        if guess_chars[i] is not None and guess_chars[i] in secret_chars:
            result[i] = YELLOW
            secret_chars[secret_chars.index(guess_chars[i])] = None

    return result


def build_board(guesses: list[dict], word_len: int) -> str:
    lines = []
    for entry in guesses:
        emoji_row  = " ".join(entry["result"])
        letter_row = " ".join(f"`{c.upper()}`" for c in entry["guess"])
        lines.append(f"{emoji_row}\n{letter_row}")
    empty_row = " ".join(["▫️"] * word_len)
    for _ in range(MAX_GUESSES - len(guesses)):
        lines.append(empty_row)
    return "\n".join(lines)


def build_keyboard(guesses: list[dict]) -> str:
    used: dict[str, str] = {}
    for entry in guesses:
        for ch, res in zip(entry["guess"], entry["result"]):
            prev = used.get(ch)
            if prev == GREEN:
                continue
            if res == GREEN or prev != YELLOW:
                used[ch] = res

    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    lines = []
    for row in rows:
        parts = []
        for ch in row:
            state = used.get(ch.lower())
            if state == GREEN:
                parts.append(f"🟩{ch}")
            elif state == YELLOW:
                parts.append(f"🟨{ch}")
            elif state == BLACK:
                parts.append(f"⬛{ch}")
            else:
                parts.append(f"⬜{ch}")
        lines.append(" ".join(parts))
    return "\n".join(lines)


def make_embed(user, game, message="", color=discord.Color.blurple()):
    wlen = len(game["word"])
    guessed = len(game["guesses"])
    last_guess = game["guesses"][-1]["guess"].upper() if game["guesses"] else None

    desc = f"👤 **{user.display_name}** đang chơi\n"
    desc += f"Từ **{wlen}** chữ cái — lượt **{guessed}/{MAX_GUESSES}**"
    if last_guess:
        desc += f"\n✏️ Vừa đoán: **{last_guess}**"

    embed = discord.Embed(
        title="🟩 WORDLE",
        description=desc,
        color=color,
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="📋 Bảng đoán", value=build_board(game["guesses"], wlen), inline=False)
    if message:
        embed.add_field(name="💬", value=message, inline=False)
    return embed


# ─── BOT ─────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# thread_id -> user_id (để biết thread nào của ai)
thread_games: dict[int, int] = {}


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔄 Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Sync error: {e}")


# ─── XỬ LÝ TIN NHẮN TRONG THREAD ────────────────────────────
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    # Chỉ xử lý trong thread đang có ván chơi
    if not isinstance(message.channel, discord.Thread):
        await bot.process_commands(message)
        return

    thread_id = message.channel.id
    if thread_id not in thread_games:
        await bot.process_commands(message)
        return

    uid = thread_games[thread_id]

    # Chỉ người chơi mới được đoán
    if message.author.id != uid:
        return

    if uid not in active_games or active_games[uid]["finished"]:
        return

    word = message.content.strip().lower()
    game = active_games[uid]
    wlen = len(game["word"])

    # Bỏ qua nếu không phải từ hợp lệ (có thể là lệnh slash hoặc tin nhắn khác)
    if not word.isalpha():
        return
    if len(word) != wlen:
        await message.reply(f"❌ Từ phải đúng **{wlen}** chữ cái!", mention_author=False)
        return

    result = evaluate_guess(game["word"], word)
    game["guesses"].append({"guess": word, "result": result})

    if all(r == GREEN for r in result):
        game["finished"] = True
        tries     = len(game["guesses"])
        pts       = lb_update_win(uid, message.author.display_name, tries, wlen)
        ratings   = {1:"🤯 Thiên tài!", 2:"🏆 Xuất sắc!", 3:"🎉 Tuyệt vời!",
                     4:"😄 Tốt lắm!", 5:"😅 Suýt rồi!", 6:"😮‍💨 May mắn!"}
        streak    = leaderboard[uid]["streak"]
        total_pts = leaderboard[uid]["points"]

        pt_lines = [f"🎯 Cơ bản: **+{pts['base']}**"]
        if pts["length"] > 0:
            pt_lines.append(f"📏 Từ dài: **+{pts['length']}**")
        if pts["streak_bonus"] > 0:
            pt_lines.append(f"🔥 Chuỗi x{streak}: **+{pts['streak_bonus']}**")
        pt_lines.append(f"✨ Tổng ván này: **+{pts['total']} điểm**")
        pt_lines.append(f"💎 Tổng điểm: **{total_pts}**")

        msg = f"{ratings.get(tries,'👍')} Đúng rồi! Từ là **{game['word'].upper()}** — {tries}/{MAX_GUESSES} lượt!\n"
        msg += "\n".join(pt_lines)
        embed = make_embed(message.author, game, msg, discord.Color.gold())
        await message.channel.send(embed=embed)
        # Đóng thread sau khi thắng
        await message.channel.edit(archived=True, locked=False)
        del thread_games[thread_id]
        return

    if len(game["guesses"]) >= MAX_GUESSES:
        game["finished"] = True
        lb_update_loss(uid, message.author.display_name)
        embed = make_embed(message.author, game,
            f"😞 Hết lượt! Từ đúng là **{game['word'].upper()}**. Dùng `/wordle` chơi lại.",
            discord.Color.red())
        await message.channel.send(embed=embed)
        await message.channel.edit(archived=True, locked=False)
        del thread_games[thread_id]
        return

    embed = make_embed(message.author, game,
        f"Còn **{MAX_GUESSES - len(game['guesses'])}** lượt. Tiếp tục gõ từ!",
        discord.Color.blurple())
    await message.channel.send(embed=embed)


# ─── LỆNH /wordle ─────────────────────────────────────────────
@bot.tree.command(name="wordle", description="Bắt đầu ván Wordle mới (tạo thread riêng)")
async def wordle_start(interaction: discord.Interaction):
    uid = interaction.user.id

    # Kiểm tra đang có ván dở
    if uid in active_games and not active_games[uid]["finished"]:
        await interaction.response.send_message(
            "⚠️ Bạn đang có ván dang dở! Vào thread cũ để tiếp tục hoặc dùng `/quit` để bỏ.",
            ephemeral=True)
        return

    # Chỉ tạo thread trong kênh text thường
    if not isinstance(interaction.channel, discord.TextChannel):
        await interaction.response.send_message(
            "❌ Chỉ dùng được trong kênh text thường!", ephemeral=True)
        return

    wlen = random.choice(list(WORD_LIST.keys()))
    word = random.choice(WORD_LIST[wlen])
    active_games[uid] = {"word": word, "guesses": [], "finished": False}

    await interaction.response.defer()

    # Tạo thread công khai
    thread = await interaction.channel.create_thread(
        name=f"🟩 Wordle của {interaction.user.display_name}",
        type=discord.ChannelType.public_thread,
        auto_archive_duration=60
    )
    thread_games[thread.id] = uid

    embed = make_embed(interaction.user, active_games[uid],
        f"🎮 Ván mới bắt đầu! Từ có **{wlen}** chữ cái — **{MAX_GUESSES}** lượt.\n"
        f"Gõ từ bình thường vào đây để đoán!\n"
        f"Dùng `/quit` nếu muốn bỏ cuộc.",
        discord.Color.green())

    await thread.send(f"{interaction.user.mention}", embed=embed)
    await interaction.followup.send(
        f"✅ Đã tạo thread cho {interaction.user.mention}! → {thread.mention}",
        ephemeral=False)


# ─── LỆNH /quit ───────────────────────────────────────────────
@bot.tree.command(name="quit", description="Bỏ cuộc ván hiện tại")
async def wordle_quit(interaction: discord.Interaction):
    uid = interaction.user.id
    if uid not in active_games or active_games[uid]["finished"]:
        await interaction.response.send_message("❌ Không có ván nào đang chạy.", ephemeral=True)
        return
    secret = active_games[uid]["word"]
    active_games[uid]["finished"] = True

    # Xóa thread khỏi danh sách
    tid = next((t for t, u in thread_games.items() if u == uid), None)
    if tid:
        del thread_games[tid]
        try:
            thread = bot.get_channel(tid)
            if thread:
                await thread.send(f"🏳️ **{interaction.user.display_name}** bỏ cuộc! Từ đúng là **{secret.upper()}**.")
                await thread.edit(archived=True, locked=False)
        except:
            pass

    await interaction.response.send_message(
        f"🏳️ **{interaction.user.display_name}** bỏ cuộc! Từ đúng là **{secret.upper()}**.")


# ─── LỆNH /hint ───────────────────────────────────────────────
@bot.tree.command(name="hint", description="Gợi ý chữ cái đầu tiên (chỉ bạn thấy)")
async def wordle_hint(interaction: discord.Interaction):
    uid = interaction.user.id
    if uid not in active_games or active_games[uid]["finished"]:
        await interaction.response.send_message("❌ Không có ván nào đang chạy.", ephemeral=True)
        return
    first = active_games[uid]["word"][0].upper()
    await interaction.response.send_message(f"💡 Chữ đầu tiên là **{first}**", ephemeral=True)


# ─── LỆNH /leaderboard ────────────────────────────────────────
@bot.tree.command(name="leaderboard", description="Xem bảng xếp hạng Wordle")
async def wordle_leaderboard(interaction: discord.Interaction):
    if not leaderboard:
        await interaction.response.send_message("📭 Chưa có ai chơi cả! Dùng `/wordle` để bắt đầu.", ephemeral=True)
        return

    sorted_lb = sorted(leaderboard.items(), key=lambda x: -x[1]["points"])
    medals = ["🥇", "🥈", "🥉"]
    lines  = []
    for i, (uid, p) in enumerate(sorted_lb[:10]):
        medal   = medals[i] if i < 3 else f"`#{i+1}`"
        wins    = p["wins"]
        losses  = p["losses"]
        total   = wins + losses
        winrate = int(wins / total * 100) if total > 0 else 0
        avg     = f"{p['total_guesses']/wins:.1f}" if wins > 0 else "—"
        best    = p["best"] if p["best"] < 999 else "—"
        streak  = p["max_streak"]
        points  = p["points"]
        name    = p["name"]
        lines.append(
            f"{medal} **{name}** — 💎 **{points} điểm**\n"
            f"　✅ {wins}W  ❌ {losses}L  📊 {winrate}%  ⚡avg {avg}  ⭐best {best}  🔥{streak}"
        )

    embed = discord.Embed(
        title="🏆 Bảng Xếp Hạng WORDLE",
        description="\n\n".join(lines),
        color=discord.Color.gold(),
        timestamp=datetime.utcnow()
    )
    embed.add_field(
        name="📐 Cách tính điểm",
        value="🎯 Lượt 1-6: 100/80/60/40/20/10đ\n📏 Từ 5/6/7 chữ: +5/+10/+20đ\n🔥 Chuỗi thắng: +5đ/ván",
        inline=False
    )
    embed.set_footer(text=f"Top {min(10, len(sorted_lb))} người chơi • Xếp theo tổng điểm")
    await interaction.response.send_message(embed=embed)


# ─── LỆNH /mystats ────────────────────────────────────────────
@bot.tree.command(name="mystats", description="Xem thống kê cá nhân của bạn")
async def wordle_mystats(interaction: discord.Interaction):
    uid = interaction.user.id
    if uid not in leaderboard:
        await interaction.response.send_message("📭 Bạn chưa chơi ván nào! Dùng `/wordle` để bắt đầu.", ephemeral=True)
        return

    p       = leaderboard[uid]
    wins    = p["wins"]
    losses  = p["losses"]
    total   = wins + losses
    winrate = int(wins / total * 100) if total > 0 else 0
    avg     = f"{p['total_guesses']/wins:.1f}" if wins > 0 else "—"
    best    = p["best"] if p["best"] < 999 else "—"

    sorted_lb = sorted(leaderboard.items(), key=lambda x: -x[1]["points"])
    rank = next((i+1 for i, (u, _) in enumerate(sorted_lb) if u == uid), "?")

    embed = discord.Embed(
        title=f"📊 Thống kê của {interaction.user.display_name}",
        color=discord.Color.blurple(),
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.add_field(name="🏅 Hạng",           value=f"#{rank} / {len(leaderboard)}", inline=True)
    embed.add_field(name="💎 Tổng điểm",       value=str(p["points"]),  inline=True)
    embed.add_field(name="✅ Thắng",            value=str(wins),         inline=True)
    embed.add_field(name="❌ Thua",             value=str(losses),       inline=True)
    embed.add_field(name="📊 Tỉ lệ thắng",     value=f"{winrate}%",     inline=True)
    embed.add_field(name="⚡ Avg lượt đoán",   value=avg,               inline=True)
    embed.add_field(name="⭐ Best",             value=str(best),         inline=True)
    embed.add_field(name="🔥 Chuỗi hiện tại",  value=str(p["streak"]),     inline=True)
    embed.add_field(name="🔥 Chuỗi cao nhất",  value=str(p["max_streak"]), inline=True)
    await interaction.response.send_message(embed=embed)


# ─── LỆNH /wordlehelp ─────────────────────────────────────────
@bot.tree.command(name="wordlehelp", description="Hướng dẫn chơi Wordle")
async def wordle_help(interaction: discord.Interaction):
    embed = discord.Embed(title="📖 Hướng dẫn WORDLE", color=discord.Color.teal())
    embed.add_field(name="🎯 Mục tiêu",
        value=f"Đoán từ tiếng Anh **4-7** chữ cái trong **{MAX_GUESSES}** lượt.\nMỗi ván độ dài từ được chọn **ngẫu nhiên**!", inline=False)
    embed.add_field(name="🎮 Cách chơi",
        value="1. Dùng `/wordle` để tạo thread\n2. Gõ từ thẳng vào thread — không cần lệnh!\n3. Mọi người có thể vào xem và cổ vũ", inline=False)
    embed.add_field(name="🎨 Màu sắc",
        value=f"{GREEN} Đúng chữ, đúng vị trí\n{YELLOW} Đúng chữ, sai vị trí\n{BLACK} Không có trong từ",
        inline=False)
    embed.add_field(name="📝 Lệnh",
        value="`/wordle` · `/hint` · `/quit`\n`/leaderboard` · `/mystats` · `/wordlehelp`", inline=False)
    await interaction.response.send_message(embed=embed)


# ─── CHẠY ────────────────────────────────────────────────────
bot.run(TOKEN)
