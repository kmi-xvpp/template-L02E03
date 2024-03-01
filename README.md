# L05E01: Read points (NamedTuple)
Vytvořte modul `points.py` obsahující funkci `read_points(text, separator=";")`. Podobně jako v úkolu [L03E01](https://github.com/kmi-jp/template-L03E01).

Funkce `read_points(text, separator=";")` funguje stejně, jediný rozdíl je, že body namísto slovníkem reprezentujeme třídou `Point` vytvořenou pomoci `NamedTuple` (vlastnosti `x` a `y`).

Třídu `Point` vytvořte v modulu `points.py` mimo funkci `read_points(text, separator=";")`.

## Příklad chování
```python
from points import read_points, Point

assert read_points("10,20;20,10") == [Point(10, 20), Point(20, 10)]
```

```python
from points import read_points, Point

assert read_points("10,20_20,10", separator="_") == [Point(10, 20), Point(20, 10)]
```

```python
from points import read_points, Point

assert read_points("1.234,0;10,20") == [Point(1.234, 0), Point(10, 20)]
```

```python
from points import read_points, Point

assert read_points("1.234,0*10,20*1.234,0*-10,20", separator="*") == [Point(1.234, 0), Point(10, 20), Point(1.234, 0), Point(-10, 20)]
```

## Lokální testování
Funkčnost řešení ověříte následujícím příkazem:

```bash
pytest tests.py
```