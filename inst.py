import instagram
from instagram.agents import WebAgent
from instagram import Account, Media, Location
agent = WebAgent()
account = Account("zuck")
loc = Location(17326249)
agent.update(account)
media = agent.get_media(loc, count = 50)
print(media)
