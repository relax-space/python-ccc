import pprint
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.extend(selfref_list)

output = open('./base/data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

pkl_file = open('./base/data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(type(data1))
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(type(data2))
pprint.pprint(data2)

pkl_file.close()
