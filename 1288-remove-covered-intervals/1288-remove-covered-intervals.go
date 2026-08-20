func removeCoveredIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})

	count := 0
	maxEnd := 0

	for _, interval := range intervals {
		end := interval[1]

		if end > maxEnd {
			count++
			maxEnd = end
		}
	}

	return count
}