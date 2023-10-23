Basic hashing is a fundamental technique to map data to servers based on their keys, but it suffers from a significant drawback: when servers are added or removed, a large portion of data must be remapped, leading to costly and disruptive redistributions.

To address this challenge, **Consistent Hashing** is an assignment technique used in distributed systems to **minimize the redistribution of data** across servers when any new server is added or an existing one is removed.

In consistent hashing, the approach is as follows:

Circular Hash Space: Instead of a linear representation, we use a circular hash space. This circular structure enables a smoother distribution of data.

Adding Servers and Request Keys: Servers and request keys are added to the hash space based on their hashed values. This hashing is done using a hash function, which determines their positions within the circular space.

Key Allocation: To allocate keys to servers, we proceed in a clockwise direction around the circular hash space. Starting from the hashed position of the key, we search for the nearest server by moving in a clockwise direction until we find a server. This ensures efficient and consistent key-to-server mapping.
