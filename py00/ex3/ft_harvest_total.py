# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarmoud <ymarmoud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 16:07:30 by ymarmoud          #+#    #+#              #
#    Updated: 2026/04/09 16:10:52 by ymarmoud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = input("Day 1 harvest:")
    day2 = input("Day 2 harvest:")
    day3 = input("Day 3 harvest:")
    print("Total harvest:", int(day1) + int(day2) + int(day3))