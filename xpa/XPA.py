import requests

from .URLs import URLs

from .classes.ACCOUNT_INFO_XUID import ACCOUNT_INFO_XUID
from .classes.ACCOUNT_INFO_GAMERTAG import ACCOUNT_INFO_GAMERTAG
from .classes.XUID_PRESENCE import XUID_PRESENCE
from .classes.CLUB_DETAILS import CLUB_DETAILS

class XPA:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = URLs()
        
    def _make_request(self, endpoint):
        headers = {'x-authorization': self.api_key}
        return requests.get(endpoint, headers=headers)
    
    def _find_setting_by_id(self, settings, setting_id):
        for setting in settings:
            if setting['id'] == setting_id:
                return setting['value']
        return None
    
    def get_account_info_xuid(self, xuid: str) -> ACCOUNT_INFO_XUID:
        """Get someone's profile information

        Args:
            xuid (str): xuid of specified user.

        Returns:
            ACCOUNT_INFO_XUID: user account info.
            
            Object attributes:
            - GameDisplayPicRaw: str
            - Gamerscore: str
            - Gamertag: str
            - AccountTier: str
            - XboxOneRep: str
            - PreferredColor: str
            - RealName: str
            - Bio: str
            - Location: str
        """
        endpoint = self.url.account_xuid_url(xuid)
        response = self._make_request(endpoint).json()
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

    def get_account_info_gamertag(self, gamertag: str) -> ACCOUNT_INFO_GAMERTAG:
        """_summary_

        Args:
            gamertag (str): gamertag of specified user

        Returns:
            ACCOUNT_INFO_GAMERTAG: user account info.
            Object attributes:
            - xuid: str
            - displayName: str
            - realName: str
            - displayPicRaw: str
            - showUserAsAvatar: str
            - gamertag: str
            - gamerScore: str
            - modernGamertag: str
            - modernGamertagSuffix: str
            - uniqueModernGamertag: str
            - xboxOneRep: str
            - presenceState: str
            - presenceText: str
            - presenceDevices: list
            - isBroadcasting: bool
            - isCloaked: bool
            - isQuarantined: bool
            - isXbox360Gamerpic: bool
            - lastSeenDateTimeUtc: str
            - preferredColor: dict
            - presenceDetails: dict
            - titlePresence: dict
            - titleSummaries: list
            - accountTier: str
            - bio: str
            - isVerified: bool
            - location: str
            - tenure: str
            - watermarks: dict
            - blocked: bool
            - mute: bool
            - followerCount: int
            - followingCount: int
            - hasGamePass: bool
            - socialManager: str
            - broadcast: str
            - avatar: str
            - linkedAccounts: list
            - colorTheme: str
            - preferredPlatforms: dict
        """
        endpoint = self.url.search_gamertag_url(gamertag)
        response = self._make_request(endpoint).json()
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
    
    def get_presence(self, xuid: str):
        endpoint = self.url.xuid_presence_url(xuid)
        response = self._make_request(endpoint).json()
        user_data = response[0]
        presence = XUID_PRESENCE(
            state = user_data["state"],
            last_seen_device_type = user_data["lastSeen"]["deviceType"],
            last_seen_title_id = user_data["lastSeen"]["titleId"],
            last_seen_title_name = user_data["lastSeen"]["titleName"],
            last_seen_timestamp = user_data["lastSeen"]["timestamp"]
        )
        return presence

    def get_user_achievements(self, xuid: str):
        endpoint = self.url.achievements_xuid_url(xuid)
        response = self._make_request(endpoint).json()
        user_data = response['titles']
        return user_data

    def get_title_achievements(self, xuid: str, titleId: str):
        endpoint = self.url.title_achievements_xuid_url(xuid, titleId)
        response = self._make_request(endpoint).json()
        user_data = response["achievements"]
        return user_data

    def get_title360_achievements(self, xuid: str, titleId: str):
        endpoint = self.url.title360_achievements_xuid_url(xuid, titleId)
        response = self._make_request(endpoint).json()
        user_data = response["achievements"]
        return user_data

    def get_player360_achievements(self, xuid: str, titleId: str):
        endpoint = self.url.player360_achievements_xuid_url(xuid, titleId)
        response = self._make_request(endpoint).json()
        user_data = response["achievements"]
        return user_data
    
    def get_club_details(self, clubId: str):
        endpoint = self.url.club_details_url(clubId)
        response = self._make_request(endpoint).json()
        club_data = response["clubs"][0]
        club_details = CLUB_DETAILS(
            identificator = club_data["id"],
            clubType = club_data["clubType"],
            creationDateUtc = club_data["creationDateUtc"],
            settings = club_data["settings"],
            followersCount = club_data["followersCount"],
            membersCount = club_data["membersCount"],
            moderatorsCount = club_data["moderatorsCount"],
            recommendedCount = club_data["recommendedCount"],
            requestedToJoinCount = club_data["requestedToJoinCount"],
            clubPresenceCount = club_data["clubPresenceCount"],
            clubPresenceTodayCount = club_data["clubPresenceTodayCount"],
            clubPresenceInGameCount = club_data["clubPresenceInGameCount"],
            roster = club_data["roster"],
            targetRoles = club_data["targetRoles"],
            recommendation = club_data["recommendation"],
            clubPresence = club_data["clubPresence"],
            state = club_data["state"],
            suspendedUntilUtc = club_data["suspendedUntilUtc"],
            reportCount = club_data["reportCount"],
            reportedItemsCount = club_data["reportedItemsCount"],
            maxMembersPerClub = club_data["maxMembersPerClub"],
            ownerXuid = club_data["ownerXuid"],
            founderXuid = club_data["founderXuid"],
            description = club_data["profile"]["description"]["value"],
            rules = club_data["profile"]["rules"]["value"],
            name = club_data["profile"]["name"]["value"],
            shortName = club_data["profile"]["shortName"]["value"],
            isSearchable = club_data["profile"]["isSearchable"]["value"],
            isRecommendable = club_data["profile"]["isRecommendable"]["value"],
            requestToJoinEnabled = club_data["profile"]["requestToJoinEnabled"]["value"],
            openJoinEnabled = club_data["profile"]["openJoinEnabled"]["value"],
            leaveEnabled = club_data["profile"]["leaveEnabled"]["value"],
            transferOwnershipEnabled = club_data["profile"]["transferOwnershipEnabled"]["value"],
            matureContentEnabled = club_data["profile"]["matureContentEnabled"]["value"],
            watchClubTitlesOnly = club_data["profile"]["watchClubTitlesOnly"]["value"],
            displayImageUrl = club_data["profile"]["displayImageUrl"]["value"],
            backgroundImageUrl = club_data["profile"]["backgroundImageUrl"]["value"],
            preferredLocale = club_data["profile"]["preferredLocale"]["value"],
            tags = club_data["profile"]["tags"]["value"],
            associatedTitles = club_data["profile"]["associatedTitles"]["value"],
            primaryColor = club_data["profile"]["primaryColor"]["value"],
            secondaryColor = club_data["profile"]["secondaryColor"]["value"],
            tertiaryColor = club_data["profile"]["tertiaryColor"]["value"]
        )
        return club_details
