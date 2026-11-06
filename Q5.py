# Q5. Notification Dispatcher - Polymorphism

class EmailNotification:
    def send(self, message):
        print(f"Email notification: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS notification: {message}")


class PushNotification:
    def send(self, message):
        print(f"Push notification: {message}")


class WhatsAppNotification:
    def send(self, message):
        print(f"WhatsApp notification: {message}")


def notify_all(notifications, message):
    for notification in notifications:
        notification.send(message)


if __name__ == "__main__":
    channels = [
        EmailNotification(),
        SMSNotification(),
        PushNotification(),
        WhatsAppNotification()
    ]
    notify_all(channels, "Your order has been shipped.")

    # Polymorphism occurs when notify_all() calls send() on different
    # objects. Each object's own send() method handles the message.
