package main

import "testing"

func TestGetCalories(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	t.Run("running subtest 1", func(t *testing.T) {
		input := [][]int{
			[]int{1000, 2000, 3000},
			[]int{4000},
			[]int{5000, 6000},
			[]int{7000, 8000, 9000},
			[]int{10000},
		}

		got := GetCalories(input)
		want := 24000

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2", func(t *testing.T) {
		input := [][]int{
			[]int{1000, 2000, 3000},
			[]int{4000},
			[]int{5000, 6000},
			[]int{7000, 8000, 9000},
			[]int{10000},
		}

		got := GetCaloriesTop3(input)
		want := 45000

		assertCorrectMessage(t, got, want)
	})
}
