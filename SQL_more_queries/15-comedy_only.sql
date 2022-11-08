-- select all comedy
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id = 5
ORDER BY title;