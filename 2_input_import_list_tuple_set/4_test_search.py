import time

to_search = [12433435, 436336, 346643, 2522, 56456 , 4353434, 34554, ]

size = 10000000
list_search = list(range(size + 1))
set_search = set(range(size + 1))


start_time = time.time()
for search_number in to_search:
    print(search_number in set_search)

end_time = time.time()
total_time = end_time - start_time
print('Time:', total_time)
