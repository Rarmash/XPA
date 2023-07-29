import requests

from .URLs import URLs

class XPA:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = URLs()
        
    def _make_requst(self, endpoint):
        headers = {'x-authorization': self.api_key}
        return requests.get(endpoint, headers=headers)
    
    def _find_setting_by_id(self, settings, setting_id):
        for setting in settings:
            if setting['id'] == setting_id:
                return setting['value']
        return None
    
    def get_account_info_xuid(self, xuid):
        endpoint = self.url.account_xuid_url(xuid)
        response = self._make_requst(endpoint).json()
        user_data = response['profileUsers'][0]['settings']
        account_info = ACCOUNT_INFO_XUID(
            GameDisplayPicRaw = self._find_setting_by_id(user_data, 'GameDisplayPicRaw'),
            Gamerscore = self._find_setting_by_id(user_data, 'Gamerscore'),
            Gamertag = self._find_setting_by_id(user_data, 'Gamertag'),
            AccountTier = self._find_setting_by_id(user_data, 'AccountTier'),
            XboxOneRep = self._find_setting_by_id(user_data, 'XboxOneRep'),
            PreferredColor = self._find_setting_by_id(user_data, 'PreferredColor'),
            RealName = self._find_setting_by_id(user_data, 'RealName'),
            Bio = self._find_setting_by_id(user_data, 'Bio'),
            Location = self._find_setting_by_id(user_data, 'Location')
        )
        return account_info

    def get_account_info_gamertag(self, gamertag):
        endpoint = self.url.search_gamertag_url(gamertag)
        response = self._make_requst(endpoint).json()
        user_data = response['people'][0]
        account_info = ACCOUNT_INFO_GAMERTAG(
            xuid = user_data["xuid"],
            displayName = user_data["displayName"],
            realName = user_data["realName"],
            displayPicRaw = user_data["displayPicRaw"],
            showUserAsAvatar = user_data["showUserAsAvatar"],
            gamertag = user_data["gamertag"],
            gamerScore = user_data["gamerScore"],
            modernGamertag = user_data["modernGamertag"],
            modernGamertagSuffix = user_data["modernGamertagSuffix"],
            uniqueModernGamertag = user_data["uniqueModernGamertag"],
            xboxOneRep = user_data["xboxOneRep"],
            presenceState = user_data["presenceState"],
            presenceText = user_data["presenceText"],
            presenceDevices = user_data["presenceDevices"],
            isBroadcasting = user_data["isBroadcasting"],
            isCloaked = user_data["isCloaked"],
            isQuarantined = user_data["isQuarantined"],
            isXbox360Gamerpic = user_data["isXbox360Gamerpic"],
            lastSeenDateTimeUtc = user_data["lastSeenDateTimeUtc"],
            preferredColor = user_data["preferredColor"],
            presenceDetails = user_data["presenceDetails"],
            titlePresence = user_data["titlePresence"],
            titleSummaries = user_data["titleSummaries"],
            accountTier = user_data["detail"]["accountTier"],
            bio = user_data["detail"]["bio"],
            isVerified = user_data["detail"]["isVerified"],
            location = user_data["detail"]["location"],
            tenure = user_data["detail"]["tenure"],
            watermarks = user_data["detail"]["watermarks"],
            blocked = user_data["detail"]["blocked"],
            mute = user_data["detail"]["mute"],
            followerCount = user_data["detail"]["followerCount"],
            followingCount = user_data["detail"]["followingCount"],
            hasGamePass = user_data["detail"]["hasGamePass"],
            socialManager = user_data["socialManager"],
            broadcast = user_data["broadcast"],
            avatar = user_data["avatar"],
            linkedAccounts = user_data["linkedAccounts"],
            colorTheme = user_data["colorTheme"],
            preferredPlatforms = user_data["preferredPlatforms"],
        )
        return account_info
    
class ACCOUNT_INFO_XUID:
    def __init__(self, GameDisplayPicRaw, Gamerscore, Gamertag, AccountTier, XboxOneRep, PreferredColor, RealName, Bio, Location):
        self.GameDisplayPicRaw = GameDisplayPicRaw
        self.Gamerscore = Gamerscore
        self.Gamertag = Gamertag
        self.AccountTier = AccountTier
        self.XboxOneRep = XboxOneRep
        self.PreferredColor = PreferredColor
        self.RealName = RealName
        self.Bio = Bio
        self.Location = Location
        
class ACCOUNT_INFO_GAMERTAG:
    def __init__(self, xuid, displayName, realName, displayPicRaw, showUserAsAvatar, gamertag, gamerScore, modernGamertag, modernGamertagSuffix, uniqueModernGamertag, xboxOneRep, presenceState, presenceText, presenceDevices, isBroadcasting, isCloaked, isQuarantined, isXbox360Gamerpic, lastSeenDateTimeUtc, preferredColor, presenceDetails, titlePresence, titleSummaries, accountTier, bio, isVerified, location, tenure, watermarks, blocked, mute, followerCount, followingCount, hasGamePass, socialManager, broadcast, avatar, linkedAccounts, colorTheme, preferredPlatforms):
        self.xuid = xuid
        self.displayName = displayName
        self.realName = realName
        self.displayPicRaw = displayPicRaw
        self.showUserAsAvatar = showUserAsAvatar
        self.gamertag = gamertag
        self.gamerScore = gamerScore
        self.modernGamertag = modernGamertag
        self.modernGamertagSuffix = modernGamertagSuffix
        self.uniqueModernGamertag = uniqueModernGamertag
        self.xboxOneRep = xboxOneRep
        self.presenceState = presenceState
        self.presenceText = presenceText
        self.presenceDevices = presenceDevices
        self.isBroadcasting = isBroadcasting
        self.isCloaked = isCloaked
        self.isQuarantined = isQuarantined
        self.isXbox360Gamerpic = isXbox360Gamerpic
        self.lastSeenDateTimeUtc = lastSeenDateTimeUtc
        self.preferredColor = preferredColor
        self.presenceDetails = presenceDetails
        self.titlePresence = titlePresence
        self.titleSummaries = titleSummaries
        self.accountTier = accountTier
        self.bio = bio
        self.isVerified = isVerified
        self.location = location
        self.tenure = tenure
        self.watermarks = watermarks
        self.blocked = blocked
        self.mute = mute
        self.followerCount = followerCount
        self.followingCount = followingCount
        self.hasGamePass = hasGamePass
        self.socialManager = socialManager
        self.broadcast = broadcast
        self.avatar = avatar
        self.linkedAccounts = linkedAccounts
        self.colorTheme = colorTheme
        self.preferredPlatforms = preferredPlatforms
        