dict_sample = {
  "sea": "море", 
  "sun": "солнце", 
  "cloud": "облако" 
}
print("size is", len(dict_sample))
list_keys = list(dict_sample.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', dict_sample[i])
dict_sample = {
  "sea": "море", 
  "sun": "солнце", 
  "cloud": "облако" 
}.items()
inv_dict=lambda d: {v: k for k, v in d}