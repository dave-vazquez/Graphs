from util import Queue, Stack
import random
import pprint
import os
p_print = pprint.PrettyPrinter(width=30).pprint
os.system("clear")


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        # Use add_user num_users times
        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Generate all friendship combinations
        possible_friendships = []
        # Avoid dupes by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle all possible friendships
        random.shuffle(possible_friendships)
        # Create for first X pairs x is total //2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # * Hint 1: To create N random friendships, you could create a
        # list with all possible friendship combinations, shuffle the
        # list, then grab the first N elements from the list. You will
        # need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as
        # `add_friendship(2, 1)`. You should avoid calling one after
        # the other since it will do nothing but print a warning. You
        # can avoid this by only creating friendships where user1 < user2.

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        qq = Queue()
        qq.enqueue([user_id])

        while qq.size() > 0:

            path = qq.dequeue()

            if path[-1] not in visited:

                visited[path[-1]] = path

                if self.friendships[path[-1]]:
                    next_friendships = self.friendships[path[-1]]
                else:
                    next_user = path[-1] + 1
                    next_friendships = self.friendships[next_user]

                for friend in next_friendships:
                    new_path = list(path)
                    new_path.append(friend)
                    qq.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    p_print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    p_print(connections)
