package main

import "testing"

func TestDay8(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	var lines = []string{
		"30373",
		"25512",
		"65332",
		"33549",
		"35390",
	}

	t.Run("running part 1:", func(t *testing.T) {

		got := Part1(lines)
		want := 21

		assertCorrectMessage(t, got, want)
	})

	t.Run("running part 2:", func(t *testing.T) {

		got := Part2(lines)
		want := 8

		assertCorrectMessage(t, got, want)
	})
}
