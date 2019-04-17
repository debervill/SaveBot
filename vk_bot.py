import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from random import randint
import os
from pyvirtualdisplay import Display
import pdfkit


class VkBot():
    
    def getRandomId(self):
        self.randId = randint(1000, 2 ** 32)
        return self.randId

    
    def startBot(self):
        self.session = requests.Session()

        self.login, self.password = '+79167941799', 'cjghjvfn1q2w3e'
        vk_session = vk_api.VkApi(self.login, self.password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

        vk_session = vk_api.VkApi(token='c74eed28be099a7295df99b6dfd84e3b0c7cf2bf1e04e96c21fac10d77200a2f7e0a866b9914784c4fa6b')
        vk = vk_session.get_api()


        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    vk.messages.send(
                            user_id=event.user_id,
                            random_id=self.getRandomId(),
                            peer_id = event.user_id,
                            user_ids = event.user_id,
                            message="Привет! Я пока маленький ботёнок и рад тебя видеть! Я много чего не умею, но я быстро учусь!"
                        )
    def saveLinks(self, url):
        display = Display(visible=0, size=(800, 600))
        display.start()
        root_directory = 'save'
        save_directory = 'save/pdf'
        os.chdir(save_directory)

        if str(url).find('https') > -1:
            url_name = url[8:].replace('/', '_')
        else:
            url_name = url[7:].replace('/', '_')

        file_name = url_name + ".pdf"

        # file = os.path.join(save_directory, file_name)
        pdfkit.from_url(url, file_name)
        print("OK")
        os.chdir(root_directory)


if __name__ == '__main__':
    bot = VkBot()
    bot.startBot()