# -*- encoding: utf-8 -*-

from ..basic_game import BasicGame


class Fallout2Game(BasicGame):
    Name = "Fallout 2 - Support Plugin"
    Author = "mrowrpurr"
    Version = "0.1.0"

    GameName = "Fallout 2"
    GameShortName = "fallout2"
    GameNexusName = "fallout2"
    GameNexusId = 430
    GameSteamId = 38410
    GameGogId = 1440166436 # https://embed.gog.com/games/ajax/filtered?mediaType=game&search=Fallout%202
    GameBinary = "fallout2HR.exe"
    GameDataPath = "%GAME_PATH%"

    # def iniFiles(self):
    #     return ["%GAME_PATH%/ddraw.ini", "%GAME_PATH%/sfall-mods.ini", "%GAME_PATH%/f2_res.ini"]