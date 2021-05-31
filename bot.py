# -*- coding: utf-8 -*-

from discord.ext import commands
from dotenv import load_dotenv as dotenv
import discord
from os import system as cmd, getenv as env, listdir as ls
print("Imported modules")
info = r"""
 ____________
| ___| | | | |
|| | |\|_| | |
||_|_|    \| |
| ________  \|
| \_______|  |
|__\______|__|

Pengaelic Bot - the custom-built robot, coded in Althon
Copyright (C) Alexander Regulus | https://github.com/AlexAwesome69/Pengaelic-Bot/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

"""
cmd("toilet -w 1000 -f standard -F border -F gay Pengaelic Bot")
print(info)


client = commands.Bot(
    command_prefix="p#",
    case_insensitive=True,
    description="Pengaelic Bot",
    help_command=None,
    activity=discord.Game(name="with liquid chaos"),
    intents=discord.Intents.all()
)


def help_menu(cog, client):
    menu = discord.Embed(
        title=cog.name.capitalize(),
        color=0x007f7f
    ).set_footer(
        text=f"Command prefix is {client.command_prefix}\n<arg> = required parameter\n[arg] = optional parameter\n[arg (value)] = default value for optional parameter\n(command/command/command) = all aliases you can run the command with"
    )
    for command in cog.get_commands():
        menu.add_field(
            name="({})".format(
                str([command.name] + command.aliases)[1:-
                                                      1].replace("'", "").replace(", ", "/")
            ),
            value=""
        )
    return menu


@commands.command(name="tupper", pass_context=True)
async def say_back(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()


@client.event
async def on_ready():
    print(f"{client.description} connected to Discord")

# load .env
dotenv(".env")
print("Loaded .env")


@client.group(name="help")
async def help(ctx, *, cogname: str = None):
    if cogname == None:
        menu = discord.Embed(
            title=client.description,
            description=f"Type `{client.command_prefix}help `**`<lowercase category name without spaces or dashes>`** for more info on each category.",
            color=0x007f7f
        )
        cogs = dict(client.cogs)
        for cog in cogs:
            menu.add_field(
                name=cogs[cog].name.capitalize(),
                value=""
            )
        menu.add_field(
            name="Links",
            value=f"My official [support server](https://discord.gg/DHHpA7k)\nMy [GitHub repo](https://github.com/AlexAwesome69/Pengaelic-Bot)",
            inline=False
        )
        await ctx.send(embed=menu)
    else:
        await ctx.send(embed=help_menu(client.get_cog(cogname.capitalize()), client))


@help.error
async def not_a_cog(ctx, error):
    if str(error) == "AttributeError: 'NoneType' object has no attribute 'name'":
        await ctx.send("There isn't a help menu for that.")

# load all the cogs
for cog in ls("cogs"):
    if cog.endswith(".py"):
        client.load_extension(f"cogs.{cog[:-3]}")
        print(f"Loaded cog {cog[:-3]}")

while True:
    try:
        client.run(env("DISCORD_TOKEN"))
    except KeyboardInterrupt:
        print("Disconnected")
        while True:
            exit(0)
    except:
        print("Unable to connect to Discord")
        while True:
            exit(1)
