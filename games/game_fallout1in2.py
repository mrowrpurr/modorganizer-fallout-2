# -*- encoding: utf-8 -*-

from ..basic_game import BasicGame


class Fallout2Game(BasicGame):
    Name = "Fallout 1 et tu - Support Plugin"
    Author = "mrowrpurr"
    Version = "0.1.0"

    GameName = "Fallout 1 et tu"
    GameShortName = "fallout1in2"
    GameNexusName = "fallout1in2"
    GameNexusId = 2667
    GameSteamId = 38400
    GameGogId = 1440166342 # https://embed.gog.com/games/ajax/filtered?mediaType=game&search=Fallout%201
    GameBinary = "fallout2.exe"
    GameDataPath = "%GAME_PATH%/Fallout1in2"

    # def iniFiles(self):
    #     return ["%GAME_PATH%/ddraw.ini", "%GAME_PATH%/sfall-mods.ini", "%GAME_PATH%/f2_res.ini"]