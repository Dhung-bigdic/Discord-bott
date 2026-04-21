import discord
from discord.ext import commands
import random
import os

# ─── CẤU HÌNH ────────────────────────────────────────────────
TOKEN = os.environ.get("DISCORD_TOKEN")  # Railway dùng DISCORD_TOKEN

MAX_GUESSES = 6

# ─── WORDLIST (rút gọn - bạn có thể thêm từ sau) ────────────
WORD_LIST = {
    4: ["able", "acid", "also", "area", "army", "away", "baby", "back", "ball", "band", "bank", "bass", "bear", "beat", "bell", "best", "bike", "bird", "bite", "blue", "boat", "body", "book", "both", "bowl", "boy", "bread", "break", "bright", "bring", "brown", "build", "busy", "call", "calm", "came", "camp", "card", "care", "case", "cash", "cast", "cave", "cent", "chain", "chair", "chalk", "chance", "change", "chant", "chaos", "charm", "chart", "chase", "cheap", "cheat", "check", "cheek", "cheer", "chess", "chest", "chew", "chick", "chief", "child", "chill", "chip", "choke", "chop", "chord", "chore", "chose", "chuck", "chunk", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloth", "cloud", "coach", "coast", "coat", "code", "coin", "cold", "come", "cook", "cool", "copy", "corn", "cost", "cough", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crush", "curve", "cycle"],
    5: ["about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "array", "aside", "asset", "avoid", "award", "aware", "badly", "baker", "bases", "basic", "bear", "beast", "begin", "being", "below", "bench", "birth", "black", "blame", "blind", "block", "blood", "board", "boost", "bound", "brain", "brand", "brave", "bread", "break", "breed", "brief", "bring", "broad", "brown", "build", "built", "buyer", "cable", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase", "cheap", "check", "chest", "chief", "child", "china", "chose", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloud", "coach", "coast", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crush", "curve", "cycle"],
    6: ["access", "across", "action", "active", "actual", "advice", "affect", "agency", "almost", "always", "animal", "annual", "answer", "anyone", "appeal", "appear", "around", "arrive", "artist", "assume", "attack", "attend", "author", "become", "before", "behind", "belief", "belong", "bridge", "bright", "brought", "budget", "center", "central", "charge", "choice", "choose", "church", "circle", "client", "closed", "coffee", "column", "combat", "coming", "common", "comply", "cotton", "county", "course", "create", "credit", "crisis", "crucial", "culture", "damage", "danger", "debate", "decade", "decide", "defeat", "defend", "define", "degree", "demand", "depend", "deputy", "desert", "design", "desire", "detail", "detect", "device", "differ", "dinner", "direct", "doctor", "dollar", "domain", "double", "driving", "during", "easily", "eating", "editor", "effect", "effort", "eighth", "either", "elect", "eleven", "emerge", "empire", "employ", "enable", "ending", "energy", "engage", "engine", "enough", "ensure", "entire", "entity", "enviro", "equity", "escape", "estate", "evening", "ever", "every", "exact", "exceed", "except", "excess", "excuse", "exempt", "exert", "exhaust", "expand", "expect", "expire", "explain", "expose", "extend", "extent", "extreme", "fabric", "factor", "failed", "fairly", "fallen", "family", "famous", "father", "fellow", "female", "figure", "finger", "finish", "firmly", "flight", "flower", "follow", "forced", "forest", "forget", "formal", "former", "forward", "fossil", "foster", "fought", "fourth", "frame", "freeze", "french", "friday", "fridge", "friend", "fright", "frozen", "future", "garden", "gender", "giant", "golden", "ground", "growth", "guilty", "handle", "happen", "health", "hearing", "heavily", "height", "helpful", "herself", "hidden", "honest", "hundred", "husband", "illegal", "imagine", "impact", "import", "income", "indeed", "injury", "inside", "insist", "intend", "intent", "invest", "involve", "island", "itself", "jacket", "joint", "judge", "knowing", "labour", "land", "language", "lawyer", "leader", "league", "legacy", "legal", "legend", "leisure", "letter", "level", "liable", "liberal", "likely", "limit", "linear", "liquid", "listen", "little", "living", "loan", "local", "locate", "lock", "logic", "long", "look", "loose", "lose", "loss", "loud", "love", "lovely", "low", "lower", "luck", "lucky", "lunch", "lung", "lying", "magic", "major", "maker", "manage", "manner", "manufacture", "many", "market", "mass", "master", "match", "maybe", "mayor", "measure", "media", "medical", "meeting", "member", "memory", "mention", "mere", "middle", "might", "mighty", "mild", "mile", "military", "milk", "million", "mind", "minimum", "minor", "minute", "mirror", "missing", "mistake", "modern", "module", "moment", "money", "month", "moral", "morning", "mother", "motion", "motor", "mountain", "mouse", "mouth", "move", "movement", "movie", "much", "multiple", "murder", "muscle", "museum", "music", "mutual", "myself", "mystery", "myth", "narrow", "nation", "native", "nature", "nearly", "neat", "necessary", "neck", "need", "negative", "neither", "nervous", "net", "network", "never", "news", "next", "nice", "night", "noble", "noise", "none", "nor", "north", "nose", "note", "nothing", "notice", "novel", "nuclear", "number", "nurse", "nut", "object", "observe", "obtain", "obvious", "occasion", "occur", "ocean", "odd", "offer", "office", "often", "oil", "okay", "old", "on", "once", "one", "only", "onto", "open", "operate", "opinion", "oppose", "option", "or", "orange", "order", "ordinary", "other", "otherwise", "ought", "our", "out", "outcome", "outside", "over", "overall", "own", "owner", "pack", "package", "page", "pain", "paint", "pair", "palace", "pale", "panel", "paper", "parent", "park", "part", "particular", "party", "pass", "past", "path", "patient", "pattern", "pause", "pay", "peace", "peak", "perform", "period", "permit", "person", "phone", "photo", "physical", "pick", "picture", "piece", "place", "plan", "plant", "play", "player", "please", "pleasure", "plenty", "plus", "point", "police", "policy", "political", "poor", "pop", "popular", "port", "pose", "position", "positive", "possible", "post", "pot", "potential", "pound", "power", "practice", "prepare", "present", "press", "pressure", "pretty", "prevent", "price", "prime", "principal", "print", "priority", "prison", "private", "probably", "problem", "proceed", "process", "produce", "product", "profile", "program", "progress", "project", "property", "propose", "protect", "prove", "provide", "public", "pull", "purpose", "push", "put", "quality", "quarter", "question", "quick", "quiet", "quite", "race", "radio", "raise", "range", "rate", "rather", "reach", "read", "ready", "real", "reality", "realize", "really", "reason", "recall", "receive", "recent", "record", "red", "reduce", "refer", "reflect", "region", "relate", "relationship", "relative", "relax", "release", "remain", "remember", "remove", "rent", "repeat", "replace", "reply", "report", "represent", "require", "research", "resource", "respect", "respond", "rest", "result", "return", "reveal", "rich", "ride", "right", "ring", "rise", "risk", "road", "rock", "role", "roll", "room", "root", "rose", "rule", "run", "safe", "same", "save", "say", "scene", "school", "science", "score", "sea", "season", "seat", "second", "section", "security", "see", "seed", "seek", "sell", "send", "senior", "sense", "series", "serious", "serve", "service", "set", "settle", "seven", "several", "sex", "sexual", "shake", "shall", "shape", "share", "she", "sheet", "ship", "shoot", "shop", "short", "shot", "should", "show", "side", "sight", "sign", "signal", "simple", "since", "sing", "single", "sir", "sit", "site", "situation", "six", "size", "skill", "skin", "small", "smile", "so", "social", "soft", "soldier", "solution", "some", "someone", "something", "son", "song", "soon", "sorry", "sort", "sound", "source", "south", "space", "speak", "special", "specific", "speed", "spend", "sport", "spring", "staff", "stage", "stand", "standard", "star", "start", "state", "station", "stay", "step", "still", "stock", "stop", "store", "story", "straight", "strange", "street", "strength", "stress", "stretch", "strike", "string", "strong", "structure", "student", "study", "stuff", "style", "subject", "submit", "success", "such", "sudden", "suggest", "summer", "sun", "support", "sure", "surprise", "take", "talk", "task", "tax", "teach", "team", "tell", "ten", "tend", "term", "test", "than", "thank", "that", "the", "their", "them", "themselves", "then", "theory", "there", "therefore", "these", "they", "thin", "thing", "think", "third", "this", "those", "though", "thought", "thousand", "three", "through", "throughout", "throw", "thus", "time", "to", "today", "together", "tomorrow", "tone", "too", "top", "total", "touch", "toward", "town", "track", "trade", "traditional", "train", "travel", "treat", "tree", "trial", "trip", "trouble", "true", "truth", "try", "turn", "tv", "two", "type", "under", "understand", "unit", "unless", "until", "up", "upon", "use", "usual", "value", "various", "very", "view", "village", "visit", "voice", "wait", "walk", "wall", "want", "war", "watch", "water", "way", "we", "wear", "week", "weight", "welcome", "well", "west", "what", "whatever", "wheel", "when", "where", "whether", "which", "while", "white", "who", "whole", "whom", "whose", "why", "wide", "wife", "will", "win", "wind", "window", "wish", "with", "within", "without", "woman", "wonder", "word", "work", "world", "worry", "would", "write", "wrong", "year", "yes", "yesterday", "yet", "you", "young", "your", "yourself"],
}

