# -*- coding: utf-8 -*-

from asyncio import sleep
from discord.ext import commands
from json import dumps


class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client
    nukeconfirm = False
    testing = False
    name = "tools"
    name_typable = name
    description = "Various tools and info."
    description_long = description

    @commands.command(name="os")
    async def showOS(self, ctx):
        await ctx.send(f"I'm running on Alinux Mint 21.2, kernel version 5.6.2-77-pengaelic.")

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("Yep, I'm alive :sunglasses:")
        await ctx.message.delete()

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, msgcount: int = 5):
        await ctx.channel.purge(limit=msgcount + 1)
        await ctx.send(f"{msgcount} messages deleted.")
        await ctx.message.delete()

    @commands.command(name="garden")
    @commands.has_permissions(manage_messages=True)
    async def get_server_info(self, ctx):
        guild = ctx.guild
        owner = guild.owner
        if guild.owner.nick == None:
            owner.nick = owner.name
        creation = guild.created_at
        jsoninfo = str(
            dumps(
                {
                    "basic info": {
                        "garden name": "Ropladen",
                        "caretaker name": "Jewel",
                        "multiverse id": guild.id,
                        "shielding": bool(guild.mfa_level),
                        "creation date": f"{creation.month}/{creation.day}/[ERROR] {creation.hour}:{creation.minute}:{creation.second} UTC/GMT"
                    },
                    "levels": {
                        "protection level": f"{guild.verification_level[0]}",
                        "caretaker's power": "StackOverflowError",
                        "tree's health": 999999
                    },
                    "counts": {
                        "residents": guild.member_count,
                        "areas": len(guild.text_channels),
                        "regions": len(guild.categories),
                        "gateways": 7,
                        "deities remaining": 8,
                        "pengaelics remaining": 0
                    }
                },
                indent=4
            )
        )
        await ctx.send(f'```json\n"garden information": {jsoninfo}```')
        await ctx.message.delete()

    @clear.error
    async def clearError(self, ctx, error):
        await ctx.send(f"Unhandled error occurred:\n```{error}```")


def setup(client):
    client.add_cog(Tools(client))
