# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarmoud <ymarmoud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 16:11:20 by ymarmoud          #+#    #+#              #
#    Updated: 2026/04/09 16:20:42 by ymarmoud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = input("Enter plant age in days:")
    if(int(age) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")