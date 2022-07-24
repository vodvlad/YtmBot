# Introduction
This bot was created to upload audio files to YouTube Music. To use the bot, you need to send him a link to a video from YouTube. The bot will download the video locally and convert it to mp3 format, then upload the audio file to the YouTube music service. You can also send a regular audio file to the bot, it will also automatically upload the file to the service.  

# Starting

First you have to create a telegram bot using a [BotFather](https://t.me/BotFather).  
After creating the bot. [BotFather](https://t.me/BotFather) will send you your bot's token.  
  
![Screenshot_1](https://user-images.githubusercontent.com/20659925/178162944-3868c067-6d90-467b-9d51-4f929ea07b23.png)  
# Setting
In the TelegBot.py file you have to insert the generated token into the TOKEN.  


![image](https://user-images.githubusercontent.com/20659925/178163089-5fb56430-1020-4c93-9315-9ca41a0921b8.png)  

In the headers_auth.json file, you must insert the Cookie and User-Agent.  
* Open a new tab  
* Open the developer tools (Ctrl-Shift-I) and select the “Network” tab  
* Go to [YouTube Music](https://music.youtube.com) and ensure you are logged in

![image](https://user-images.githubusercontent.com/20659925/178163460-dd89957a-fcf3-4904-a26c-685489b29f6c.png)  
* Find an authenticated POST request. The simplest way is to filter by ***/browse*** using the search bar of the developer tools. If you don’t see the request, try scrolling down a bit or clicking on the library button in the top bar.

![image](https://user-images.githubusercontent.com/20659925/178163481-ee1e4127-3cfd-4c18-a11f-d1138fb5018e.png)
* Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy everything starting from “accept: */*” to the end of the section

![image](https://user-images.githubusercontent.com/20659925/178163502-ab512085-0f53-47c2-8dd3-805e0538dc1f.png)

![image](https://user-images.githubusercontent.com/20659925/178163535-265b319e-4ddf-4c8e-95ad-ed14bafc4c65.png)
* Copy the cookie string and paste it.

![image](https://user-images.githubusercontent.com/20659925/178163593-f207d826-38e0-485e-9f05-368cc7185e15.png)
![image](https://user-images.githubusercontent.com/20659925/178163852-72835f0c-28a7-456c-bc0c-3787e1129105.png)
* In Google search, enter "My user agent" and copy the data.  
![image](https://user-images.githubusercontent.com/20659925/178163890-1b648f20-92de-4467-83fb-d4a542e20884.png)
![image](https://user-images.githubusercontent.com/20659925/178163932-9393d7d8-4805-4bec-bfbb-d7e9175de9b3.png)
Launch the bot via ***TelegBot.py***



