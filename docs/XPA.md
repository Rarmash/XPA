# XPA Class Documentation

## Overview
The `XPA` class provides methods for accessing Xbox Live API endpoints to retrieve various information related to Xbox Live users, achievements, clubs, Game Pass, marketplace, sessions, groups, etc.

## Constructor
### `__init__(self, api_key)`
- **Description:** Initializes the XPA class with the provided API key.
- **Parameters:**
  - `api_key` (str): The API key used for authentication.

## Methods
### `get_account_info_xuid(xuid: str) -> ACCOUNT_INFO_XUID`
- **Description:** Get someone's profile information using their XUID (Xbox User ID).
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** An instance of `ACCOUNT_INFO_XUID` with the following attributes:
  - `GameDisplayPicRaw` (str): URL of the user's profile picture.
  - `Gamerscore` (str): User's gamerscore.
  - `Gamertag` (str): User's gamertag.
  - `AccountTier` (str): User's account tier.
  - `XboxOneRep` (str): User's Xbox One reputation.
  - `PreferredColor` (str): User's preferred color.
  - `RealName` (str): User's real name.
  - `Bio (str)`: User's bio.
  - `Location (str)`: User's location.

### `get_account_info_gamertag(gamertag: str) -> ACCOUNT_INFO_GAMERTAG`
- **Description:** Get someone's profile information using their Gamertag.
- **Parameters:**
  - `gamertag` (str): Gamertag of the specified user.
- **Returns:** An instance of `ACCOUNT_INFO_GAMERTAG` with the following attributes:
  - `xuid` (str): User's XUID.
  - `displayName` (str): User's display name.
  - `realName` (str): User's real name.
  - `displayPicRaw` (str): URL of the user's profile picture.
  - `showUserAsAvatar` (bool): Whether to show the user as an avatar.
  - `gamertag` (str): User's gamertag.
  - `gamerScore` (str): User's gamerscore.
  - `modernGamertag` (str): User's modern gamertag.
  - `modernGamertagSuffix` (str): User's modern gamertag suffix.
  - `uniqueModernGamertag` (str): User's unique modern gamertag.
  - `xboxOneRep` (str): User's Xbox One reputation.
  - `presenceState` (str): User's presence state.
  - `presenceText` (str): User's presence text.
  - `presenceDevices` (list): List of devices the user is present on.
  - `isBroadcasting` (bool): Whether the user is broadcasting.
  - `isCloaked` (bool): Whether the user is cloaked.
  - `isQuarantined` (bool): Whether the user is quarantined.
  - `isXbox360Gamerpic` (bool): Whether the user has an Xbox 360 gamerpic.
  - `lastSeenDateTimeUTC` (str): Last seen date and time in UTC.
  - `preferredColor` (str): User's preferred color.
  - `presenceDetails` (str): User's presence details.
  - `titlePresence` (str): User's title presence.
  - `titleSummaries` (list): List of title summaries.
  - `accountTier` (str): User's account tier.
  - `bio` (str): User's bio.
  - `isVerified` (bool): Whether the user is verified.
  - `location` (str): User's location.
  - `tenure` (str): User's tenure.
  - `watermarks` (list): List of watermarks.
  - `blocked` (bool): Whether the user is blocked.
  - `mute` (bool): Whether the user is muted.
  - `followerCount` (int): Number of followers.
  - `followingCount` (int): Number of users the user is following.
  - `hasGamePass` (bool): Whether the user has Game Pass.
  - `socialManager` (str): User's social manager.
  - `broadcast` (str): User's broadcast.
  - `avatar` (str): User's avatar.
  - `linkedAccounts` (list): List of linked accounts.
  - `colorTheme` (str): User's color theme.
  - `preferredPlatforms` (list): List of preferred platforms.

### `get_presence(xuid: str) -> XUID_PRESENCE`
- **Description:** Get user presence information using their XUID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** An instance of `XUID_PRESENCE` with the following attributes:
  - `state` (str): User's state.
  - `devices` (list): List of devices the user is present on with titles information.

