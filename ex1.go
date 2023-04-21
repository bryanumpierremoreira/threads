package main

import (
	"fmt"
	"math/rand"
	"sync"
)

func sum(v1 []int, v2 []int, c []int, begin int, end int, id int) {
	println("\nThread ", id)
	for i := range v1 {
		fmt.Printf("\n%d+%d = %d\n", v1[i], v2[i], c[i])
		c[i] = v1[i] + v2[i]

	}
}

var begin int

func main() {
	var n, t int
	var end, resto int

	var wg sync.WaitGroup

	fmt.Print("Type the number of elements of vector: ")
	fmt.Scanln(&n)
	fmt.Println("Your numbers are:", n)
	fmt.Print("Type the number of threads: ")
	fmt.Scanln(&t)

	resto = n % t

	v1 := make([]int, n)
	v2 := make([]int, n)
	c := make([]int, n)

	for i := 0; i < n; i++ {
		v1[i] = rand.Intn(1000)
		v2[i] = rand.Intn(1000)
	}

	if resto > 0 {
		resto = resto - 1
	}

	for i := 0; i < t; i++ {
		if i == 0 {
			begin = i * (n / t)
			end = i*(n/t) + n/t
		} else if i == t-1 {
			begin = end
			end = n
		} else {
			begin = end
			end = i*(n/t) + n/t + resto
		}
		wg.Add(1)
		i := i

		go func() {
			defer wg.Done()
			sum(v1, v2, c, begin, end, i)
		}()

	}
	wg.Wait()
	fmt.Println("v1: ", v1)
	fmt.Println("v2: ", v2)
	fmt.Println("c: ", c)

}
