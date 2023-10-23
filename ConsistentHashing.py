HASH_SPACE = 256
VIRTUAL_SERVERS = 3


class ConsistentHashing:
    """
    Consistent Hashing is an assignment technique used in distributed systems to minimize the redistribution of data
     across servers when any new server is added or existing one is removed
    """
    def __init__(self):
        self.hash_space = [0] * HASH_SPACE
        self.servers = []
        self.request_keys = []

    def add_server(self, server):
        """
        Method to add the servers in hash_space as per VIRTUAL_SERVERS value
        :param server: Server
        """
        self.servers.append(server)
        for i in range(VIRTUAL_SERVERS):
            # Performing modulo operation with HASH_SPACE just for easier implementation.
            # Ideally, in consistent hashing we do not perform modulo operation to avoid any kind of collisions
            hash_value = hash(server + str(i)) % HASH_SPACE
            self.hash_space[hash_value] = server

    def add_request_key(self, request_key):
        """
        Method to add the Request key in hash_space
        :param request_key: Request key
        """
        self.request_keys.append(request_key)
        hash_value = hash(request_key) % HASH_SPACE
        self.hash_space[hash_value] = request_key

    def get_servers(self):
        """
        Method to print the servers
        """
        print("Servers:", self.servers)

    def get_request_keys(self):
        """
        Method to print the request keys
        """
        print("Request keys:", self.request_keys)

    def remove_server(self, server):
        """
        Method to remove all the servers (VIRTUAL_SERVERS for the given server) from the hash_space
        :param server: Server
        """
        self.servers.remove(server)
        for i in range(VIRTUAL_SERVERS):
            hash_value = hash(server + str(i)) % HASH_SPACE
            self.hash_space[hash_value] = 0

    def get_key_server_mapping(self):
        """
        Method to get the Request-Key server Mapping. Currently, using linear search to find the servers but binary
        search can be used to improve performance
        """
        for key in self.request_keys:
            key_hash = hash(key) % HASH_SPACE
            key_index = self.hash_space[key_hash] % HASH_SPACE

            # Search for server in clockwise direction
            server_found = False
            for i in range(key_index, len(self.hash_space)):  # This can be improved by using binary search
                if self.hash_space[i] in self.servers:
                    print("Key {} is mapped to server {}".format(key, self.hash_space[i]))
                    server_found = True
                    break

            # Since we are assuming our hash space to be circular, if server is not found till the end of hash space,
            # we will search for it from start again
            if not server_found:
                for i in range(0, len(self.hash_space)):  # This can be improved by using binary search
                    if self.hash_space[i] in self.servers:
                        print("Key {} is mapped to server {}".format(key, self.hash_space[i]))
                        break


if __name__ == "__main__":
    ch = ConsistentHashing()

    ###################################
    # Define Servers
    ch.add_server("s1")
    ch.add_server("s2")
    ch.add_server("s3")
    ch.add_server("s4")

    # Add Request Keys
    ch.add_request_key(1000000)
    ch.add_request_key(1010210)
    ch.add_request_key(1017695)
    ch.add_request_key(1010493)

    # Get Servers
    ch.get_servers()

    # Get Request keys
    ch.get_request_keys()

    # Get Request keys server mapping
    ch.get_key_server_mapping()

    ###################################
    # Add new server
    ch.add_server("s5")

    # Get Servers
    ch.get_servers()

    # Get Request keys
    ch.get_request_keys()

    # Get Request keys server mapping
    ch.get_key_server_mapping()

    ###################################
    # Remove a server
    ch.remove_server("s1")

    # Get Servers
    ch.get_servers()

    # Get Request keys
    ch.get_request_keys()

    # Get Request keys server mapping
    ch.get_key_server_mapping()

    ###################################
    # Add new Request keys
    ch.add_request_key(1231231)
    ch.add_request_key(1253231)
    ch.add_request_key(1230431)
    ch.add_request_key(1899231)
    ch.add_request_key(2131231)

    # Get Servers
    ch.get_servers()

    # Get Request keys
    ch.get_request_keys()

    # Get Request keys server mapping
    ch.get_key_server_mapping()

    ###################################
    # Remove server s2
    ch.remove_server("s2")

    # Get Servers
    ch.get_servers()

    # Get Request keys
    ch.get_request_keys()

    # Get Request keys server mapping
    ch.get_key_server_mapping()

