# -*- coding: utf-8 -*-

from discord.ext import commands


class Interactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.formatChars = "*`~|"
    name = "interactions"
    name_typable = name

    async def vact(self, ctx, act, actee):
        await ctx.send(f"*He {act}s {actee}.*")
        await ctx.message.delete()

    @commands.command(name="slap")
    async def slap(self, ctx, *, slap):
        await self.vact(
            ctx,
            "slap",
            slap
        )

    @commands.command(name="stab")
    async def stab(self, ctx, *, stab):
        await self.vact(
            ctx,
            "stab",
            stab
        )

    @commands.command(name="shoot")
    async def shoot(self, ctx, *, shoot):
        await self.vact(
            ctx,
            "shoot",
            shoot
        )

    @slap.error
    @stab.error
    @shoot.error
    async def error(self, ctx, error):
        await ctx.send(f"Unhandled error occurred:\n```{error}```")


def setup(client):
    client.add_cog(Interactions(client))
