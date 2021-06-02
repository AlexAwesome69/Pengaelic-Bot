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
        await ctx.message.delete()

    @roll_dice.error
    async def error(self, ctx, error):
        if str(error) == """Command raised an exception: HTTPException: 400 Bad Request (error code: 50035): Invalid Form Body
In content: Must be 2000 or fewer in length.""":
            await ctx.send("Sending all that would put me over the 2000-character limit!")
        else:
            await ctx.send(f"Unhandled error occurred:\n```{error}```")


def setup(client):
    client.add_cog(Games(client))
