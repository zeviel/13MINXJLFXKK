import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_STEEL_BLUE + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminojlfxck", font="graffiti"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
chats = client.my_chat_threads(ndc_Id=ndc_Id, size=100)
for z, title in enumerate(chats.title, 1):
    print(f"{z}.{title}")
thread_Id = chats.thread_Id[int(input("Select The Chat >> ")) - 1]


def join_and_leave():
    try:
        client.leave_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
        client.join_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
    except BaseException:
        return


def main_process():
    while True:
        print("Joining and Leaving....")
        with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
            _ = [executor.submit(join_and_leave) for _ in range(100000)]


main_process()
