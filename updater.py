from github import Github


def run():
    g = Github("5856c7d3b38da3f93c089b9d85102902173afa01")

    repo = g.get_repo("tctn27/combiner_discord_bot")

    hub_file = repo.get_contents("main.py")

    with open("main.py", "w") as local:
        with open(hub_file.download_url, "r") as remote:
            for line in remote.read():
                local.write(line)
