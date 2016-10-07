package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	s := "hello world"

	fmt.Println(len(s))

	fmt.Println(s[1])

	fmt.Printf("%c\n", s[1])

	fmt.Println(s[0:5]) // "hello"

	fmt.Println("中国人")

	fmt.Println() // \n

	fmt.Printf("Hello %d\n", 23)

	fmt.Fprint(os.Stdout, "Hello ", 23, "\n")

	for i := 0; i < len(s); i++ {
		fmt.Printf("0x%x\n", s[i])
		fmt.Printf("%c\n", s[i])
		fmt.Println(s[i])
	}

	fmt.Println(strings.LastIndex(s, "w"))
}
