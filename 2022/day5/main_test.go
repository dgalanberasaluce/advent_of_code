package main

import "testing"

func TestDay5(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want string) {
		t.Helper()
		if got != want {
			t.Errorf("got %s want %s", got, want)
		}
	}

	var lines = []string{
		"    [D]    ",
		"[N] [C]    ",
		"[Z] [M] [P]",
		" 1   2   3 ",
		"",
		"move 1 from 2 to 1",
		"move 3 from 1 to 3",
		"move 2 from 2 to 1",
		"move 1 from 1 to 2",
	}

	t.Run("running part 1:", func(t *testing.T) {

		got := Part1(lines)
		want := "CMZ"

		assertCorrectMessage(t, got, want)
	})

	t.Run("running part 2:", func(t *testing.T) {

		got := Part2(lines)
		want := "MCD"

		assertCorrectMessage(t, got, want)
	})
}
