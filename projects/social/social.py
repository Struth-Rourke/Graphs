import random

class User:
    def __init__(self, name):
        self.name = name

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
            # print(" ")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            # print(" ")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.last_id += 1
        # set the users attribute value, at the specified last_id, as the 
        # User(name) to add an entry
        self.users[self.last_id] = User(name)
        # instantiate friendship attribute, at the specified last_id, as a set()
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

        # loop through idx in num_users
        for idx in range(num_users):
            # add_user to the index + 1 (ex. idx = 0, .key() = 1)
            self.add_user(idx + 1)

        ## Create friendships
        # instantiate an empty dictionary to jold the number of friends they have
        num_friends = {}
        # loop through the index of the num_users on the platform
        for i in range(1, num_users + 1):
            # add number of friends equal to a number between n and 0.5n
            # where n is the average friendship, normally distributed
            n = round(random.normalvariate(avg_friendships, avg_friendships * 0.5))
            # set the num_friends value equal to n (normal distribution around avg)
            num_friends[i] = n
        ## CHECK:
        # print(num_friends)

        # loop through the num_users
        for i in range(1, num_users + 1):
            # instantiate num_friends value
            n = num_friends[i]
            # get a list of all_users
            all_users = list(range(1, num_users + 1))
            # remove the person at index i
            all_users.remove(i)
            # instantiate an empty list to remove all the other people who do 
            # not have friends
            remove_list = []
            # loop through the users in all_users
            for user in all_users:
                # if the value of the num_friends for that user is less than 0
                if num_friends[user] <= 0:
                    # append that user to the remove_list
                    remove_list.append(user)

            # loop through all the people in remove_list
            for person in remove_list:
                # remove the person from the all_users list
                all_users.remove(person)
            # if there are no other people in all_users
            if not all_users:
                # the value of the num_friends equals 0
                num_friends[i] = 0
                # num_friends value equals 0
                n = 0

            ## add friendships
            ## CHECK:
            # print(f'Person {i} adding friends from {all_users}')
            # print(f'Friends left in each: {[num_friends[n] for n in all_users]}')
            # while the num_friends value is greater than 0
            while n > 0:
                # create a person variable equal to random.choice of all_users
                person = random.choice(all_users)
                # use add_friendship method between i and person
                self.add_friendship(i, person)
                # subtract from n to reduce the value as you loop
                n -= 1
                # subtract from num_friends value
                num_friends[i] -= 1
                # subtract from num_friends value at that specific person
                num_friends[person] -= 1
            ## CHECK:
            # print(person)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # instantiate an empty dictionary to hold which has already been visited
        visited = {}
        # instantiate an empty queue list
        queue = []
        # append the user_id to the queue
        queue.append(user_id)
        # while the len(queue) is greater than 0
        while len(queue) > 0:
            # current_user = first indexed value in the queue
            current_user = queue.pop(0)
            # print(current_user, queue)
            # get all the connections for the current_user
            for friend in self.friendships[current_user]:
                # don't add people we are going to add (in queue already)
                # or have already added (in visited)
                if friend not in queue and friend not in visited:
                    # append the friend to the queue
                    queue.append(friend)

            ## link backwards
            # if the current_user equals the user_id
            if current_user == user_id:
                # visited value for the specificed current_user equals a list 
                # with current_user inserted
                visited[current_user] = [current_user]
            # else (otherwise)
            else:
                # for a given connection in the list of friendships, if it is
                # also in visited
                for conn in [x for x in self.friendships[current_user] if x in visited]:
                    # create a copy of the conn
                    visited[current_user] = visited[conn][:]
                    # append the current_user to the visited value at teh specified
                    # current_user spot
                    visited[current_user].append(current_user)
        # return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
