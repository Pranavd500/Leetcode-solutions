func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
	sumAlice := 0
	sumBob := 0

	for _, x := range aliceSizes {
		sumAlice += x
	}

	for _, x := range bobSizes {
		sumBob += x
	}

	// Alice gives x and Bob gives y.
	// sumAlice - x + y = sumBob - y + x
	//
	// Therefore:
	// y - x = (sumAlice - sumBob) / 2

	diff := (sumAlice - sumBob) / 2

	bobSet := make(map[int]bool)

	for _, x := range bobSizes {
		bobSet[x] = true
	}

	for _, x := range aliceSizes {
		y := x - diff

		if bobSet[y] {
			return []int{x, y}
		}
	}

	return []int{}
}