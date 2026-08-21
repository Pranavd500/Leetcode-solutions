func shipWithinDays(weights []int, days int) int {
	left := 0
	right := 0

	// Minimum capacity = heaviest package
	// Maximum capacity = sum of all packages
	for _, weight := range weights {
		if weight > left {
			left = weight
		}
		right += weight
	}

	// Binary search for minimum valid capacity
	for left < right {
		mid := left + (right-left)/2

		currentWeight := 0
		requiredDays := 1

		for _, weight := range weights {
			if currentWeight+weight > mid {
				requiredDays++
				currentWeight = 0
			}

			currentWeight += weight
		}

		if requiredDays <= days {
			// Capacity works.
			// Try a smaller capacity.
			right = mid
		} else {
			// Capacity is too small.
			left = mid + 1
		}
	}

	return left
}