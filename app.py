class SongApp:

    def __init__(self):
        self._login_list = [["admin", "admin", []], 
                            ["u", "p", [["Bad Blood", "Taylor Swift", "Pop"], ["Whiskey Glasses", "Morgan Wallen", "Country"]]]]
        self._song_database = [["Bad Blood", "Taylor Swift", "Pop"], 
                               ["Whiskey Glasses", "Morgan Wallen", "Country"], 
                               ["In Da Club", "50 Cent", "Hip-Hop"], 
                               ["Dial Drunk", "Noah Kahan", "Indie"], 
                               ["Lover", "Taylor Swift", "Pop"], 
                               ["Cinderella Man", "Eminem", "Hip-Hop"], 
                               ["Down to One", "Luke Bryan", "Country"], 
                               ["Shake it Off", "Taylor Swift", "Pop"]]

    def login_page(self):
        print()
        print("This app is used to help you with organizing your music playlist.")
        print()
        print("It has the capabilities of adding, removing, and ordering of songs.")
        print()
        print("It also has song recommendations, which you could add to your playlist,")
        print("keeping track of your current playlist by focusing on most popular artists and genres.")
        print()
        print()
        print()
        flag = False
        while flag is False:
            try:
                print()
                log_or_create_num = int(input("Hello! Do you have an existing account (type 1) or would you like to create a new account (type 0)? "))
                print()
            except ValueError:
                print()
                log_or_create_num = -1
            if log_or_create_num == 0:
                self.create_account()
                return
            elif log_or_create_num == 1:
                break
            else:
                print("Please choose a valid number")
                print()
                continue
        username = self.username_login()
        self.password_login(username)
        return

    def create_account(self):
        create_cred = False
        while create_cred is False:
            user_string = input("Enter a new and valid username: ")
            print()
            is_dup = self.is_username_dup(user_string)
            if is_dup is True:
                continue
            if len(user_string) > 0:
                password_string = self.password_valid()
                create_cred = True
                print("Successful creation of account.")
                print()
                self._login_list.append([user_string, password_string, []])
                create_cred = True
        self._login_list.append([user_string, password_string, []])
        self.about_nav(user_string, [])

    def username_login(self):
        is_valid = False
        while is_valid is False:
            username = input("What is your username? ")
            print()
            for i in range(len(self._login_list)):
                if self._login_list[i][0] == username:
                    is_valid = True
                    break
        return username
    
    def password_login(self, username):
        is_valid = False
        while is_valid is False:
            password = input("What is your password? ")
            print()
            for i in range(len(self._login_list)):
                if self._login_list[i][0] == username:
                    if self._login_list[i][1] == password:
                        if username == "admin":
                            print("Here is the current database of songs.")
                            for i in range(len(self._song_database)):
                                print(self._song_database[i])
                            print()
                        self.about_nav(username, self._login_list[i][2])
                        return

    def password_valid(self):
        password_cred = False
        while password_cred is False:
            password_string = input("Enter a new and valid password: ")
            print()
            if len(password_string) > 0:
                password_cred = True
        return password_string

    def is_username_dup(self, username):
        for i in range(len(self._login_list)):
            if self._login_list[i][0] == username:
                print("Username already taken. Please choose another.")
                print()
                return True
        return False
    
    def about_nav(self, username, playlist):
        about_nav = False
        while about_nav is False:
            try:
                about_num = int(input("Would you like to learn more about this application (1 for yes, 0 for no): "))
                print()
            except ValueError:
                print()
                # set to a number to avoid if conditional error
                about_num = -1
            if about_num == 1:
                self.about_page(username, playlist, True)
                about_nav = True
            elif about_num == 0:
                self.welcome_page(username, playlist)
                about_nav = True
            else:
                print("Please choose either 0 or 1.")
                print()
        return

    def welcome_page(self, username, playlist):
        print("Welcome to this music and database app!")
        print()
        print()
        print()
        print("The navigation listed will help you with the main pages of this app.")
        print()
        print("Your Playlist allows you to view your current playlist and order of songs")
        print("(edit and remove are inside of this page)")
        print()
        print("Artist/Genre Stats allows you to find out what artists and genres are your most popular")
        print()
        print("Add Song allows you to add songs by different type of search")
        print()
        print("About allows you to find out more information about the app")
        print()
        self.navigation(username, playlist)
    
    def navigation(self, username, playlist):
        print("0 for Your Playlist")
        print("1 for Arist/Genre Stats")
        print("2 for Add Song")
        print("3 for About")
        print("4 for Exit (Warning: In this current implentation, you will lose all playlist data)")
        print()
        nav_flag = False
        while nav_flag is False:
            try:
                nav_num = int(input("Where would you like to proceed? "))
                print()
            except ValueError:
                print()
                nav_num = -1
            if nav_num != 0 and nav_num != 1 and nav_num != 2 and nav_num != 3 and nav_num != 4:
                print("Enter a valid number")
                print()
            else:
                if nav_num == 0:
                    self.your_playlist_page(username, playlist)
                elif nav_num == 1:
                    self.artist_genra_stats_page(username, playlist)
                elif nav_num == 2:
                    self.add_song_page(username, playlist)
                elif nav_num == 3:
                    self.about_page(username, playlist, False)
                else:
                    print("Warning: In this current implentation, you will lose all playlist data")
                    try:
                        exit_num = int(input("Are you sure you want to exit? (1 for yes, 0 for no) "))
                        print()
                    except ValueError:
                        print()
                        exit_num = -1
                    if exit_num == 0:
                        continue
                    else:
                        return
                nav_flag = True

    def your_playlist_page(self, username, playlist):
        for i in range(len(self._login_list)):
            if self._login_list[i][0] == username:
                for j in range(len(self._login_list[i][2])):
                    print(self._login_list[i][2][j])
                print()
        action_flag = False
        while action_flag is False:
            try:
                action_num = int(input("Would you like to take action on editing the order or removing a song? (1 for yes, 0 for no) "))
                print()
            except ValueError:
                print()
                action_num = -1
            if action_num != 0 and action_num != 1:
                print("Please choose either 1 or 0.")
                print()
            else:
                if action_num == 1:
                    self.edit_or_remove_option_page(username, playlist)
                else:
                    self.navigation(username, playlist)
                action_flag = True

    def edit_or_remove_option_page(self, username, playlist):
        action_flag = False
        while action_flag is False:
            try:
                action_num = int(input("Would you like to edit the order (<____||) of the songs in the playlist or remove the song (\_/)? (1 for edit, 0 for remove) "))
                print()
            except ValueError:
                print()
                action_num = -1
            if action_num != 0 and action_num != 1:
                print("Please choose either 1 or 0.")
                print()
            else:
                if action_num == 1:
                    self.edit_page(username, playlist)
                else:
                    self.remove_page(username, playlist)
                action_flag = True

    def edit_page(self, username, playlist):
        print("Edit song order <____||")
        print()
        print("Here is your playlist")
        print()
        for i in range(len(self._login_list)):
            if self._login_list[i][0] == username:
                for j in range(len(self._login_list[i][2])):
                    print(self._login_list[i][2][j])
                print()
        song_flag = False
        correct_title = False
        j = -1
        while song_flag is False:
            song_title = input("What song would you like to change the order of? (by moving it up 1 spot) ")
            print()
            for i in range(len(playlist)):
                if playlist[i][0] == song_title:
                    if i == 0:
                        print("Can't move up first song in playlist. Choose a different song.")
                        print()
                        correct_title = False
                    else:
                        playlist[i], playlist[i - 1] = playlist[i - 1], playlist[i]
                        for i in range(len(self._login_list)):
                            if self._login_list[i][0] == username:
                                self._login_list[i][2] = playlist
                                correct_title = True
                    j = 0
                    break
            if correct_title is True:
                song_flag = True
            if j == -1:
                print("Make sure you are typing in the correct song title from your playlist.")
                print()
        self.your_playlist_page(username, playlist)
        return


                        # not sure if I want to include this part since other edit options will be implemented later
                        # self.display_updated_playlist(username)
                        # edit_flag = False
                        # while edit_flag is False:
                        #     edit_num = int(input("Would you like to continue editing the order of your playlist? (1 for yes, 0 for no) "))
                        #     print()
                        #     if edit_num != 0 and edit_num != 1:
                        #         print("Please choose either 1 or 0.")
                        #         print()
                        #     else:
                        #         # if edit_num == 
                        #         edit_flag = True
                        #         pass
            

    def display_updated_playlist(self, username):
        for i in range(len(self._login_list)):
            if self._login_list[i][0] == username:
                for j in range(len(self._login_list[i][2])):
                    print(self._login_list[i][2][j])
                print()

    def remove_page(self, username, playlist):
        song_flag = False
        j = -1
        while song_flag is False:
            if len(playlist) == 0:
                print("Can't remove from an empty playlist.")
                print()
                song_flag = True
                continue
            song_title = input("What Song would you like to remove? ")
            print()
            remove_flag = False
            while remove_flag is False:
                print("ARE YOU SURE YOU WANT TO REMOVE THIS SONG?")
                print("This will remove the song from this playlist.")
                print("You can add this song back, but will have to go to the add song page/edit the position of the song if you wish.")
                try:
                    remove_num = int(input("1 for remove (Yes), 0 for No: "))
                    print()
                except ValueError:
                    print()
                    remove_num = -1
                if remove_num != 0 and remove_num != 1:
                    print("Please choose a valid number.")
                    print()
                else:
                    remove_flag = True
            for i in range(len(playlist)):
                if playlist[i][0] == song_title:
                    del playlist[i]
                    j = 0
                    for i in range(len(self._login_list)):
                        if self._login_list[i][0] == username:
                            self._login_list[i][2] = playlist
                            break
                    song_flag = True
                    break
            if j == -1:
                print("Make sure you are typing in the correct song title from your playlist.")
                print()
        self.your_playlist_page(username, playlist)
        return

    def artist_genra_stats_page(self, username, playlist):
        pass

    def add_song_page(self, username, playlist):
        print("Here are the current available songs to add:")
        print()
        temp_database = []
        for i in range(len(self._song_database)):
            if self._song_database[i] not in playlist:
                temp_database.append(self._song_database[i])
        for i in range(len(temp_database)):
            print(temp_database[i])
        print()
        artist_temp_database = []
        genre_temp_database = []
        add_dec_flag = False
        while add_dec_flag is False:
            try:
                add_dec_num = int(input("Do you wish to add a song from this database? (1 for yes, 0 for no) "))
                print()
            except ValueError:
                print()
                add_dec_num = -1
            if add_dec_num == 0:
                print("Back to navigation page")
                print()
                self.navigation(username, playlist)
                add_dec_flag = True
            elif add_dec_num == -1:
                print("Please choose a valid number")
                continue
            else:
                type_search_flag = False
                while type_search_flag is False:
                    print("0 to search by title")
                    print("1 to search by artist")
                    print("2 to search by genre")
                    try:
                        type_search_num = int(input("How would you like to search to add a song? (pick a number) "))
                        print()
                    except ValueError:
                        print()
                        type_search_num = -1
                    if type_search_num == 0:
                        self.add_song_by_title(username, playlist, temp_database)
                        type_search_flag = True
                        add_dec_flag = True
                        return
                    elif type_search_num == 1:
                        artist_flag = False
                        while artist_flag is False:
                            artist = input("What artist would you like to search for? ")
                            print()
                            j = -1
                            for i in range(len(temp_database)):
                                if artist == temp_database[i][1]:
                                    artist_temp_database.append(temp_database[i])
                                    j = 0
                            if j == 0:
                                self.add_song_by_title(username, playlist, artist_temp_database)
                                artist_flag = True
                                type_search_flag = True
                                add_dec_flag = True
                                return
                            else:
                                print("Please choose an artist from this database")
                                print()
                    elif type_search_num == 2:
                        genre_flag = False
                        while genre_flag is False:
                            genre = input("What genre would you like to search for? ")
                            print()
                            j = -1
                            for i in range(len(temp_database)):
                                if genre == temp_database[i][2]:
                                    genre_temp_database.append(temp_database[i])
                                    j = 0
                            if j == 0:
                                self.add_song_by_title(username, playlist, genre_temp_database)
                                genre_flag = True
                                type_search_flag = True
                                add_dec_flag = True
                                return
                            else:
                                print("Please choose a genre from this database")
                                print()
                        input("What genre would you like to search for? ")
                    else:
                        print("Please choose a valid number")
                        print()

    def add_song_by_title(self, username, playlist, temp_database):
        print("Here are the current available songs to add:")
        print()
        for i in range(len(temp_database)):
            print(temp_database[i])
        print()
        title_flag = False
        while title_flag is False:
            title = input("What title would you like to add? ")
            print()
            j = -1
            for i in range(len(temp_database)):
                if title == temp_database[i][0]:
                    playlist.append(temp_database[i])
                    j = 0
                    break
            if j == 0:
                for i in range(len(self._login_list)):
                    if self._login_list[i][0] == username:
                        self._login_list[i][2] = playlist
                        self.navigation(username, playlist)
                        title_flag = True
                        return
            else:
                print("Please choose a song to add from this database")
                print()
            
    
    def about_page(self, username, playlist, from_login):
        print("This app is used to help you with organizing your music playlist.")
        print()
        print("It has the capabilities of adding, removing, and ordering of songs.")
        print()
        print("It also has song recommendations, which you could add to your playlist,")
        print("keeping track of your current playlist by focusing on most popular artists and genres.")
        print()
        print()
        print()
        if from_login is True:
            print("Welcome page")
            print()
            self.welcome_page(username, playlist)
        else:
            self.navigation(username, playlist)

PlaylistObj = SongApp()
PlaylistObj.login_page()