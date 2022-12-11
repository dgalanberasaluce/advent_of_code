package main

import "testing"

func TestPriority(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	t.Run("running subtest 1: a=1", func(t *testing.T) {

		got := priority('a')
		want := 1

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2: z=26", func(t *testing.T) {

		got := priority('z')
		want := 26

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 3: A=27", func(t *testing.T) {

		got := priority('A')
		want := 27

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 4: Z=52", func(t *testing.T) {

		got := priority('Z')
		want := 52

		assertCorrectMessage(t, got, want)
	})
}

func TestGetCommonCharacter(t *testing.T) {
	assertCorrectMessage := func(t testing.TB, got, want byte) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	t.Run("running subtest 1: vJrwpWtwJgWr hcsFMMfFFhFp", func(t *testing.T) {

		got := getCommonCharacter("vJrwpWtwJgWr", "hcsFMMfFFhFp")
		want := byte('p')

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2: PmmdzqPrV vPwwTWBwg", func(t *testing.T) {

		got := getCommonCharacter("PmmdzqPrV", "vPwwTWBwg")
		want := byte('P')

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 3: NQrcLNmQGRfGLHHLZ gbbnpjZJJJndbgnlv", func(t *testing.T) {

		got := getCommonCharacter("NQrcLNmQGRfGLHHLZ", "gbbnpjZJJJndbgnlv")
		want := byte('Z')

		assertCorrectMessage(t, got, want)
	})

}

func TestGetPriority(t *testing.T) {

	assertCorrectMessage := func(t testing.TB, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d want %d", got, want)
		}
	}

	input := []string{"vJrwpWtwJgWrhcsFMMfFFhFp",
		"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
		"PmmdzqPrVvPwwTWBwg",
		"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
		"ttgJtRGJQctTZtZT",
		"CrZsJsPPZsGzwwsLwLmpwMDw"}

	t.Run("running subtest 1: vJrwpWtwJgWr hcsFMMfFFhFp", func(t *testing.T) {

		got := getPriority(input[0])
		want := 16

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 2: jqHRNqRjqzjGDLGL rsFMfFZSrLrFZsSL", func(t *testing.T) {

		got := getPriority(input[1])
		want := 38

		assertCorrectMessage(t, got, want)
	})

	t.Run("running subtest 3: PmmdzqPrV vPwwTWBwg", func(t *testing.T) {

		got := getPriority(input[2])
		want := 42

		assertCorrectMessage(t, got, want)
	})

	t.Run("Get Sum of all priorities", func(t *testing.T) {

		got := GetTotalPriority(input)
		want := 157

		assertCorrectMessage(t, got, want)
	})
}
