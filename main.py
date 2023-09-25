from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform
from kivy.logger import Logger
if platform == 'android':
    from kivmob_mod import KivMob, TestIds, RewardedListenerInterface


#give class the name of Otameshi
class Otameshi(BoxLayout):
    pass


#Kivmob rewarded ads
class RewardsHandler(RewardedListenerInterface):

    def on_rewarded(self, reward_type, reward_amount):
        print("User rewarded", "Type; ", reward_type, "Amount; ", reward_amount)
        #load rewarded_ads
        App.get_running_app().ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)  # for tests


#give class the name of MainApp
class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "kivmob_test"

    def build(self):
        if platform == 'android':
            self.ads = KivMob(TestIds.APP)  # for tests
            # banner
            self.ads.new_banner(TestIds.BANNER, top_pos=False)  # for tests
            self.ads.request_banner()
            self.ads.show_banner()
            # interstitial
            self.ads.load_interstitial(TestIds.INTERSTITIAL)  # for tests
            # rewarded_ad
            self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)  # for tests
            # Pass a RewardsHandler instance inheriting RewardedAdLoadCallback4kivy to set_rewarded_ad_listener
            self.ads.set_rewarded_ad_listener(RewardsHandler())
        return Otameshi()

    def on_resume(self):
        Logger.info("kivmob_test: on_resume()")
        if platform == 'android':
            self.load_ads()

    def load_ads(self):
        if platform == 'android':
            Logger.info("kivmob_test: load_ads() fired")
            # banner
            self.ads.request_banner()
            # interstitial
            self.ads.load_interstitial(TestIds.INTERSTITIAL)  # for tests
            # rewarded_ad
            self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)  # for tests

    def show_banner(self):
        if platform == 'android':
            Logger.info("kivmob_test: show_banner() fired")
            self.ads.show_banner()

    def hide_banner(self):
        if platform == 'android':
            Logger.info("kivmob_test: hide_banner() fired")
            self.ads.hide_banner()

    def load_interstitial(self):
        if platform == 'android':
            Logger.info("kivmob_test: load_interstitial() fired")
            self.ads.load_interstitial(TestIds.INTERSTITIAL)  # for tests

    def show_interstitial(self):
        if platform == 'android':
            Logger.info("kivmob_test: show_interstitial() fired")
            self.ads.show_interstitial()

    def load_rewarded_ad(self):
        if platform == 'android':
            Logger.info("kivmob_test: load_rewarded_ad() fired")
            self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)  # for tests

    def show_rewarded_ad(self):
        if platform == 'android':
            Logger.info("kivmob_test: show_rewarded_ad() fired")
            self.ads.show_rewarded_ad()


if __name__ == '__main__':
    MainApp().run()
