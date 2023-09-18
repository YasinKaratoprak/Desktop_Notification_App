#Masaüstü Bildirim Uygulaması (ipucu: plyer, notification)
import time
from plyer import notification
if __name__ == "__main__":

    notification.notify(
        title = "Bu bir test mesajıdır",
        message = "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet",
        timeout = 2


    )
    time.sleep(7)


