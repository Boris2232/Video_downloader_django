-- There is a explanation from Download_vedos.views function --

!!! When resolution button is pushed, javascritp script print Downloading..


?? After importing and downloading required libraries, create some global variables ??

                            mistakes = Mistakes()
                            resolution = Resolution()
                            mistakes.mistakes['empty_link'], mistakes.mistakes['age_restriction'] = False, False
                            Link = Link()

?? The function below retrieves the list of resolutions to illustrate them on web page ??


                    def link_inserting(link):
                    ## link is a argument which contains video link in string format
                    
                        ## using pytube.YouTube
                        video_link = YouTube(link, use_oauth=True, allow_oauth_cache=True)
                        
                        ## get the streams of the video
                        streams = video_link.streams
                        resolutions = set()
                        
                        ## adding different available resolutions for the video in a set (to not have repetitions)
                        for stream in streams:
                            resolutions.add(stream.resolution)
                            
                        ## creating object of a Resolution class
                        current_resol = Resolution()
                        
                        ## altering Resolution.resolution argument

                        ## !!!! All resolutions are illlustrated as the buttons on this page
            
                        current_resol.resolution = sorted([i for i in list(resolutions) if i is not None],
                                                          key=lambda x: int(x.split('p')[0]))
                        return current_resol.resolution
## List of resolutions generates dynamically accordingly to the number of resolutions available to choose in YouTube                       


?? function below checks if the provided link is valid (not empty or link from youtube) or if the video is not under age restriction ??

                def form1_view(request):

                  ## creating python dictionary to store the type of mistake
                  mistakes.mistakes['empty_link'], mistakes.mistakes['age_restriction'] = False, False
                  
                  if request.method == 'POST':
                      Link.link = request.POST.get('link', '')
                      
                      ## check if provided link is invalid
                      try:
                          response = requests.get(Link.link)
                          
                          ## if the status code == 200 ---> link is valid
                          if response.status_code != 200:
                              mistakes.mistakes['empty_link'] = True
                              
                          ## catch raised mistakes
                      except requests.exceptions.RequestException:
                          mistakes.mistakes['empty_link'] = True
                      if not Link.link:
                          mistakes.mistakes['empty_link'] = True
                      else:
                          if mistakes.mistakes['empty_link'] is False:
                              try:
                              
                              ## if everything is okay with the video --> extract resolution
                                  resolution.resolution = link_inserting(Link.link)
                                  
                                  ## if thoose exceptions are created --> material is age restricted
                              except (pytube.exceptions.AgeRestrictedError, pytube.exceptions.RegexMatchError):
                                  mistakes.mistakes['age_restriction'] = True
                                  
                                  ## render the page with context dectionary (provided in {} brackets)
                  return render(request, 'loadfile.html', {'resol': resolution.resolution, 'mistakes': mistakes.mistakes})

?? if the video doesn't have the integrated audio track -> download separetely ??

      def form2_view(request):

        mp4, progres = False, False
        if request.method == 'POST':
            action = request.POST.get('data_name', '').rstrip()
            path = './'
            
            ## create folder with video
            if 'videos' not in os.listdir(path):
                makedir(path)
                
            ## create folder with audios
            if 'audios' not in os.listdir(path):
                os.mkdir(path=f'{path}/audios')
            new_path = './videos'
            audio_path = './audios'
            
            ## !!!!! PROGRESSIVE means video with integrated audio
            ## in code below we check if the video is progressive and | or it is downloaded in mp4 extension
            
            if YouTube(Link.link).streams.filter(res=action, progressive=True, file_extension='mp4').first() is not None:
                mp4 = True
                progres = True
            elif YouTube(Link.link).streams.filter(res=action, progressive=True).first() is not None:
                progres = True
            ## call the function dowload with given variables
            download(Link.link, action, mp4, progres, new_path, audio_path)
            
            ## call the function which checks all videos and their format, if the format is wem --> change it
            change_extension(new_path, audio_path)
    
            ## clear up dictionaries with mistakes
            mistakes.mistakes['empty_link'], mistakes.mistakes['age_restriction'] = False, False
    
            ## render page
        return render(request, 'loadfile.html', {'resol': resolution.resolution, 'mistakes': mistakes.mistakes})

