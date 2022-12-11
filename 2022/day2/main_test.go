package main

import "testing"

func TestGetTotalScore(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	input := [][]string{
		[]string{"A", "Y"},
		[]string{"B", "X"},
		[]string{"C", "Z"},
	}

	t.Run("running subtest 1", func(t *testing.T) {

		got := getScore(input[0][0], input[0][1])
		want := 2 + 6

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2", func(t *testing.T) {

		got := getScore(input[1][0], input[1][1])
		want := 1

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 3", func(t *testing.T) {

		got := getScore(input[2][0], input[2][1])
		want := 6

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 4", func(t *testing.T) {

		got := getTotalScore(input)
		want := 15

		assertCorrectMessage(t, got, want)
	})
}

func TestGetTotalScore2(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	input := [][]string{
		[]string{"A", "Y"},
		[]string{"B", "X"},
		[]string{"C", "Z"},
	}

	t.Run("running subtest 1", func(t *testing.T) {

		got := getScorePart2(input[0][0], input[0][1])
		want := 1 + 3

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2", func(t *testing.T) {

		got := getScorePart2(input[1][0], input[1][1])
		want := 1 + 0

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 3", func(t *testing.T) {

		got := getScorePart2(input[2][0], input[2][1])
		want := 1 + 6

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 4", func(t *testing.T) {

		got := getTotalScorePart2(input)
		want := 12

		assertCorrectMessage(t, got, want)
	})
}