### `get_user_achievements(xuid: str) -> list`
- **Description:** Get user achievements using their XUID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** A list of user achievements.

### `get_title_achievements(xuid: str, titleId: str) -> list`
- **Description:** Get user achievements for a specific title using their XUID and the title ID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
  - `titleId` (str): Title ID of the specified title.
- **Returns:** A list of user achievements for the specified title.

### `get_title360_achievements(xuid: str, titleId: str) -> list`
- **Description:** Get user achievements for a specific Xbox 360 title using their XUID and the title ID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
  - `titleId` (str): Title ID of the specified Xbox 360 title.
- **Returns:** A list of user achievements for the specified Xbox 360 title.

### `get_player360_achievements(xuid: str, titleId: str) -> list`
- **Description:** Get player achievements for a specific Xbox 360 title using their XUID and the title ID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
  - `titleId` (str): Title ID of the specified Xbox 360 title.
- **Returns:** A list of player achievements for the specified Xbox 360 title.

### `get_club_details(clubId: str) -> CLUB_DETAILS`
- **Description:** Get club details using the club ID.
- **Parameters:**
  - `clubId` (str): Club ID of the specified club.
- **Returns:** An instance of `CLUB_DETAILS` with the following attributes:
  - `identificator` (str): Club's identificator.
  - `clubType` (str): Club's type.
  - `creationDateUtc` (str): Club's creation date in UTC.
  - `settings` (list): Club's settings.
  - `followersCount` (int): Number of followers.
  - `membersCount` (int): Number of members.
  - `moderatorsCount` (int): Number of moderators.
  - `recommendedCount` (int): Number of recommended.
  - `requestedToJoinCount` (int): Number of requested to join.
  - `clubPresenceCount` (int): Number of club presence.
  - `clubPresenceTodayCount` (int): Number of club presence today.
  - `clubPresenceInGameCount` (int): Number of club presence in-game.
  - `roster` (list): Club's roster.
  - `targetRoles` (list): Club's target roles.
  - `recommendation` (list): Club's recommendations.
  - `clubPresence` (list): Club's presence.
  - `state` (str): Club's state.
  - `suspendedUntilUtc` (str): Club's suspended until in UTC.
  - `reportCount` (int): Number of reports.
  - `reportedItemsCount` (int): Number of reported items.
  - `maxMembersPerClub` (int): Maximum number of members per club.
  - `ownerXuid` (str): Club's owner XUID.
  - `founderXuid` (str): Club's founder XUID.
  - `description` (str): Club's description.
  - `rules` (str): Club's rules.
  - `name` (str): Club's name.
  - `shortName` (str): Club's short name.
  - `isSearchable` (bool): Whether the club is searchable.
  - `isRecommendable` (bool): Whether the club is recommendable.
  - `requestToJoinEnabled` (bool): Whether request to join is enabled.
  - `openJoinEnabled` (bool): Whether open join is enabled.
  - `leaveEnabled` (bool): Whether leave is enabled.
  - `tranferOwnershipEnabled` (bool): Whether transfer ownership is enabled.
  - `matureContentEnabled` (bool): Whether mature content is enabled.
  - `watchClubTitlesOnly` (bool): Whether to watch club titles only.
  - `displayImageUrl` (str): Club's display image URL.
  - `backgroundImageUrl` (str): Club's background image URL.
  - `preferredLocale` (str): Club's preferred locale.
  - `tags` (list): Club's tags.
  - `associatedTitles` (list): Club's associated titles.
  - `primaryColor` (str): Club's primary color.
  - `secondaryColor` (str): Club's secondary color.
  - `tertiaryColor` (str): Club's tertiary color.

