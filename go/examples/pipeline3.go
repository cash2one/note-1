package main

import "fmt"

// 单向chan
// 类型 chan<- int 表示一个只发送int的channel，只能发送不能接收.
// 类型 <-chan int 表示一个只接收int的channel，只能接收不能发送.
// 任何双向channel向单向channel变量的赋值操作都将导致该隐式转换

func counter(out chan<- int) {
	for x := 0; x < 100; x++ {
		out <- x
	}
	close(out)
}

func squarer(out chan<- int, in <-chan int) {
	for v := range in {
		out <- v * v
	}
	close(out)
}

func printer(in <-chan int) {
	for v := range in {
		fmt.Println(v)
	}
}

func main() {
	naturals := make(chan int)
	squares := make(chan int)
	go counter(naturals)
	go squarer(squares, naturals)
	printer(squares)
}
