# krasGEM
My upgrade of classical LandGEM v3.02 landfill gas generation model

There is an "augmeted" version of landfill gases generation model LandGEM v3.02:

https://www.waste.ccacoalition.org/document/landfill-gas-emissions-model-landgem-version-302

It was written with Python 3 instead of Exel+VBA used in original LandGEM model.
It does not mean that you should know Python to use it! Just install Python 3
(theoretically it should run with Python 2.7, but I never test this) and follow
instructions.

Key features:
1. Now you can run several landfills with different parameters simultaniosly!
2. In simulation you can divide year not only 10 times as it was in original LangGEM v3.02,
but as much as you wish.

Getting started:

1. Install any Python 3 version.
2. Clon this repo.
3. Open input.csv with Office or LibreOffice.
4. Made you own tabels with langfills. Upper rows are:
k - metane generation rate 1/year
L0 - potential metan generation capasity (m3/Mg or m3/tonn)
nT - "accuracy" of simulation. 10 mean that you want to divide year 10 times.

Then you should write years of ssimulated period in first columt beyond nT. Аnd then
add waste acceptences per year in megegrames (or tonns).

Each columns, exept of first one, represent one landfill.

WARNING! Delimiters in you input.csv must be semicolons!

After creation of input table run krasGEM.py as python script and it shold create results.csv table with results.

Enjoy it!
