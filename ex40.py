class Song(object):

    # 定义一个名为Song的类
    def __init__(self, lyrics):
        # 这是初始化方法，当创建类的新实例时将被调用
        # 参数lyrics是一个列表，包含歌曲的歌词行
        self.lyrics = lyrics  # 将传入的歌词列表赋值给实例变量self.lyrics

    def sing_me_a_song(self):
        # 这个方法用于打印出歌曲的所有歌词
        for line in self.lyrics:
            # 遍历self.lyrics中的每一行歌词
            print(line)  # 打印当前行的歌词

# 创建Song类的一个实例，并传入生日歌的部分歌词
happy_baby = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# 调用happy_baby实例的sing_me_a_song方法来打印出歌词
happy_baby.sing_me_a_song()

# 创建Song类的另一个实例，并传入不同的歌词
bulls_baby = Song(["Why can't we have kids like they used to",
                    "All of them were so much fun",])

# 调用bulls_baby实例的sing_me_a_song方法来打印出歌词
bulls_baby.sing_me_a_song()

# 创建一个叫 Song 的类，它是 object 的一种。
# 类 Song 有一个 __init__ 初始化函数/方法，它接收 self 和 lyrics 作为参数，将 lyrics 赋值给 self.lyrics。
# 类 Song 有一个名为 sing_me_a_song 的函数/方法，它接收 self 作为参数，遍历 self.lyrics 中的每一行，并打印出来。
# 将 happy_baby 和 bulls_baby 分别赋/设为 Song 类的实例，传入不同的歌词列表。
# 从 Song 中找到 sing_me_a_song 方法，并调用它，传入 happy_baby 和 bulls_baby 作为参数。
