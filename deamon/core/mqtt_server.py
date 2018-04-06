from hbmqtt.broker import Broker

default_config = {
        'listeners':{
            'default': {
                'type': 'tcp',
                'bind': '0.0.0.0:1883'
                }
            }
        }

class Server:
    def __init__(self,config = default_config):
        self.broker = Broker(config)

    async def start(self):
        await self.broker.start()

if __name__ == '__main__':
    import logging
    import asyncio
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    mqtt = Server()
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(mqtt.start())
    asyncio.get_event_loop().run_forever()

