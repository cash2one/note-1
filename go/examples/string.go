package main

import (
	"fmt"
	"os"
	"strings"
)

// 字符串不能被索引赋值, 会编译错误
func main() {
	s := "hello 白雪"
	ss := []rune(s)

	fmt.Println(len(s))
	fmt.Println(len(ss))

	fmt.Println(s[0])
	fmt.Printf("%c\n", s[0])

	fmt.Println(s[6])
	fmt.Printf("%c\n", s[6])

	fmt.Println(ss[0])
	fmt.Printf("%c\n", ss[0])

	fmt.Println(ss[6])
	fmt.Printf("%c\n", ss[6])

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
