func findPeakElement(nums []int) int {
	left, right := 0, len(nums)-1

	for left < right {
		mid := left + (right-left)/2

		if nums[mid] > nums[mid+1] {
			// We are on the decreasing side.
			// A peak exists at mid or to the left.
			right = mid
		} else {
			// We are on the increasing side.
			// A peak must exist to the right.
			left = mid + 1
		}
	}

	return left
}