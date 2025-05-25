import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("\n")
    print('*' * 80)
    print("\nAvailable YouTube Videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['name']} , Duration: {video['duration']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video duration: ")
    video = {'name': name, 'duration': time}
    videos.append(video)
    save_data(videos)

def update_video(videos):
    list_videos(videos)
    try:
        index = int(input("Enter the index of the video to modify: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new video title: ")
            duration = input("Enter new video duration: ")
            videos[index] = {'name': name, 'duration': duration}
            save_data(videos)
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def delete_video(videos):
    list_videos(videos)
    try:
        index = int(input("Enter the index of the video to remove: ")) - 1
        if 0 <= index < len(videos):
            del videos[index]
            save_data(videos)
            print("Video removed successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()

    while True:
        print("\n====== YouTube Video Manager ======")
        print("1. Show all videos")
        print("2. Insert new video")
        print("3. Modify existing video")
        print("4. Remove a video")
        print("5. Exit")

        choice = input("Enter your choice: \n")

        if choice == '1':
            list_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
