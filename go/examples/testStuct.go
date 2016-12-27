// Struct扩展
package main

import (
	"fmt"
	"image/color"
)

type Point struct{ X, Y float64 }

type ColoredPoint struct {
	Point
	Color color.RGBA
}

type Counter struct{ n int }

func (c *Counter) N() int     { return c.n }
func (c *Counter) Increment() { c.n++ }
func (c *Counter) Reset()     { c.n = 0 }

func main() {
	red := color.RGBA{255, 0, 0, 255}
	blue := color.RGBA{0, 0, 255, 255}
	var p = ColoredPoint{Point{1, 1}, red}
	var q = ColoredPoint{Point{5, 4}, blue}

	fmt.Printf("%v\n", p.X)
	fmt.Printf("%v\n", p.Y)

	fmt.Printf("%v\n", q.X)
	fmt.Printf("%v\n", q.Y)
	q.X = 122
	q.Y = 133
	fmt.Printf("%v\n", q.X)
	fmt.Printf("%v\n", q.Y)
}
