U
    f_�^x  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZdZe	ed� ze
dd	�Ze�� Zej W nJ   eed
��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX z&e
dd	�Ze
dd	�Ze�� Zej W nJ   eed��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX zd dlZW nF ek
�rp   e	d� e�d� e	d� e�d� d dlZeZY nX dd� Zdedd�ZeZeed��Zd Zeee�D ]�Ze�d� e	e� d Zejeed�Z ee �Z!e!dk�r�e	e� n,e!dk�r�e	e� ne	e� e	d� e	e� ed7 Ze	dee�ddd� ed�D ]BZ"e"d d  Z#e	d!eee#��d" dd� e �$d#� ej%�d$� �q8�q�e�d%� e&�  d&d'� Z&e'd(k�r�e�  dS ))�    N�clearz'     >>>>    WON data    <<<<          z(      >>>>    NO  data    <<<<          zG[1;36;40m
___________________________________________________________
a�  [1;36;40m

             **                  **                 M
               **               **                  E 
                ** *********** **                   G
                 ***************                    A
                ******************
              **** @ ****** @ *****
             ***********************                R
            *************************               U
           ***************************              N          
                                        
        ****    ******************     ****         2  
       ******  ********************   ******          
       ******  *********************  ******        0     
       ******  *********************  ******         
       ******  *********************  ******        2     
       ******  *********************  ******          
       ******  *********************  ******        0  
       ******  *********************  ******            
       ******  *********************  ******              
       ******  *********************  ******              
       ******  *********************  ******              
       ******    *****************    ******           
        ****       *************       ****           
                                                    
                ******       *****                 R     
               ********     ********               J      
               ********     ********                     
               ********     ********               S     
               ********     ********               T    
               ********     ********               U      
               ********     ********               D      
               ********     ********               I      
                ******       ******                O      
__________________________________________________________

[1;35;40m             [Be Cool] mod by RJ studio 2020
� zfile_auth.txt�rz![1;0;40mPaste Your Auth here :- �wzfile_url.txtzPaste Your URL here :- zwaiting.......zpip3 install requestsz%s Requests installed.c                   C   s   t �d� ttd� d S )Nr   �
)�os�system�print�name� r   r   �/storage/emulated/0/mega.py�main_   s    
r   zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionz[1;36;40mEnter Amount - )Zheadersz<Response [204]>z<Response [200]>zC
[1;31;40m [retry] Check Again your internet connection... [retry]�   z
[1;0;40m
zWait For Next request)�end�   �d   z[1;36;40m
>>> [+]z% g      �?z[Fzfiglet FINISHEDc                  C   s<   t d�} | dks| dkr t�  n| dks0| dkr8t�  n d S )NzRestart Algorithm  (y/n) :- �y�Y�n�N)�inputr   �quit)�againr   r   r   r   �   s    r   �__main__)(�timeZurllib�sysr   r   Zwon_dataZno_data�liner
   r	   �open�f�readZ	file_auth�close�strr   Zwr�writeZ	file_url1Zrequests�ImportErrorZauthr   �headZurl�int�sZrr�range�size�getZrjZrequest�jZrrr�sleep�stdoutr   �__name__r   r   r   r   �<module>   s�   
(














 �







