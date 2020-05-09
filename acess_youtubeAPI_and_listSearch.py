#from pytube import Youtube
import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


#scope_to_find = $"https://www.youtube.com/watch?v={videoID}"

arq = open("cantores.txt", "r")

str = arq.read().split("\n") #Vira uma lista por causa do split


scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]

def main(): #Connect YouTubeAPI
    
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_2.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    #get searched data
    for dado in str:
        request = youtube.search().list(
            part="snippet",
            maxResults=30,
            q=dado,
            type="video"
        )
        response = request.execute()

        for data in response['items']: #print Autor - Name of the music

            print(data['snippet']['title']) 

            #print(data['id']) Retorna conteúdo tudo: {'kind': 'youtube#video', 'videoId': 'r_0JjYUe5jo'}
            #Agora é só montar o prog. Faz uma função pra playlist e outra pra videos...

        print("\n")


if __name__ == "__main__":
    main()
