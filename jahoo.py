U
    �@_�  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZz&edd�Z	edd�Z	e	�
� Ze	j W nJ   eed��Zedd	�Z	e	�e� e	j edd�Z	e	�
� Ze	j Y nX d
ZdZededdd� eD ]$Zej�e� ej��  e �d� q�zedd�Z	e	�
� Ze	j W nJ   eed��Zedd	�Z	e	�e� e	j edd�Z	e	�
� Ze	j Y nX z&edd�Z	edd�Z	e	�
� Ze	j W nJ   eed��Zedd	�Z	e	�e� e	j edd�Z	e	�
� Ze	j Y nX zd dlZW nB ek
�r   ed� e�d� ed� e�d� d dlZY nX zd dlmZ W nB ek
�rf   e�d� ed� e�d� d dlmZ eZY nX dd� Zdd� Ze dk�r�e�  dS )�    N�clearz�[1;34;40m       \             /
        \___________/                 won data 
        /           \ 
       /   @     @   \ 
      ||             || 
       \   \_ __ _/  / 
        \___________/
z�[1;34;40m       \             /
        \___________/                  no data 
        /           \ 
       /   @     @   \ 
      ||    _ _ _    || 
       \   /     \   / 
        \___________/
zG[1;36;40m
___________________________________________________________
z	name1.dat�rz'[1;35;40mEnter your name :- [1;33;40m�wa0  [1;31;40m       Warning...


[1;36;40m Don't use Same time when Algorithm is running  in one sim 

[1;36;40m Don't use vpn

 Don't turn off the mobile data when Algorithm is running

[1;33;40m Detalis

[1;34;40m Not hacking

 Dialog user only

 version 1.1.0

 Junior script


  Create by Jahoo	2020zCreate by R*v*ndu J*y*shan

 z,

[1;32;40m    Welcome  [1;33;40m
        z:[1;32;40m
                     please follow intruction

� ��end皙�����?zfile_auth.txtz![1;0;40mPaste Your Auth here :- zfile_url.txtzPaste Your URL here :- zwaiting.......zpip3 install requestsz%s Requests installed.)�tqdmzpip3 install tqdmc               	   C   s  t �d� tD ]$} tj�| � tj��  t�d� qdt	dd�}t
}ttd��}d}d}t||�D �]�}t �d� tt� d}|dkr�td� td	dd
d�}td	�D ]@}|�d�|�� |�d� |d	 d }	t�d� tj�d� q�qbtj||d�}
t|
�}|dk�r6tD ]&} tj�| � tj��  t�d� �qnX|dk�rv|d7 }tD ]&} tj�| � tj��  t�d� �qLntt� td� tt� |d7 }tdt|�� tdt|d �ddddd� td	dd
d�}td	�D ]6}|�d�|�� |�d� |d	 d }	t�d� �q�qbt�  d S )Nr   r   zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionz[1;30;40mEnter Amount - r   z[1;36;40mOpening Algorithm
�Z   F)ZtotalZpositionZleavez
lording...�   �d   g      �?z[F)Zheadersz<Response [204]>g{�G�z�?z<Response [200]>zC
[1;31;40m [retry] Check Again your internet connection... [retry]z[1;32;40m
NUMBER of Message : z[1;32;40m
request: �
� zWait For Next requestr   r   )�os�system�name�sys�stdout�write�flush�time�sleep�	file_auth�	file_url1�int�input�range�printr	   Zset_description�format�update�requests�get�str�no_data�won_data�line�again)�char�headZurl�s�mZrr�sizeZloop�jZrrrZrjZrequest� r-   �rj.py�main\   sh    

 �







r/   c                  C   sJ   t d�} | dks| dkr t�  n&| dks0| dkr8t�  ntd� t�  d S )Nz*[1;0;40m
Do Restart Algorithm :  (y/n) - �y�Y�n�Nz[1;30;40mReEnter)r   r/   �quitr   r&   )�rer-   r-   r.   r&   �   s    r&   �__main__)!r   Zurllibr   r   r   r$   r#   r%   �open�f�readZname1�closer"   r   �wrr   �messager   r   r'   r   r   r   r   r   r    �ImportErrorr	   Zauthr/   r&   �__name__r-   r-   r-   r.   �<module>   s�   








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





@