GREEN  = "🟩"
YELLOW = "🟨"
BLACK  = "⬛"

active_games: dict[int, dict] = {}

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
    embed.add_field(name="⌨️ Bàn phím",  value=build_keyboard(game["guesses"]), inline=False)
    if message:
        embed.add_field(name="💬", value=message, inline=False)
    return embed

# ─── BOT ─────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True  # QUAN TRỌNG: để đọc nội dung tin nhắn
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công: {bot.user}")
    print(f"📡 Đang hoạt động trên {len(bot.guilds)} server")

@bot.event
async def on_message(message):
    # Không phản hồi tin nhắn của chính bot
    if message.author == bot.user:
        return
    
    uid = message.author.id
    word = message.content.lower().strip()
    
    # Chỉ xử lý nếu người dùng đang có game active
    if uid in active_games and not active_games[uid]["finished"]:
        game = active_games[uid]
        wlen = len(game["word"])
        
        # Kiểm tra nếu tin nhắn là từ có độ dài phù hợp
        if len(word) == wlen and word.isalpha():
            # Xử lý đoán từ
            result = evaluate_guess(game["word"], word)
            game["guesses"].append({"guess": word, "result": result})
            
            # Kiểm tra thắng
            if all(r == GREEN for r in result):
                game["finished"] = True
                tries = len(game["guesses"])
                ratings = {1:"🤯 Thiên tài!", 2:"🏆 Xuất sắc!", 3:"🎉 Tuyệt vời!",
                           4:"😄 Tốt lắm!", 5:"😅 Suýt rồi!", 6:"😮‍💨 May mắn!"}
                embed = make_embed(message.author, game,
                    f"{ratings.get(tries,'👍')} Đúng rồi! Từ là **{game['word'].upper()}** — {tries}/{MAX_GUESSES} lượt!",
                    discord.Color.gold())
                await message.channel.send(embed=embed)
                return
            
            # Kiểm tra thua
            if len(game["guesses"]) >= MAX_GUESSES:
                game["finished"] = True
                embed = make_embed(message.author, game,
                    f"😞 Hết lượt! Từ đúng là **{game['word'].upper()}**. Gõ `!wordle` để chơi lại.",
                    discord.Color.red())
                await message.channel.send(embed=embed)
                return
            
            # Tiếp tục
            embed = make_embed(message.author, game,
                f"Còn **{MAX_GUESSES - len(game['guesses'])}** lượt. Tiếp tục!",
                discord.Color.blurple())
            await message.channel.send(embed=embed)
            return
    
    # Xử lý lệnh !wordle để bắt đầu game mới
    if message.content.startswith('!wordle'):
        uid = message.author.id
        if uid in active_games and not active_games[uid]["finished"]:
            game = active_games[uid]
            embed = make_embed(message.author, game,
                "⚠️ Bạn đang có ván dang dở! Hãy đoán tiếp hoặc gõ `!quit` để bỏ.",
                discord.Color.orange())
            await message.channel.send(embed=embed)
            return
        
        wlen = random.choice(list(WORD_LIST.keys()))
        word = random.choice(WORD_LIST[wlen])
        active_games[uid] = {"word": word, "guesses": [], "finished": False}
        embed = make_embed(message.author, active_games[uid],
            f"🎮 Ván mới! Từ có **{wlen}** chữ cái — có **{MAX_GUESSES}** lượt.\n💡 **Chỉ cần chat từ đó ra** là bot sẽ nhận!",
            discord.Color.green())
        await message.channel.send(embed=embed)
        return
    
    # Xử lý lệnh !quit
    if message.content.startswith('!quit'):
        uid = message.author.id
        if uid not in active_games or active_games[uid]["finished"]:
            await message.channel.send("❌ Không có ván nào đang chạy.")
            return
        secret = active_games[uid]["word"]
        active_games[uid]["finished"] = True
        await message.channel.send(f"🏳️ **{message.author.display_name}** bỏ cuộc! Từ đúng là **{secret.upper()}**. Gõ `!wordle` để chơi lại.")
        return
    
    # Xử lý lệnh !hint
    if message.content.startswith('!hint'):
        uid = message.author.id
        if uid not in active_games or active_games[uid]["finished"]:
            await message.channel.send("❌ Không có ván nào đang chạy.")
            return
        first = active_games[uid]["word"][0].upper()
        await message.channel.send(f"💡 Chữ đầu tiên là **{first}**")
        return
    
    # Xử lý lệnh !help
    if message.content.startswith('!help'):
        embed = discord.Embed(title="📖 Hướng dẫn WORDLE", color=discord.Color.teal())
        embed.add_field(name="🎯 Mục tiêu",
            value=f"Đoán từ tiếng Anh **4-7** chữ cái trong **{MAX_GUESSES}** lượt.", inline=False)
        embed.add_field(name="🎨 Màu sắc",
            value=f"{GREEN} Đúng chữ, đúng vị trí\n{YELLOW} Đúng chữ, sai vị trí\n{BLACK} Không có trong từ",
            inline=False)
        embed.add_field(name="📝 Cách chơi",
            value="`!wordle` - Bắt đầu ván mới\n`!hint` - Gợi ý chữ đầu\n`!quit` - Bỏ cuộc\n`!help` - Hướng dẫn\n\n**👉 CHỈ CẦN CHAT TỪ CẦN ĐOÁN LÀ BOT TỰ NHẬN!**", inline=False)
        await message.channel.send(embed=embed)
        return
    
    # Xử lý các lệnh prefix khác (nếu có)
    await bot.process_commands(message)

# ─── CHẠY BOT ────────────────────────────────────────────────
if __name__ == "__main__":
    from datetime import datetime
    bot.run(TOKEN)