### `get_friends_xuid(xuid: str) -> ACCOUNT_INFO_GAMERTAG`
- **Description:** Get user friends using their XUID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** An instance of `ACCOUNT_INFO_GAMERTAG` with following attributes:
  - `xuid` (str): User's XUID.
  - `displayName` (str): User's display name.
  - `realName` (str): User's real name.
  - `displayPicRaw` (str): URL of the user's profile picture.
  - `showUserAsAvatar` (bool): Whether to show the user as an avatar.
  - `gamertag` (str): User's gamertag.
  - `gamerScore` (str): User's gamerscore.
  - `modernGamertag` (str): User's modern gamertag.
  - `modernGamertagSuffix` (str): User's modern gamertag suffix.
  - `uniqueModernGamertag` (str): User's unique modern gamertag.
  - `xboxOneRep` (str): User's Xbox One reputation.
  - `presenceState` (str): User's presence state.
  - `presenceText` (str): User's presence text.
  - `presenceDevices` (list): List of devices the user is present on.
  - `isBroadcasting` (bool): Whether the user is broadcasting.
  - `isCloaked` (bool): Whether the user is cloaked.
  - `isQuarantined` (bool): Whether the user is quarantined.
  - `isXbox360Gamerpic` (bool): Whether the user has an Xbox 360 gamerpic.
  - `lastSeenDateTimeUTC` (str): Last seen date and time in UTC.
  - `preferredColor` (str): User's preferred color.
  - `presenceDetails` (str): User's presence details.
  - `titlePresence` (str): User's title presence.
  - `titleSummaries` (list): List of title summaries.
  - `accountTier` (str): User's account tier.
  - `bio` (str): User's bio.
  - `isVerified` (bool): Whether the user is verified.
  - `location` (str): User's location.
  - `tenure` (str): User's tenure.
  - `watermarks` (list): List of watermarks.
  - `blocked` (bool): Whether the user is blocked.
  - `mute` (bool): Whether the user is muted.
  - `followerCount` (int): Number of followers.
  - `followingCount` (int): Number of users the user is following.
  - `hasGamePass` (bool): Whether the user has Game Pass.
  - `socialManager` (str): User's social manager.
  - `broadcast` (str): User's broadcast.
  - `avatar` (str): User's avatar.
  - `linkedAccounts` (list): List of linked accounts.
  - `colorTheme` (str): User's color theme.
  - `preferredPlatforms` (list): List of preferred platforms.

### `search_friend_list(gamertag: str) -> FRIEND_INFO_GAMERTAG`
- **Description:** Search for a friend using their Gamertag.
- **Parameters:**
  - `gamertag` (str): Gamertag of the specified user.
- **Returns:** An instance of `FRIEND_INFO_GAMERTAG` with the following attributes:
  - `GameDisplayPicRaw` (str): URL of the user's profile picture.
  - `Gamerscore` (str): User's gamerscore.
  - `Gamertag` (str): User's gamertag.
  - `AccountTier` (str): User's account tier.
  - `XboxOneRep` (str): User's Xbox One reputation.
  - `RealName` (str): User's real name.
  - `Bio` (str): User's bio.
  - `TenureLevel` (str): User's tenure level.
  - `Watermarks` (list): List of watermarks.
  - `Location` (str): User's location.
  - `ShowUserAsAvatar` (bool): Whether to show the user as an avatar.
  
### `get_gamepass_all_games() -> list`
- **Description:** Get all games available on Game Pass.
- **Returns:** A list of Game Pass games.

### `get_gamepass_pc_games() -> list`
- **Description:** Get all games available on Game Pass for PC.
- **Returns:** A list of Game Pass PC games.

### `get_gamepass_eaplay_games() -> list`
- **Description:** Get all games available on EA Play.
- **Returns:** A list of EA Play games.

### `get_gamepass_nocontroller_games() -> list`
- **Description:** Get all games available on Game Pass that don't require a controller.
- **Returns:** A list of Game Pass games that don't require a controller.

### `get_new_marketplace_games() -> list`
- **Description:** Get all new games available on the marketplace.
- **Returns:** A list of new marketplace games.

### `get_toppaid_marketplace_games() -> list`
- **Description:** Get all top paid games available on the marketplace.
- **Returns:** A list of top paid marketplace games.

