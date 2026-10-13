class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        keyhash = self.hash(key)
        bucket = self.buckets[keyhash]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        keyhash = self.hash(key)
        bucket = self.buckets[keyhash]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        keyhash = self.hash(key)
        bucket = self.buckets[keyhash]

        return key in bucket
        
    def hash(self, val: int) -> int:
        return val % len(self.buckets)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)