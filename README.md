# Fillomino: make the most of your performance data
*Fillomino* is a Python package whose purpose is to
fill incomplete performance maps using correction curves.
**It is meant to create variable capacity air-to-air heat pumps
performance maps that can be used by the
[Type 3254](https://github.com/polymtl-bee/vcaahp-model) in TRNSYS**.

With Fillomino, the whole process of extending and formatting
performance maps becomes quite straightforward,
see [basic usage](#basic-usage).

## Features
- Performance map manipulation using pandas dataframes
- Extend performance maps using custom correction curves
- Automatic normalization
- Rated values adjsutments
- Write performance maps in the format required by the
  [Type 3254](https://github.com/polymtl-bee/vcaahp-model)

### Incoming features
- Plot slices of the performance map
- Use basic functionalities with a user interface

## Installation
Install Fillomino with [`pip`](https://pip.pypa.io/en/stable/) by running

    $ pip install fillomino

## Basic usage
Import the package and load the (incomplete) performance map into a dataframe
```python
import fillomino
hpm = fillomino.build_heating_permap("heating-performance-map.dat")
```

Specify the entries of the variable you want to extend,
e.g. the frequency
```python
# Add entries 0.1, 0.2, ..., 1.0
hpm.pmf.entries['freq'] = np.arange(1, 1.1, 0.1)
```

Specify the operating mode
(required to use the appropriate corrections)
```python
hpm.pmf.mode = 'heating'
```

Fill the missing performance values for the specified frequencies
```python
hpm_full = hpm.pmf.fill()
```

*Note:*
The [Type 3254](https://github.com/polymtl-bee/vcaahp-model)
uses normalized performance maps.
Normalization can be carried out with the `normalize` method,
or directly through the `fill` method using the rated values
of any two quantities amongst `capacity`, `power` and `COP`.
For example, with a rated capacity of 4.69&nbsp;W and a rated power
of 1.01&nbsp;W,
```python
rated_values = pd.DataFrame({'capacity': [4.69], 'power': [1.01]})
hpm_full = hpm.pmf.fill(norm=rated_values)
```

Extend the operating frequency range to [0,1]
```python
hpm_full.pmf.ranges['freq'] = [0, 1]
```

And finally write the full performance map
```python
hpm_full.pmf.write("permap-heating.dat")
```
Now the generated file `permap-heating.dat` should be compatible
with the [Type 3254](https://github.com/polymtl-bee/vcaahp-model).

## Support
If you are having problems, please open an issue in the issue tracker
and submit a minimal working example to highlight what is not working.
