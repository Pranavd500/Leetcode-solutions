func findJudge(n int, trust [][]int) int {
	score := make([]int, n+1)

	for _, t := range trust {
		a, b := t[0], t[1]

		// a trusts someone -> a cannot be the judge
		score[a]--

		// b is trusted by someone -> b could be the judge
		score[b]++
	}

	for person := 1; person <= n; person++ {
		if score[person] == n-1 {
			return person
		}
	}

	return -1
}