from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.buzzsprout.com/1768544.rss"
url2 = "https://anchor.fm/s/4b8b7144/podcast/rss"
url3 = "https://feeds.buzzsprout.com/1434298.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://storage.buzzsprout.com/variants/3ny3yresi3694lge2ji2aisxq7vz/f81607a3cd537406cf0cf506c726bfe2824c5e584c9e9dc5e04e42436c820a79.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://github.com/leopheard/ShadowProof/blob/master/resources/media/1.jpg?raw=true"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://i1.sndcdn.com/avatars-Tiohp0BVzNTdhRn1-aZ6Iqg-original.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
