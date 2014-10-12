def inBucket(t,low,high):
	count = 0
	for num in t
		if low < num < high:
			count +=1
	print count 







numBuckets=8
buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
for i in range(bucketWidth)
	low= i*bucketWidth
	high = low + bucketWidth
	buckets[i]=inBucket(t,low,high)
print buckets
