def main(client):
    print(client.user)


if __name__ == "__main__":
    from base import client as example_client
    main(example_client)