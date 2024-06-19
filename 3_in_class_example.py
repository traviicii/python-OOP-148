
# User class

class User():

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.friends = []
        self.posts = {}

    def change_pword(self, new_pword):
        self.password = new_pword

    # user contact method
    def get_info(self):
        print(f"{self.username} can be contacted at {self.email}")

    def login(self):
        logged_in.append(self)

    def logout(self):
        logged_in.remove(self)

    # Method to add to friends list
    def add_friend(self, friend):
        if isinstance(friend, User):
            print(f"Adding {friend.username} to {self.username}'s friend list!")
            self.friends.append(friend)
        else:
            print("Hmm, looks like that's an invalid user!")

    # View friends list
    def friends_list(self):
        for friend in self.friends:
            print(friend.username)

    # Create a post
    def create_post(self):
        while True:
            caption = input("Enter a caption for your post: ")
            if len(caption) > 250:
                print("Hey that's way too long for this fake Twitter site!")
                continue
            new_id = self.next_id()
            self.posts[new_id] = caption
            break

    def next_id(self):
        last_id = 0
        for key in self.posts.keys():
            if key > last_id:
                last_id = key
        return last_id + 1



logged_in = []

travis = User('travisp@codingtemple.com', 'traviicii', '1234')
cole = User('coleeubanks73@gmail.com', 'ceubie', '9876')
ari = User('ari828@gmail.com', 'spoon828', 'password')
brad = User('bradk@yahoo.com', 'bk1998', 'wordpass')

travis.get_info()
cole.get_info()

brad.login()
cole.login()
travis.login()
print(logged_in)

print(logged_in[0].username)
print(logged_in[2].username)

travis.add_friend(cole)
travis.add_friend(ari)
travis.add_friend(brad)

print("These are Travis' friends")
travis.friends_list()

cole.create_post()
cole.create_post()
print(cole.posts)

list1 = []
print(type(list1))

list1 = {}
print(type(list1))