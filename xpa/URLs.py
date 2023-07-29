class URLs:
    def __init__(self):
        
        self.base_url = "https://xbl.io/api/v2/"
        
        # account
        self.account_xuid = f"account/{'{xuid}'}"
        self.search_gamertag = "search/{gamertag}"
        self.xuid_presence = f"{'{xuid}'}/presence"
        
        # achievements
        self.achievements_xuid = f"achievements/player/{'{xuid}'}"
        self.title_achievements_xuid = f"achievements/player/{'{xuid}'}/{'{titleId}'}"
        self.title360_achievements_xuid = f"achievements/player/{'{xuid}'}/title/{'{titleId}'}"
        self.player360_achievements_xuid = f"achievements/x360/{'{xuid}'}/title/{'{titleId}'}"
        
        # clubs
        self.club_details = f"clubs/{'{clubId}'}"
        self.find_club = f"clubs/find?q={'{query}'}"
        
        # friends
        self.friends_xuid = f"friends/{'{xuid}'}"
        self.search_friend = f"friends/search/{'{xuid}'}"
        
        # gamepass
        self.gamepass_all = "gamepass/all"
        self.gamepass_pc = "gamepass/pc"
        self.gamepass_eaplay = "gamepass/ea-play"
        self.gamepass_nocontroller = "gamepass/no-controller"
        
        # marketplace
        self.marketplace_new = "marketplace/new"
        self.marketplace_toppaid = "marketplace/top-paid"
        self.marketplace_bestrated = "marketplace/best-rated"
        self.marketplace_comingsoon = "marketplace/coming-soon"
        self.marketplace_deals = "marketplace/deals"
        self.marketplace_topfree = "marketplace/top-free"
        self.marketplace_mostplayed = "marketplace/most-played"
        
        # player
        self.player_summary = f"player/summary/{'{xuid}'}"
        self.player_titleHistory = f"player/titleHistory/{'{xuid}'}"
        
        # session
        self.session_details = f"session/{'{sessionName}'}"
        
        # group
        self.group_summary = f"group/summary/{'{groupId}'}"
        self.group_messages = f"group/messages/{'{groupId}'}"
        
    def base_url(self):
        return self.base_url
    
    def account_xuid_url(self, xuid):
        return self.base_url + self.account_xuid.format(xuid=xuid)
    
    def search_gamertag_url(self, gamertag):
        return self.base_url + self.search_gamertag.format(gamertag=gamertag)
    
    def xuid_presence_url(self):
        return self.base_url + self.xuid_presence
    
    def achievements_xuid_url(self):
        return self.base_url + self.achievements_xuid
    
    def title_achievements_xuid_url(self):
        return self.base_url + self.title_achievements_xuid
    
    def title360_achievements_xuid_url(self):
        return self.base_url + self.title360_achievements_xuid
    
    def player360_achievements_xuid_url(self):
        return self.base_url + self.player360_achievements_xuid
    
    def club_details_url(self):
        return self.base_url + self.club_details
    
    def find_club_url(self):
        return self.base_url + self.find_club
    
    def friends_xuid_url(self):
        return self.base_url + self.friends_xuid
    
    def search_friend_url(self):
        return self.base_url + self.search_friend
    
    def gamepass_all_url(self):
        return self.base_url + self.gamepass_all
    
    def gamepass_pc_url(self):
        return self.base_url + self.gamepass_pc 
    
    def gamepass_eaplay_url(self):
        return self.base_url + self.gamepass_eaplay
    
    def gamepass_nocontroller_url(self):
        return self.base_url + self.gamepass_nocontroller
    
    def marketplace_new_url(self):
        return self.base_url + self.marketplace_new
    
    def marketplace_toppaid_url(self):
        return self.base_url + self.marketplace_toppaid
    
    def marketplace_bestrated_url(self):
        return self.base_url + self.marketplace_bestrated
    
    def marketplace_comingsoon_url(self):
        return self.base_url + self.marketplace_comingsoon
    
    def marketplace_deals_url(self):
        return self.base_url + self.marketplace_deals
    
    def marketplace_topfree_url(self):
        return self.base_url + self.marketplace_topfree
    
    def marketplace_mostplayed_url(self):
        return self.base_url + self.marketplace_mostplayed
    
    def player_summary_url(self):
        return self.base_url + self.player_summary
    
    def player_titleHistory_url(self):
        return self.base_url + self.player_titleHistory
    
    def session_details_url(self):
        return self.base_url + self.session_details
    
    def group_summary_url(self):
        return self.base_url + self.group_summary
    
    def group_messages_url(self):
        return self.base_url + self.group_messages
