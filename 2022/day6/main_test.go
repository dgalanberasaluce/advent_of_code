package main

import "testing"

func TestDay6Part1(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	t.Run("running example 1:", func(t *testing.T) {
		var line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

		got := Part1(line)
		want := 7

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 2:", func(t *testing.T) {
		var line = "bvwbjplbgvbhsrlpgdmjqwftvncz"

		got := Part1(line)
		want := 5

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 3:", func(t *testing.T) {
		var line = "nppdvjthqldpwncqszvftbrmjlhg"

		got := Part1(line)
		want := 6

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 4:", func(t *testing.T) {
		var line = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

		got := Part1(line)
		want := 10

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 4:", func(t *testing.T) {
		var line = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

		got := Part1(line)
		want := 11

		assertCorrectMessage(t, got, want)
	})
}

func TestDay6Part2(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	t.Run("running example 1:", func(t *testing.T) {
		var line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

		got := Part2(line)
		want := 19

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 2:", func(t *testing.T) {
		var line = "bvwbjplbgvbhsrlpgdmjqwftvncz"

		got := Part2(line)
		want := 23

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 3:", func(t *testing.T) {
		var line = "nppdvjthqldpwncqszvftbrmjlhg"

		got := Part2(line)
		want := 23

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 4:", func(t *testing.T) {
		var line = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

		got := Part2(line)
		want := 29

		assertCorrectMessage(t, got, want)
	})

	t.Run("running example 4:", func(t *testing.T) {
		var line = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

		got := Part2(line)
		want := 26

		assertCorrectMessage(t, got, want)
	})
}
