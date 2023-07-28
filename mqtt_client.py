import paho.mqtt.client as mqtt
import threading, time, queue

Qmqtt = queue.Queue()


###
# 接收 Question/DeviceID/Timestamp or index  # 每个设备需要一个device id
# 发送 Answer/DeviceID/Timestamp/
###
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Answer/#")
    print("Connected with result code " + str(rc))
    client.publish("Question/test", "如果不会，就回答我不知道。在40个字内描述一下，杜甫")  # 两句话描述一下,#唐宋八大家？


# The callback for when a PUBLISH message is received from the server.
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic)
    Qmqtt.put({"topic": msg.topic, "payload": msg.payload})


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
ip = "10.193.97.217"
ip = "127.0.0.1"
# ip = "172.20.192.1"
ip = "172.20.192.1"
ip = "7.247.135.228"

print("client.connect(ip, 1883)", ip)
client.connect(ip, 1883)
threading.Thread(target=client.loop_forever, args=()).start()


def main():
    global stop_stream
    while True:
        history = []
        data = Qmqtt.get()
        print(data["payload"].decode("utf-8", errors="ignore"))


if __name__ == "__main__":
    main()
