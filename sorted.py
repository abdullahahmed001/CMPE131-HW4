def reverse_sort_dictionary(my_dict):
   sorted_dictionary = dict(sorted(my_dict.items(), reverse=True))

   sorted_list = []
   for name, information in sorted_dictionary.items():
      sorted_list.append((name, information[0]))

   return sorted_list


