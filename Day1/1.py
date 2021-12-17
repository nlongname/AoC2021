with open('input.txt', 'r+') as f:
    data = [int(line.strip('\n')) for line in f.readlines()]
    f.close

#testdata = [199,200,208,210,200,207,240,269,260,263]

depth_increases = [1 for i,d in enumerate(data[1:]) if d > data[i]]
print("one-by-one:", sum(depth_increases))

window_size = 3
depth_chunks = [sum(data[i:i+window_size]) for i,d in enumerate(data[window_size-1:])]
chunk_increases = [1 for i,d in enumerate(depth_chunks[1:]) if d > depth_chunks[i]]
print(str(window_size)+'-chunks: '+str(sum(chunk_increases)))
