# -*- coding: utf-8 -*-

from pyload.plugin.internal.DeadHoster import DeadHoster, create_getInfo


class SharebeesCom(DeadHoster):
    __name    = "SharebeesCom"
    __type    = "hoster"
    __version = "0.02"

    __pattern = r'http://(?:www\.)?sharebees\.com/\w{12}'

    __description = """ShareBees hoster plugin"""
    __license     = "GPLv3"
    __authors     = [("zoidberg", "zoidberg@mujmail.cz")]


getInfo = create_getInfo(SharebeesCom)