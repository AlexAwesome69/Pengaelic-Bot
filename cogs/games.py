from discord.ext import commands
from random import choice


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
    name = "games"
    name_typable = name

    @commands.command(name="roll")
    async def roll_dice(self, ctx):
        await ctx.send(":game_die:You rolled " + choice("You rolled NaN dice and got [REDACTED]", "You rolled an [ERROR]-sided die and got `DivideByZeroError`", "You rolled 0xbadc0de `err`-sided dice and got [NULL]"))

    @commands.command(name="draw")
    async def draw_cards(self, ctx, cards: int = 1, replace_cards: bool = False):
        suits = [
            "Diamonds",
            "Spades",
            "Hearts",
            "Clubs"
        ]
        values = {
            1: "Ace",
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        all_cards = []
        faces = []
        numbers = []
        drawn = []
        if replace_cards:
            for _ in range(cards):
                random_value = str(choice(list(values.values())))
                card = str(
                    random_value + (" " * (6 - len(random_value))) + "of " + choice(suits))
                if card[1] == "0" or card[1] == "1" or card[1] == "2" or card[1] == "3":
                    faces.append(card)
                else:
                    numbers.append(card)
            drawn = faces + numbers
        else:
            for suit in range(int(len(suits)/1)):
                for value in values:
                    if value == 10:
                        length = 2
                    elif value == 1:
                        length = 3
                    elif value == 11 or value == 13:
                        length = 4
                    elif value == 12:
                        length = 5
                    else:
                        length = 1
                    all_cards.append(
                        str(values[value]) + (" " * (6 - length)) + "of " + suits[suit])
            if cards > 52:
                await ctx.send(":black_joker:You can't draw more than the entire deck!")
                return
            elif cards == 52:
                await ctx.send(":black_joker:You picked up the entire deck. What was the point of that?")
                return
            else:
                for _ in range(cards):
                    card = choice(all_cards)
                    if card[1] == "0" or card[1] == "1" or card[1] == "2" or card[1] == "3":
                        faces.append(card)
                    else:
                        numbers.append(card)
                    all_cards.remove(card)
                drawn = faces + numbers
        if cards == 1:
            while "  " in drawn[0]:
                drawn[0] = drawn[0].replace("  ", " ")
            await ctx.send(f":black_joker:You drew {drawn[0]}")
        else:
            await ctx.send(":black_joker:You drew...```{}```".format(str(drawn)[1:-1].replace("'", "").replace(", ", "\n")))

    @commands.command(name="pop")
    async def bubblewrap(self, ctx, size: str = "5"):
        try:
            if len(size) == 5:
                width = int(size[0:1])
                height = int(size[3:4])
            elif len(size) == 4:
                if "x" == size[1]:
                    width = int(size[0])
                    height = int(size[2:3])
                elif "x" == size[2]:
                    width = int(size[0:1])
                    height = int(size[3])
            elif len(size) == 3:
                width = int(size[0])
                height = int(size[2])
            elif len(size) == 2 or len(size) == 1:
                width = int(size)
                height = int(size)
            else:
                raise(SyntaxError)
            if width > 10 or height > 10:
                raise(SyntaxError)
        except SyntaxError:
            await ctx.send("Invalid size parameter. Use just a single number or two numbers with an `x` in between (e.g. `3x5`), and no larger than `10x10`")
            return
        sheet = ""
        for _ in range(height):
            sheet = sheet + str(["||pop||" for _ in range(width)]
                                )[1:-1].replace("'", "").replace(", ", "") + "\n"
        await ctx.send(sheet)

    @roll_dice.error
    @draw_cards.error
    @bubblewrap.error
    async def error(self, ctx, error):
        if str(error) == """Command raised an exception: HTTPException: 400 Bad Request (error code: 50035): Invalid Form Body
In content: Must be 2000 or fewer in length.""":
            await ctx.send("Sending all that would put me over the 2000-character limit!")
        else:
            await ctx.send(f"Unhandled error occurred:\n```{error}```")


def setup(client):
    client.add_cog(Games(client))