### `get_bestrated_marketplace_games() -> list`
- **Description:** Get all best rated games available on the marketplace.
- **Returns:** A list of best rated marketplace games.

### `get_comingsoon_marketplace_games() -> list`
- **Description:** Get all coming soon games available on the marketplace.
- **Returns:** A list of coming soon marketplace games.

### `get_deals_marketplace_games() -> list`
- **Description:** Get all deals available on the marketplace.
- **Returns:** A list of deals marketplace games.

### `get_topfree_marketplace_games() -> list`
- **Description:** Get all top free games available on the marketplace.
- **Returns:** A list of top free marketplace games.

### `get_mostplayed_marketplace_games() -> list`
- **Description:** Get all most played games available on the marketplace.
- **Returns:** A list of most played marketplace games.

### `search_marketplace_game(titleId: str) -> list`
- **Description:** Search for a game on the marketplace using its title ID.
- **Parameters:**
  - `titleId` (str): Title ID of the specified game.
- **Returns:** A list of marketplace games.

### `get_player_summary(xuid: str) -> PLAYER_SUMMARY`
- **Description:** Get player summary using their XUID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** An instance of `PLAYER_SUMMARY` with following attributes:
  - `xuid` (str): User's XUID.
  - `isFavorite` (bool): Whether the user is a favorite.
  - `isFollowingCaller` (bool): Whether the user is following the caller.
  - `isFollowedByCaller` (bool): Whether the user is followed by the caller.
  - `isIdentityShared` (bool): Whether the user's identity is shared.
  - `addedDateTimeUtc` (str): Added date and time in UTC.
  - `displayName` (str): User's display name.
  - `realName` (str): User's real name.
  - `displayPicRaw` (str): URL of the user's profile picture.
  - `useAvatar` (bool): Whether to use the avatar.
  - `gamertag` (str): User's gamertag.
  - `gamerScore` (str): User's gamerscore.
  - `xboxOneRep` (str): User's Xbox One reputation.
  - `presenceState` (str): User's presence state.
  - `presenceText` (str): User's presence text.
  - `presenceDevices` (list): List of devices the user is present on.
  - `isBroadcasting` (bool): Whether the user is broadcasting.
  - `isCloaked` (bool): Whether the user is cloaked.
  - `isQuarantined` (bool): Whether the user is quarantined.
  - `suggestion` (str): User's suggestion.
  - `recommendation` (str): User's recommendation.
  - `titleHistory` (list): List of title history.
  - `multiplayerSummary` (dict): Multiplayer summary.
  - `recentPlayer` (list): List of recent players. // check
  - `follower` (list): List of followers.
  - `preferredColor` (str): User's preferred color.
  - `presenceDetails` (dict): Presence details.
  - `titlePresence` (dict): Title presence.
  - `titleSummaries` (list): List of title summaries.
  - `presenceTitleIds` (list): List of presence title IDs.
  - `detail` (dict): User's detail.
  - `communityManagerTitles` (list): List of community manager titles.
  - `socialManager` (str): User's social manager.
  - `broadcast` (str): User's broadcast.
  - `tournamentSummary` (dict): Tournament summary.
  - `avatar` (str): User's avatar.

### `get_player_title_history(xuid: str) -> list`
- **Description:** Get player title history using their XUID.
- **Parameters:**
  - `xuid` (str): XUID of the specified user.
- **Returns:** A list of player title history.

### `get_session_details(sessionName: str) -> dict`
- **Description:** Get session details using the session name.
- **Parameters:**
  - `sessionName` (str): Name of the specified session.
- **Returns:** A dictionary containing session details.

### `get_group_summary(groupId: str) -> dict`
- **Description:** Get group summary using the group ID.
- **Parameters:**
  - `groupId` (str): Group ID of the specified group.
- **Returns:** A dictionary containing group summary.

### `get_group_messages(groupId: str) -> list`
- **Description:** Get group messages using the group ID.
- **Parameters:**
  - `groupId` (str): Group ID of the specified group.
- **Returns:** A list of group messages.
