// slice
package main

import (
	"fmt"
)

func reverse(s []int) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

// slice切片是和原切片共享内存数据的
func main() {
	var c = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	cc := c[1:4]
	fmt.Println(cc)

	cc[0] = 222

	fmt.Println(cc)
	fmt.Println(c)
}
