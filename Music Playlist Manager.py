class Song:

    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"ID: {self.song_id} | Title: {self.title} | Artist: {self.artist} | Duration: {self.duration}"


class Node:

    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self._size

    def insertFirst(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        print("[SUCCESS]: Song added at the beginning.")

    def insertLast(self, song):
        new_node = Node(song)

        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self._size += 1
        print("[SUCCESS]: Song added at the end.")

    def insertAt(self, position, song):

        if position < 1 or position > self._size + 1:
            print(f"[ERROR]: Invalid position! Enter between 1 and {self._size + 1}.")
            return False

        if position == 1:
            self.insertFirst(song)
            return True

        new_node = Node(song)
        current = self.head
        count = 1

        while count < position - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

        self._size += 1
        print(f"[SUCCESS]: Song inserted at position {position}.")

        return True

    def search(self, song_id):

        current = self.head

        while current is not None:

            if current.song.song_id == song_id:
                return current.song

            current = current.next

        return None

    def delete(self, song_id):

        if self.isEmpty():
            return False

        if self.head.song.song_id == song_id:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head

        while current.next is not None:

            if current.next.song.song_id == song_id:
                current.next = current.next.next
                self._size -= 1
                return True

            current = current.next

        return False

    def display(self):

        if self.isEmpty():
            print("\nPlaylist is empty.")
            return

        print("\n--- MUSIC PLAYLIST ---")

        current = self.head
        pos = 1

        while current is not None:
            print(f"[{pos}] {current.song}")
            current = current.next
            pos += 1

        print(f"Total Songs: {self._size}")


def main_playlist_manager():

    playlist = LinkedList()

    while True:

        print("\n" + "=" * 30)
        print(" MUSIC PLAYLIST MANAGER ")
        print("=" * 30)

        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:

            sid = input("Enter Song ID: ").strip()

            if playlist.search(sid) is not None:
                print("[ERROR]: Song ID already exists in playlist!")
                continue

            title = input("Enter Song Title: ").strip()
            artist = input("Enter Artist: ").strip()
            duration = input("Enter Duration (e.g. 4:23): ").strip()

            song = Song(sid, title, artist, duration)

            if choice == "1":
                playlist.insertFirst(song)

            elif choice == "2":
                playlist.insertLast(song)

            elif choice == "3":

                try:
                    pos = int(input("Enter Position to insert: "))
                    playlist.insertAt(pos, song)

                except ValueError:
                    print("[ERROR]: Invalid integer input for position.")

        elif choice == "4":

            playlist.display()

        elif choice == "5":

            sid = input("Enter Song ID to search: ").strip()

            found_song = playlist.search(sid)

            if found_song:
                print(f"\n[FOUND]: {found_song}")

            else:
                print("\n[ERROR]: Song not found.")

        elif choice == "6":

            sid = input("Enter Song ID to remove: ").strip()

            if playlist.delete(sid):
                print("[SUCCESS]: Song successfully removed from playlist.")

            else:
                print("\n[ERROR]: Song ID not found.")

        elif choice == "7":

            print(f"\nTotal songs in playlist: {playlist.size()}")

        elif choice == "8":

            print("Exiting Music Playlist Manager...")
            break

        else:

            print("[ERROR]: Invalid choice. Please select from 1 to 8.")


if __name__ == "__main__":
    main_playlist_manager()