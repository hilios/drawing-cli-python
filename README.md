# Springer Challenge

#### A simple drawing application

A command line application that let's you draw simple stuff like lines and rectangles.

##### Installing

```shell
$ pip install --editable .
$ simple-draw
enter command:
```

##### Test

To run tests

```shell
python test.py
```

##### Debug mode

```
python main.py -d
```

### The problem

You're given the task of writing a simple console version of a drawing program. The functionality of the program is
quite limited but should be extensible. The program should work as follows:

1. create a new canvas.
2. start drawing on the canvas by issuing various commands.
3. quit.

The program should support the following commands:

| Command | Description |
| ------- | ----------- |
| `C w  h` | Should create a new canvas of width w and height h. |
| `L x1 y1 x2 y2` | Should create a new line from (x1,y1)to (x2,y2). Currently only horizontal or vertical lines are supported. Horizontal and vertical lines will be drawn using the xcharacter. |
| `R x1 y1 x2 y2` | Should create a new rectangle, whose upper left corner is (x1,y1)and lower right corner is(x2,y2). Horizontal and vertical lines will be drawn using the xcharacter. |
| `B x y c` | Should fill the entire area connected to (x,y)with colour 'c'. The behaviour of this is the same as that of the "bucket fill" tool in paint programs. |
| `Q` | Should quit the program. |
