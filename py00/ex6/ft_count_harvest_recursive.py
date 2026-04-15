# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarmoud <ymarmoud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 16:33:52 by ymarmoud          #+#    #+#              #
#    Updated: 2026/04/09 16:36:38 by ymarmoud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def recu(d):
    if(d < 1):
        return 0
    recu(d-1)
    print("Day", d)
    
def ft_count_harvest_recursive():
    days = input("Days until harvest:")
    recu(int(days))
    print("Harvest time!")