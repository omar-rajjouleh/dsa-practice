def deep_v2(lst):
   return list(reversed([item if not isinstance(item,list) else deep_v2(item) for item in lst]))
