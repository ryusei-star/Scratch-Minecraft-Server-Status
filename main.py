import scratchattach as sa
import time
from mcstatus import JavaServer

USERNAME = "ユーザー名"
PASSWORD = "パスワード"
PROJECT_ID = "プロジェクトID"
VARIABLE_NAME = "クラウド変数の名前"
MC_ADDRESS = "確認したいマインクラフトサーバーのIPとポート"

session = sa.login(USERNAME, PASSWORD)
cloud = session.connect_cloud(PROJECT_ID)
server = JavaServer.lookup(MC_ADDRESS)

try:
    while True:
        try:
            status = server.status()
            online = 1
            players = status.players.online
        except Exception:
            online = 0
            players = 0

        cloud_value = str(online) + str(players)
        cloud.set_var(VARIABLE_NAME, cloud_value)
        time.sleep(5)
except KeyboardInterrupt:
    cloud.set_var(VARIABLE_NAME, "2")
