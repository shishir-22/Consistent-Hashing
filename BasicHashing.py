class BasicHasing:
    def __init__(self):
        self.servers = []
        self.request_keys = {}
        self.server_space = 0

    def add_server(self, server_id):
        print("Adding server:", server_id)
        self.servers.append(server_id)
        self.server_space += 1
        self.redistribute_keys()

    def remove_server(self, server_id):
        print("Removing server:", server_id)
        self.servers.remove(server_id)
        self.server_space -= 1
        self.redistribute_keys()

    def redistribute_keys(self):
        for key in self.request_keys:
            server = self.basic_hash(key, self.server_space)
            self.request_keys[key] = self.servers[server]

    def add_request_key(self, key_id):
        print("Adding Request Key", key_id)
        server_name = self.basic_hash(key_id, self.server_space)
        self.request_keys[key_id] = self.servers[server_name]

    @staticmethod
    def basic_hash(key_id, server_space):
        return key_id % server_space

    def get_key_server_mapping(self):
        print("Key server mapping:", self.request_keys)

    def get_servers(self):
        print("Servers:", self.servers)


if __name__ == '__main__':
    bh = BasicHasing()

    # Define Servers
    bh.add_server("s1")
    bh.add_server("s2")
    bh.add_server("s3")
    bh.add_server("s4")

    # Add Request Keys
    bh.add_request_key(1000000)
    bh.add_request_key(1010210)
    bh.add_request_key(1017695)
    bh.add_request_key(1010493)

    # Get Servers
    bh.get_servers()

    # Get Key server Mapping
    bh.get_key_server_mapping()

    # Add new server
    bh.add_server("s5")

    # Get Servers
    bh.get_servers()

    # Get Key server Mapping
    bh.get_key_server_mapping()

    # Remove a server
    bh.remove_server("s1")

    # Get Servers
    bh.get_servers()

    # Get Key server Mapping
    bh.get_key_server_mapping()

    # Add new Request key
    bh.add_request_key(1231231)

    # Get Servers
    bh.get_servers()

    # Get Key server Mapping
    bh.get_key_server_mapping()
