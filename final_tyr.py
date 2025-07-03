# youtube_project/final_tyr.py
# final_tyr.py
# final_tyr.py

import json
import sys

fil='you.txt'
def load_videos():
    try:
        with open(fil,'r') as file:
            return json.load(file)
    except:
        return []


def list_videos(videos):
    if videos:
        for index,video in enumerate(videos,start=1):
            if 'name' in video and 'time' in video:
                print(f"{index}.{video['name']},{video['time']}")
    else:
        print("Video list is empty .")
def Add_video(videos):
    
    name=input("Add video name : ")
    time=input("Add video tme  : ")
    videos.append({'name':name,'time':time})
    save_videos(videos)




def Update_video(videos):
    list_videos(videos)
    index=int(input('Which no of video you want to update : '))
    if(1<=index<=len(videos)):
        name=input("Enter video name : ")
        time=input("ENter video duration :")
        videos[index-1]={'name':name,'time':time}
        save_videos(videos)
    else:
        print("Invalid input...")
def Delete_video(videos):
    list_videos(videos)
    index=int(input("Enter whhcih no of video you want to delete : "))
    if (1<=index<=len(videos)):
        del videos[index-1]
        print(f" Video {index} deleted sucessfully .")
        save_videos(videos)
    else:
        print("Invalid video no")

def save_videos(videos):
    try:
        with open(fil,'w') as file:
            json.dump(videos,file)
    except:
        print("Error occur..")

def exit_fun():
    
    print("\n Sucessfully exit")
    exit()
    

def main():
    while True:
        videos=load_videos()
        print(" "+"*"*52)
        print("*                                                    *")
        print("*           $%*Youtube management system*%$          *")
        print("*                                                    *")
        print(" "+"*"*52)
        print("\n\n")
        print("Choose an option : ")
        print("1.List youtube video")
        print("2.Add youtube video")
        print("3.Update youtube video")
        print("4.Delete youtube video")
        print("5.Exit list")

        choice=input("Enter your choice : ")

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                Add_video(videos)
            case'3':
                Update_video(videos)
            case'4':
                Delete_video(videos)
            case'5':
                exit_fun()
            case _:
                print("Invalid input")
if __name__ == '__main__':
    main()