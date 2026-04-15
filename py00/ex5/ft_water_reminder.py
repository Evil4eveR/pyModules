# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarmoud <ymarmoud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 16:16:20 by ymarmoud          #+#    #+#              #
#    Updated: 2026/04/09 16:19:00 by ymarmoud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    p = input("Days since last watering:")
    if(int(p) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")