from hbmqtt.client import MQTTClient, ClientException

default_config = {
        'keep_alive': 10,
        'ping_delay': 2,
        'default_qos': 0,
        'default_retain': False,
        'auto_reconnect': True,
        'reconnect_max_interval': 5,
        'reconnect_retries': 10,
    }


class Conn:
    async def __init__(self,uri):
        self.conn = MQTTClient()
        await self.conn.connect(uri)

    async def subscribe(self,topic):
        return await self.conn.subscribe([(topic,2)])

    async def recv(self):
        message = await self.conn.deliver_message()
        return message.data

    async def public(self,topic,message):
        return self.conn.publish(topic,message)

    
