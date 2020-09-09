import pygame
from pygame import sprite, image, mixer, time

class AudioSource():
    def __init__(self):
        self.__audio_clips = {}
        self.__musics = {}
        self.__time = 0
        
    def add_audio_clip(self, audio_path : str, audio_name : str,volume=1.0 ):
        try:
            if self.__audio_clip_exitst(audio_name):
                raise ValueError("[WARNING] The key exists.")
            else:
                self.__audio_clips[audio_name] = mixer.Sound(audio_path)
                self.__audio_clips[audio_name].set_volume(volume)
        except ValueError:
            print("[WARNING] The key exists.")
        except:
            print("[WARINIG] Not found.")
            
    def play_audio_clip(self, audio_name:str):
        if self.__audio_clip_exitst(audio_name):
            self.__audio_clips[audio_name].play()
        else:
            raise ValueError("[WARNING] The key don't exists.")
        
    def stop_audio_clip(self, audio_name:str):
        if self.__audio_clip_exitst(audio_name):
            self.__audio_clips[audio_name].stop()
            self.__time = 0
        else:
            raise ValueError("[WARNING] The key don't exists.")
    
    def play_audio_clip_each(self, audio_name:str, ms : int):
        if self.__audio_clip_exitst(audio_name):
            if self.__time == 0:
                self.__time = time.get_ticks() + ms
                self.__audio_clips[audio_name].play()
            elif self.__time<time.get_ticks():
                self.__time = 0
        else:
            raise ValueError("[WARNING] The key don't exists.")
        
    def __audio_clip_exitst(self,audio_name:str):
        return not self.__audio_clips.get(audio_name,None)==None
    
    @staticmethod
    def play_music_loop(music_path : str,volume = 1.0):
        try:
           mixer.music.load(music_path)
           mixer.music.set_volume(volume)
           mixer.music.play(-1)
        except:
           print("[WARINIG] Not found.")
    
    @staticmethod
    def play_music_each(music_path : str, loops : int, volume = 1.0):
       try:
           mixer.music.load(music_path)
           mixer.music.set_volume(volume)
           mixer.music.play(loops)
       except:
           print("[WARINIG] Not found.")
    
    @staticmethod
    def stop_music():
        mixer.music.stop()