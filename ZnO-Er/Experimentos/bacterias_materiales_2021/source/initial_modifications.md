---
title: "Analysis_ZnER_NanoBiotechLab"
author: "Kaled Corona-Romero"
date: "4/23/2021"
output:
  pdf_document: default
  html_document: default
---

# Initial setup

```r
knitr::opts_chunk$set(echo = TRUE)
# Change the default directory to the one who has the datasets to work with
setwd("/mnt/veracrypt2/nanobiotech_lab/bacterias_materiales_2021/source")
```

## Load the libraries

```r
# read excel files
library(readxl)
# Work with data
library(tibble)
library(stringr)
library(purrr)
library(dplyr)
library(readr)
# Plot
library(ggplot2)
# Knitr
library(knitr)
```


## Read the files

```r
# Load the location
ZnER_SA_location <- "../datasets_modificados/ZnER-SA_sheet.csv"
ZnER_EC_location <- "../datasets_modificados/ZnER-EC_sheet.csv"
ZnER_description_location <- "../datasets/VariablesZnOEr.xlsx"

# read the xlsx and csv files
dataframe_SA <- read_csv(ZnER_SA_location)
```

```
## 
## ── Column specification ────────────────────────────────────────────────────────────────────────────────────────────────────────
## cols(
##   tiempo = col_double(),
##   Tratamiento = col_character(),
##   Conc = col_character(),
##   sample = col_double(),
##   blank = col_double(),
##   abs = col_double()
## )
```

```r
dataframe_EC <- read_csv(ZnER_EC_location)
```

```
## 
## ── Column specification ────────────────────────────────────────────────────────────────────────────────────────────────────────
## cols(
##   tiempo = col_double(),
##   Tratamiento = col_character(),
##   Conc = col_character(),
##   sample = col_double(),
##   blank = col_double(),
##   abs = col_double()
## )
```

```r
ZnER_cristal_description <- read_excel(ZnER_description_location)
```

```
## New names:
## * `` -> ...3
## * `` -> ...4
## * `` -> ...5
## * `` -> ...6
## * `` -> ...7
## * ...
```

## Convert the csv files into tibble dataframes

```r
# Create a tibble dataframe
dataframe_SA <- as_tibble(dataframe_SA)
dataframe_EC <- as_tibble(dataframe_EC)
glossary <- as_tibble(ZnER_cristal_description)
```

# Replace every concentration C by their numeric value

```r
# ZnO_SA convert to factor
dataframe_SA$Conc <- as.factor(dataframe_SA$Conc)
# ZnO_EC convert to factor
dataframe_EC$Conc <- as.factor(dataframe_EC$Conc)
```

```r
# Replacement- ZnO_EC
 str_replace_all(dataframe_EC$Conc, "C1", "400") %>%
    str_replace_all("C2", "800") %>%
    str_replace_all("C3", "1000") -> dataframe_EC$Conc
# Replacement- ZnO_SA
 str_replace_all(dataframe_SA$Conc, "C1", "400") %>%
    str_replace_all("C2", "800") %>%
    str_replace_all("C3", "1000") -> dataframe_SA$Conc
 
# Transform column to numbers
dataframe_EC$Conc <- as.integer(dataframe_EC$Conc)
dataframe_SA$Conc <- as.integer(dataframe_SA$Conc)
```

# Replace every treatment T-Zn?-SA/EC by their numeric value

```r
# Replacement- ZnO_EC
 str_replace_all(dataframe_EC$Tratamiento, "T-EC", "1") %>%
    str_replace_all("TZn0-EC", "2") %>%
    str_replace_all("TZn1-EC", "3") %>%
    str_replace_all("TZn5-EC", "4") %>%
    str_replace_all("TZn10-EC", "5") -> dataframe_EC$Tratamiento
# Replacement- ZnO_SA
 str_replace_all(dataframe_SA$Tratamiento, "T-SA", "1") %>%
    str_replace_all("TZn0-SA", "2") %>%
    str_replace_all("TZn1-SA", "3") %>%
    str_replace_all("TZn5-SA", "4") %>%
    str_replace_all("TZn10-SA", "5") -> dataframe_SA$Tratamiento
 
# Transform column to numbers
dataframe_EC$Tratamiento <- as.integer(dataframe_EC$Tratamiento)
dataframe_SA$Tratamiento <- as.integer(dataframe_SA$Tratamiento)
```

# Create a copy from the exist datasets and delete sample and blank columns

```r
# Select columns Zn_EC
dataframe_EC_mod <- dataframe_EC[ , c(1,2,3,6)]
#Select columns Zn_SA
dataframe_SA_mod <- dataframe_SA[ , c(1,2,3,6)]
```

# Export the dataframes as csv

```r
write_csv(dataframe_EC_mod, "../datasets_modificados/dataframe_Zn_EC_clean.csv")
write_csv(dataframe_SA_mod, "../datasets_modificados/dataframe_ZnER_SA_clean.csv")
```


```r
knit2pdf("/mnt/veracrypt2/nanobiotech_lab/bacterias_materiales_2021/source/initial_modifications.Rmd")
```

```
## 
## 
## processing file: /mnt/veracrypt2/nanobiotech_lab/bacterias_materiales_2021/source/initial_modifications.Rmd
```

```
## Error in parse_block(g[-1], g[1], params.src, markdown_mode): Duplicate chunk label 'setup', which has been used for the chunk:
## knitr::opts_chunk$set(echo = TRUE)
## # Change the default directory to the one who has the datasets to work with
## setwd("/mnt/veracrypt2/nanobiotech_lab/bacterias_materiales_2021/source")
```

