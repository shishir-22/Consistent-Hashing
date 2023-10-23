Basic hashing is a fundamental technique to map data to servers based on their keys, but it suffers from a significant drawback: when servers are added or removed, a large portion of data must be remapped, leading to costly and disruptive redistributions.

To address this challenge, **Consistent Hashing** is an assignment technique used in distributed systems to **minimize the redistribution of data** across servers when any new server is added or an existing one is removed.
