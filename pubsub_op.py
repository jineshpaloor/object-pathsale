from collections import defaultdict


class Youtube(object):
    """Notifier"""
    # publisher
    channels = {}
    subscriber_list = defaultdict(list)

    @classmethod
    def add_publisher(self, channel):
        pass

    @classmethod
    def remove_publisher(self, channel):
        pass

    @classmethod
    def add_subscriber(self, subscriber, topic):
        self.subscriber_list[topic].append(subscriber)

    @classmethod
    def remove_subscriber(self, channel):
        pass

    @classmethod
    def subscribe(self, subscriber, topic):
        self.add_subscriber(subscriber, topic)

    @classmethod
    def sendMessage(self, topic, *args, **kwargs):
        for subscriber in self.subscriber_list[topic]:
            subscriber.__call__(*args, **kwargs)

class Channel(object):
    """Publisher"""
    def __init__(self, name):
        self.channel_name = name
        self.play_list = []

    def __unicode__(self):
        return self.name

    def publish_play(self, name):
        self.play_list.append(name)
        #Youtube.sendMessage(self.channel_name, name=name, channel=self)
        Youtube.sendMessage(self.channel_name, name, self)


class User(object):
    """Subscriber"""
    def __init__(self, name):
        self.name = name

    def subscribe_channel(self, channel):
        Youtube.subscribe(self.notify, channel.channel_name)

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
