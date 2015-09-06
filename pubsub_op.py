from pubsub import pub


class Youtube(object):
    """Notifier"""
    def __init__(self):
        self.channels = []

    def add_publisher(self, channel):
        self.channels.append(channel)


class Channel(object):
    """Publisher"""
    def __init__(self, name):
        self.channel_name = name
        self.play_list = []

    def __unicode__(self):
        return self.name

    def publish_play(self, name):
        self.play_list.append(name)
        pub.sendMessage(self.channel_name, name=name, channel=self)


class User(object):
    """Subscriber"""
    def __init__(self, name):
        self.name = name

    def subscribe_channel(self, channel):
        pub.subscribe(self.notify, channel.channel_name)

    def notify(self, name, channel):
        print "{0}, New album '{1}' released in '{2}' Channel".format(self.name, name, channel.channel_name)


def main():
    jinesh = User('Jinesh')
    rohit = User('Rohit')
    discovery_channel = Channel('Discovery')
    ng_channel = Channel('National Geographic')

    # user subscribe to channel
    jinesh.subscribe_channel(discovery_channel)
    jinesh.subscribe_channel(ng_channel)
    rohit.subscribe_channel(ng_channel)

    discovery_channel.publish_play("Discover UFO")
    ng_channel.publish_play("Animal Earth")


if __name__ == '__main__':
    main()