?? download audio if required ??

      def download_audio(link, audio_path):
          ## audio with the best quality
          YouTube(link).streams.filter(only_audio=True).first().download(output_path=audio_path)

?? This function shows progress bar of video downloading ??

            def download(link, action, mp4, progres, new_path, audio_path):
            
                ## extract file size
                file_size = YouTube(Link.link).streams.filter(res=action).first().filesize
                
                ## create progress bar with using pithon tqdm
                progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
            
                ## always update progress bar
                def progress_callback(stream, chunk, bytes_remaining):
                    progress_bar.update(len(chunk))
            
                if mp4 is False:
                    YouTube(Link.link, on_progress_callback=progress_callback).streams.filter(res=action,
                                                                                              progressive=progres).first().download(
                        output_path=new_path)
                else:
                    YouTube(Link.link, on_progress_callback=progress_callback).streams.filter(res=action, progressive=progres,
                                                                                              file_extension='mp4').first().download(
                        output_path=new_path)
            
                ## if the video is not progressive
                
                if progres is False:
                    download_audio(link, audio_path)
                progress_bar.close()

?? if the video extension it wedm, change and save it in mp4 format ??

              def change_extension(new_path, audio_path):
                  for i in os.listdir(new_path):
                  
                      ## if the last letters of file extension is webm (splitting is by "."
                      if i.split('.')[-1] == 'webm':
                      
                          ## changing to mp4
                          output_file = f'{new_path}/{i.split(".")[:-1:][0]}.mp4'
                          
                          ## saving to a another foler
                          video = VideoFileClip(f'{new_path}/{i}')
                          video.write_videofile(output_file, codec='libx264')
                          os.remove(path=f'{new_path}/{i}')
                          
                  ## call a function to insert audio and a video
                  combine_video_audio(new_path, audio_path)

?? this function checks if the video and audio are downloaded separetely, combines it ??

        def combine_video_audio(new_path, audio_path):
      
          ## if it is the first downloaded video -> create a folder
          if 'My_Downloaded_videos' not in os.listdir('./'):
              os.mkdir(path='./My_Downloaded_videos')
              
          ## loop to check if the audio corresponds to video
          for i in os.listdir(f'{new_path}'):
              for j in os.listdir(f'{audio_path}'):
              ## found
                  if i == j:
                      video = VideoFileClip(f'{new_path}/{i}')
                      audio = AudioFileClip(f'{audio_path}/{i}')
                      
                      ## !!! it is important to have the audio and the video with the same duration
                      audio = audio.set_duration(video.duration)
                      video = video.set_audio(audio)
                      pat = './My_Downloaded_videos'
                      video.write_videofile(f'{pat}/{i}', codec="libx264", audio_codec='aac')
                      
                      ## removing video and audio to not do the same step afterwards
                      os.remove(path=f'./audios/{i}')
                      os.remove(path=f'./videos/{i}')

?? function that creates folder ??

              def makedir(path):
                  os.mkdir(path=f'{path}/videos')


?? render the page and clear up variables ??

        def collector(request):
            mistakes.mistakes['empty_link'], mistakes.mistakes['age_restriction'] = False, False
            return render(request, 'loadfile.html', {'resol': resolution.resolution, 'mistakes': mistakes.mistakes})




DOWNLOADING PROCESS: 
IF the VIDEO does not have integrate audio, it is stored in ./videos folder   and   AUDIO stored in ./audios folder

!!! WHEN rendering and inserting audio activities are finished  -> video and audio will be deleted from this folder

#####
!!! FINALLY :::: When all steps are passed, FINAL VIDEO is stored in ./My_Downloaded_videos
#####
