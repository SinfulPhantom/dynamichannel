import os


def load_extensions(client):
    for directory in os.listdir("./cogs"):
        if not directory.startswith("_"):
            for file in os.listdir(f"./cogs/{directory}"):
                if file.endswith(".py") and not file.startswith("__init__"):
                    client.load_extention(f"cogs.{directory}.{file[:3]}")
