# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarmoud <ymarmoud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 16:32:01 by ymarmoud          #+#    #+#              #
#    Updated: 2026/04/09 16:33:43 by ymarmoud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = input("Days until harvest:")
    for i in range(int(days)):
        print("Day",i+1)
    print("Harvest time!")