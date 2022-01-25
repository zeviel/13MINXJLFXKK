import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.LIGHT_STEEL_BLUE + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminojlfxck", font="graffiti"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
chats = sub_client.get_chat_threads(start=0, size=100)
for z, title in enumerate(chats.title, 1):
    print(f"{z}.{title}")
chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]


def join_and_leave():
    try:
        sub_client.leave_chat(chatId=chat_id)
        sub_client.join_chat(chatId=chat_id)
    except BaseException:
        return


def main_process():
    while True:
        print("-- Joining and Leaving...")
        with ThreadPoolExecutor(max_workers=100) as executor:
            _ = [executor.submit(join_and_leave) for _ in range(100000)]


main_process()
