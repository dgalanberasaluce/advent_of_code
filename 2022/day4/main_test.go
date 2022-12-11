package main

import "testing"

func TestDay4(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	var lines = []string{
		"2-4,6-8",
		"2-3,4-5",
		"5-7,7-9",
		"2-8,3-7",
		"6-6,4-6",
		"2-6,4-8"}

	t.Run("running part 1:", func(t *testing.T) {

		got := Part1(lines)
		want := 2

		assertCorrectMessage(t, got, want)
	})

	t.Run("running part 2:", func(t *testing.T) {

		got := Part2(lines)
		want := 4

		assertCorrectMessage(t, got, want)
	})
}
