children = 4
candies_with_chef = 2
each_packet = 4
remain_need_to_buy = children - candies_with_chef
final_packets = 0
if (remain_need_to_buy % 4) != 0:
    final_packets+=1
print(final_packets+remain_need_to_buy // 4)