# Compendium of Physical Activity

Cleaned up data from [updated 2011 Adult Compendium of Physical Activities](https://sites.google.com/site/compendiumofphysicalactivities/).

Provided in CSV (separated by `|`, which is not otherwise in the data), SQLite, HTML, JSON, parquet, and Excel formats.

## Suggested citation

Manuscript:

```
Ainsworth BE, Haskell WL, Herrmann SD, Meckes N, Bassett Jr DR, Tudor-Locke C, Greer JL, Vezina J, Whitt-    Glover MC, Leon AS. 2011 Compendium of Physical Activities: a second update of codes and MET values. Medicine and Science in Sports and Exercise, 2011;43(8):1575-1581.
```

Website:

```
Ainsworth BE, Haskell WL, Herrmann SD, Meckes N, Bassett Jr DR, Tudor-Locke C, Greer JL, Vezina J, Whitt-Glover MC, Leon AS. The Compendium of Physical Activities Tracking Guide. Healthy Lifestyles Research Center, College of Nursing & Health Innovation, Arizona State University. Retrieved [date] from the World Wide Web.
```

## Rebuilding output

Install virtual env and the deps:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the script:

```
python3 combine_sheets.py
```