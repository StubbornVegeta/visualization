
## matplotlib中文乱码解决方案

输出matplotlibrc所在路径

```python
import matplotlib
print(matplotlib.matplotlib_fname())
```
1. 复制路径中的matplotlibrc到~/.config/matplotlib/下

2. 取消font.family和font.sans-serif两行的注释

3. 在font.sans-serif后添加Microsoft YaHei

4. 删除~/.cache/matplotlib/目录下的fontList.json文件（.json文件都可以删除，重启python后会自动生成，如果不放心，可以对json文件重命名，比如将后缀名从.json改成.json.bak）

5. 在python的代码本件中写入:
```python
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']    # 解决中文显示问题
plt.rcParams['axes.unicode_minus']=False        # 正常显示负号
```
--------------------------------------------------------------------------


## plot选项
- ls: line shape
    - '-'  : solid line
    - '--' : dashed line
    - '-.' : dash-dot line
    - ':'  : dotted line
- lw: linewidth
- marker: point shape
    - '.' : point
    - ',' : pixel
    - 'o' : circle
    - 'v' : triangle down
    - '^' : triangle up
    - '>' : triangle right
    - '<' : triangle left
    - '1' : v
    - '2' : ^
    - '3' : <
    - '4' : >
    - 's' : square
    - 'p' : pentagon
    - '*' : star
    - '+' : +
    - 'h' : hexagon1
    - 'H' : hexagon2
    - 'x' : x
    - 'D' : diamond
    - 'd' : thin_diamond
    - '|' : vline
    - '_' : hline

- c: line color
    - aliceblue      : #f0f8ff
    - antiquewhite   : #faebd7
    - aqua/cyan      : #00ffff
    - aquamarine     : #7fffd4
    - azure          : #f0ffff
    - beige          : #f5f5dc
    - bisque         : #ffe4c4
    - black          : #000000
    - blanchedalmond : #ffebcd
    - blue           : #0000ff
    - blueviolet     : #8a2be2
    - brown          : #a52a2a
    - burlywood      : #deb887
    - cadetblue      : #5f9ea0
    - chartreuse     : #7fff00
    - chocolate      : #d2691e
    - coral          : #ff7f50
    - cornflowerblue : #6495ed
    - cornsilk       : #fff8dc
    - crimson        : #dc143c
    - darkblue       : #00008b
    - darkcyan       : #008b8b
    - darkgoldenrod  : #b8860b
    - darkgray       : #a9a9a9
    - darkgreen      : #006400
    - ...
- marksize: point size
- markeredgecolor
- makerfacecolor
- label

## legend
- loc : location
    - best
    - upper right
    - upper left
    - lower left
    - lower right
    - right
    - center left
    - center right
    - lower center
    - upper center
    - center
