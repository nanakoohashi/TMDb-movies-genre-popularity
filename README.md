# TMDb-movies-genre-popularity
## Summary

This study uses the data set containing information from about 10,000 movies collected from The Movie Database (TMDb). This data set contains information on a list of movies including its popularity, adjusted budget, adjusted revenue, run time, release year, vote average and so on. This study evaluates how each of the factors listed in the previous sentence impacts the popularity of a movie’s genre. Is there a correlation between each of these factors and the genre of the movie?


## Getting Started
### Dependencies
Windows 10

### Libraries
- pandas
- numpy
- matplotlib


## Steps
1. Wrangle Data.

2. Exploratory Data Analysis. What contributes to making a movie genre popular? I found the average popularity of each genre and compared them with average adjusted budget of genres, average adjusted revenue of genres, average release year of genres, average runtime of genres, and vote average of genres.


## Main Findings
There are many different factors that seem to correlate with the popularity of a genre, but from the limited data we have here, we cannot conclude what exactly causes a genre to be popular.

### Factors that seem to contribute to making a genre popular:
- Budget (positive correlation)
- Revenue (positive correlation)
### Factors that don't seem to contribute to making a genre popular:
- Runtime (no correlation)
- Vote average (no correlation)
- Release year (no correlation)
### The most popular genres ranked from most popular to least popular:
1. Science Fiction
2. Adventure
3. Fantasy
4. Animation
5. Action
6. Family
7. Thriller
8. War
9. Mystery
10. Western
11. Crime
12. Comedy
13. Drama
14. History
15. Romance
16. Music
17. Horror
18. Documentary
19. TV Movie
20. Foreign
### Limitations:
- We don't have data for every movie ever made.
- Genre of movies may not be accurate.
- Movies can have multiple genres, so each movie may not be a pure representation of those genres.
